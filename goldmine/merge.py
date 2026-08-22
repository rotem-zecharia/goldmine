"""Collapse records for the same repository, and compute star velocity.

Velocity comes from diffing the previous committed catalog rather than from the
stargazers API: per-star timestamps cost one paginated request per repository,
which does not fit the rate limit at catalog scale.
"""

from __future__ import annotations

import dataclasses
from datetime import date

VELOCITY_WINDOW_DAYS = 30
MIN_VELOCITY_WINDOW_DAYS = 3


def _key(repo: str) -> str:
    # GitHub repository names are case-insensitive, so two spellings of the same
    # repository must collapse into one row.
    return repo.lower()


def merge_tools(tools: list) -> list:
    by_repo: dict[str, object] = {}

    for tool in tools:
        existing = by_repo.get(_key(tool.repo))
        if existing is None:
            by_repo[_key(tool.repo)] = tool
            continue

        by_repo[_key(tool.repo)] = dataclasses.replace(
            existing,
            categories=sorted(set(existing.categories) | set(tool.categories)),
            stars=max(existing.stars, tool.stars),
            contributors=max(
                (c for c in (existing.contributors, tool.contributors) if c is not None),
                default=None,
            ),
            open_issues=max(existing.open_issues, tool.open_issues),
            closed_issues=max(existing.closed_issues, tool.closed_issues),
            summary=max(existing.summary, tool.summary, key=len),
            install=max(existing.install, tool.install, key=len),
            last_push=max(existing.last_push, tool.last_push),
            has_license=existing.has_license or tool.has_license,
            has_releases=existing.has_releases or tool.has_releases,
            has_install_section=existing.has_install_section or tool.has_install_section,
            source=",".join(sorted(set(existing.source.split(",")) | set(tool.source.split(",")))),
            tags=sorted(set(existing.tags) | set(tool.tags)),
        )

    return list(by_repo.values())


def attach_velocity(tool, previous: dict, today: str):
    snapshot = previous.get(_key(tool.repo)) or previous.get(tool.repo)
    if not snapshot:
        return tool

    days = (date.fromisoformat(today) - date.fromisoformat(snapshot["generated_at"])).days
    # Extrapolating a one-day window to thirty turns ordinary noise into an
    # apparent breakout, so hold velocity until the window is wide enough.
    if days < MIN_VELOCITY_WINDOW_DAYS:
        return tool

    gained = tool.stars - snapshot["stars"]
    return dataclasses.replace(tool, star_velocity_90d=gained / days * VELOCITY_WINDOW_DAYS)
