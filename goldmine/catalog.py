"""Read and write the committed catalog."""

from __future__ import annotations

import json
from pathlib import Path

from goldmine.models import validate_row

SHRINK_FLOOR = 0.80
INDEX_HEADER = (
    "| repo | tier | score | stars | last push | categories | tags | summary |\n"
    "|---|---|---|---|---|---|---|---|\n"
)


class CatalogShrank(RuntimeError):
    """The new catalog is far smaller than the last one; likely a partial crawl."""


def load_previous(directory) -> dict:
    directory = Path(directory)
    tools_path = directory / "tools.jsonl"
    meta_path = directory / "meta.json"
    if not tools_path.exists() or not meta_path.exists():
        return {}

    try:
        generated_at = json.loads(meta_path.read_text())["generated_at"]
    except (json.JSONDecodeError, KeyError):
        return {}

    previous = {}
    for line in tools_path.read_text().splitlines():
        if not line.strip():
            continue
        try:
            row = json.loads(line)
        except json.JSONDecodeError:
            # One bad line must not cost us every velocity measurement.
            continue
        previous[row["repo"].lower()] = {
            "stars": row["stars"],
            "generated_at": generated_at,
        }
    return previous


def _index_line(row: dict) -> str:
    return (
        f"| {row['repo']} | {row.get('tier') or ''} | {row.get('score') or 0:.0f} | "
        f"{row['stars']} | {row['last_push']} | {','.join(row['categories'])} | "
        f"{','.join(row.get('tags') or [])} | {row['summary']} |"
    )


def _detail_body(repo: str, summary: str, sections: dict) -> str:
    body = [f"# {repo}", "", summary, ""]
    for name, text in sections.items():
        body += [f"## {name}", "", text, ""]
    return "\n".join(body)


def write_catalog(
    tools: list, directory, today: str, details: dict | None = None, allow_shrink: bool = False
) -> None:
    directory = Path(directory)
    directory.mkdir(parents=True, exist_ok=True)

    previous_count = len(load_previous(directory))
    if not allow_shrink and previous_count and len(tools) < previous_count * SHRINK_FLOOR:
        raise CatalogShrank(
            f"refusing to write {len(tools)} rows over a previous {previous_count}; "
            "a source probably failed. Pass allow_shrink=True to override."
        )

    # Validate everything before touching disk, so a bad row cannot leave a
    # half-written catalog behind.
    rows = []
    for tool in tools:
        row = tool.to_json()
        validate_row(row)
        rows.append(row)

    (directory / "tools.jsonl").write_text(
        "".join(json.dumps(row, sort_keys=True) + "\n" for row in rows)
    )
    (directory / "index.md").write_text(
        INDEX_HEADER + "\n".join(_index_line(row) for row in rows) + "\n"
    )
    (directory / "meta.json").write_text(
        json.dumps({"generated_at": today, "count": len(rows)}, indent=2) + "\n"
    )

    details_dir = directory / "details"
    if details:
        details_dir.mkdir(exist_ok=True)
        by_repo = {tool.repo: tool for tool in tools}
        written = set()
        for repo, sections in details.items():
            tool = by_repo.get(repo)
            if not tool:
                continue
            (details_dir / tool.detail_filename).write_text(
                _detail_body(repo, tool.summary, sections)
            )
            written.add(tool.detail_filename)

        # A detail file for a tool no longer in the catalog is a lie the skill
        # would happily read.
        for path in details_dir.glob("*.md"):
            if path.name not in written:
                path.unlink()
