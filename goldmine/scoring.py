"""Quality signals and the weighted score.

Every signal returns 0.0-1.0, or None when the underlying data is unavailable.
A None signal is dropped and its weight is redistributed across the rest, so a
missing measurement never silently reads as a bad one.
"""

from __future__ import annotations

import math
from datetime import date

import yaml

STAR_SATURATION = 200_000
CONTRIBUTOR_SATURATION = 20
RECENCY_FLOOR_DAYS = 365
VELOCITY_SATURATION = 500.0


def _days_between(earlier: str, later: str) -> int:
    return (date.fromisoformat(later) - date.fromisoformat(earlier)).days


def star_signal(stars: int) -> float:
    if stars <= 0:
        return 0.0
    return round(min(1.0, math.log10(stars) / math.log10(STAR_SATURATION)), 6)


def recency_signal(last_push: str, today: str) -> float:
    days = _days_between(last_push, today)
    if days <= 0:
        return 1.0
    if days >= RECENCY_FLOOR_DAYS:
        return 0.0
    return round(1.0 - days / RECENCY_FLOOR_DAYS, 6)


def contributor_signal(contributors: int) -> float:
    if contributors <= 0:
        return 0.0
    return round(
        min(1.0, math.log10(contributors + 1) / math.log10(CONTRIBUTOR_SATURATION + 1)), 6
    )


def issue_close_signal(open_issues: int, closed_issues: int) -> float:
    total = open_issues + closed_issues
    if total == 0:
        return 0.5
    return round(closed_issues / total, 6)


def velocity_signal(star_velocity_90d: float | None) -> float | None:
    if star_velocity_90d is None:
        return None
    if star_velocity_90d <= 0:
        return 0.0
    return round(
        min(1.0, math.log10(star_velocity_90d + 1) / math.log10(VELOCITY_SATURATION + 1)), 6
    )


def load_weights(path: str) -> dict:
    with open(path) as handle:
        return yaml.safe_load(handle)


def packaging_signal(tool) -> float:
    parts = (tool.has_install_section, tool.has_license, tool.has_releases)
    return round(sum(1 for part in parts if part) / len(parts), 6)


def _signals(tool, today: str) -> dict:
    return {
        "stars": star_signal(tool.stars),
        "velocity": velocity_signal(tool.star_velocity_90d),
        "recency": recency_signal(tool.last_push, today=today),
        "contributors": contributor_signal(tool.contributors),
        "issue_close": issue_close_signal(tool.open_issues, tool.closed_issues),
        "packaging": packaging_signal(tool),
    }


def _penalty_multiplier(tool, config: dict, today: str) -> float:
    penalties = config["penalties"]
    thresholds = config["thresholds"]
    multiplier = 1.0

    if tool.archived:
        multiplier *= penalties["archived"]

    if _days_between(tool.last_push, today) >= thresholds["unmaintained_days"]:
        multiplier *= penalties["unmaintained_12mo"]

    if tool.is_fork:
        multiplier *= penalties["unresolved_fork"]

    is_new = _days_between(tool.created_at, today) < thresholds["new_repo_days"]
    if is_new and tool.stars < thresholds["new_repo_min_stars"]:
        multiplier *= penalties["new_without_traction"]

    return multiplier


def score_tool(tool, config: dict, today: str) -> float:
    """Weighted signal sum, 0-100, with penalty multipliers applied after."""
    signals = _signals(tool, today)
    weights = config["weights"]

    available = {name: value for name, value in signals.items() if value is not None}
    total_weight = sum(weights[name] for name in available)
    if total_weight == 0:
        return 0.0

    base = sum(value * weights[name] for name, value in available.items()) / total_weight

    return round(base * 100.0 * _penalty_multiplier(tool, config, today), 4)
