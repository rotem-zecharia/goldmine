"""Second pass over the candidates worth spending requests on.

Search results carry stars and dates but not contributor counts, release
history, or README text. Each of those costs a request, so only candidates that
could plausibly reach the established tier are enriched.

Consequence worth knowing: a repository that is never enriched has no
contributor count, and the established tier requires three. The enrichment
budget is therefore the ceiling on how many tools can ever be established.
"""

from __future__ import annotations

import dataclasses
import re

from goldmine.readme import extract_install_command, extract_sections, has_install_section

CONTRIBUTORS_URL = "https://api.github.com/repos/{repo}/contributors?per_page=1&anon=1"
RELEASES_URL = "https://api.github.com/repos/{repo}/releases?per_page=1"
README_URL = "https://api.github.com/repos/{repo}/readme"

LAST_PAGE = re.compile(r'[?&]page=(\d+)>;\s*rel="last"')
REQUESTS_PER_TOOL = 4


def contributor_count(fetcher, repo: str) -> int:
    """With per_page=1, the last page number is the contributor count.

    Paging through contributors would cost one request per contributor; the
    Link header gives the same number in one.
    """
    body, headers = fetcher.get_json_meta(CONTRIBUTORS_URL.format(repo=repo))
    if not body:
        return 0

    match = LAST_PAGE.search(headers.get("Link", ""))
    if match:
        return int(match.group(1))

    # No Link header means a single page, which at per_page=1 is one contributor.
    return len(body) if isinstance(body, list) else 0


def select_for_enrichment(tools: list, limit: int, per_category: int) -> list:
    """Pick which repositories are worth spending requests on, in priority order.

    Taking the global top N starves every small category: 3,400 MCP servers
    would consume the whole budget, and the leader of a niche category would
    never be enriched, so it could never clear its own percentile gate.

    Order matters as much as membership. The rate-limit guard can cut the pass
    short, so the sequence round-robins across categories - every category's
    leader, then every category's runner-up - rather than running in global
    score order, which drains the budget on the largest category first.
    """
    by_category: dict[str, list] = {}
    for tool in tools:
        for category in tool.categories or ["_uncategorised"]:
            by_category.setdefault(category, []).append(tool)

    ranked = {
        category: sorted(items, key=lambda tool: tool.score or 0.0, reverse=True)
        for category, items in by_category.items()
    }
    # Largest categories first within a round, so crowded pools still get their
    # leaders early.
    category_order = sorted(ranked, key=lambda name: -len(ranked[name]))

    chosen: list = []
    seen: set = set()

    def take(repo: str) -> None:
        if repo not in seen:
            seen.add(repo)
            chosen.append(repo)

    for rank in range(per_category):
        for category in category_order:
            items = ranked[category]
            if rank < len(items):
                take(items[rank].repo)

    # Spend whatever is left on the highest scorers overall.
    for tool in sorted(tools, key=lambda tool: tool.score or 0.0, reverse=True):
        if len(chosen) >= limit:
            break
        take(tool.repo)

    return chosen[:limit]


def _enrich_one(tool, fetcher) -> tuple[dict, dict]:
    """Return (field updates, README sections) for one tool."""
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


def enrich_tools(
    tools: list, fetcher, limit: int, min_remaining: int = 200, selected: list | None = None
) -> tuple[dict, list]:
    """Return (details_by_repo, enriched_tools).

    Enrichment stops early when the rate-limit budget runs low: stalling an hour
    mid-crawl is worse than enriching fewer tools.
    """
    if selected is None:
        selected = [tool.repo for tool in tools[:limit]]

    by_repo = {tool.repo: tool for tool in tools}
    details: dict[str, dict] = {}
    updated: dict = {}
    skipped = 0

    for repo in selected:
        tool = by_repo.get(repo)
        if tool is None:
            continue

        budget = getattr(fetcher, "remaining", None)
        if budget is not None and budget < min_remaining + REQUESTS_PER_TOOL:
            skipped += 1
            continue

        try:
            changes, sections = _enrich_one(tool, fetcher)
        except Exception as error:
            # One unreachable repository must not end the crawl.
            print(f"warning: enrich {repo} failed: {type(error).__name__}: {error}")
            continue

        if sections:
            details[repo] = sections
        updated[repo] = dataclasses.replace(tool, **changes)

    if skipped:
        # Never let a cap look like full coverage.
        print(f"enrich: skipped {skipped} tools, rate-limit budget exhausted")

    return details, [updated.get(tool.repo, tool) for tool in tools]
