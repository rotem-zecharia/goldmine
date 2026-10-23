# mvanhorn/last30days-skill

AI agent skill that researches any topic across Reddit, X, YouTube, HN, Polymarket, and the web - then synthesizes a grounded summary

## features

I built it to keep up in AI. Everything changes every day and the Reddit and X nerds are always on top of it first. I needed better prompts, and the training data was always months behind what the community had already figured out.

But it turned into something bigger. Now I run it before a sales call to know the last 30 days truth about a business. Before a meeting to read someone's recent tweets and podcast transcripts. Before a Disney World trip to know which rides are closed and what the community says about Genie+. Before I build anything to know what problems people are actually hitting.

If you're meeting with a CEO, have you read all their tweets and YouTube transcripts from the last 30 days? I have.

## Sources, scored by the people

| Source | What the people tell you |
|--------|--------------------------|
| **Reddit** | The unfiltered take. Top comments with real upvote counts, free, no API key. The real opinions that Google buries. |
| **X / Twitter** | The hot take, the expert thread, the breaking reaction. First to know, first to argue. |
| **YouTube** | The 45-minute deep dive. Full transcripts searched for the 5 quotable sentences that matter. |
| **TikTok** | The creator reaching 3.6M people with a take you'll never find on Google. |
| **Instagram Reels** | The influencer perspective with spoken-word transcripts. The visual culture signal. |
| **Hacker News** | The developer consensus. 825 points, 899 comments. Where technical people actually argue. |
| **Polymarket** | Not opinions. Odds. Backed by real money. 96% confidence on album sales. 4% on an acquisition. |
| **GitHub** | For people: PR velocity, top repos by stars, release notes. For topics: issues and discussions. |
| **Digg** | Story clusters from Digg's AI and Tech sections, with attributable inline quotes from X (no X auth required). Auto-enabled when `digg-pp-cli` is on PATH. |
| **arXiv** | The papers behind the hype. New research in the window, free, no API key. Auto-enabled when `arxiv-pp-cli` is on PATH (first-run setup installs it). |
| **Techmeme** | The tech-news editorial layer, date-windowed to your 30 days. Free, no API key. Auto-enabled when `techmeme-pp-cli` is on PATH (first-run setup installs it). |
| **LinkedIn** | The professional signal. Posts and articles, with articles weighted as high signal. |
| **Meta Ads** | What a brand is paying to say. Live Meta ad creatives launched this month, with copy, promo codes, and spoken transcripts. |
| **StockTwits** | Trader sentiment. Auto-activates when your topic is a ticker or crypto. |
| **Threads** | The post-Twitter text layer. Conversations from creators and brands. |
| **Pinterest** | Visual discovery. Pins, saves, and comments on products and ideas. |
| **Xiaohongshu (RED)** | Chinese lifestyle, product, and creator signals. Requested explicitly with `--search xhs` when a logged-in x-mcp browser plugin or `xiaohongshu-mcp` service is running locally. |
| **Bluesky** | The decentralized social layer. AT Protocol posts from the post-Twitter migration. |
| **Perplexity** | Controlled Agent API synthesis, OpenRouter Sonar fallback, raw Search API rows, and explicit Deep Research. |
| **DEV Community (dev.to)** | Developer articles and top comments through the public, keyless API. Opt in with `--devto-tags`, `--search devto`, or `INCLUDE_SOURCES=devto`. |
| **Truth Social** | Posts searched with `TRUTHSOCIAL_TOKEN`; available when authenticated. |
| **Telegram** | Public posts from named channels. Opt-in; requires `SCRAPECREATORS_API_KEY` and a channel list. No keyword discovery. |
| **Trustpilot** | Company TrustScore, review count, and an AI summary of customer feedback. Opt-in; requires `trustpilot-pp-cli` on PATH and a usable session. |
| **Amazon** | Product ratings, prices, and customer reviews. Opt-in; requires an authenticated `brightdata` CLI and uses your Bright Data credits. |
| **DripStack** | Financial newsletters and analyst writeups through a public, keyless API. Opt in w

## installation

| Surface | Install | Updates |
|---------|---------|---------|
| **Claude Code** (recommended) | `/plugin marketplace add mvanhorn/last30days-skill` | Auto via marketplace, or `claude plugin update last30days@last30days-skill` |
| **Grok** (xAI Build CLI) | `grok plugin marketplace add mvanhorn/last30days-skill` then `grok plugin install last30days` | `grok plugin update last30days` |
| **Codex, Cursor, Copilot, Gemini CLI, or any of 50+ [Agent Skills](https://agentskills.io) hosts** | `npx skills add mvanhorn/last30days-skill -g` | `npx skills update last30days -g` |
| **claude.ai** (web) | [Download `last30days.skill`](https://github.com/mvanhorn/last30days-skill/releases/latest/download/last30days.skill) and upload via claude.ai > Customize > Skills > + > Create skill > Upload a skill | Re-download and re-upload |
| **Claude Desktop** | [Download the `.mcpb` for your platform](https://github.com/mvanhorn/last30days-skill/releases/latest) and drag into Settings > Extensions | Re-download and drag the new bundle in |
| **OpenClaw** | `clawhub install last30days-official` | `clawhub update last30days-official` |

### Claude Code (recommended)

```
/plugin marketplace add mvanhorn/last30days-skill
```

Recommended because the Claude Code marketplace handles updates for you — the plugin cache is versioned and auto-refreshes when a new release publishes. Run `claude plugin update last30days@last30days-skill` to force a check.

If you'd rather use the agent-skills install path on Claude Code, that's also supported:

```
npx skills add mvanhorn/last30days-skill -g -a claude-code
```

### Quick Try-Link

[Try Last30Days Research Skill in Telegram or WhatsApp](https://app.clawmama.run/skills/2ne05f/hermes?utm_source=github&utm_medium=issue&utm_campaign=skill_outreach_mvanhorn_last30days_skill)

The native plugin and the `npx skills` install can coexist. Note that Claude Code does not dedupe across install methods: if you have both the marketplace plugin and the `npx skills` copy active, `/last30days` will show two entries. Use one install method per machine.

### Grok (xAI Build CLI)

[Grok Build](https://docs.x.ai/build/features/skills-plugins-marketplaces) (`grok`) installs last30days as a native plugin. Direct install tracks the repository:

```bash
grok plugin install mvanhorn/last30days-skill
```

Or add this repo as a marketplace source, then install by plugin name:

```bash
grok plugin marketplace add mvanhorn/last30days-skill
grok plugin install last30days
```

Add `--trust` to skip the install confirmation. Update with `grok plugin update last30days`. Grok also reads the Claude Code manifests for compatibility; the native `.grok-plugin/` pair is the first-class lane (and what an official [xAI marketplace](https://github.com/xai-org/plugin-marketplace) listing points at). `npx skills add` remains a valid cross-host fallback. On Grok Bot, X works out of the box through the bot's built-in X tools, then the bot's X connector, with the official X API (`X_BEARER_TOKEN`) as backup.

### Codex, Cursor, Copilot, Gemini CLI, and other Agent Skills hosts

Install via the open [Agent Skills](https://agentskills.io) CLI — supports 50+ harnesses including `codex`, `cursor`, `github-copilot`, `gemini-cli`, `claude-code`, `windsurf`, `cline`, `continue`, `roo`, `aider-desk`, `opencode`, `goose`, and more (full list on the [vercel-labs/skills repo](https://github.com/vercel-labs/skills)).

```bash
npx skills add mvanhorn/last30days-skill -g
```

The `-g` (global) flag installs to your user directory so the skill is available across all projects. Without `-g`, `npx skills` installs project-locally into `./.skills/` (committed with the repo). For a research-the-world tool, global is what you want.

Codex desktop and other folder-mode hosts can work in ordinary folders as well as Git repos. To inspect what a run would read and write without starting research, run the bundled `scripts/last30days.py --preflight` from the loaded skill directory; 

## configuration

Two things you'll likely want to know on day one:

**Where research files are saved.** `LAST30DAYS_MEMORY_DIR` defaults to `~/Documents/Last30Days/` (Windows: `C:\Users\<you>\Documents\Last30Days\`). Override by setting that env var to any path in your shell, or `--save-dir <path>` per run. Use `--output <file>` when you need the rendered result at an exact path, using the format selected by `--emit`. Use `--save-suffix=<name>` to keep multiple variations of the same topic separate (e.g. per client). Each `--save-dir` run produces `<slug>-raw[-suffix].md`. Optionally run `python3 skills/last30days/scripts/last30days.py --preflight` to review planned writes without starting research.

**Structured output for agents and workflows.** Ask `/last30days` for machine-readable JSON to receive the stable, versioned agent profile. For direct engine use in scripts or development, run `python3 skills/last30days/scripts/last30days.py "AI coding agents" --emit=json`; add `--json-profile=raw` only when you need the unversioned internal `Report` dump. See the [JSON export field reference and versioning policy](docs/reference/json-export.md).

**Topic-less discovery.** Ask `/last30days what's trending in AI agents?` to get a ranked discovery brief instead of researching a topic you already know - on an agent host this runs the three-command host-judged protocol (the model names topics, filters junk, scores worthiness, and writes the content angles). For direct engine use in scripts or cron, run `python3 skills/last30days/scripts/last30days.py --discover "AI agents"` (one-shot: deterministic topic names, no angles); add `--emit=json` for the versioned discovery contract. Discovery is mutually exclusive with a positional topic and `--drill`.

**Trend monitoring across runs.** The default mode produces a fresh markdown snapshot per run. To accumulate findings over time, add `--store` to persist into a SQLite database, then use [`scripts/watchlist.py`](skills/last30days/scripts/watchlist.py) for scheduled runs (with optional Slack / webhook delivery on new findings) and [`scripts/briefing.py`](skills/last30days/scripts/briefing.py) for daily / weekly digests. The full cadence pattern is in [CONFIGURATION.md](CONFIGURATION.md#trend-monitoring-store--watchlist--briefings).

**A subscribable research library.** Ask `/last30days` to build your library feed, or use `python3 skills/last30days/scripts/last30days.py library feed` directly for scripting and development. It turns saved briefs into `index.html`, a local Atom `feed.xml`, and readable brief pages. Add `--publish` only when you want the HTML index and brief pages hosted; publishing is explicit opt-in and public by default. To make the Atom feed subscribable, host the generated output directory on a static host such as GitHub Pages.

**Search everything you've researched.** Ask `/last30days search my library for MCP servers` or `/last30days have I researched MCP servers before?`. For direct engine use, run `python3 skills/last30days/scripts/last30days.py library search "MCP servers"`. Search is offline and deterministic: it incrementally indexes the same saved briefs used by the library feed, merges matching per-run store sightings, and groups results by topic and date. Fresh runs also surface a compact **From your library** section when prior research overlaps the current topic; set `LAST30DAYS_LIBRARY_CONTEXT=off` to disable that passive context.

Per-client wrapper scripts, custom category-peer subreddits, and the experimental beta channel for in-progress customizations are also documented in [CONFIGURATION.md](CONFIGURATION.md).

## Showcase: community research feeds

Published a recurring AI update, market watch, or wonderfully narrow obsession with last30days? Share the public library URL—or the Atom URL after hosting `feed.xml` on a static host—in [the community showcase thread](https://github.com/mvanhorn/last30days-skill/issues/532). Community feeds will be linked here as their owners s
