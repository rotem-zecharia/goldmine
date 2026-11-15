# eugeniughelbur/obsidian-second-brain

Persistent memory for Claude Code, Codex and 6 other AI agents, stored as plain markdown in your Obsidian vault. New: Crew, one shared logbook so Claude Code, Codex, Cursor and Grok Bot know what each

## installation

Inside any Claude Code session, run:

```
/plugin marketplace add eugeniughelbur/obsidian-second-brain
/plugin install obsidian-second-brain@obsidian-second-brain
```

Then tell Claude where your vault is. Add this to the `env` section of `~/.claude/settings.json`:

```json
"env": { "OBSIDIAN_VAULT_PATH": "/path/to/your/vault" }
```

Restart Claude Code and run `/obsidian-second-brain:obsidian-init` inside your vault. Start with three commands: `obsidian-init` to set up, `obsidian-save` to capture and `obsidian-find` to recall.

No vault yet, another AI tool, or bare command names? See the [full install guide](#install).

**On Grok Bot?** Start with one prompt and no install: [GROK-BOT.md](GROK-BOT.md).

<p align="center">
  <em>If this helps you, a <a href="https://github.com/eugeniughelbur/obsidian-second-brain">star</a> helps other people find it.</em>
</p>

<p align="center">
  <strong>An evolution of <a href="https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f">Karpathy's LLM Wiki pattern</a>: a vault that rewrites itself.</strong>
  <br />
  <em>Every source updates the pages you already have, not only adds new ones. <a href="#how-this-extends-karpathys-llm-wiki">How it differs &rarr;</a></em>
  <br /><br />
  <strong>Powered by <a href="references/freshness-policy.md">Open Knowledge Metabolism (OKM)</a>:</strong> <em>each fact is timeless, dated, or a pointer. Your notes never fill with facts that used to be true.</em>
</p>

---

## The Problem

You use Claude every day. Every session starts from scratch. You re-explain everything. The conversation ends. Everything disappears. Claude Code has no persistent memory across sessions - and neither does Grok Bot, Codex, Gemini, or any of the others.

You take notes in Obsidian. Hundreds of files. They just sit there. You make the same decision twice because you forgot you made it six months ago. Ideas rot in daily notes. Nobody connects the dots.

**Two powerful tools. Completely disconnected.** You already have the long-term memory. The thing doing the thinking cannot reach it.

---

## Who builds this

I'm Eugeniu Ghelbur, an AI automation engineer. I built this for my own vault, and I still run my work on it every day. I review and merge every change myself, and close to 50 people have shipped fixes so far ([see who](#contributors)).

I write up what I learn twice a week on [The AI Operator](https://theaioperator.io/subscribe?utm_source=github&utm_medium=readme&utm_campaign=who-builds-this), and post shorter notes on [X](https://x.com/eugeniu_ghelbur) and [LinkedIn](https://www.linkedin.com/in/eugeniu-ghelbur/).

---

## How this extends Karpathy's LLM Wiki

Karpathy's pattern is brilliant. Drop sources, LLM creates wiki pages, ask questions. This skill takes it further:

| | Karpathy's LLM Wiki | obsidian-second-brain |
|---|---|---|
| **New sources** | Append new pages, cross-reference | **Rewrite existing pages.** People get updated, claims revised, stale facts replaced. |
| **Contradictions** | Flagged, you resolve manually | `/obsidian-reconcile` resolves them automatically |
| **Patterns** | Surface when you ask | `/obsidian-synthesize` finds unnamed patterns and writes synthesis pages on its own |
| **When it runs** | On demand, when you prompt | 4 scheduled agents: morning brief, nightly consolidation, weekly review, vault-health check |
| **Note format** | Human-readable wiki pages | AI-first: `## For future agent` preamble + frontmatter for LLM retrieval, not human review |

If Karpathy's wiki is a knowledge base you maintain with an LLM, this is a knowledge base that maintains itself.

---

## What Happens When You Install This

**After a meeting:** `/obsidian-save`
Claude pulls out every decision, person, task, and idea and saves each one to the right note. You do nothing.

**You recorded a voice memo:** `/obsidian-ingest meeting.m4a`
Claude transcribes it with a local Whisper install, attributes speakers where the transcript makes them identifiab

## tools

### Operations -- Claude remembers

| Command | What it does |
|---|---|
| `/obsidian-save` | Saves everything from the conversation -- decisions, tasks, people, ideas |
| `/obsidian-ingest` | Ingest a URL, file, or resumable folder batch (text, PDFs, `.docx`/`.doc`/`.odt` via LibreOffice, audio, images). The vault REWRITES itself. 5-15 pages touched per source. |
| `/obsidian-synthesize` | Auto-finds patterns across sources and writes synthesis pages |
| `/obsidian-reconcile` | Finds contradictions and resolves them. The vault maintains its own truth. |
| `/obsidian-checkin` | Asks you whether old people and project notes still hold. Shows what each says, re-asks until you answer, saves the news. |
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
| `/obsidian-merge` | Merge two near-duplicate notes from `/obsidian-health` into one -- dry run by default, frontmatter union, retired note becomes a redirect (never deleted) |
| `/obsidian-reindex` | Refreshes the incremental semantic index and reports coverage before and after, with clear embedding-backend failures |
| `/obsidian-retrieval-eval` | Measures vault search quality -- recall@k + MRR on natural-language questions, with the concrete failures and ranked fixes |
| `/obsidian-decide [--formal]` | Logs decisions to the right project notes; `--formal` writes a full ADR record (the vault knows why it's structured this way) |
| `/obsidian-visualize` | Generates a visual canvas map of your second brain |
| `/obsidian-learn` | Reviews vault learnings, prunes stale ones, surfaces patterns to promote into rules |
| `/obsidian-init` | Generates `_CLAUDE.md`, `index.md`, `log.md` |
| `/obsidian-architect` | Scans a codebase and writes maintained architecture notes (overview, modules, decisions) into the vault; re-run to refresh |
| `/crew setup` | Shared job log and lessons with a human keep decision; works without Obsidian |
| `/create-command` | Interview flow that scaffolds a new command into `commands/<name>.md`, no markdown editing |

### Thinking -- Claude thinks with you

| Command | What it does |
|---|---|
| `/obsidian-brainstorm [topic]` | Multi-turn Socratic interview - one question per turn until the idea converges, then a design note with named alternatives |
| `/obsid

## features

Command reference: https://eugeniughelbur.github.io/obsidian-second-brain/ - every command, with the plain-language phrases that trigger it in English, German, Spanish, Portuguese and Simplified Chinese.

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

This project is maintained by one person but built with many. Close to 50 people have landed merged PRs: security fixes, platform ports (Pi came from a contributor), Windows compatibility, translations, and the first automated test. Ideas from closed or stalled PRs get reimplemented with the original author credited as co-author rather than dropped.

Thank you to everyone below, and to the nearly 100 people who filed issues or PRs by November 2026. Every report made the tool better.

<a href="https://github.com/eugeniughelbur/obsidian-second-brain/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=eugeniughelbur/obsidian-second-brain" alt="Avatars of obsidian-second-brain contributors" />
</a>

If your PR goes quiet mid-review, that is normal life - the idea stays on the table, and if it lands later you stay on the commit.

---

## Sponsors

obsidian-second-brain is free and MIT-licensed. If it saves you time, a paid subscription to The AI Operator is the best way to support it. That is where I write about building it, and paid readers also get a monthly no-code guide and a monthly Q&A.

[![Support on Substack](https://img.shields.io/badge/Support_on_Substack-EA4AAA?style=for-the-badge&logo=substack&logoColo
