import json

from goldmine.sources.github import categorize, normalize_repo, search_topic

TAXONOMY = {
    "video": ["video", "ffmpeg", "multimodal"],
    "mcp": ["mcp", "mcp-server"],
    "scraping": ["scraper", "crawler"],
}


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


def test_normalize_extracts_the_fields_the_scorer_needs():
    tool = normalize_repo(load("github_repo.json"), categories=["video"], source="test")

    assert tool.repo.count("/") == 1
    assert tool.stars > 0
    assert tool.last_push.count("-") == 2
    assert tool.created_at.count("-") == 2
    assert "video" in tool.categories


def test_normalize_handles_a_missing_description():
    raw = load("github_repo.json") | {"description": None}

    assert normalize_repo(raw, categories=[], source="test").summary == ""


def test_normalize_truncates_a_runaway_description():
    raw = load("github_repo.json") | {"description": "x" * 500}

    assert len(normalize_repo(raw, categories=[], source="test").summary) <= 200


def test_normalize_reads_archived_and_fork_flags():
    raw = load("github_repo.json") | {"archived": True, "fork": True}
    tool = normalize_repo(raw, categories=[], source="test")

    assert tool.archived and tool.is_fork


def test_normalize_collapses_whitespace_in_a_description():
    # Newlines in a description would corrupt the grep-friendly index table.
    raw = load("github_repo.json") | {"description": "line one\nline two\ttabbed"}

    assert "\n" not in normalize_repo(raw, categories=[], source="test").summary


def test_normalize_escapes_pipes_that_would_break_the_index_table():
    raw = load("github_repo.json") | {"description": "a | b"}

    assert "|" not in normalize_repo(raw, categories=[], source="test").summary


def test_categorize_maps_repo_topics_onto_catalog_categories():
    assert set(categorize(["ffmpeg", "mcp-server"], TAXONOMY)) == {"video", "mcp"}


def test_categorize_ignores_unknown_topics():
    assert categorize(["unrelated-topic"], TAXONOMY) == []


def test_normalize_merges_search_category_with_topic_categories():
    tool = normalize_repo(
        load("github_repo.json"), categories=["claude-code"], source="test", taxonomy=TAXONOMY
    )

    # The fixture repo carries ffmpeg/multimodal/mcp-server topics.
    assert "claude-code" in tool.categories
    assert "video" in tool.categories and "mcp" in tool.categories


def test_search_topic_returns_tools_tagged_with_the_category():
    tools = search_topic(StubFetcher([load("github_search.json")]), "mcp-server", ["mcp"], 1)

    assert tools
    assert all("mcp" in tool.categories for tool in tools)


def test_search_topic_stops_at_max_pages():
    fetcher = StubFetcher([load("github_search.json"), load("github_search.json")])

    search_topic(fetcher, "mcp-server", ["mcp"], max_pages=1)

    assert len(fetcher.urls) == 1


def test_search_topic_requests_the_topic_it_was_given():
    fetcher = StubFetcher([load("github_search.json")])

    search_topic(fetcher, "claude-skills", ["skill"], max_pages=1)

    assert "topic:claude-skills" in fetcher.urls[0]


def test_search_topic_survives_an_empty_result():
    assert search_topic(StubFetcher([{"items": []}]), "nothing", [], max_pages=1) == []


def test_search_topic_survives_a_dead_response():
    assert search_topic(StubFetcher([None]), "nothing", [], max_pages=1) == []
