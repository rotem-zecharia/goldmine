import dataclasses

from goldmine.enrich import contributor_count, enrich_tools
from goldmine.models import Tool


class StubFetcher:
    """Serves canned responses per URL substring."""

    def __init__(self, routes, headers=None):
        self.routes = routes
        self.header_routes = headers or {}
        self.calls = []

    def _match(self, url, table):
        for needle, value in table.items():
            if needle in url:
                return value
        return None

    def get_json(self, url):
        self.calls.append(url)
        return self._match(url, self.routes)

    def get_json_meta(self, url):
        self.calls.append(url)
        return self._match(url, self.routes), (self._match(url, self.header_routes) or {})

    def get_text(self, url):
        self.calls.append(url)
        return self._match(url, self.routes)


LAST_PAGE_171 = {
    "Link": '<https://api.github.com/repositories/1/contributors?per_page=1&page=2>; rel="next", '
    '<https://api.github.com/repositories/1/contributors?per_page=1&page=171>; rel="last"'
}


def make_tool(repo="a/b", **overrides):
    defaults = dict(
        repo=repo,
        summary="a tool",
        categories=["mcp"],
        stars=100,
        contributors=0,
        last_push="2026-08-01",
        created_at="2025-01-01",
        source="test",
    )
    defaults.update(overrides)
    return Tool(**defaults)


def test_contributor_count_reads_the_last_page_number():
    # per_page=1 means the last page number IS the contributor count.
    fetcher = StubFetcher({"contributors": [{"login": "x"}]}, headers={"contributors": LAST_PAGE_171})

    assert contributor_count(fetcher, "a/b") == 171


def test_contributor_count_of_a_single_contributor_repo_has_no_link_header():
    fetcher = StubFetcher({"contributors": [{"login": "x"}]}, headers={})

    assert contributor_count(fetcher, "a/b") == 1


def test_contributor_count_of_an_empty_repo_is_zero():
    fetcher = StubFetcher({"contributors": []}, headers={})

    assert contributor_count(fetcher, "a/b") == 0


def test_contributor_count_survives_a_missing_response():
    assert contributor_count(StubFetcher({}), "a/b") == 0


def test_enrich_fills_in_contributors():
    fetcher = StubFetcher(
        {"contributors": [{"login": "x"}], "releases": [], "readme": None},
        headers={"contributors": LAST_PAGE_171},
    )

    _, tools = enrich_tools([make_tool()], fetcher, limit=1)

    assert tools[0].contributors == 171


def test_enrich_reads_readme_sections_and_install_command():
    readme = "# t\n\n## Installation\n\n```bash\npip install thing\n```\n\n## Features\n\n- does x\n"
    fetcher = StubFetcher(
        {
            "readme": {"download_url": "https://raw.example/README.md"},
            "raw.example": readme,
            "contributors": [],
            "releases": [{"tag_name": "v1"}],
        }
    )

    details, tools = enrich_tools([make_tool()], fetcher, limit=1)

    assert details["a/b"]["features"].startswith("- does x")
    assert tools[0].install == "pip install thing"
    assert tools[0].has_install_section is True
    assert tools[0].has_releases is True


def test_enrich_respects_the_budget():
    fetcher = StubFetcher({"contributors": [], "releases": [], "readme": None})

    _, tools = enrich_tools([make_tool("a/b"), make_tool("c/d")], fetcher, limit=1)

    assert not any("c/d" in call for call in fetcher.calls)
    assert len(tools) == 2


def test_enrich_survives_a_repo_that_errors():
    class Exploding(StubFetcher):
        def get_json(self, url):
            if "readme" in url:
                raise RuntimeError("boom")
            return super().get_json(url)

    fetcher = Exploding({"contributors": [], "releases": []})

    _, tools = enrich_tools([make_tool()], fetcher, limit=1)

    assert len(tools) == 1


class BudgetedFetcher(StubFetcher):
    def __init__(self, routes, remaining):
        super().__init__(routes)
        self.remaining = remaining


def test_enrichment_stops_when_the_rate_limit_budget_runs_low():
    # Sleeping out a full hour mid-crawl is worse than enriching fewer tools.
    fetcher = BudgetedFetcher({"contributors": [], "releases": [], "readme": None}, remaining=5)
    tools = [make_tool(f"o/r{i}") for i in range(10)]

    _, enriched = enrich_tools(tools, fetcher, limit=10, min_remaining=100)

    assert len(enriched) == 10
    assert not fetcher.calls, "should not have started with the budget already spent"


def test_enrichment_proceeds_when_the_budget_is_healthy():
    fetcher = BudgetedFetcher({"contributors": [], "releases": [], "readme": None}, remaining=5000)

    _, enriched = enrich_tools([make_tool()], fetcher, limit=1, min_remaining=100)

    assert fetcher.calls


def test_an_unknown_budget_does_not_block_enrichment():
    fetcher = StubFetcher({"contributors": [], "releases": [], "readme": None})

    enrich_tools([make_tool()], fetcher, limit=1, min_remaining=100)

    assert fetcher.calls


def test_reports_how_many_tools_were_skipped_for_budget(capsys):
    fetcher = BudgetedFetcher({"contributors": [], "releases": [], "readme": None}, remaining=5)

    enrich_tools([make_tool(f"o/r{i}") for i in range(10)], fetcher, limit=10, min_remaining=100)

    # A silent cap reads as "we covered everything" when we did not.
    assert "skipped" in capsys.readouterr().out.lower()


def test_selection_covers_every_category_not_just_the_global_leaders():
    from goldmine.enrich import select_for_enrichment

    big = [make_tool(f"o/big{i}", categories=["mcp"], stars=1000 - i) for i in range(50)]
    niche = [make_tool(f"o/niche{i}", categories=["scraping"], stars=10 - i) for i in range(5)]
    for tools in (big, niche):
        for index, tool in enumerate(tools):
            tools[index] = dataclasses.replace(tool, score=float(tool.stars))

    chosen = select_for_enrichment(big + niche, limit=20, per_category=3)

    # The niche leader must be reachable even though 50 mcp tools outscore it.
    assert "o/niche0" in chosen


def test_selection_respects_the_overall_limit():
    from goldmine.enrich import select_for_enrichment

    tools = [
        dataclasses.replace(make_tool(f"o/r{i}", categories=["mcp"]), score=float(100 - i))
        for i in range(100)
    ]

    assert len(select_for_enrichment(tools, limit=10, per_category=50)) == 10


def test_selection_prefers_the_highest_scoring_within_a_category():
    from goldmine.enrich import select_for_enrichment

    tools = [
        dataclasses.replace(make_tool(f"o/r{i}", categories=["mcp"]), score=float(i))
        for i in range(10)
    ]

    chosen = select_for_enrichment(tools, limit=2, per_category=2)

    assert "o/r9" in chosen and "o/r0" not in chosen


def test_selection_handles_a_tool_with_no_categories():
    from goldmine.enrich import select_for_enrichment

    tools = [dataclasses.replace(make_tool("o/x", categories=[]), score=99.0)]

    assert select_for_enrichment(tools, limit=5, per_category=2) == ["o/x"]


def test_enrich_only_touches_the_selected_repos():
    fetcher = StubFetcher({"contributors": [], "releases": [], "readme": None})
    tools = [make_tool("a/b"), make_tool("c/d")]

    enrich_tools(tools, fetcher, limit=2, selected={"a/b"})

    assert not any("c/d" in call for call in fetcher.calls)


def test_selection_order_round_robins_across_categories():
    from goldmine.enrich import select_for_enrichment

    # Fair selection is not enough: if enrichment then runs in global score
    # order, a big category drains the budget before a niche leader is reached.
    big = [
        dataclasses.replace(make_tool(f"o/big{i}", categories=["mcp"]), score=1000.0 - i)
        for i in range(50)
    ]
    niche = [dataclasses.replace(make_tool("o/niche", categories=["scraping"]), score=1.0)]

    order = select_for_enrichment(big + niche, limit=100, per_category=5)

    assert order.index("o/niche") < 5, "niche leader must be enriched early, not last"


def test_selection_returns_an_ordered_sequence():
    from goldmine.enrich import select_for_enrichment

    tools = [
        dataclasses.replace(make_tool(f"o/r{i}", categories=["mcp"]), score=float(i))
        for i in range(5)
    ]

    order = select_for_enrichment(tools, limit=5, per_category=5)

    assert order[0] == "o/r4"


def test_enrich_follows_the_given_order_under_a_tight_budget():
    class Draining(StubFetcher):
        def __init__(self, routes):
            super().__init__(routes)
            self.remaining = 210

        def get_json(self, url):
            self.remaining -= 1
            return super().get_json(url)

        def get_json_meta(self, url):
            self.remaining -= 1
            return super().get_json_meta(url)

        def get_text(self, url):
            self.remaining -= 1
            return super().get_text(url)

    fetcher = Draining({"contributors": [], "releases": [], "readme": None})
    tools = [make_tool("a/first"), make_tool("b/second"), make_tool("c/third")]

    enrich_tools(tools, fetcher, limit=3, min_remaining=200, selected=["c/third", "a/first"])

    assert any("c/third" in call for call in fetcher.calls)


def test_selection_can_exclude_repos_already_covered():
    from goldmine.enrich import select_for_enrichment

    # A backfill should spend its budget on what is missing, not redo what is
    # already on disk.
    tools = [
        dataclasses.replace(make_tool(f"o/r{i}", categories=["mcp"]), score=float(100 - i))
        for i in range(5)
    ]

    order = select_for_enrichment(tools, limit=5, per_category=5, exclude={"o/r0", "o/r1"})

    assert "o/r0" not in order and "o/r1" not in order
    assert "o/r2" in order


def test_excluding_everything_selects_nothing():
    from goldmine.enrich import select_for_enrichment

    tools = [dataclasses.replace(make_tool("o/r0"), score=1.0)]

    assert select_for_enrichment(tools, limit=5, per_category=5, exclude={"o/r0"}) == []
