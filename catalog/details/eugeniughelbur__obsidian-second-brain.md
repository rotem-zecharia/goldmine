# eugeniughelbur/obsidian-second-brain

Persistent memory for Claude Code and 6 other CLI agents, stored as plain markdown in your Obsidian vault. Stop re-explaining your projects, decisions and people every session. 45 commands: hybrid sem

## installation

**After a meeting:** `/obsidian-save`
Claude pulls out every decision, person, task, and idea and saves each one to the right note. You do nothing.

**You recorded a voice memo:** `/obsidian-ingest meeting.m4a`
Claude transcribes it with a local Whisper install, attributes speakers where the transcript makes them identifiable, extracts every promise and action item, and distributes across entity pages, task boards, and the daily note.

**You screenshot a whiteboard:** `/obsidian-ingest photo.png`
Claude reads the image, extracts text and structure, creates concept notes, links to related projects. A photo becomes knowledge.

**You find a great video:** `/obsidian-ingest https://youtube.com/...`
Claude doesn't summarize into one note. It REWRITES your existing pages. People get updated. Contradictions get resolved. Patterns trigger new synthesis pages. One URL in. The vault is smarter.

**Before a big decision:** `/obsidian-challenge`
Claude searches your vault for past failures and reversed decisions on the same topic. Pushes back with your own words. Your vault holds you accountable.

**You want to see the big picture:** `/obsidian-visualize`
Claude generates a visual canvas of your entire vault. Hub nodes centered, color-coded by type, orphans highlighted. Open it in Obsidian and see the shape of your knowledge.

**You go to sleep:** The nightly agent runs 5 phases: closes the day, reconciles contradictions, synthesizes cross-source patterns, heals orphan notes, and rebuilds the index. You wake up to a smarter vault.

**You start a new day:** `/obsidian-daily`
Claude pulls your calendar events, overdue tasks, and overnight changes into today's note. Your morning starts informed.

**Someone shares an X post:** `/x-read https://x.com/...`
Grok with live X access fetches the post, the thread, and the replies. Returns verbatim text + TL;DR + key claims + reply sentiment + voices to watch. No more screenshots.

**You're planning today's content:** `/x-pulse "AI automation"`
Grok scans X for what's trending in your topic right now. Returns 3-5 emerging themes (with rep posts + key voices), gaps nobody is filling, hook formats that are working, and 3 specific post ideas you could write today.

**You need real research:** `/research "AI memory tools"`
Perplexity Sonar Pro pulls a deep dossier with citations: summary, key facts (every claim with a recency marker and source domain), timeline, key players, contrarian views, recommended further reading, open questions. Saved to your vault, auto-opens in Obsidian.

**You want vault-first deep research:** `/research-deep "AI memory tools"`
Scans your vault for what you already know. Identifies gaps. Spawns 3-5 targeted searches via Perplexity (web) and Grok (X discourse). Synthesizes a delta report: what's new, what's confirmed, contradictions to resolve, recommended vault updates. Vault baseline doesn't get re-researched. Only gaps get filled.

**You hit a great YouTube video:** `/youtube https://youtu.be/...`
Free transcript via youtube-transcript-api. Optional metadata + top comments via YouTube Data API v3. Gemini (free tier, Grok fallback) summarizes into TL;DR, Key Points, Notable Quotes (verbatim), Themes, Comment Sentiment, and Worth Following Up On. Saved as an AI-first note in your vault. Add `--visual` to also *watch* it: scene-change frame extraction (ffmpeg) that Claude reads with its own vision to capture on-screen text, code, diagrams, and demos the transcript misses.

**You never open Obsidian.** Everything happens through Claude.

---

## Before & After

| | Without this skill | With this skill |
|---|---|---|
| Saving decisions | Copy-paste or lose them | Auto-saved to the right project note |
| Daily notes | Write it yourself, forget half the time | Created automatically |
| Finding patterns | Re-read dozens of notes | `/emerge` finds them for you |
| Challenging yourself | Nobody pushes back | `/challenge` uses your own history against you |
| Session continuity | Re-e

## tools

### Operations -- Claude remembers

| Command | What it does |
|---|---|
| `/obsidian-save` | Saves everything from the conversation -- decisions, tasks, people, ideas |
| `/obsidian-ingest` | Drop a URL, PDF, audio file, or screenshot. The vault REWRITES itself. 5-15 pages touched per source. |
| `/obsidian-synthesize` | Auto-finds patterns across sources and writes synthesis pages |
| `/obsidian-reconcile` | Finds contradictions and resolves them. The vault maintains its own truth. |
| `/obsidian-export` | Clean JSON/markdown snapshot any AI tool can read |
| `/obsidian-daily` | Creates or updates today's daily note |
| `/obsidian-calendar <mode>` | One calendar command, four modes: `agenda` (read a snapshot), `reconcile` (flag commitments not yet scheduled), `meeting` (event to note), `schedule` (create/move an event from a task or standalone) |
| `/obsidian-recurring` | Tracks a recurring obligation with a cadence and a computed next-due date |
| `/obsidian-log` | Logs a work session, links it everywhere |
| `/obsidian-task` | Adds task to the right board with priority and due date |
| `/obsidian-person` | Creates or updates a person note |
| `/obsidian-capture` | Zero-friction idea capture |
| `/obsidian-catchup` | Process captures dumped from the Telegram bot (voice/text/image/PDF/link) into the vault |
| `/obsidian-find` | Smart search with context |
| `/obsidian-recap` | Summary of a day, week, or month |
| `/obsidian-review` | Structured weekly or monthly review |
| `/obsidian-board` | Kanban board view and updates |
| `/obsidian-board-hygiene` | Bulk-triage a board -- surface stale/overdue items, then archive / reschedule / mark-Done in one pass |
| `/obsidian-project` | Project note with board and daily links |
| `/obsidian-projects` | Live project status from git + local docs -- infers all context from vault notes, no config required |
| `/obsidian-health` | Vault audit -- contradictions, gaps, stale claims, orphans, freshness violations (the [freshness policy](references/freshness-policy.md): every fact timeless, dated, or a pointer), typed-edge lint (unknown types, dangling targets, contradiction cycles in the `relations:` graph), and a tag taxonomy audit ([opt-in](references/taxonomy-format.md) via `_meta/taxonomy.md`) |
| `/obsidian-reindex` | Refreshes the incremental semantic index and reports coverage before and after, with clear embedding-backend failures |
| `/obsidian-retrieval-eval` | Measures vault search quality -- recall@k + MRR on natural-language questions, with the concrete failures and ranked fixes |
| `/obsidian-decide [--formal]` | Logs decisions to the right project notes; `--formal` writes a full ADR record (the vault knows why it's structured this way) |
| `/obsidian-visualize` | Generates a visual canvas map of your second brain |
| `/obsidian-learn` | Reviews vault learnings, prunes stale ones, surfaces patterns to promote into rules |
| `/obsidian-init` | Generates `_CLAUDE.md`, `index.md`, `log.md` |
| `/obsidian-architect` | Scans a codebase and writes maintained architecture notes (overview, modules, decisions) into the vault; re-run to refresh |
| `/create-command` | Interview flow that scaffolds a new command into `commands/<name>.md`, no markdown editing |

### Thinking -- Claude thinks with you

| Command | What it does |
|---|---|
| `/obsidian-brainstorm [topic]` | Multi-turn Socratic interview - one question per turn until the idea converges, then a design note with named alternatives |
| `/obsidian-challenge` | Your vault argues against your idea using your own history |
| `/obsidian-panel` | Convenes a panel of distinct perspectives on a decision, one verdict each + synthesis |
| `/obsidian-emerge` | Surfaces patterns from 30 days of notes you never named |
| `/obsidian-connect [A] [B]` | Bridges two unrelated domains to spark new ideas |
| `/vault-deep-synthesis [topic]` | Cross-references every note on a topic: agreements, contradictions, stale claims, gaps |
| `/obsidian-dist

## features

Command reference: https://eugeniughelbur.github.io/obsidian-second-brain/ - every command, with the plain-language phrases that trigger it in English, Spanish, Portuguese and Simplified Chinese.

Retrieval benchmark: [scripts/eval/BENCHMARK.md](scripts/eval/BENCHMARK.md) - a reproducible 300-note synthetic corpus and three query sets, so the search numbers are something you can run yourself rather than something this README claims.

The rule on its own: [AI-FIRST.md](AI-FIRST.md) - the note spec as a 50-line block you can paste into any `CLAUDE.md` or `AGENTS.md`. Installs nothing, works without this project, keep the attribution line.

GitHub Issues: https://github.com/eugeniughelbur/obsidian-second-brain/issues. PRs welcome, see Contributing below.

---

## Philosophy

Most second brain tools make you the janitor.

This skill inverts that. You think, work, and talk. Claude handles the memory. Then it uses that memory to make you think better -- surfacing what you'd miss, challenging what you'd assume, connecting what you'd never link, and synthesizing patterns you didn't ask for.

The vault doesn't grow. It evolves.

**Your notes are the moat.**

Inspired by [Andrey Karpathy's LLM-Wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).

---

## Contributing

**Want a specific place to start?** [Good first issues](https://github.com/eugeniughelbur/obsidian-second-brain/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22) are scoped to name the exact files and lines, what to watch out for, and how big the change is. They range from adding trigger phrases in a language you speak (no Python at all) to a one-command lint fix to a new slash command. Comment on one to claim it.

PRs welcome more generally:
- New thinking tools
- Note type schemas (habits, books, investments)
- MCP integrations (Calendar, Linear, Slack)
- Alternative vault structures
- VS Code / Cursor setup guides

**Own a platform.** Eight builds, one maintainer who can test two. [adapters/OWNERS.md](adapters/OWNERS.md) has the open list; using the platform is the whole qualification, and your handle ships inside that build.

Building a domain-specific fork (academic, legal, finance, medical)? See [ECOSYSTEM.md](ECOSYSTEM.md). The upstream repo ships primitives; forks own the domain knowledge. First proof case: [`scholarbrain`](https://github.com/SHzzzAyys/scholarbrain) for academic research.

Customizing your own fork? Copy [`references/DELTAS.template.md`](references/DELTAS.template.md) to a `DELTAS.md` at your fork root and record your local deviations there. Upstream never touches that file, so you can keep merging `upstream/main` cleanly instead of fighting conflicts in stock commands.

### Contributors

This project is maintained by one person but built with many. 18+ external contributors have landed merged PRs - security fixes, platform ports (Pi came from a contributor), Windows compatibility, translations, and the first automated test. Ideas from closed or stalled PRs get reimplemented with the original author credited as co-author rather than dropped. See the full list on the [contributors graph](https://github.com/eugeniughelbur/obsidian-second-brain/graphs/contributors).

If your PR goes quiet mid-review, that is normal life - the idea stays on the table, and if it lands later you stay on the commit.

---

## Sponsors

Sponsorships help fund ongoing development of obsidian-second-brain: new commands, research-toolkit API costs, and ongoing maintenance.

[![Sponsor on GitHub](https://img.shields.io/badge/Sponsor-eugeniughelbur-EA4AAA?style=for-the-badge&logo=github-sponsors&logoColor=white)](https://github.com/sponsors/eugeniughelbur)

---

## Author

<div align="center">

<table>
<tr>
<td align="center" width="700">

Built by **Eugeniu Ghelbur**, AI Automation Engineer @ Single Grain

*If this skill helped you, the best thanks is following along.*

<a href="https://x.com/eugeniu_ghelbur"><img src="https://img.shields.io/bad
