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

### Recommended — a free key for `research` & `agent`

Search, fetch, crawl, extract, cache, and find-similar are **fully keyless**. `research`, `agent`, and `search format=answer` use an LLM to write the synthesized, cited answer. Without one they hand back a raw brief and evidence for your agent to assemble. A free Gemini key turns that into a finished answer:

```bash
export WIGOLO_LLM_PROVIDER=gemini
export GEMINI_API_KEY=<free-key>      # grab one at aistudio.google.com/apikey — the free tier is plenty
```

Any provider works (`anthropic` · `openai` · `groq`), or stay fully local and keyless with `WIGOLO_LLM_PROVIDER=ollama` (or any OpenAI-compatible URL). Set it in your shell or your agent's MCP `env` block. Providers, models, and the keyless local-model ladder are in the [configuration guide](docs/configuration.md).

## What your agent gets back

Every search result is evidence the agent can act on. It carries a verbatim excerpt pinned to its exact position in the source, a citation ID the agent can quote, and a score it can inspect (abridged real shape):

```jsonc
{
  "results": [{
    "title": "Logical replication - PostgreSQL docs",
    "url": "https://www.postgresql.org/docs/current/logical-replication.html",
    "excerpt": "Logical replication is a method of replicating data objects…",
    "citation_id": "src-1",
    "source_span": { "start": 1042, "end": 1305 },          // byte-exact provenance
    "evidence_score": { "final": 0.86, "semantic": 0.91, "lexical": 0.78, "engine_consensus": 3 }
  }],
  "citations": [{ "id": "src-1", "url": "…" }],
  "freshness_signal": { "published": "2026-05-12", "confidence": "high" }
}
```

Weak results get flagged as junk by wigolo's own scorer. Failed engines are reported and stale cache is labeled, so the agent always knows what it's standing on. Full response contracts per tool are in the [tools reference](docs/tools.md).

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

## Sponsors

Thank you to the sponsors below, who help keep wigolo maintained and free for everyone to use. Their support goes straight into the work.

<div align="center">

<a href="https://knockoutez.github.io/wigolo/go/testmu/?ref=readme">
<picture>
<source media="(prefers-color-scheme: dark)" srcset="assets/sponsors/testmu-ai-dark.svg">
<img alt="TestMu AI" src="assets/sponsors/testmu-ai.svg" width="240">
</picture>
</a>

<sub>**[TestMu AI](https://knockoutez.github.io/wigolo/go/testmu/?ref=readme)** (formerly LambdaTest) is the world's first full-stack agentic AI quality engineering platform, trusted by 18,000+ enterprises.</sub>

</div>

**wigolo is free for all and is meant to stay that way.** If you or your company would like to help keep it maintained, there's room for more sponsors — reach out at **[ktowhid20@gmail.com](mailto:ktowhid20@gmail.com)**, or see [SPONSORS.md](SPONSORS.md) for the terms. A one-off via [Buy Me a Coffee](https://buymeacoffee.com/knockoutez) is welcome too.

## Benchmark

> **All four tools converged on the same core answer, and only one of them handed back verbatim, byte-pinned evidence while doing it.**

One cold query ran live inside a single **Claude Fable 5** session, fanned out to four web tools on equal footing (built-in **WebSearch**, **wigolo**, **Tavily**, **Exa**), and was judged by the agent on the evidence alone. All four converged on the same answer and the same top source, so the parity is demonstrated on-screen. wigolo alone returned verbatim excerpts pinned to byte-offset source spans, an explainable score decomposition, and live per-engine telemetry, and its own scorer flagged two weak results as junk. The cloud tools earn their place too: Exa rendered the official docs' comparison matrix in full. Run your own query and you'll see the same shape.

<div align="center">

<img alt="wigolo vs built-in WebSearch, Tavily, and Exa on one real query, driven by Claude Fable 5" src="assets/wigolo-vs.gif" width="900">

</div>

### How it compares

| | wigolo | Firecrawl | Exa | Tavily |
|---|:---:|:---:|:---:|:---:|
| Multi-engine web search | ✅ | ✅ | ✅ | ✅ |
| Fetch & structured extraction | ✅ | ✅ | ✅ | ✅ |
| Whole-site crawl & map | ✅ | ✅ | — | ✅ |
| Verbatim excerpts pinned to byte-offset source spans | ✅ | — | — | — |
| Explainable per-result score decomposition | ✅ | — | — | — |
| Persistent local memory — re-qu

## configuration

A clean install works out of the box. Three settings raise output quality:

```bash
# 1. Synthesis — the biggest lever (research / agent / search-answer write real prose)
export WIGOLO_LLM_PROVIDER=gemini                   # or anthropic / openai / groq / ollama (keyless)
export GEMINI_API_KEY=<your-key>

# 2. Wider retrieval funnel
export WIGOLO_SEARCH=hybrid                         # core engines + aggregator fallback
export WIGOLO_GITHUB_TOKEN=...                      # GitHub code search 10 → 30 req/min

# 3. Land more fetches, stay warm
export WIGOLO_TLS_TIER=auto                         # per-domain learned fetch hardening
export WIGOLO_EAGER_WARMUP=1                        # pay the ~1s model load up front
```

**Per-call habits that pay off:** query **arrays** (`["a","b","c"]`) for parallel breadth · `search_depth: "deep"` for queries that matter · `include_domains` as a hard filter for docs lookups. The full reference covers every environment variable, config-file key, search backend, cache TTL, and serve limit; it's in the [configuration guide](docs/configuration.md).
