# goldmine — Design Spec

**Date:** 2026-08-22
**Status:** Approved (design), not yet implemented

## Problem

Developers using Claude Code constantly need a tool — an MCP server, a skill, a plugin, or a plain
open-source project — to solve the problem in front of them. Those tools surface on social media and
are impossible to track. GitHub stars are the best available proof of value, but raw star search is
noisy: it rewards fame over fitness, and it fails when the user's phrasing does not match the
vocabulary maintainers use.

goldmine is a discovery layer that lives inside Claude Code. It answers "is there already a tool for
this?" at the moment the question comes up, and it answers honestly when the best available tool only
gets you part of the way.

## Goals

- Suggest established, maintained tools at the moment of need, without leaving the terminal.
- Rank by evidence of real usage and maintenance, not by star count alone.
- Report partial coverage: "this tool solves 65% of your ask, here is the remaining gap."
- Stay free and offline-fast at query time.

## Non-goals

- Not a website or hosted service.
- Not a replacement for MCP registries; goldmine spans skills, plugins, and general OSS too.
- No paid tools, no affiliate ranking, no telemetry.

## Shape

A Claude Code plugin consisting of three pieces:

1. A **crawler** that runs in GitHub Actions and never on the user's machine.
2. A **catalog** committed to the repository, refreshed by that Action.
3. A **skill** that reads the catalog and answers questions.

Users get fresh data by updating the plugin. No local API token, no local crawl, no database.

## Component 1 — Crawler

Runs nightly in CI. Written in Python (stdlib plus `requests`), single entry point `crawl.py`.

### Sources

Ecosystem tier:
- GitHub Search API over topics: `mcp-server`, `model-context-protocol`, `mcp`, `claude-code`,
  `claude-skills`, `claude-plugin`, `agent-skills`, `ai-agent-tools`.
- Curated seed repositories whose READMEs are lists: `modelcontextprotocol/servers`,
  `awesome-mcp-servers`, `awesome-claude-code`.
- MCP registries, all of which expose JSON APIs and were verified reachable on 2026-08-22:
  - `registry.modelcontextprotocol.io/v0/servers` — the official registry, primary source.
  - `registry.smithery.ai/servers` — page/pageSize pagination.
  - `glama.ai/api/mcp/v1/servers` — cursor pagination.
  - `api.mcp.so` was checked and returned 502; it is excluded.

No HTML scraping is required anywhere in the pipeline. Every source is either the GitHub REST/Search
API, one of the registry JSON APIs above, or `raw.githubusercontent.com` for README text. A
markdown-extraction service such as Firecrawl was considered and rejected: it solves HTML-only
sources, which goldmine does not have, and would add either a paid dependency or a self-hosted
service for no gain. Revisit only if a future source is HTML-only.

Fallback tier (general OSS):
- Topic and keyword search across a category taxonomy defined in `config/taxonomy.yaml`
  (media/video, scraping, transcription, vision, data, devops, testing, docs, security, and so on).
- Only crawled for categories the taxonomy declares, to keep the catalog bounded.

### Normalisation and dedupe

Every source produces records keyed by `owner/repo`. Duplicates merge, keeping the union of
categories and the earliest discovery date. Forks resolve to their parent unless the fork has more
stars and more recent commits than the parent.

### Rate limits and failure

- Conditional requests with stored ETags; a 304 reuses the previous record untouched.
- Exponential backoff on 403 with `X-RateLimit-Remaining: 0`, honouring `X-RateLimit-Reset`.
- A source that fails entirely logs a warning and leaves the previous catalog rows for that source in
  place. The crawl never publishes a catalog smaller than 80% of the previous one; it fails the
  Action instead, so a partial outage cannot silently gut the catalog.

## Component 2 — Scorer

Produces a 0–100 quality score and a tier. This is the core of the project and the part worth
publishing openly, in `config/scoring.yaml`, so weights can be argued about in pull requests.

### Signals

| Signal | Why |
|---|---|
| `log(stars)` | Baseline popularity, log-scaled so 50k does not swamp 2k |
| Star velocity, last 90 days | Separates a still-growing tool from a repo that peaked in 2024 |
| Days since last push | Maintenance, the single strongest predictor of a tool that still works |
| Contributor count | One-person projects break when that person loses interest |
| Issue close ratio | Whether maintainers actually respond |
| README has an install section | Proxy for "someone other than the author has used this" |
| Has a licence | Usability |
| Has releases or tags | Release discipline |

### Penalties

Archived, unmaintained for 12 months, unresolved fork, or younger than 30 days with no traction. Each
is a hard demotion, not a small subtraction.

### Tiers

Tiers are **percentile-based within a category**, not absolute star thresholds. An absolute floor was
explicitly rejected: `topic:mcp-server` holds 25,248 repositories of which only 36 exceed 10,000
stars, and those 36 are large frameworks rather than the specific tools a developer needs day to day.
The ecosystem is roughly eighteen months old, so a high absolute floor measures fame, not proof.

- **established** — top 5% of its category by score, pushed within 90 days, 3 or more contributors.
- **rising** — steep positive star velocity, young, actively pushed. The "goldmine before it is
  famous" bucket.
- **watch** — passes relevance but not the above.

An absolute floor remains available per query as a `--min-stars` filter. It is never the default gate.

## Component 3 — Catalog

Committed to the repository under `catalog/`.

- `catalog/tools.jsonl` — one JSON object per line: `repo`, `categories`, `summary` (one line),
  `install`, `score`, `tier`, `stars`, `star_velocity_90d`, `last_push`, `contributors`, `tags`,
  `source`. Target size 1,000–3,000 entries.
- `catalog/index.md` — a compact grep-friendly table over the same rows, for fast scanning.
- `catalog/details/<owner>__<repo>.md` — per-tool detail, fetched only when the user drills in.
  Stores **structured README sections**, not a summary paragraph: features, the tool or command list,
  configuration, limitations, and requirements. Coverage analysis depends on this being faithful, so
  the crawler extracts sections verbatim rather than paraphrasing.
- `catalog/meta.json` — generation timestamp, source counts, crawler version.

## Component 4 — Skill

`skills/goldmine/SKILL.md`, plus a `/goldmine` command.

### Triggering

Moderate, deliberately. Two cases fire it:

1. The user explicitly asks — "is there a tool for X", `/goldmine ...`.
2. Claude is about to hand-roll something the catalog covers well. It names the top hit once, in one
   line, then continues with the work. It does not nag, and it does not fire twice for the same topic
   in a session.

Anything looser was rejected as noise.

### Query pipeline

1. **Requirement decomposition.** Break the ask into discrete capability requirements. "Analyze an
   Instagram reel frame by frame" becomes: fetch the reel, extract keyframes, vision per frame,
   transcribe audio, read caption and hashtag metadata, synthesize.

2. **Vocabulary expansion.** Translate the ask into 4–6 domain vocabularies before searching. This
   step exists because of a measured failure: searching the user's own words, "instagram reel
   analysis", returned a 26-star top result, while the correct answer,
   `jordanrendric/claude-video-vision` at 1,253 stars, only surfaced under "video analysis mcp". User
   phrasing and maintainer phrasing routinely diverge, and without expansion the catalog looks empty
   when it is not.

3. **Relevance gating, then ranking.** Filter candidates by relevance to the expanded vocabularies
   first, and only then order by score. Star-first ordering was measured to put an irrelevant
   5.9k-star desktop agent above the correct 1.25k-star answer.

4. **Answer, in one of three modes:**
   - **Exact match** — one established tool covers the ask. Show the top 3 with tier, stars, last
     push, and a one-line install command.
   - **Coverage and gap** — the usual case for a specific ask. For each top candidate, report the
     percentage of requirements covered, which are met, which are not, and what would have to be
     built on top. Coverage is judged at query time by reading the detail file, so no capability tags
     are precomputed and none go stale.
   - **Compose from scratch** — a last-resort fallback when nothing covers a meaningful share.
     Returns an ordered pipeline of catalog tools. Deliberately rare; single tools usually exist.

5. **Install.** On selection, read the detail file and offer to run the install.

### Coverage output, worked example

```
"analyze IG reel, frame-by-frame, full understanding"
→ requirements: fetch reel · extract keyframes · vision per frame ·
                transcribe audio · caption/hashtag metadata · synthesize

claude-video-vision (1.25k★, established, pushed 2026-08-07)   ~65% covered
  covered:  keyframe extraction, vision per frame, transcription, synthesis
  missing:  Instagram fetching, caption/hashtag metadata
  gap:      two small pieces — a yt-dlp or instaloader wrapper, plus a metadata fetch
```

## Freshness

A nightly GitHub Action regenerates the catalog and commits it. The skill reads
`catalog/meta.json`; if the catalog is more than 30 days old it says so in its answer rather than
presenting stale data as current.

Categories where upstream breaks often, social-media scraping in particular, weight last-push
recency more heavily. Those libraries stop working when a platform changes, and a year-old scraper is
usually a dead one.

## Error handling

- **Rate limits** — ETag conditional requests and backoff in CI; the skill itself makes no network
  calls at query time.
- **No catalog present** — the skill says so and points at the plugin update command. It does not
  attempt a local crawl.
- **Stale catalog** — surfaced as a warning in the answer.
- **No relevant hit** — say so plainly and fall through to compose mode. Never pad the answer with
  weak matches.

## Testing

- **Scorer** — unit tests over fixture repositories with known-good expected tiers, including the
  penalty cases (archived, single contributor, brand new).
- **Catalog** — schema validation on every generated row; CI fails on a malformed catalog.
- **Shrink guard** — a test asserting the 80% floor rejects a truncated crawl.
- **Query evaluation** — roughly 10 canned queries with expected repositories, run against a frozen
  catalog snapshot. Includes the reel case, asserting `claude-video-vision` surfaces and that the
  irrelevant high-star desktop agent does not. This suite is what catches vocabulary-expansion and
  relevance-gating regressions.

## Repository layout

```
goldmine/
  crawl.py                      crawler entry point
  scoring.py                    score and tier computation
  config/scoring.yaml           published weights
  config/taxonomy.yaml          fallback-tier categories
  config/sources.yaml           topics, seed lists, registries
  catalog/                      generated, committed
  skills/goldmine/SKILL.md
  commands/goldmine.md
  tests/
  .github/workflows/refresh.yml nightly regeneration
  LICENSE                       MIT
```

## Open questions

- Whether the three registry JSON endpoints stay stable enough to depend on. The official
  `registry.modelcontextprotocol.io` is the safest bet; Smithery and Glama are secondary and the
  crawler should tolerate either disappearing.
- Whether star velocity can be computed from the stargazers API within rate limits at catalog scale,
  or whether a stored week-over-week snapshot diff is the practical route.
