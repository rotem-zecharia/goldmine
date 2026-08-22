"""MCP registry clients.

The three registries disagree on payload shape and pagination, so rather than
modelling each schema we walk the JSON and pull out every github.com repository
URL we find. That is the only field we need: everything else about a repository
comes from the GitHub API afterwards. It also means a registry can restructure
its response without breaking the crawl.
"""

from __future__ import annotations

import re
from urllib.parse import quote

GITHUB_URL = re.compile(r"https?://(?:www\.)?github\.com/([^/\s\"']+)/([^/\s\"'#?)\]]+)")
MAX_PAGES = 50

# github.com paths that look like owner/repo but are not repositories.
RESERVED_OWNERS = {
    "sponsors",
    "orgs",
    "topics",
    "features",
    "marketplace",
    "apps",
    "settings",
    "login",
    "about",
    "pricing",
    "collections",
    "explore",
    "notifications",
    "search",
}


def _clean(name: str) -> str:
    return name.removesuffix(".git").rstrip("/.,")


def extract_repos(body) -> list[str]:
    """Walk any JSON body and return the unique owner/repo pairs inside it."""
    found: list[str] = []
    seen: set[str] = set()

    def walk(node):
        if isinstance(node, dict):
            for value in node.values():
                walk(value)
        elif isinstance(node, list):
            for value in node:
                walk(value)
        elif isinstance(node, str):
            for match in GITHUB_URL.finditer(node):
                owner, name = match.group(1), _clean(match.group(2))
                if owner.lower() in RESERVED_OWNERS or not name:
                    continue
                repo = f"{owner}/{name}"
                if repo not in seen:
                    seen.add(repo)
                    found.append(repo)

    walk(body)
    return found


def _next_url(url: str, style: str, body, page: int) -> str | None:
    if style == "cursor_token":
        # The official MCP registry paginates with an opaque cursor in
        # metadata.nextCursor and has no hasNextPage flag.
        cursor = ((body or {}).get("metadata") or {}).get("nextCursor")
        if not cursor:
            return None
        base = re.sub(r"&cursor=[^&]*", "", url)
        return f"{base}&cursor={quote(cursor, safe='')}"

    if style == "page":
        if "page=" not in url:
            return None
        return re.sub(r"(?<![a-zA-Z])page=\d+", f"page={page + 1}", url, count=1)

    page_info = (body or {}).get("pageInfo") or {}
    cursor = page_info.get("endCursor")
    if not cursor or not page_info.get("hasNextPage"):
        return None
    # Replace the previous cursor rather than appending a second one: glama
    # rejects a repeated after= as an array with a 400.
    base = re.sub(r"&after=[^&]*", "", url)
    return f"{base}&after={quote(cursor, safe='')}"


def fetch_registry(fetcher, url: str, style: str) -> list[str]:
    repos: list[str] = []
    seen: set[str] = set()
    current = url
    previous_page: tuple | None = None

    for page in range(1, MAX_PAGES + 1):
        body = fetcher.get_json(current)
        if not body:
            break

        page_repos = extract_repos(body)

        # A page with no repositories is normal, not the end: the official
        # registry's first pages are remote-only servers that carry no GitHub
        # URL at all. Stop on an exhausted cursor instead.

        # A registry that ignores its own pagination parameters would otherwise
        # hand back the same page until MAX_PAGES.
        signature = tuple(page_repos)
        if page_repos and signature == previous_page:
            break
        previous_page = signature

        for repo in page_repos:
            if repo not in seen:
                seen.add(repo)
                repos.append(repo)

        nxt = _next_url(current, style, body, page)
        if not nxt:
            break
        current = nxt

    return repos
