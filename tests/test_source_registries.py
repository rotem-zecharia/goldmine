import json

from goldmine.sources.registries import extract_repos, fetch_registry


def load(name):
    with open(f"tests/fixtures/{name}") as handle:
        return json.load(handle)


class StubFetcher:
    def __init__(self, bodies):
        self.bodies = list(bodies)
        self.urls = []

    def get_json(self, url):
        self.urls.append(url)
        return self.bodies.pop(0) if self.bodies else None


def test_extracts_owner_repo_pairs_from_the_official_registry():
    # Page 1 of this registry is remote-only servers with no GitHub URL, which
    # is exactly why the walker must not stop on an empty page.
    assert all(repo.count("/") == 1 for repo in extract_repos(load("registry_mcp_official.json")))


def test_extracts_owner_repo_pairs_from_smithery():
    assert all(repo.count("/") == 1 for repo in extract_repos(load("registry_smithery.json")))


def test_extracts_owner_repo_pairs_from_glama():
    assert all(repo.count("/") == 1 for repo in extract_repos(load("registry_glama.json")))


def test_ignores_entries_with_no_github_url():
    assert extract_repos({"servers": [{"repository": {"url": "https://gitlab.com/a/b"}}]}) == []


def test_strips_dot_git_and_trailing_slash():
    body = {"servers": [{"repository": {"url": "https://github.com/Owner/Name.git/"}}]}

    assert extract_repos(body) == ["Owner/Name"]


def test_deduplicates_within_one_page():
    body = {
        "servers": [
            {"repository": {"url": "https://github.com/a/b"}},
            {"repository": {"url": "https://github.com/a/b"}},
        ]
    }

    assert extract_repos(body) == ["a/b"]


def test_ignores_non_repository_github_urls():
    # Sponsor links, user profiles, and gists are not tools.
    body = {
        "servers": [
            {"docs": "https://github.com/sponsors/someone"},
            {"author": "https://github.com/someuser"},
            {"repository": {"url": "https://github.com/real/tool"}},
        ]
    }

    assert extract_repos(body) == ["real/tool"]


def test_a_dead_registry_yields_nothing_instead_of_raising():
    assert fetch_registry(StubFetcher([None]), "https://dead.example?page=1", "page") == []


def test_paginates_until_a_page_is_empty():
    pages = [{"servers": [{"repository": {"url": "https://github.com/a/b"}}]}, {"servers": []}]

    assert fetch_registry(StubFetcher(pages), "https://x.example?page=1", "page") == ["a/b"]


def test_page_style_increments_the_page_number():
    pages = [{"s": [{"u": "https://github.com/a/b"}]}, {"s": []}]
    fetcher = StubFetcher(pages)

    fetch_registry(fetcher, "https://x.example?page=1&pageSize=100", "page")

    assert "page=2" in fetcher.urls[1]


def test_cursor_style_stops_when_there_is_no_next_page():
    body = {
        "servers": [{"repository": {"url": "https://github.com/a/b"}}],
        "pageInfo": {"hasNextPage": False, "endCursor": "x"},
    }
    fetcher = StubFetcher([body])

    assert fetch_registry(fetcher, "https://x.example?first=100", "cursor") == ["a/b"]
    assert len(fetcher.urls) == 1


def test_cursor_style_follows_the_cursor():
    pages = [
        {
            "servers": [{"repository": {"url": "https://github.com/a/b"}}],
            "pageInfo": {"hasNextPage": True, "endCursor": "CURSOR1"},
        },
        {"servers": [], "pageInfo": {"hasNextPage": False}},
    ]
    fetcher = StubFetcher(pages)

    fetch_registry(fetcher, "https://x.example?first=100", "cursor")

    assert "after=CURSOR1" in fetcher.urls[1]


def test_a_page_that_repeats_the_previous_one_stops_the_walk():
    # A registry that ignores pagination would otherwise loop to MAX_PAGES.
    same = {"servers": [{"repository": {"url": "https://github.com/a/b"}}]}
    fetcher = StubFetcher([same] * 10)

    assert fetch_registry(fetcher, "https://x.example?page=1", "page") == ["a/b"]
    assert len(fetcher.urls) <= 2


def test_a_page_with_no_github_urls_does_not_end_the_walk():
    # The official registry's early pages are remote-only servers carrying no
    # GitHub URL. Treating that as the end would collect almost nothing.
    pages = [
        {"servers": [{"name": "remote-only"}], "metadata": {"nextCursor": "c1"}},
        {"servers": [{"repository": {"url": "https://github.com/a/b"}}], "metadata": {}},
    ]

    assert fetch_registry(StubFetcher(pages), "https://x.example?limit=100", "cursor_token") == ["a/b"]


def test_cursor_token_style_appends_the_next_cursor():
    pages = [
        {"servers": [{"u": "https://github.com/a/b"}], "metadata": {"nextCursor": "ai.x/y:1.0.6"}},
        {"servers": [], "metadata": {}},
    ]
    fetcher = StubFetcher(pages)

    fetch_registry(fetcher, "https://x.example?limit=100", "cursor_token")

    assert "cursor=ai.x%2Fy%3A1.0.6" in fetcher.urls[1]


def test_cursor_token_style_stops_when_the_cursor_runs_out():
    pages = [{"servers": [{"u": "https://github.com/a/b"}], "metadata": {}}]
    fetcher = StubFetcher(pages)

    fetch_registry(fetcher, "https://x.example?limit=100", "cursor_token")

    assert len(fetcher.urls) == 1


def test_cursor_style_replaces_rather_than_appends_the_cursor():
    # Appending a second after= makes glama reject the query as an array (400).
    pages = [
        {"servers": [{"u": "https://github.com/a/b"}], "pageInfo": {"hasNextPage": True, "endCursor": "C1"}},
        {"servers": [{"u": "https://github.com/c/d"}], "pageInfo": {"hasNextPage": True, "endCursor": "C2"}},
        {"servers": [], "pageInfo": {"hasNextPage": False}},
    ]
    fetcher = StubFetcher(pages)

    fetch_registry(fetcher, "https://x.example?first=100", "cursor")

    assert fetcher.urls[2].count("after=") == 1
    assert "after=C2" in fetcher.urls[2]


def test_cursor_token_style_also_replaces_its_cursor():
    pages = [
        {"servers": [{"u": "https://github.com/a/b"}], "metadata": {"nextCursor": "c1"}},
        {"servers": [{"u": "https://github.com/c/d"}], "metadata": {"nextCursor": "c2"}},
        {"servers": [], "metadata": {}},
    ]
    fetcher = StubFetcher(pages)

    fetch_registry(fetcher, "https://x.example?limit=100", "cursor_token")

    assert fetcher.urls[2].count("cursor=") == 1
