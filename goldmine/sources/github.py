"""GitHub topic search, normalised into Tool records."""

from __future__ import annotations

import re

from goldmine.models import Tool

SEARCH_URL = (
    "https://api.github.com/search/repositories"
    "?q=topic:{topic}&sort=stars&order=desc&per_page=100&page={page}"
)
MAX_SUMMARY = 200
WHITESPACE = re.compile(r"\s+")


def clean_summary(description: str | None) -> str:
    """One line, no pipes: the index is a markdown table and a grep target."""
    text = WHITESPACE.sub(" ", (description or "").replace("|", "/")).strip()
    return text[:MAX_SUMMARY]


def categorize(topics: list[str], taxonomy: dict) -> list[str]:
    """Map a repository's own topics onto catalog categories.

    Categories drive per-category percentile tiering, so deriving them from the
    repository's topics rather than only from the search term keeps a niche tool
    competing against its actual peers.
    """
    lowered = {topic.lower() for topic in topics}
    matched = []
    for category, needles in taxonomy.items():
        if any(needle in lowered for needle in needles):
            matched.append(category)
    return matched


def normalize_repo(raw: dict, categories: list[str], source: str, taxonomy: dict | None = None) -> Tool:
    topics = list(raw.get("topics") or [])
    merged = sorted(set(categories) | set(categorize(topics, taxonomy or {})))

    return Tool(
        repo=raw["full_name"],
        summary=clean_summary(raw.get("description")),
        categories=merged,
        stars=raw.get("stargazers_count", 0),
        contributors=raw.get("_contributors"),
        last_push=(raw.get("pushed_at") or "1970-01-01")[:10],
        created_at=(raw.get("created_at") or "1970-01-01")[:10],
        open_issues=raw.get("open_issues_count", 0),
        archived=bool(raw.get("archived")),
        is_fork=bool(raw.get("fork")),
        has_license=bool(raw.get("license")),
        tags=topics,
        source=source,
    )


def search_topic(
    fetcher, topic: str, categories: list[str], max_pages: int, taxonomy: dict | None = None
) -> list[Tool]:
    tools: list[Tool] = []
    source = f"github:topic:{topic}"

    for page in range(1, max_pages + 1):
        body = fetcher.get_json(SEARCH_URL.format(topic=topic, page=page))
        if not body:
            break
        items = body.get("items", [])
        if not items:
            break
        tools.extend(normalize_repo(item, categories, source, taxonomy) for item in items)
        if len(items) < 100:
            break

    return tools
