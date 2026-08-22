---
name: goldmine
description: Use when the user needs a tool for a problem - asks "is there a tool for X", "what should I use for X", "does something already do X", "find me an MCP/skill/plugin for X" - or when you are about to hand-roll functionality that an established open-source tool already provides. Searches a scored catalog of MCP servers, Claude Code skills and plugins, and general open-source projects, and reports honest partial coverage when nothing fully solves the ask.
---

# goldmine

Find a tool that already solves the problem, and say plainly how much of it is solved.

## When to fire

Two cases, and only two:

1. **The user asks.** "Is there a tool for X", "what should I use", `/goldmine ...`.
2. **You are about to build something the catalog covers.** Name the top hit in one line, then keep
   working. Do not stop, do not lecture, and do not fire twice for the same topic in one session.

Anything looser is noise. A conversation that merely touches a topic is not a request, and a request
to write ordinary code is not a request for a tool.

## The catalog

Find it at `catalog/` in the goldmine plugin directory.

- `catalog/index.md` - one grep-friendly line per tool: repo, tier, score, stars, last push,
  categories, topics, summary. **Start here.** Grep it, do not read it whole.
- `catalog/tools.jsonl` - the same rows as JSON when you need a field.
- `catalog/details/<owner>__<repo>.md` - README sections, verbatim. Read only for the two or three
  candidates you are seriously considering.
- `catalog/meta.json` - `generated_at`. If that is more than 30 days ago, say so in your answer
  rather than presenting stale data as current.

If there is no catalog, say so and point at the plugin update command. Never attempt a live crawl.

## Query pipeline

### 1. Decompose the ask into requirements

Write them down before searching.

> "analyze an IG reel frame by frame" ->
> fetch reel · extract keyframes · vision per frame · transcribe audio · caption metadata · synthesize

### 2. Expand into 4-6 domain vocabularies before you grep

This is not optional and it is the single most important step.

Users describe problems in their own words. Maintainers describe repositories in domain words.
Searching `instagram reel analysis` returns a 26-star toy. Searching `video analysis mcp` returns the
1,253-star tool that actually does the job. Same need, completely different results.

Generate the alternates from the **requirements**, not from the user's phrasing. Include the words a
maintainer would put in a repository description: the format, the technique, the library.

```bash
grep -iE "video|frame|multimodal|vision|transcri" catalog/index.md | head -40
```

### 3. Gate on relevance, then rank

Collect candidates across all vocabularies, discard anything that does not plausibly address a
requirement, and only then order by tier and score.

**Never sort by stars first.** A 5.9k-star general-purpose desktop agent will outrank the 1.25k-star
tool that is actually right. A 42k-star video downloader will outrank the 19k-star gallery downloader
that is the correct answer for image carousels. Both are measured failures, not hypotheticals.

### 4. Answer in one of three modes

**Exact match** - one established tool covers effectively everything:

> **claude-video-vision** · established · 1.25k★ · pushed 2026-08-07
> Frame extraction plus per-frame vision analysis for Claude.
> `claude plugin install claude-video-vision`

Show at most three. Always include tier, stars, and last push: a stale tool is a broken tool.

**Coverage and gap** - the common case for a specific ask. Read the detail file, judge each
requirement against what the README actually claims, and report the gap:

> **claude-video-vision** (1.25k★, established) - roughly 65% of what you need
> covered: keyframe extraction, per-frame vision, transcription, synthesis
> missing: Instagram fetching, caption and hashtag metadata
> gap: two small pieces - a yt-dlp or instaloader wrapper, plus a metadata fetch

Do not inflate the percentage. A tool that covers half the ask is more useful described as half,
because the user is deciding what to build on top of it.

**Compose from scratch** - rare, and only when no single tool covers a meaningful share. Return an
ordered pipeline of catalog tools with the glue named.

### 5. Offer to install

Use the `install` field from the catalog row. If it is empty, read the detail file's installation
section rather than guessing a command.

## Tiers

- **established** - top 5% of its category, pushed within 90 days, 3+ contributors. Safe to depend on.
- **rising** - young, growing fast, actively maintained. Promising, not yet proven.
- **watch** - everything else that matched.

Tiers are percentiles **within a category**, not star thresholds. Do not apply a star floor of your
own. In an ecosystem this young, 1k stars is a well-established tool and 10k means famous rather than
good: of roughly 25,000 repositories tagged `mcp-server`, only about 36 clear 10k stars, and those
are large frameworks rather than the specific tool anyone actually needs.

## Honesty rules

- No relevant hit means say so. Never pad an answer with weak matches.
- Report last push whenever it is old. In fast-breaking categories, scrapers above all, a year
  without a push usually means the tool is broken regardless of its stars.
- If a tool requires credentials, a paid API, or a login session, say so up front. "Solved, but only
  with auth" is a different answer from "solved".
- Prefer an honest 60% over an optimistic 90%.
