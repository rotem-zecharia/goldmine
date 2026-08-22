"""Percentile-based tiering, computed inside each category.

An absolute star floor was rejected: topic:mcp-server holds ~25k repositories of
which only ~36 exceed 10k stars, and those are large frameworks rather than the
specific tools a developer needs. Percentile within a category surfaces the
leader of a niche as readily as the leader of a crowded one.
"""

from __future__ import annotations

import dataclasses
from datetime import date

ESTABLISHED_PERCENTILE = 0.95
ESTABLISHED_MAX_PUSH_AGE_DAYS = 90
ESTABLISHED_MIN_CONTRIBUTORS = 3

RISING_MAX_AGE_DAYS = 365
RISING_MIN_VELOCITY = 50.0


def _days_between(earlier: str, later: str) -> int:
    return (date.fromisoformat(later) - date.fromisoformat(earlier)).days


def _percentile_threshold(scores: list[float], percentile: float) -> float:
    ordered = sorted(scores)
    index = min(len(ordered) - 1, int(len(ordered) * percentile))
    return ordered[index]


def _is_established(tool, threshold: float, today: str) -> bool:
    return (
        tool.score >= threshold
        and _days_between(tool.last_push, today) <= ESTABLISHED_MAX_PUSH_AGE_DAYS
        and (tool.contributors or 0) >= ESTABLISHED_MIN_CONTRIBUTORS
    )


def _is_rising(tool, today: str) -> bool:
    young = _days_between(tool.created_at, today) <= RISING_MAX_AGE_DAYS
    growing = (tool.star_velocity_90d or 0.0) >= RISING_MIN_VELOCITY
    active = _days_between(tool.last_push, today) <= ESTABLISHED_MAX_PUSH_AGE_DAYS
    return young and growing and active


def assign_tiers(tools: list, today: str) -> list:
    by_category: dict[str, list[float]] = {}
    for tool in tools:
        for category in tool.categories:
            by_category.setdefault(category, []).append(tool.score)

    thresholds = {
        category: _percentile_threshold(scores, ESTABLISHED_PERCENTILE)
        for category, scores in by_category.items()
    }

    tiered = []
    for tool in tools:
        # A tool in several categories keeps its best standing.
        best = "watch"
        for category in tool.categories:
            if _is_established(tool, thresholds[category], today):
                best = "established"
                break
        if best != "established" and _is_rising(tool, today):
            best = "rising"

        tiered.append(dataclasses.replace(tool, tier=best))

    return tiered
