import json

from goldmine.crawl import run_crawl
from goldmine.models import Tool


def make_tool(repo, **overrides):
    defaults = dict(
        repo=repo,
        summary="a tool",
        categories=["mcp"],
        stars=800,
        contributors=5,
        last_push="2026-08-15",
        created_at="2025-01-01",
        source="test",
    )
    defaults.update(overrides)
    return Tool(**defaults)


def fake_collect(_config, _fetcher, _taxonomy):
    return [make_tool("a/b"), make_tool("c/d", stars=50, contributors=1)]


def crawl(tmp_path, today, collect=fake_collect, **kwargs):
    return run_crawl(
        catalog_dir=tmp_path,
        scoring_path="config/scoring.yaml",
        sources_path="config/sources.yaml",
        taxonomy_path="config/taxonomy.yaml",
        today=today,
        collect=collect,
        fetcher=None,
        enrich=lambda tools, fetcher, limit, min_remaining=0, selected=None: ({}, tools),
        **kwargs,
    )


def rows_of(tmp_path):
    return [json.loads(line) for line in (tmp_path / "tools.jsonl").read_text().splitlines()]


def test_produces_a_scored_and_tiered_catalog(tmp_path):
    crawl(tmp_path, "2026-08-22")

    assert all(row["score"] is not None and row["tier"] is not None for row in rows_of(tmp_path))


def test_a_second_run_fills_in_velocity(tmp_path):
    crawl(tmp_path, "2026-07-23")

    def grown(_c, _f, _t):
        return [make_tool("a/b", stars=1_800), make_tool("c/d", stars=50, contributors=1)]

    crawl(tmp_path, "2026-08-22", collect=grown)

    assert {r["repo"]: r for r in rows_of(tmp_path)}["a/b"]["star_velocity_90d"] > 0


def test_rows_are_sorted_by_score_descending(tmp_path):
    crawl(tmp_path, "2026-08-22")

    scores = [row["score"] for row in rows_of(tmp_path)]
    assert scores == sorted(scores, reverse=True)


def test_an_empty_collection_writes_no_catalog(tmp_path):
    crawl(tmp_path, "2026-08-22", collect=lambda c, f, t: [])

    assert not (tmp_path / "tools.jsonl").exists()


def test_an_empty_collection_leaves_an_existing_catalog_intact(tmp_path):
    crawl(tmp_path, "2026-08-22")
    before = (tmp_path / "tools.jsonl").read_text()

    crawl(tmp_path, "2026-08-23", collect=lambda c, f, t: [])

    assert (tmp_path / "tools.jsonl").read_text() == before


def test_duplicates_from_two_sources_collapse(tmp_path):
    def dupes(_c, _f, _t):
        return [make_tool("a/b", source="github"), make_tool("a/b", source="glama")]

    crawl(tmp_path, "2026-08-22", collect=dupes)

    assert len(rows_of(tmp_path)) == 1


def test_the_configured_sources_include_a_general_oss_tier():
    # Without it, anything outside the Claude ecosystem is unreachable:
    # gallery-dl, instaloader, and firecrawl carry none of the ecosystem topics.
    import yaml

    config = yaml.safe_load(open("config/sources.yaml"))

    assert config.get("oss_topics"), "no general OSS fallback tier configured"
    assert config["max_pages_per_oss_topic"] < config["max_pages_per_topic"]


def test_collect_searches_both_topic_tiers():
    import yaml

    from goldmine.crawl import collect

    searched = []

    class RecordingFetcher:
        def get_json(self, url):
            searched.append(url)
            return {"items": []}

    config = yaml.safe_load(open("config/sources.yaml"))
    config["registries"] = []
    collect(config, RecordingFetcher(), {})

    assert any("topic:mcp-server" in url for url in searched)
    assert any("topic:instagram-scraper" in url for url in searched)
