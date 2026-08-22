"""The record type that flows through the whole pipeline."""

from __future__ import annotations

import dataclasses
from dataclasses import dataclass, field

TIERS = ("established", "rising", "watch")

REQUIRED_FIELDS = (
    "repo",
    "summary",
    "categories",
    "stars",
    "contributors",
    "last_push",
    "created_at",
    "source",
)


class ValidationError(ValueError):
    """A catalog row does not match the expected schema."""


@dataclass(frozen=True)
class Tool:
    repo: str
    summary: str
    categories: list[str]
    stars: int
    contributors: int
    last_push: str
    created_at: str
    source: str
    install: str = ""
    open_issues: int = 0
    closed_issues: int = 0
    archived: bool = False
    is_fork: bool = False
    has_license: bool = False
    has_releases: bool = False
    has_install_section: bool = False
    tags: list[str] = field(default_factory=list)
    star_velocity_90d: float | None = None
    score: float | None = None
    tier: str | None = None

    @property
    def owner(self) -> str:
        return self.repo.split("/", 1)[0]

    @property
    def name(self) -> str:
        return self.repo.split("/", 1)[1]

    @property
    def detail_filename(self) -> str:
        return f"{self.owner}__{self.name}.md"

    def to_json(self) -> dict:
        return dataclasses.asdict(self)

    @classmethod
    def from_json(cls, row: dict) -> "Tool":
        known = {f.name for f in dataclasses.fields(cls)}
        return cls(**{k: v for k, v in row.items() if k in known})


def validate_row(row: dict) -> None:
    for name in REQUIRED_FIELDS:
        if name not in row or row[name] is None:
            raise ValidationError(f"missing required field: {name}")

    repo = row["repo"]
    if (
        not isinstance(repo, str)
        or repo.count("/") != 1
        or repo.startswith("/")
        or repo.endswith("/")
    ):
        raise ValidationError(f"repo must be 'owner/name', got: {repo!r}")

    tier = row.get("tier")
    if tier is not None and tier not in TIERS:
        raise ValidationError(f"tier must be one of {TIERS}, got: {tier!r}")

    if not isinstance(row["categories"], list):
        raise ValidationError("categories must be a list")
