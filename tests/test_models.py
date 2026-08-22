import pytest

from goldmine.models import Tool, ValidationError, validate_row


def make_tool(**overrides):
    defaults = dict(
        repo="jordanrendric/claude-video-vision",
        summary="Give Claude the ability to watch and understand videos",
        categories=["video", "claude-plugin"],
        install="claude plugin install claude-video-vision",
        stars=1253,
        contributors=7,
        last_push="2026-08-07",
        created_at="2025-11-02",
        open_issues=4,
        closed_issues=61,
        archived=False,
        is_fork=False,
        has_license=True,
        has_releases=True,
        has_install_section=True,
        source="github:topic:claude-code",
    )
    defaults.update(overrides)
    return Tool(**defaults)


def test_round_trips_through_json():
    tool = make_tool()

    assert Tool.from_json(tool.to_json()) == tool


def test_owner_and_name_split_from_repo():
    tool = make_tool()

    assert tool.owner == "jordanrendric"
    assert tool.name == "claude-video-vision"


def test_detail_filename_is_filesystem_safe():
    assert make_tool().detail_filename == "jordanrendric__claude-video-vision.md"


def test_optional_score_fields_default_to_none():
    tool = make_tool()

    assert tool.score is None
    assert tool.tier is None
    assert tool.star_velocity_90d is None


def test_validate_row_accepts_a_complete_row():
    validate_row(make_tool().to_json() | {"score": 88.0, "tier": "established"})


def test_validate_row_rejects_a_missing_required_field():
    row = make_tool().to_json()
    del row["stars"]

    with pytest.raises(ValidationError, match="stars"):
        validate_row(row)


def test_validate_row_rejects_an_unknown_tier():
    with pytest.raises(ValidationError, match="tier"):
        validate_row(make_tool().to_json() | {"score": 88.0, "tier": "legendary"})


def test_validate_row_rejects_a_malformed_repo():
    with pytest.raises(ValidationError, match="repo"):
        validate_row(make_tool().to_json() | {"repo": "no-slash-here"})
