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
| **Digg** | Curated story clusters from Digg's AI 1000 leaderboard (~1000 high-signal AI accounts on X), with attributable inline quotes (no X auth required). Auto-enabled when `digg-pp-cli` is on PATH. |
| **arXiv** | The papers behind the hype. New research in the window, free, no API key. Auto-enabled when `arxiv-pp-cli` is on PATH (first-run setup installs it). |
| **Techmeme** | The tech-news editorial layer, date-windowed to your 30 days. Free, no API key. Auto-enabled when `techmeme-pp-cli` is on PATH (first-run setup installs it). |
| **LinkedIn** | The professional signal. Posts and articles, with articles weighted as high signal. |
| **StockTwits** | Trader sentiment. Auto-activates when your topic is a ticker or crypto. |
| **Threads** | The post-Twitter text layer. Conversations from creators and brands. |
| **Pinterest** | Visual discovery. Pins, saves, and comments on products and ideas. |
| **Xiaohongshu (RED)** | Chinese lifestyle, product, and creator signals. Requested explicitly with `--search xhs` when a logged-in x-mcp browser plugin or `xiaohongshu-mcp` service is running locally. |
| **Bluesky** | The decentralized social layer. AT Protocol posts from the post-Twitter migration. |
| **Perplexity** | Controlled Agent API synthesis, OpenRouter Sonar fallback, raw Search API rows, and explicit Deep Research. |
| **Web** | The editorial coverage, the blog comparisons. One signal of many, not the only one. |

Community contributors keep adding more. Truth Social and other niche sources are in the engine with more on the way.

A Reddit thread with 1,500 upvotes is a stronger signal than a blog post nobody read. A TikTok with 3.6M views tells you more about what's culturally relevant than a press release. Polymarket odds backed by $66K in volume are harder to argue with than a pundit's guess.

The synthesis ranks by what real people actually engaged with. Social relevancy, not SEO relevancy.

## What people actually use it for

**Before a meeting.** `/last30days Peter Steinberger` - joined OpenAI's Codex team, fighting Anthropic's ban on third-party agents, 23 PRs merged at 85% merge rate on GitHub, building LobsterOS for cross-device agent control. r/ClaudeCode: "Ever since OpenClaw released, it was widely known that if

## tools

arXiv brings the papers behind the hype and Techmeme brings the editorial tech-news layer - free, zero keys, and first-run setup installs their CLIs so they activate automatically (#709). Digg's AI 1000 story clusters arrive without X auth the same way - setup installs the free Digg CLI for you (#590). Trustpilot ships opt-in for consumer-brand research.

### Free Reddit grew real scores and top comments

Reddit's public .json API died; the free path came back stronger. Keyless RSS + shreddit scraping (#457), dedicated-subreddit discovery with real upvote counts via arctic-shift (#696), and a relevance floor so a viral off-topic post can't hijack your brief (#488, thanks [@rzachsmith](https://github.com/rzachsmith)). No API key. Real scores. Top comments included.

### The best comments in every brief

Comments are now a default-on layer across sources: Instagram comments with rank-based diversity so five hot takes don't all come from one post (#751), YouTube comments plus a ScrapeCreators transcript backup for when yt-dlp strikes out (#637), and crowd-voted comments weighted into Best Takes so the community's funniest lines survive scoring (#592, #608).

### One doctor command

Ask for a health check and the doctor runs every source, then prescribes exact fixes - which key is missing, which CLI is off PATH, which cookie expired (#753). No more guessing why X came back thin.

### X search, rebuilt

The X pipeline got a ground-up overhaul: FROM and ABOUT lanes so a person's own posts and the conversation about them both rank (#610), person-aware subquery disambiguation (#611), first-party authorship grounding with interaction-signal ranking (#613), and a single X source with automatic backend failover (#622). Plus an honest `--diagnose` that actually probes auth (#609).

### More sources joined

LinkedIn via ScrapeCreators, with articles as high signal ([@ravstr](https://github.com/ravstr), #702). StockTwits auto-activates for ticker and crypto topics ([@wtiwana](https://github.com/wtiwana), #658). Perplexity grew direct API modes and async Deep Research ([@sk-holmes](https://github.com/sk-holmes), #629).

### Hardened by the community

The security wave was almost entirely community work: stored-XSS fixes in the HTML renderer ([@iliaal](https://github.com/iliaal), [@aaronjmars](https://github.com/aaronjmars)), locked-down cookie temp files, supply-chain-hardened CI with OpenSSF Scorecard and build provenance attestation ([@shaanmajid](https://github.com/shaanmajid), [@hammadxcm](https://github.com/hammadxcm), [@aniruddh909](https://github.com/aniruddh909)), Semgrep and OSV-Scanner scans plus a PR dependency-review gate ([@23241a6749](https://github.com/23241a6749)), a test-coverage floor introduced at 60% and since raised to 84% ([@gourab5139014](https://github.com/gourab5139014)), and a Hermes security scan cleared of every CRITICAL finding (#768).

### Reaches further

Hebrew and non-Latin languages ([@dudyme](https://github.com/dudyme)). CJK-aware tokenization for Chinese sources ([@An-idd](https://github.com/An-idd)). A Windows compatibility wave. Cookie extraction across the full Chromium family - Brave, Edge, Vivaldi, Opera, Arc ([@andrey-esipov](https://github.com/andrey-esipov)) - plus macOS Keychain and Linux pass(1) credential sources. `--as-of` historical lookback ([@chiyi-creator](https://github.com/chiyi-creator)). Auto-provisioned Python 3.12 via uv ([@buntysomroy](https://github.com/buntysomroy)). `--hiring-signals` for reading a company's job pages. Watchlist deltas between runs.

### Still in the box from v3

The v3 foundations are all still here: the pre-research brain that resolves the right handles, subreddits, and hashtags before a single API call fires (built by [@j-sperling](https://github.com/j-sperling)); Best Takes scoring for humor and virality alongside relevance; cross-source cluster merging; single-pass comparisons ("CLI vs MCP" in 3 minutes, not 12); auto-discovered `--competitors` comparisons; G

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

Add `--trust` to skip the install confirmation. Update with `grok plugin update last30days`. Grok also reads the Claude Code manifests for compatibility; the native `.grok-plugin/` pair is the first-class lane (and what an official [xAI marketplace](https://github.com/xai-org/plugin-marketplace) listing points at). `npx skills add` remains a valid cross-host fallback.

### Codex, Cursor, Copilot, Gemini CLI, and other Agent Skills hosts

Install via the open [Agent Skills](https://agentskills.io) CLI — supports 50+ harnesses including `codex`, `cursor`, `github-copilot`, `gemini-cli`, `claude-code`, `windsurf`, `cline`, `continue`, `roo`, `aider-desk`, `opencode`, `goose`, and more (full list on the [vercel-labs/skills repo](https://github.com/vercel-labs/skills)).

```bash
npx skills add mvanhorn/last30days-skill -g
```

The `-g` (global) flag installs to your user directory so the skill is available across all projects. Without `-g`, `npx skills` installs project-locally into `./.skills/` (committed with the repo). For a research-the-world tool, global is what you want.

Codex desktop and other folder-mode hosts can work in ordinary folders as well as Git repos. Before first research, ask the host agent to run the bundled `scripts/last30days.py --preflight` from the loaded skill directory; in a source checkout, the equivalent command is `python3 skills/last30days/scripts/last30days.py --preflight`. It shows the config source, browser-cookie plan, planned writes, optional commands, and ignored project config without reading cookies, writing files, or running research.

By default this installs for whichever harness `npx skills` detects. To target a specific one (or multiple):

## configuration

Two things you'll likely want to know on day one:

**Where research files are saved.** `LAST30DAYS_MEMORY_DIR` defaults to `~/Documents/Last30Days/` (Windows: `C:\Users\<you>\Documents\Last30Days\`). Override by setting that env var to any path in your shell, or `--save-dir <path>` per run. Use `--output <file>` when you need the rendered result at an exact path, using the format selected by `--emit`. Use `--save-suffix=<name>` to keep multiple variations of the same topic separate (e.g. per client). Each `--save-dir` run produces `<slug>-raw[-suffix].md`. Run `python3 skills/last30days/scripts/last30days.py --preflight` to review planned writes before a research run.

**Structured output for agents and workflows.** Ask `/last30days` for machine-readable JSON to receive the stable, versioned agent profile. For direct engine use in scripts or development, run `python3 skills/last30days/scripts/last30days.py "AI coding agents" --emit=json`; add `--json-profile=raw` only when you need the unversioned internal `Report` dump. See the [JSON export field reference and versioning policy](docs/reference/json-export.md).

**Topic-less discovery.** Ask `/last30days what's trending in AI agents?` to get a ranked discovery brief instead of researching a topic you already know - on an agent host this runs the three-command host-judged protocol (the model names topics, filters junk, scores worthiness, and writes the content angles). For direct engine use in scripts or cron, run `python3 skills/last30days/scripts/last30days.py --discover "AI agents"` (one-shot: deterministic topic names, no angles); add `--emit=json` for the versioned discovery contract. Discovery is mutually exclusive with a positional topic and `--drill`.

**Trend monitoring across runs.** The default mode produces a fresh markdown snapshot per run. To accumulate findings over time, add `--store` to persist into a SQLite database, then use [`scripts/watchlist.py`](skills/last30days/scripts/watchlist.py) for scheduled runs (with optional Slack / webhook delivery on new findings) and [`scripts/briefing.py`](skills/last30days/scripts/briefing.py) for daily / weekly digests. The full cadence pattern is in [CONFIGURATION.md](CONFIGURATION.md#trend-monitoring-store--watchlist--briefings).

**A subscribable research library.** Ask `/last30days` to build your library feed, or use `python3 skills/last30days/scripts/last30days.py library feed` directly for scripting and development. It turns saved briefs into `index.html`, a local Atom `feed.xml`, and readable brief pages. Add `--publish` only when you want the HTML index and brief pages hosted; publishing is explicit opt-in and public by default. To make the Atom feed subscribable, host the generated output directory on a static host such as GitHub Pages.

**Search everything you've researched.** Ask `/last30days search my library for MCP servers` or `/last30days have I researched MCP servers before?`. For direct engine use, run `python3 skills/last30days/scripts/last30days.py library search "MCP servers"`. Search is offline and deterministic: it incrementally indexes the same saved briefs used by the library feed, merges matching per-run store sightings, and groups results by topic and date. Fresh runs also surface a compact **From your library** section when prior research overlaps the current topic; set `LAST30DAYS_LIBRARY_CONTEXT=off` to disable that passive context.

Per-client wrapper scripts, custom category-peer subreddits, and the experimental beta channel for in-progress customizations are also documented in [CONFIGURATION.md](CONFIGURATION.md).

## Showcase: community research feeds

Published a recurring AI update, market watch, or wonderfully narrow obsession with last30days? Share the public library URL—or the Atom URL after hosting `feed.xml` on a static host—in [the community showcase thread](https://github.com/mvanhorn/last30days-skill/issues/532). Community feeds will be linked here as their owners submit them; the
