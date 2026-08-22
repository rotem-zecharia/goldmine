"""Second pass over the top candidates.

Search results carry stars and dates but not contributor counts, closed-issue
counts, or README text. Those cost extra requests each, so only the candidates
that could plausibly reach the established tier are enriched.
"""

from __future__ import annotations

import dataclasses

from goldmine.readme import extract_install_command, extract_sections, has_install_section

CONTRIBUTORS_URL = "https://api.github.com/repos/{repo}/contributors?per_page=1&anon=1"
SEARCH_CLOSED = "https://api.github.com/search/issues?q=repo:{repo}+type:issue+state:closed&per_page=1"
RELEASES_URL = "https://api.github.com/repos/{repo}/releases?per_page=1"
README_URL = "https://api.github.com/repos/{repo}/readme"


def contributor_count(fetcher, repo: str) -> int:
    """Read the count from the Link header's last page rather than paging."""
    body = fetcher.get_json(CONTRIBUTORS_URL.format(repo=repo))
    if body is None:
        return 0
    # Without pagination metadata we can only see the page we asked for.
    return len(body) if isinstance(body, list) else 0


def enrich_tools(tools: list, fetcher, limit: int) -> tuple[dict, list]:
    """Return (details_by_repo, enriched_tools).

    Only the first `limit` tools (already sorted by a provisional score) are
    enriched; the rest keep their search-result fields.
    """
    details: dict[str, dict] = {}
    enriched = []

    for index, tool in enumerate(tools):
        if index >= limit:
            enriched.append(tool)
            continue

        updates: dict = {}

        readme = fetcher.get_json(README_URL.format(repo=tool.repo))
        text = ""
        if readme and readme.get("download_url"):
            text = fetcher.get_text(readme["download_url"]) or ""

        if text:
            sections = extract_sections(text)
            if sections:
                details[tool.repo] = sections
            updates["has_install_section"] = has_install_section(text)
            command = extract_install_command(text)
            if command:
                updates["install"] = command

        releases = fetcher.get_json(RELEASES_URL.format(repo=tool.repo))
        updates["has_releases"] = bool(releases)

        closed = fetcher.get_json(SEARCH_CLOSED.format(repo=tool.repo))
        if closed and "total_count" in closed:
            updates["closed_issues"] = closed["total_count"]

        count = contributor_count(fetcher, tool.repo)
        if count:
            updates["contributors"] = max(tool.contributors, count)

        enriched.append(dataclasses.replace(tool, **updates))

    return details, enriched
