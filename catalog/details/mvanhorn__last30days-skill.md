# mvanhorn/last30days-skill

AI agent skill that researches any topic across Reddit, X, YouTube, HN, Polymarket, and the web - then synthesizes a grounded summary

## features

I built it to keep up in AI. Everything changes every day and the Reddit and X nerds are always on top of it first. I needed better prompts, and the training data was always months behind what the community had already figured out.

But it turned into something bigger. Now I run it before a sales call to know the last 30 days truth about a business. Before a meeting to read someone's recent tweets and podcast transcripts. Before a Disney World trip to know which rides are closed and what the community says about Genie+. Before I build anything to know what problems people are actually hitting.

If you're meeting with a CEO, have you read all their tweets and YouTube transcripts from the last 30 days? I have.

## tools

arXiv brings the papers behind the hype and Techmeme brings the editorial tech-news layer - free, zero keys, and first-run setup installs their CLIs so they activate automatically (#709). Digg's AI 1000 story clusters arrive without X auth the same way - setup installs the free Digg CLI for you (#590). Trustpilot ships opt-in for consumer-brand research.

## installation

| Surface | Install | Updates |
|---------|---------|---------|
| **Claude Code** (recommended) | `/plugin marketplace add mvanhorn/last30days-skill` | Auto via marketplace, or `claude plugin update last30days@last30days-skill` |
| **Grok** (xAI Build CLI) | `grok plugin marketplace add mvanhorn/last30days-skill` then `grok plugin install last30days` | `grok plugin update last30days` |
| **Codex, Cursor, Copilot, Gemini CLI, or any of 50+ [Agent Skills](https://agentskills.io) hosts** | `npx skills add mvanhorn/last30days-skill -g` | `npx skills update last30days -g` |
| **claude.ai** (web) | [Download `last30days.skill`](https://github.com/mvanhorn/last30days-skill/releases/latest/download/last30days.skill) and upload via claude.ai > Customize > Skills > + > Create skill > Upload a skill | Re-download and re-upload |
| **Claude Desktop** | [Download the `.mcpb` for your platform](https://github.com/mvanhorn/last30days-skill/releases/latest) and drag into Settings > Extensions | Re-download and drag the new bundle in |
| **OpenClaw** | `clawhub install last30days-official` | `clawhub update last30days-official` |

## configuration

Two things you'll likely want to know on day one:

**Where research files are saved.** `LAST30DAYS_MEMORY_DIR` defaults to `~/Documents/Last30Days/` (Windows: `C:\Users\<you>\Documents\Last30Days\`). Override by setting that env var to any path in your shell, or `--save-dir <path>` per run. Use `--output <file>` when you need the rendered result at an exact path, using the format selected by `--emit`. Use `--save-suffix=<name>` to keep multiple variations of the same topic separate (e.g. per client). Each `--save-dir` run produces `<slug>-raw[-suffix].md`. Run `python3 skills/last30days/scripts/last30days.py --preflight` to review planned writes before a research run.

**Structured output for agents and workflows.** Ask `/last30days` for machine-readable JSON to receive the stable, versioned agent profile. For direct engine use in scripts or development, run `python3 skills/last30days/scripts/last30days.py "AI coding agents" --emit=json`; add `--json-profile=raw` only when you need the unversioned internal `Report` dump. See the [JSON export field reference and versioning policy](docs/reference/json-export.md).

**Topic-less discovery.** Ask `/last30days what's trending in AI agents?` to get a ranked discovery brief instead of researching a topic you already know - on an agent host this runs the three-command host-judged protocol (the model names topics, filters junk, scores worthiness, and writes the content angles). For direct engine use in scripts or cron, run `python3 skills/last30days/scripts/last30days.py --discover "AI agents"` (one-shot: deterministic topic names, no angles); add `--emit=json` for the versioned discovery contract. Discovery is mutually exclusive with a positional topic and `--drill`.

**Trend monitoring across runs.** The default mode produces a fresh markdown snapshot per run. To accumulate findings over time, add `--store` to persist into a SQLite database, then use [`scripts/watchlist.py`](skills/last30days/scripts/watchlist.py) for scheduled runs (with optional Slack / webhook delivery on new findings) and [`scripts/briefing.py`](skills/last30days/scripts/briefing.py) for daily / weekly digests. The full cadence pattern is in [CONFIGURATION.md](CONFIGURATION.md#trend-monitoring-store--watchlist--briefings).

**A subscribable research library.** Ask `/last30days` to build your library feed, or use `python3 skills/last30days/scripts/last30days.py library feed` directly for scripting and development. It turns saved briefs into `index.html`, a local Atom `feed.xml`, and readable brief pages. Add `--publish` only when you want the HTML index and brief pages hosted; publishing is explicit opt-in and public by default. To make the Atom feed subscribable, host the generated output directory on a static host such as GitHub Pages.

**Search everything you've researched.** Ask `/last30days search my library for MCP servers` or `/last30days have I researched MCP servers before?`. For direct engine use, run `python3 skills/last30days/scripts/last30days.py library search "MCP servers"`. Search is offline and deterministic: it incrementally indexes the same saved briefs used by the library feed, merges matching per-run store sightings, and groups results by topic and date. Fresh runs also surface a compact **From your library** section when prior research overlaps the current topic; set `LAST30DAYS_LIBRARY_CONTEXT=off` to disable that passive context.

Per-client wrapper scripts, custom category-peer subreddits, and the experimental beta channel for in-progress customizations are also documented in [CONFIGURATION.md](CONFIGURATION.md).
