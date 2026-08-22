from goldmine.models import Tool
from goldmine.tiering import assign_tiers

TODAY = "2026-08-22"


def make_tool(repo, score, category="mcp", **overrides):
    defaults = dict(
        repo=repo,
        summary="a tool",
        categories=[category],
        stars=1_000,
        contributors=5,
        last_push="2026-08-15",
        created_at="2025-01-01",
        source="test",
        score=score,
    )
    defaults.update(overrides)
    return Tool(**defaults)


def tiers_of(tools):
    return {tool.repo: tool.tier for tool in assign_tiers(tools, today=TODAY)}


def test_top_scorer_in_a_healthy_category_is_established():
    tiered = tiers_of([make_tool(f"o/r{i}", score=float(i)) for i in range(100)])

    assert tiered["o/r99"] == "established"
    assert tiered["o/r50"] != "established"


def test_established_requires_recent_activity():
    tools = [make_tool(f"o/r{i}", score=float(i)) for i in range(99)]
    tools.append(make_tool("o/stale", score=200.0, last_push="2026-01-01"))

    assert tiers_of(tools)["o/stale"] != "established"


def test_established_requires_three_contributors():
    tools = [make_tool(f"o/r{i}", score=float(i)) for i in range(99)]
    tools.append(make_tool("o/solo", score=200.0, contributors=1))

    assert tiers_of(tools)["o/solo"] != "established"


def test_percentile_is_computed_per_category_not_globally():
    big = [make_tool(f"o/big{i}", score=90.0 + i, category="mcp") for i in range(100)]
    small = [make_tool(f"o/small{i}", score=10.0 + i, category="niche") for i in range(20)]

    assert tiers_of(big + small)["o/small19"] == "established"


def test_a_tool_in_two_categories_takes_its_best_tier():
    tools = [make_tool(f"o/r{i}", score=float(i), category="mcp") for i in range(100)]
    tools += [make_tool(f"o/n{i}", score=float(i), category="niche") for i in range(20)]
    crossover = make_tool("o/cross", score=19.5)
    crossover = Tool.from_json(crossover.to_json() | {"categories": ["mcp", "niche"]})

    assert tiers_of(tools + [crossover])["o/cross"] == "established"


def test_fast_growing_young_tool_is_rising():
    tools = [make_tool(f"o/r{i}", score=float(i)) for i in range(100)]
    tools.append(make_tool("o/rocket", score=30.0, created_at="2026-05-01", star_velocity_90d=400.0))

    assert tiers_of(tools)["o/rocket"] == "rising"


def test_everything_else_is_watch():
    assert tiers_of([make_tool(f"o/r{i}", score=float(i)) for i in range(100)])["o/r0"] == "watch"


def test_every_tool_gets_a_tier():
    tiered = assign_tiers([make_tool(f"o/r{i}", score=float(i)) for i in range(37)], today=TODAY)

    assert all(tool.tier is not None for tool in tiered)


def test_unknown_contributors_cannot_reach_established():
    # Established is a claim about a real team; we cannot make it without data.
    tools = [make_tool(f"o/r{i}", score=float(i)) for i in range(99)]
    tools.append(make_tool("o/unknown", score=200.0, contributors=None))

    assert tiers_of(tools)["o/unknown"] != "established"
