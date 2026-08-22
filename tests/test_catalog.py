import json

import pytest

from goldmine.catalog import CatalogShrank, load_previous, write_catalog
from goldmine.models import Tool


def make_tool(repo, **overrides):
    defaults = dict(
        repo=repo,
        summary="a tool",
        categories=["mcp"],
        stars=500,
        contributors=4,
        last_push="2026-08-15",
        created_at="2025-01-01",
        source="test",
        score=70.0,
        tier="established",
    )
    defaults.update(overrides)
    return Tool(**defaults)


def test_writes_one_jsonl_line_per_tool(tmp_path):
    write_catalog([make_tool("a/b"), make_tool("c/d")], tmp_path, today="2026-08-22")

    assert len((tmp_path / "tools.jsonl").read_text().strip().splitlines()) == 2


def test_every_written_row_passes_schema_validation(tmp_path):
    write_catalog([make_tool("a/b")], tmp_path, today="2026-08-22")

    row = json.loads((tmp_path / "tools.jsonl").read_text().strip())
    assert row["repo"] == "a/b" and row["tier"] == "established"


def test_writes_a_grep_friendly_index(tmp_path):
    write_catalog([make_tool("a/b", summary="does a thing")], tmp_path, today="2026-08-22")

    index = (tmp_path / "index.md").read_text()
    assert "a/b" in index and "does a thing" in index


def test_index_rows_stay_on_one_line_each(tmp_path):
    # grep -n is the skill's primary access path; a wrapped row breaks it.
    write_catalog([make_tool("a/b"), make_tool("c/d")], tmp_path, today="2026-08-22")

    body = (tmp_path / "index.md").read_text().strip().splitlines()
    assert len(body) == 4  # header, separator, one line per tool
    assert all(line.startswith("|") and line.endswith("|") for line in body)


def test_index_includes_tags_so_vocabulary_expansion_can_match(tmp_path):
    tool = make_tool("a/b", tags=["ffmpeg", "whisper"])

    write_catalog([tool], tmp_path, today="2026-08-22")

    assert "ffmpeg" in (tmp_path / "index.md").read_text()


def test_writes_meta_with_the_generation_date(tmp_path):
    write_catalog([make_tool("a/b")], tmp_path, today="2026-08-22")

    meta = json.loads((tmp_path / "meta.json").read_text())
    assert meta["generated_at"] == "2026-08-22" and meta["count"] == 1


def test_writes_detail_files_when_sections_are_supplied(tmp_path):
    details = {"a/b": {"features": "- does things", "limitations": "- not everything"}}

    write_catalog([make_tool("a/b")], tmp_path, today="2026-08-22", details=details)

    text = (tmp_path / "details" / "a__b.md").read_text()
    assert "does things" in text and "not everything" in text


def test_refuses_to_write_a_catalog_that_shrank_past_the_floor(tmp_path):
    write_catalog([make_tool(f"o/r{i}") for i in range(100)], tmp_path, today="2026-08-22")

    with pytest.raises(CatalogShrank):
        write_catalog([make_tool("o/r0")], tmp_path, today="2026-08-23")


def test_allows_a_small_shrink(tmp_path):
    write_catalog([make_tool(f"o/r{i}") for i in range(100)], tmp_path, today="2026-08-22")

    write_catalog([make_tool(f"o/r{i}") for i in range(95)], tmp_path, today="2026-08-23")


def test_the_shrink_guard_can_be_overridden_deliberately(tmp_path):
    write_catalog([make_tool(f"o/r{i}") for i in range(100)], tmp_path, today="2026-08-22")

    write_catalog([make_tool("o/r0")], tmp_path, today="2026-08-23", allow_shrink=True)

    assert len((tmp_path / "tools.jsonl").read_text().strip().splitlines()) == 1


def test_a_failed_write_leaves_the_previous_catalog_intact(tmp_path):
    write_catalog([make_tool(f"o/r{i}") for i in range(100)], tmp_path, today="2026-08-22")
    broken = make_tool("o/x")
    object.__setattr__(broken, "tier", "legendary")

    with pytest.raises(Exception):
        write_catalog([broken] * 100, tmp_path, today="2026-08-23")

    assert len((tmp_path / "tools.jsonl").read_text().strip().splitlines()) == 100


def test_stale_detail_files_are_removed(tmp_path):
    write_catalog([make_tool("a/b")], tmp_path, today="2026-08-22", details={"a/b": {"features": "x"}})
    write_catalog(
        [make_tool("c/d")] * 1, tmp_path, today="2026-08-23", details={"c/d": {"features": "y"}},
        allow_shrink=True,
    )

    assert not (tmp_path / "details" / "a__b.md").exists()
    assert (tmp_path / "details" / "c__d.md").exists()


def test_load_previous_returns_stars_keyed_by_repo(tmp_path):
    write_catalog([make_tool("a/b", stars=42)], tmp_path, today="2026-08-22")

    previous = load_previous(tmp_path)
    assert previous["a/b"]["stars"] == 42 and previous["a/b"]["generated_at"] == "2026-08-22"


def test_load_previous_is_empty_on_a_first_run(tmp_path):
    assert load_previous(tmp_path) == {}


def test_load_previous_survives_a_corrupt_line(tmp_path):
    write_catalog([make_tool("a/b")], tmp_path, today="2026-08-22")
    path = tmp_path / "tools.jsonl"
    path.write_text(path.read_text() + "{not json\n")

    assert "a/b" in load_previous(tmp_path)
