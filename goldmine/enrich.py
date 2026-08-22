"""Second pass over the top candidates.

Search results carry stars and dates but not contributor counts, release
history, or README text. Those cost extra requests each, so only the candidates
that could plausibly reach the established tier are enriched.

Consequence worth knowing: a repository that is never enriched has no
contributor count, and the established tier requires three. Enrichment budget
is therefore the ceiling on how many tools can ever be marked established.
"""

from __future__ import annotations

import dataclasses
import re

from goldmine.readme import extract_install_command, extract_sections, has_install_section

CONTRIBUTORS_URL = "https://api.github.com/repos/{repo}/contributors?per_page=1&anon=1"
RELEASES_URL = "https://api.github.com/repos/{repo}/releases?per_page=1"
README_URL = "https://api.github.com/repos/{repo}/readme"

LAST_PAGE = re.compile(r'[?&]page=(\d+)>;\s*rel="last"')


def contributor_count(fetcher, repo: str) -> int:
    """With per_page=1, the last page number is the contributor count.

    Paging through contributors would cost one request per contributor; the
    Link header gives the same number for one request.
    """
    body, headers = fetcher.get_json_meta(CONTRIBUTORS_URL.format(repo=repo))
    if not body:
        return 0

    match = LAST_PAGE.search(headers.get("Link", ""))
    if match:
        return int(match.group(1))

    # No Link header means a single page, which at per_page=1 is one contributor.
    return len(body) if isinstance(body, list) else 0


def _enrich_one(tool, fetcher) -> tuple[dict, dict]:
    """Return (updates, sections) for one tool."""
    updates: dict = {}
    sections: dict = {}

    readme = fetcher.get_json(README_URL.format(repo=tool.repo))
    text = ""
    if readme and readme.get("download_url"):
        text = fetcher.get_text(readme["download_url"]) or ""

    if text:
        sections = extract_sections(text)
        updates["has_install_section"] = has_install_section(text)
        command = extract_install_command(text)
        if command:
            updates["install"] = command

    updates["has_releases"] = bool(fetcher.get_json(RELEASES_URL.format(repo=tool.repo)))

    count = contributor_count(fetcher, tool.repo)
    if count is not None:
        updates["contributors"] = max(tool.contributors or 0, count)

    return updates, sections


REQUESTS_PER_TOOL = 4


def select_for_enrichment(tools: list, limit: int, per_category: int) -> set:
    """Pick which repositories are worth spending requests on.

    Taking the global top N starves every small category: 3,400 MCP servers
    would consume the whole budget and the leader of a niche category would
    never be enriched, so it could never clear its own percentile gate. Taking
    the top few of each category first spreads the same budget across the pools
    that tiering actually compares within.
    """
    by_category: dict[str, list] = {}
    for tool in tools:
        for category in tool.categories or ["_uncategorised"]:
            by_category.setdefault(category, []).append(tool)

    chosen: list = []
    seen: set = set()

    def take(tool):
        if tool.repo not in seen:
            seen.add(tool.repo)
            chosen.append(tool.repo)

    for category_tools in by_category.values():
        category_tools.sort(key=lambda tool: tool.score or 0.0, reverse=True)
        for tool in category_tools[:per_category]:
            take(tool)

    # Spend whatever is left on the highest scorers overall.
    for tool in sorted(tools, key=lambda tool: tool.score or 0.0, reverse=True):
        if len(chosen) >= limit:
            break
        take(tool)

    return set(chosen[:limit])


def _enrich_one(tool, fetcher) -> tuple[dict, dict]:
    """Return (updates, sections) for one tool."""
    updates: dict = {}
    sections: dict = {}

    readme = fetcher.get_json(README_URL.format(repo=tool.repo))
    text = ""
    if readme and readme.get("download_url"):
        text = fetcher.get_text(readme["download_url"]) or ""

    if text:
        sections = extract_sections(text)
        updates["has_install_section"] = has_install_section(text)
        command = extract_install_command(text)
        if command:
            updates["install"] = command

    updates["has_releases"] = bool(fetcher.get_json(RELEASES_URL.format(repo=tool.repo)))

    count = contributor_count(fetcher, tool.repo)
    if count is not None:
        updates["contributors"] = max(tool.contributors or 0, count)

    return updates, sections


REQUESTS_PER_TOOL = 4


def select_for_enrichment(tools: list, limit: int, per_category: int) -> set:
    """Pick which repositories are worth spending requests on.

    Taking the global top N starves every small category: 3,400 MCP servers
    would consume the whole budget and the leader of a niche category would
    never be enriched, so it could never clear its own percentile gate. Taking
    the top few of each category first spreads the same budget across the pools
    that tiering actually compares within.
    """
    by_category: dict[str, list] = {}
    for tool in tools:
        for category in tool.categories or ["_uncategorised"]:
            by_category.setdefault(category, []).append(tool)

    chosen: set = set()
    for category_tools in by_category.values():
        category_tools.sort(key=lambda tool: tool.score or 0.0, reverse=True)
        for tool in category_tools[:per_category]:
            chosen.add(tool.repo)

    # Spend anything left over on the highest scorers overall.
    if len(chosen) < limit:
        for tool in sorted(tools, key=lambda tool: tool.score or 0.0, reverse=True):
            if len(chosen) >= limit:
                break
            chosen.add(tool.repo)

    if len(chosen) <= limit:
        return chosen

    ranked = sorted(tools, key=lambda tool: tool.score or 0.0, reverse=True)
    return {tool.repo for tool in ranked if tool.repo in chosen}.intersection(
        {tool.repo for tool in ranked[: limit * 10]}
    ) and set(list(dict.fromkeys(tool.repo for tool in ranked if tool.repo in chosen))[:limit])


def enrich_tools(
    tools: list, fetcher, limit: int, min_remaining: int = 200, selected: set | None = None
) -> tuple[dict, list]:
    """Return (details_by_repo, enriched_tools).

    Only the first `limit` tools, already ordered by a provisional score, are
    enriched; the rest keep their search-result fields. Enrichment also stops
    early when the rate-limit budget runs low, because stalling an hour
    mid-crawl is worse than enriching fewer tools.
    """
    details: dict[str, dict] = {}
    enriched = []
    skipped = 0

    if selected is None:
        selected = {tool.repo for tool in tools[:limit]}

    for tool in tools:
        budget = getattr(fetcher, "remaining", None)
        out_of_budget = budget is not None and budget < min_remaining + REQUESTS_PER_TOOL
        wanted = tool.repo in selected

        if not wanted or out_of_budget:
            if wanted:
                skipped += 1
            enriched.append(tool)
            continue

        try:
            updates, sections = _enrich_one(tool, fetcher)
        except Exception as error:
            # One unreachable repository must not end the crawl.
            print(f"warning: enrich {tool.repo} failed: {type(error).__name__}: {error}")
            enriched.append(tool)
            continue

        if sections:
            details[tool.repo] = sections
        enriched.append(dataclasses.replace(tool, **updates))

    if skipped:
        # Never let a cap look like full coverage.
        print(f"enrich: skipped {skipped} tools, rate-limit budget exhausted")

    return details, enriched
