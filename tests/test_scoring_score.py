from goldmine.models import Tool
from goldmine.scoring import load_weights, score_tool

TODAY = "2026-08-22"
WEIGHTS = load_weights("config/scoring.yaml")


def make_tool(**overrides):
    defaults = dict(
        repo="owner/name",
        summary="a tool",
        categories=["video"],
        stars=1_500,
        contributors=6,
        last_push="2026-08-10",
        created_at="2025-01-01",
        open_issues=3,
        closed_issues=40,
        has_license=True,
        has_releases=True,
        has_install_section=True,
        source="test",
    )
    defaults.update(overrides)
    return Tool(**defaults)


def test_score_is_within_range():
    assert 0.0 <= score_tool(make_tool(), WEIGHTS, today=TODAY) <= 100.0


def test_a_healthy_repo_beats_a_neglected_one():
    neglected = make_tool(last_push="2025-01-05", contributors=1, closed_issues=2, open_issues=40)

    assert score_tool(make_tool(), WEIGHTS, today=TODAY) > score_tool(neglected, WEIGHTS, today=TODAY)


def test_archived_is_a_hard_demotion():
    assert score_tool(make_tool(archived=True), WEIGHTS, today=TODAY) < (
        score_tool(make_tool(), WEIGHTS, today=TODAY) / 2
    )


def test_unresolved_fork_is_penalised():
    assert score_tool(make_tool(is_fork=True), WEIGHTS, today=TODAY) < score_tool(
        make_tool(), WEIGHTS, today=TODAY
    )


def test_brand_new_with_no_traction_is_penalised():
    assert score_tool(make_tool(created_at="2026-08-10", stars=4), WEIGHTS, today=TODAY) < 30.0


def test_brand_new_with_real_traction_is_not_penalised():
    breakout = make_tool(created_at="2026-08-10", stars=3_000)

    assert score_tool(breakout, WEIGHTS, today=TODAY) > 40.0


def test_a_missing_velocity_does_not_lower_the_score():
    unknown = make_tool(star_velocity_90d=None)
    stagnant = make_tool(star_velocity_90d=0.0)

    assert score_tool(unknown, WEIGHTS, today=TODAY) > score_tool(stagnant, WEIGHTS, today=TODAY)


def test_weights_file_sums_to_one():
    assert round(sum(WEIGHTS["weights"].values()), 6) == 1.0
