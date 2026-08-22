from goldmine.models import Tool
from goldmine.merge import attach_velocity, merge_tools


def make_tool(repo, **overrides):
    defaults = dict(
        repo=repo,
        summary="a tool",
        categories=["mcp"],
        stars=100,
        contributors=2,
        last_push="2026-08-01",
        created_at="2025-01-01",
        source="a",
    )
    defaults.update(overrides)
    return Tool(**defaults)


def test_merges_duplicates_into_one_row():
    assert len(merge_tools([make_tool("a/b"), make_tool("a/b")])) == 1


def test_merged_row_takes_the_union_of_categories():
    merged = merge_tools([make_tool("a/b", categories=["mcp"]), make_tool("a/b", categories=["video"])])

    assert sorted(merged[0].categories) == ["mcp", "video"]


def test_merged_row_keeps_the_higher_star_count():
    assert merge_tools([make_tool("a/b", stars=10), make_tool("a/b", stars=900)])[0].stars == 900


def test_merged_row_records_every_source():
    merged = merge_tools([make_tool("a/b", source="github"), make_tool("a/b", source="glama")])

    assert "github" in merged[0].source and "glama" in merged[0].source


def test_merged_row_keeps_the_longer_summary():
    merged = merge_tools([make_tool("a/b", summary="short"), make_tool("a/b", summary="a longer one")])

    assert merged[0].summary == "a longer one"


def test_merge_is_case_insensitive_on_the_repo_name():
    # GitHub repo names are case-insensitive; two spellings are one tool.
    merged = merge_tools([make_tool("Owner/Repo"), make_tool("owner/repo")])

    assert len(merged) == 1


def test_merged_row_keeps_the_richer_flags():
    merged = merge_tools(
        [make_tool("a/b", has_license=False), make_tool("a/b", has_license=True)]
    )

    assert merged[0].has_license is True


def test_velocity_is_computed_against_the_previous_snapshot():
    previous = {"a/b": {"stars": 100, "generated_at": "2026-07-23"}}

    tool = attach_velocity(make_tool("a/b", stars=200), previous, today="2026-08-22")

    assert round(tool.star_velocity_90d) == 100


def test_velocity_is_none_on_a_first_crawl():
    assert attach_velocity(make_tool("a/b"), {}, today="2026-08-22").star_velocity_90d is None


def test_velocity_is_none_when_no_time_has_passed():
    previous = {"a/b": {"stars": 100, "generated_at": "2026-08-22"}}

    assert attach_velocity(make_tool("a/b"), previous, today="2026-08-22").star_velocity_90d is None


def test_velocity_lookup_is_case_insensitive():
    previous = {"owner/repo": {"stars": 100, "generated_at": "2026-07-23"}}

    assert attach_velocity(make_tool("Owner/Repo", stars=200), previous, "2026-08-22").star_velocity_90d


def test_a_very_short_window_does_not_manufacture_a_huge_velocity():
    # One day of data extrapolated to 30 would make any noise look explosive.
    previous = {"a/b": {"stars": 100, "generated_at": "2026-08-21"}}

    tool = attach_velocity(make_tool("a/b", stars=110), previous, today="2026-08-22")

    assert tool.star_velocity_90d is None


def test_previous_enrichment_is_carried_forward():
    from goldmine.merge import carry_forward_enrichment

    # The nightly budget only reaches a fraction of the catalog. Without this
    # the catalog forgets everything it learned the night before.
    previous = {
        "a/b": {
            "stars": 100,
            "generated_at": "2026-07-23",
            "contributors": 42,
            "install": "pip install thing",
            "has_releases": True,
            "has_install_section": True,
        }
    }

    tool = carry_forward_enrichment(make_tool("a/b", contributors=None), previous)

    assert tool.contributors == 42
    assert tool.install == "pip install thing"
    assert tool.has_releases is True


def test_a_fresh_enrichment_wins_over_the_carried_value():
    from goldmine.merge import carry_forward_enrichment

    previous = {"a/b": {"stars": 1, "generated_at": "2026-07-23", "contributors": 5}}

    tool = carry_forward_enrichment(make_tool("a/b", contributors=9), previous)

    assert tool.contributors == 9


def test_carry_forward_is_a_no_op_without_a_previous_row():
    from goldmine.merge import carry_forward_enrichment

    tool = make_tool("a/b", contributors=None)

    assert carry_forward_enrichment(tool, {}).contributors is None
