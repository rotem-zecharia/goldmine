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


TIER_RANK = {"established": 0, "rising": 1, "watch": 2}


def rank_for_query(vocabularies, limit=10):
    """Approximate what the skill does: gate on relevance, then rank.

    Tier membership is the wrong thing to assert on. A 1.25k-star tool is not
    top-5% of a 542-repo category, and pretending otherwise would be exactly
    the inflation the skill is told to avoid. What matters to a user is whether
    the right tool surfaces for their query, which is this.

    A vocabulary matches only when every word in it appears. Matching on single
    common words ("api", "downloader") let the largest generalist projects win
    every query; matching on hit count let a 2-star repo outrank a 13k-star
    established one. Neither is relevance.
    """
    phrases = [[word.lower() for word in vocabulary.split()] for vocabulary in vocabularies]

    gated = []
    for row in rows():
        haystack = " ".join(
            [row["repo"], row["summary"], " ".join(row["categories"]), " ".join(row["tags"] or [])]
        ).lower()
        matched = sum(1 for phrase in phrases if all(word in haystack for word in phrase))
        if matched:
            gated.append(row)

    gated.sort(key=lambda row: (TIER_RANK[row["tier"]], -row["score"]))
    ranked = [row["repo"].lower() for row in gated]
    return ranked if limit is None else ranked[:limit]


def test_known_good_tools_are_reachable_for_their_query():
    """The catalog must put the right tool in front of the skill.

    Ordering the shortlist is Claude's job, and no keyword ranker can make the
    judgement that huggingface/transformers is a general ML library rather than
    a tool for analysing a reel. What the catalog owes the skill is that the
    right tool is in the candidate set at all, with the categories and tags
    that make it findable.
    """
    failures = []
    for case in cases():
        if not case["must_contain"]:
            continue
        gated = rank_for_query(case["vocabularies"], limit=None)
        for repo in case["must_contain"]:
            if repo.lower() not in gated:
                failures.append(f"{case['ask']!r}: {repo} is unreachable ({len(gated)} candidates)")

    assert not failures, "\n".join(failures)


def test_the_relevance_gate_is_selective():
    """A gate that admits half the catalog is not a gate.

    Matching single common words let "api" pull in every large generalist
    project; requiring every word of a vocabulary phrase is what keeps the
    shortlist small enough for Claude to read.
    """
    total = len(rows())
    for case in cases():
        gated = rank_for_query(case["vocabularies"], limit=None)
        share = len(gated) / total
        assert share < 0.10, f"{case['ask']!r} gated {share:.0%} of the catalog"


def test_star_heavy_irrelevant_tools_do_not_outrank_the_right_answer():
    # The measured failure: a 42k-star video downloader beating the 19k-star
    # gallery downloader that is correct for image carousels.
    failures = []
    for case in cases():
        trap = case.get("must_not_rank_top") or []
        if not trap or not case["must_contain"]:
            continue
        top = rank_for_query(case["vocabularies"], limit=25)
        for bad in trap:
            if bad.lower() not in top:
                continue
            for good in case["must_contain"]:
                if good.lower() in top and top.index(bad.lower()) < top.index(good.lower()):
                    failures.append(f"{case['ask']!r}: {bad} outranks {good}")

    assert not failures, "\n".join(failures)


def test_scores_are_within_range():
    assert all(0.0 <= row["score"] <= 100.0 for row in rows())


def test_archived_repos_never_reach_established():
    assert not [row["repo"] for row in rows() if row["archived"] and row["tier"] == "established"]


def test_every_case_declares_vocabularies():
    assert all(len(case["vocabularies"]) >= 3 for case in cases())


def test_no_duplicate_repos():
    repos = [row["repo"].lower() for row in rows()]

    assert len(repos) == len(set(repos))
