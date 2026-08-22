"""Wire the pipeline together. Everything it calls is pure and tested elsewhere."""

from __future__ import annotations

import argparse
import dataclasses
import os
from datetime import date

import yaml

from goldmine.catalog import load_previous, write_catalog
from goldmine.enrich import enrich_tools, select_for_enrichment
from goldmine.http import Fetcher
from goldmine.merge import attach_velocity, merge_tools
from goldmine.scoring import load_weights, score_tool
from goldmine.sources.github import search_topic
from goldmine.sources.registries import fetch_registry
from goldmine.tiering import assign_tiers

REPO_URL = "https://api.github.com/repos/{repo}"


def collect(config: dict, fetcher, taxonomy: dict) -> list:
    from goldmine.sources.github import normalize_repo

    tools = []

    topic_groups = (
        (config["github_topics"], config["max_pages_per_topic"], "ecosystem"),
        (config.get("oss_topics", []), config.get("max_pages_per_oss_topic", 3), "oss"),
    )

    for entries, max_pages, label in topic_groups:
        for entry in entries:
            found = search_topic(
                fetcher,
                topic=entry["topic"],
                categories=entry["categories"],
                max_pages=max_pages,
                taxonomy=taxonomy,
            )
            print(f"{label} topic:{entry['topic']}: {len(found)} repos")
            tools.extend(found)

    known = {tool.repo.lower() for tool in tools}

    for registry in config["registries"]:
        try:
            repos = fetch_registry(fetcher, url=registry["url"], style=registry["style"])
        except Exception as error:  # a dead registry must not fail the crawl
            print(f"warning: registry {registry['name']} failed: {error}")
            continue

        # Only fetch detail for repositories topic search did not already reach;
        # each one costs a request.
        fresh = [repo for repo in repos if repo.lower() not in known][
            : config.get("registry_detail_budget", 300)
        ]
        added = 0
        for repo in fresh:
            raw = fetcher.get_json(REPO_URL.format(repo=repo))
            if not raw or "full_name" not in raw:
                continue
            tools.append(normalize_repo(raw, ["mcp"], f"registry:{registry['name']}", taxonomy))
            known.add(repo.lower())
            added += 1
        print(f"registry:{registry['name']}: {len(repos)} listed, {added} new")

    return tools


def run_crawl(
    catalog_dir,
    scoring_path,
    sources_path,
    taxonomy_path,
    today,
    collect=collect,
    fetcher=None,
    enrich=enrich_tools,
    enrich_limit: int = 400,
    min_remaining: int = 200,
    per_category: int = 40,
):
    with open(sources_path) as handle:
        sources = yaml.safe_load(handle)
    with open(taxonomy_path) as handle:
        taxonomy = yaml.safe_load(handle)
    weights = load_weights(scoring_path)

    tools = merge_tools(collect(sources, fetcher, taxonomy))
    if not tools:
        print("no tools collected; leaving the existing catalog untouched")
        return

    previous = load_previous(catalog_dir)
    tools = [attach_velocity(tool, previous, today=today) for tool in tools]

    def rescore(items):
        return [
            dataclasses.replace(item, score=score_tool(item, weights, today=today))
            for item in items
        ]

    # Provisional score orders the enrichment budget; the real score follows.
    tools = rescore(tools)
    tools.sort(key=lambda tool: tool.score, reverse=True)

    selected = select_for_enrichment(tools, limit=enrich_limit, per_category=per_category)
    print(f"enriching {len(selected)} of {len(tools)} tools")
    details, tools = enrich(tools, fetcher, enrich_limit, min_remaining, selected)

    tools = rescore(tools)
    tools = assign_tiers(tools, today=today)
    tools.sort(key=lambda tool: tool.score, reverse=True)

    write_catalog(tools, catalog_dir, today=today, details=details)
    print(f"wrote {len(tools)} tools to {catalog_dir}")


def main() -> None:
    parser = argparse.ArgumentParser(prog="goldmine-crawl")
    parser.add_argument("--catalog-dir", default="catalog")
    parser.add_argument("--scoring", default="config/scoring.yaml")
    parser.add_argument("--sources", default="config/sources.yaml")
    parser.add_argument("--taxonomy", default="config/taxonomy.yaml")
    # 4 requests per enriched tool. GitHub Actions' GITHUB_TOKEN allows roughly
    # 1000 requests/hour, so the nightly default has to stay modest; a personal
    # token allows 5000 and can afford much more.
    parser.add_argument("--enrich-limit", type=int, default=400)
    parser.add_argument("--min-remaining", type=int, default=200)
    parser.add_argument("--per-category", type=int, default=40)
    args = parser.parse_args()

    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        print("warning: no GITHUB_TOKEN; unauthenticated crawls hit 60 requests/hour")

    run_crawl(
        catalog_dir=args.catalog_dir,
        scoring_path=args.scoring,
        sources_path=args.sources,
        taxonomy_path=args.taxonomy,
        today=date.today().isoformat(),
        fetcher=Fetcher(token=token),
        enrich_limit=args.enrich_limit,
        min_remaining=args.min_remaining,
        per_category=args.per_category,
    )


if __name__ == "__main__":
    main()
