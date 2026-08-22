"""Evaluation against the real committed catalog.

Skipped when no catalog is present, so a fresh clone can still run the unit
suite. These assertions encode the failures measured during design: vocabulary
mismatch, and star-first ranking burying the correct answer.
"""

import json
from pathlib import Path

import pytest
import yaml

CATALOG = Path("catalog/tools.jsonl")

pytestmark = pytest.mark.skipif(not CATALOG.exists(), reason="no catalog generated yet")


def rows():
    return [json.loads(line) for line in CATALOG.read_text().splitlines() if line.strip()]


def cases():
    return yaml.safe_load(Path("tests/eval/queries.yaml").read_text())


def by_repo():
    return {row["repo"].lower(): row for row in rows()}


def test_catalog_is_a_useful_size():
    assert 500 <= len(rows()) <= 20_000


def test_established_is_a_minority():
    tiers = [row["tier"] for row in rows()]

    assert tiers.count("established") / len(tiers) < 0.15


def test_every_row_has_a_category():
    # A row with no category never enters a percentile pool and can never be
    # established, so it is invisible to the skill.
    uncategorised = [row["repo"] for row in rows() if not row["categories"]]

    assert len(uncategorised) / len(rows()) < 0.05, f"{len(uncategorised)} rows have no category"


def test_every_expected_repo_is_present():
    catalog = by_repo()
    missing = [
        repo
        for case in cases()
        for repo in case["must_contain"]
        if repo.lower() not in catalog
    ]

    assert not missing, f"catalog is missing known-good tools: {missing}"


def test_expected_repos_are_not_buried_in_watch():
    catalog = by_repo()
    buried = [
        repo
        for case in cases()
        for repo in case["must_contain"]
        if catalog.get(repo.lower(), {}).get("tier") == "watch"
    ]

    assert not buried, f"known-good tools landed in watch: {buried}"


def test_scores_are_within_range():
    assert all(0.0 <= row["score"] <= 100.0 for row in rows())


def test_archived_repos_never_reach_established():
    assert not [row["repo"] for row in rows() if row["archived"] and row["tier"] == "established"]


def test_every_case_declares_vocabularies():
    assert all(len(case["vocabularies"]) >= 3 for case in cases())


def test_no_duplicate_repos():
    repos = [row["repo"].lower() for row in rows()]

    assert len(repos) == len(set(repos))
