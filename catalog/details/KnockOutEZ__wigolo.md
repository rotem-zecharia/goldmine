# KnockOutEZ/wigolo

The go-to web for your AI coding agent — local-first search, fetch, crawl & research over MCP. No API keys, no cloud, $0/query. Public beta.

## installation

```bash
npx wigolo init                              # set up the local engine — any system
npx wigolo init --agents=claude-code,cursor  # …or set up + wire your day-to-day agents in one command
```

Requires **Node ≥ 20** and ~1.5 GB of free disk on macOS, Linux, or Windows. Bare `init` sets up the local engine: it downloads the browser engine and on-device models, runs a health check, and reports each component. Adding `--agents` wires the named agents in the same run, so a coding agent you use daily is ready in one command.

- **Supported agents** — `--agents` takes any of `claude-code` · `cursor` · `codex` · `gemini-cli` · `opencode` · `vscode` · `windsurf` · `zed` · `antigravity` (comma-separated); wigolo writes the MCP config and, where supported, instructions for each.
- **Any other setup** — any MCP client, agent framework, or self-hosted agent registers `npx -y wigolo` in its own MCP config. The [installation guide](docs/installation.md) has the exact config block for every client, plus Docker, Homebrew, and single-file-binary channels.
- **More on the way** — the supported list keeps growing, and a PR to add your agent is welcome; see [CONTRIBUTING.md](CONTRIBUTING.md).
- **Interactive setup** — `--interactive` is a plain-text flow; `--wizard` is the full terminal TUI.
- **Defer downloads** — `--no-warmup` waits until first use. A failed component download never fails setup; init reports what's not ready with the exact fix and still completes.

`init` is unattended by default, so it's safe in scripts and CI, and any setup problem surfaces right here in the per-component report, before your agent's first call. **Search, fetch, crawl, extract, cache, and find-similar work with no API key.** Check it's healthy anytime:

```bash
npx wigolo doctor
```

To remove everything cleanly, run `npx wigolo config --uninstall --yes`. You can also paste the [installation guide](docs/installation.md) into any AI assistant and let it do the setup; it's written to be self-contained.

## tools

| Tool | What it does |
|------|--------------|
| 🔎 `search` | Multi-engine web search (18 direct adapters) with rank fusion, ML reranking, and an explainable per-result score. Pass a query **array** for parallel breadth. Scope by domain and time range, match an exact phrase, or return image results. |
| 📄 `fetch` | Load one URL through a tiered router that auto-escalates from plain HTTP to a headless browser engine on anti-bot challenges or SPA shells. Clean markdown + metadata + links. Handles PDFs, a single-heading `section`, authenticated sessions, and page actions (click / type / scroll / screenshot). |
| 🕸️ `crawl` | Multi-page crawl — BFS, DFS, sitemap, or map-only. Per-domain rate limits, robots.txt respect, boilerplate dedup. |
| 🧩 `extract` | Structured data from a page: tables, metadata, JSON-LD, brand identity, named schemas (Article / Recipe / Product / …), or any custom JSON Schema. |
| 💾 `cache` | Query everything already seen — keyword or hybrid semantic. Plus stats, clear, and change detection. |
| 🧲 `find_similar` | Pages similar to a URL or a concept, via 3-way fusion of keyword + semantic + live web. |
| 🧠 `research` | Decompose a question → fan out sub-queries → fetch sources → synthesize a cited report (or a structured brief the host LLM writes from). |
| 🤖 `agent` | Autonomous gather loop: plan → search → fetch → extract → synthesize, with a step log, time budget, and optional output schema. |
| 🔁 `diff` + ⏱️ `watch` | See exactly what changed on a page since last visit; re-check on demand and deliver changes to a webhook. |

Every tool also runs from the terminal (`wigolo search "…" --json`), from an interactive shell with NDJSON piping (`wigolo shell`), over REST, and through the SDKs — [CLI reference](docs/cli.md). Per-tool guides with the full parameter set are in [docs/tools.md](docs/tools.md); runnable examples are in [examples/](examples/README.md).

## features

wigolo isn't a free stand-in for the paid tools — it's built to match them. It's a focused web layer for your agents: an MCP and REST surface they call directly, with the search and extraction quality the paid services charge for. What separates it:

- **Built for agents.** One MCP call fans out many queries across many engines in parallel, which a serial host tool-loop can't replicate. Every result carries transparent per-result scoring, and output is budget-aware.
- **Honest output.** Stale cache, failed fetches, degraded backends, and truncation are surfaced in the result. When a bot-protected page can't be read, you get a labeled `blocked_by_challenge` failure, not a challenge shell returned as content.
- **$0 per query, free to re-query.** Default search talks to public engines through direct adapters; the reranker and embeddings run on-device. Every response is cached, so asking again is instant and costs nothing.
- **Private by default.** Cache, embeddings, models, and config live under `~/.wigolo/`. Nothing reaches a third party unless you explicitly opt into an LLM for synthesis.

Here's what one real result looks like, dissected. It includes the failed engine and the weak result, because those are part of the answer too:

<div align="center">

<picture>
<source media="(prefers-color-scheme: dark)" srcset="assets/promo/anatomy-dark.svg">
<img alt="Anatomy of a wigolo result: explainable score decomposition, live engine telemetry, surfaced degradation, self-flagged junk — one real query, captured live" src="assets/promo/anatomy.svg" width="880">
</picture>

</div>

## configuration

A clean install works out of the box. Three settings raise output quality:

```bash
