# giancarloerra/SocratiCode

Enterprise-grade (40m+ LOC) codebase intelligence, zero-setup, local & private Plugin/Skill/Extension or MCP: hybrid semantic search, polyglot dependency graphs, symbol-level impact analysis & call-fl

## installation

> **Only [Docker](https://www.docker.com/products/docker-desktop/) (running) required.**

**One-click install** — Claude Code, VS Code and Cursor:

[![Install Claude Code Plugin](https://img.shields.io/badge/Claude_Code-Install_Plugin-CC785C?style=flat-square&logoColor=white)](#claude-code-plugin-recommended-for-claude-code-users)
[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_MCP_Server-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=socraticode&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22socraticode%22%5D%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_MCP_Server-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=socraticode&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22socraticode%22%5D%7D&quality=insiders) [![Install in Cursor](https://img.shields.io/badge/Cursor-Install_MCP_Server-F14C28?style=flat-square&logo=cursor&logoColor=white)](cursor://anysphere.cursor-deeplink/mcp/install?name=socraticode&config=eyJjb21tYW5kIjoibnB4IiwiYXJncyI6WyIteSIsInNvY3JhdGljb2RlIl19) 

**All MCP hosts** — add the following to your `mcpServers` (Claude Desktop, Windsurf, Cline, Roo Code) or `servers` (VS Code project-local `.vscode/mcp.json`) config:

```json
"socraticode": {
  "command": "npx",
  "args": ["-y", "socraticode"]
}
```

**Claude Code** — install the plugin (recommended, includes workflow skills for best results):

From your shell:

```bash
claude plugin marketplace add giancarloerra/socraticode
claude plugin install socraticode@socraticode
```

Or from within Claude Code:

```
/plugin marketplace add giancarloerra/socraticode
/plugin install socraticode@socraticode
```

> **Auto-updates:** After installing, enable automatic updates by opening `/plugin` → Marketplaces → select `socraticode` → Enable auto-update.

Or as MCP only (without skills):

```bash
claude mcp add socraticode -- npx -y socraticode
```

> **Updating:** `npx` caches the package after the first run. To get the latest version, clear the cache and restart your MCP host: `rm -rf ~/.npm/_npx && claude mcp restart socraticode`. Alternatively, use `npx -y socraticode@latest` in your config to always check for updates on startup (slightly slower).

**OpenCode** — add to your `opencode.json` (or `opencode.jsonc`):

```json
{
  "mcp": {
    "socraticode": {
      "type": "local",
      "command": ["npx", "-y", "socraticode"],
      "enabled": true
    }
  }
}
```

**OpenAI Codex CLI** — add to `~/.codex/config.toml`:

```toml
[mcp_servers.socraticode]
command = "npx"
args = ["-y", "socraticode"]
```

Restart your host. On first use SocratiCode automatically pulls Docker images, starts its own Qdrant and Ollama containers, and downloads the embedding model — one-time setup, ~5 minutes depending on your connection. After that, it starts in seconds.

**First time on a project** — ask your AI: **"Index this codebase"**. Indexing runs in the background; ask **"What is the codebase index status?"** to monitor progress. Depending on codebase size and whether you're using GPU-accelerated Ollama or cloud embeddings, first-time indexing can take anywhere from a few seconds to a few minutes (it takes under 10 minutes to first-index +3 million lines of code on a Macbook Pro M4). Once complete it doesn't need to be run again, you can search, explore the dependency graph, and query context artifacts.

**Every time after that** — just use the tools (search, graph, etc.). On server startup SocratiCode automatically detects previously indexed projects, restarts the file watcher, and runs an incremental update to catch any changes made while the server was down. If indexing was interrupted, it resumes automatically from the last checkpoint. You can also explicitly start or restart the watcher with `codebase_watch { action: "start" }`.

> **mac

## features

I built SocratiCode because I regularly work on existing, large, and complex codebases across different languages and need to quickly understand them and act. Existing solutions were either too limited, insufficiently tested for production use, or bloated with unnecessary complexity. I wanted a single focused tool that does deep codebase intelligence well — zero setup, no bloat, fully automatic — and gets out of the way.

### Built-in Code Search vs SocratiCode

| Feature | Claude Code | Cursor | VS Code Copilot | + SocratiCode |
|:--------|:-----------:|:------:|:---------------:|:-------------:|
| Text / grep search | ✅ | ✅ | ✅ | ✅ |
| Semantic search | — | ✅ | ✅¹ | ✅ |
| Hybrid search (fused) | — | — | — | ✅ |
| Code dependency graph | — | — | ✅² | ✅ |
| Symbol-level impact / blast radius | — | — | — | ✅ |
| Call-flow tracing (entry point → callees) | — | — | — | ✅ |
| Interactive visual graph explorer | — | — | — | ✅ |
| Circular dependency detection | — | — | — | ✅ |
| Non-code knowledge (schemas, API specs) | — | — | — | ✅ |
| Cross-project search | — | — | — | ✅ |
| Branch-aware indexing | — | — | — | ✅ |
| Multi-agent shared index | — | — | — | ✅ |
| Tool-independent (survives switching AI) | — | — | — | ✅ |
| Fully local / private | ✅ | —³ | —⁴ | ✅ |
| Resumable indexing | — | — | — | ✅ |
| Live file watching | — | ✅ | — | ✅ |

<sub>¹ VS Code Copilot: remote index via GitHub / Azure DevOps; local "External Ingest" gradually rolling out. ² LSP-based Find References / Go to Definition (Usages tool), not a full dependency graph. ³ Cursor: embeddings processed on Cursor servers (encrypted in transit and at rest). ⁴ VS Code Copilot: remote index hosted on GitHub / Azure DevOps. Sources: [Cursor docs](https://docs.cursor.com/context/codebase-indexing), [Claude Code docs](https://docs.anthropic.com/en/docs/claude-code/overview), [VS Code Copilot docs](https://code.visualstudio.com/docs/copilot/chat/codebase-context).</sub>

> **🔌 The context lives with your codebase, not with the assistant.** Built-in indexes (Cursor's, Copilot's) are tied to that one tool — switch assistants and you start from scratch. SocratiCode is independent: index once, then plug it into Claude Code, Cursor, Copilot, Windsurf, your own private model, or all of them at once. They share the same understanding of your code.

On VS Code's 2.45M‑line codebase, SocratiCode answers architectural questions with **61% less data**, **84% fewer steps**, and **37× faster** response than a grep‑based AI agent. [Full benchmark →](#real-world-benchmark-vs-code-245m-lines-of-code-with-claude-opus-46)

## Features

- **Hybrid code search** — Built on Qdrant, a purpose-built vector database with HNSW indexing, concurrent read/write, and payload filtering. Each chunk stores both a dense vector and a BM25 sparse vector; the Query API runs both sub-queries in a single round-trip and fuses results with Reciprocal Rank Fusion (RRF). Semantic search handles conceptual queries like "authentication middleware" even when those exact words don't appear in the code. BM25 handles exact identifier and keyword lookups. You get the best of both in every query with no tuning required.
- **Configurable Qdrant** — Use the built-in Docker Qdrant (default, zero config) or connect to your own instance (self-hosted, remote server, or Qdrant Cloud). Configure via `QDRANT_MODE`, `QDRANT_URL`, and `QDRANT_API_KEY` environment variables.
- **Configurable Ollama** — Use the built-in Docker Ollama (default, zero config) or point to your own Ollama instance (native install -GPU access-, remote server, etc.). Configure via `OLLAMA_MODE`, `OLLAMA_URL`, `EMBEDDING_MODEL` and `EMBEDDING_DIMENSIONS` environment variables.
- **Multi-provider embeddings** — Switch between Local Ollama (private, GPU access), Docker Ollama (zero-config), OpenAI (`text-embedding-3-small`, fastest), Google Gemini (`gemini-embedding-001`, free tier), LM Studio (local OpenAI-compatible server), or LiteLLM (proxy gateway in fron

## requirements

| Dependency | Purpose | Install |
|------------|---------|---------|
| [Docker](https://www.docker.com/products/docker-desktop/) | Runs Qdrant (vector DB) and by default Ollama (embeddings) | [docker.com](https://www.docker.com/products/docker-desktop/) |
| Node.js 18+ | Runs the MCP server | [nodejs.org](https://nodejs.org/) |

Docker must be **running** when you use the server in the default `managed` mode. 

The Qdrant container is managed automatically. If you set `QDRANT_MODE=external` and point `QDRANT_URL` at a remote or cloud Qdrant instance, Docker is only needed for Ollama (embeddings) in that case.

The Ollama container (embeddings) is also managed automatically in the default `auto` mode. SocratiCode first checks if Ollama is already running natively — if so it uses it. Otherwise it manages a Docker container for you. First-time download of the docker images or embedding models may take a few minutes, depending on your internet speed, and is required only at first launch.

### Embedding performance on macOS / Windows

Docker containers on macOS and Windows cannot access the GPU (no Metal or CUDA passthrough). For small projects this is fine, but for medium-to-large codebases the CPU-only container is noticeably slower.

**For best performance, install native Ollama:** download and run the installer from [ollama.com/download](https://ollama.com/download). Once Ollama is running, SocratiCode will automatically detect and use it — no extra configuration needed (first-time download of the embedding model, if not present, might take a few minutes). This gives you Metal GPU acceleration on macOS and CUDA on Windows/Linux.

If you prefer speed without a local install, see [OpenAI Embeddings](#openai-embeddings) and [Google Generative AI Embeddings](#google-generative-ai-embeddings) below for cloud-based options. OpenAI is very fast with no local setup required. Google’s free tier is functional but rate-limited. See [Environment Variables](#environment-variables) for configuration details.

## Example Workflow

All tools default `projectPath` to the current working directory, so you never need to specify a path for the active project.

```
User: "Index this project"
→ codebase_index {}
  ⚡ Indexing started in the background — call codebase_status to check progress
→ codebase_status {}
  ⚠ Full index in progress — Phase: generating embeddings (batch 1/1)
  Progress: 247/1847 chunks embedded (13%) — Elapsed: 12s
→ codebase_status {}
  ✓ Indexing complete: 342 files, 1,847 chunks (took 115.2s)
  File watcher: active (auto-updating on changes)

User: "Search for how authentication is handled"
→ codebase_search { query: "authentication handling" }
  Runs dense semantic search + BM25 keyword search in parallel, fuses results with RRF
  Returns top 10 results ranked by combined relevance

User: "What files depend on the auth middleware?"
→ codebase_graph_query { filePath: "src/middleware/auth.ts" }
  Returns imports and dependents
  (graph was auto-built after indexing — no manual build needed)

User: "Show me the dependency graph"
→ codebase_graph_visualize {}
  Returns a Mermaid diagram colour-coded by language

User: "Are there any circular dependencies?"
→ codebase_graph_circular {}
  Found 2 cycles: src/a.ts → src/b.ts → src/a.ts

User: "What breaks if I rename validateUser?"
→ codebase_impact { target: "validateUser" }
  Blast radius for symbol: validateUser
  Hop 1 (3 files): src/auth/login.ts, src/api/users.ts, tests/auth.test.ts
  Hop 2 (5 files): ...

User: "What does the server entry point actually do?"
→ codebase_flow {}
  Detected 4 entry point(s):
    main (cmd/server.go:10) — well-known-name:main
    healthz (src/api/routes.ts:42) — framework:get
    ...
→ codebase_flow { entrypoint: "main" }
  └── main (cmd/server.go:10)
      ├── loadConfig (cmd/server.go:15)
      └── startServer (src/server.ts:8)
          └── ...

User: "Who calls bcryptCompare and what does it call?"
→ codebase_symbol { name: "bcryptCompare"

## configuration

> All `env` options below apply equally to the `npx` install. Just add the `"env"` block to the npx config shown above.

Add to your MCP settings - `mcpServers` (Claude Desktop, Windsurf, Cline, Roo Code) or `servers` (VS Code project-local `.vscode/mcp.json`):

#### Default (zero config, from source)

> Using **npx**? Your config is already in [Quick Start](#quick-start). Add any `"env"` block from the examples below as needed.

```json
{
  "mcpServers": {
    "socraticode": {
      "command": "node",
      "args": ["/absolute/path/to/socraticode/dist/index.js"]
    }
  }
}
```

> **Tip**: The default `OLLAMA_MODE=auto` detects native Ollama (port 11434) on startup and uses it if available, otherwise falls back to a managed Docker container. To make your config self-documenting, add an `"env"` block with explicit values. See [Environment Variables](#environment-variables) for all options.

#### External Ollama (native install)

If you have [Ollama](https://ollama.com) installed natively, set `OLLAMA_MODE=external` and point to your instance:

```json
{
  "mcpServers": {
    "socraticode": {
      "command": "node",
      "args": ["/absolute/path/to/socraticode/dist/index.js"],
      "env": {
        "OLLAMA_MODE": "external",
        "OLLAMA_URL": "http://localhost:11434"
      }
    }
  }
}
```

The embedding model is pulled automatically on first use. To pre-download: `ollama pull nomic-embed-text`

#### Remote Ollama server

```json
{
  "mcpServers": {
    "socraticode": {
      "command": "node",
      "args": ["/absolute/path/to/socraticode/dist/index.js"],
      "env": {
        "OLLAMA_MODE": "external",
        "OLLAMA_URL": "http://gpu-server.local:11434"
      }
    }
  }
}
```

#### OpenAI Embeddings

Use OpenAI's cloud embedding API instead of local Ollama. Requires an [API key](https://platform.openai.com/api-keys).

```json
{
  "mcpServers": {
    "socraticode": {
      "command": "node",
      "args": ["/absolute/path/to/socraticode/dist/index.js"],
      "env": {
        "EMBEDDING_PROVIDER": "openai",
        "OPENAI_API_KEY": "sk-..."
      }
    }
  }
}
```

> Defaults: `EMBEDDING_MODEL=text-embedding-3-small`, `EMBEDDING_DIMENSIONS=1536`. For higher quality, use `text-embedding-3-large` with `EMBEDDING_DIMENSIONS=3072`.

#### Google Generative AI Embeddings

Use Google's Gemini embedding API. Requires an [API key](https://aistudio.google.com/apikey).

```json
{
  "mcpServers": {
    "socraticode": {
      "command": "node",
      "args": ["/absolute/path/to/socraticode/dist/index.js"],
      "env": {
        "EMBEDDING_PROVIDER": "google",
        "GOOGLE_API_KEY": "AIza..."
      }
    }
  }
}
```

> Defaults: `EMBEDDING_MODEL=gemini-embedding-001`, `EMBEDDING_DIMENSIONS=3072`.

#### LM Studio (local, OpenAI-compatible)

[LM Studio](https://lmstudio.ai/) ships with a Local Server that exposes an OpenAI-compatible
API on `http://localhost:1234/v1`. Use this provider when you want to host embedding models
in LM Studio (e.g. when LM Studio is your single source for both chat and embedding models,
or when you want a Mac/Windows-friendly desktop UI for managing GGUF models).

```json
{
  "mcpServers": {
    "socraticode": {
      "command": "node",
      "args": ["/absolute/path/to/socraticode/dist/index.js"],
      "env": {
        "EMBEDDING_PROVIDER": "lmstudio",
        "EMBEDDING_MODEL": "nomic-embed-text-v1.5",
        "EMBEDDING_DIMENSIONS": "768"
      }
    }
  }
}
```

> **No defaults — `EMBEDDING_MODEL` and `EMBEDDING_DIMENSIONS` are required.** LM Studio has
> no out-of-the-box embedding model; you load one yourself in the Local Server tab. SocratiCode
> fails fast if either is missing.
>
> Optional: `LMSTUDIO_URL` (default `http://localhost:1234/v1`) for non-default ports;
> `LMSTUDIO_API_KEY` if you've enabled API key auth in LM Studio.

#### LiteLLM (proxy gateway, 100+ providers)

[LiteLLM](https://docs.litellm.ai/docs/simple_proxy) Proxy Server exposes an OpenAI-compatible
`/v1/embeddings` end

## tools

Once connected, 21 tools are available to your AI assistant:

#### Indexing

| Tool | Description |
|------|-------------|
| `codebase_index` | Start indexing a codebase in the background (poll `codebase_status` for progress) |
| `codebase_stop` | Gracefully stop an in-progress indexing operation (current batch finishes and checkpoints; resume with `codebase_index`) |
| `codebase_update` | Incremental update — only re-indexes changed files |
| `codebase_remove` | Remove a project's index (safely stops watcher, cancels in-flight indexing/update, waits for graph build) |
| `codebase_watch` | Start/stop file watching — on start, catches up missed changes then watches for future ones |

#### Search

| Tool | Description |
|------|-------------|
| `codebase_search` | Hybrid semantic + keyword search (dense + BM25, RRF-fused) with optional file path, language filters, and cross-project search (`includeLinked`) |
| `codebase_status` | Check index status and chunk count |

#### Code Graph

| Tool | Description |
|------|-------------|
| `codebase_graph_build` | Build a polyglot dependency graph (runs in background — poll with `codebase_graph_status`) |
| `codebase_graph_query` | Query imports and dependents for a specific file |
| `codebase_graph_stats` | Get graph statistics (most connected files, orphans, language breakdown) |
| `codebase_graph_circular` | Detect circular dependencies |
| `codebase_graph_visualize` | Generate a Mermaid diagram (`mode=mermaid`, default) or an interactive HTML explorer (`mode=interactive`) of the dependency graph. Interactive mode writes a self-contained page (vendored Cytoscape.js + Dagre, works offline) and opens it in your default browser — file + symbol views, blast-radius overlay, live search, PNG export. |
| `codebase_graph_status` | Check graph build progress or persisted graph metadata |
| `codebase_graph_remove` | Remove a project's persisted code graph (waits for in-flight graph build to finish first) |

#### Impact Analysis (symbol-level call graph)

A second graph layer goes one step deeper than file imports — it tracks which functions
and methods call which. Use these tools BEFORE refactoring, renaming, or deleting code.

| Tool | Description |
|------|-------------|
| `codebase_impact` | Blast radius — what files break if you change file/function X (BFS through reverse-call edges) |
| `codebase_flow` | Trace forward execution flow from an entry point. Call with no args to discover entry points (orphans, `main()`, framework routes, tests) |
| `codebase_symbol` | 360° view of one symbol — its definition, callers, and callees |
| `codebase_symbols` | List symbols in a file or search by name across the project |

> **Accepted limits.** The call graph is static-analysis-based — no type inference. Dynamic dispatch (`getattr`, `obj[key](...)`, reflection, `eval`), unexpanded macros, and framework magic (Spring `@Autowired`, Angular DI, Rails `has_many`, decorator-driven routing) are invisible. Callers that reach a method only through these mechanisms will not appear in `codebase_impact`. Treat "zero callers" as a hint to double-check on DI-heavy codebases. `codebase_graph_status` reports `unresolvedEdgePct` as a quality signal. See [DEVELOPER.md § Impact Analysis](DEVELOPER.md) for the full list.

#### Interactive graph explorer

Ask your AI *"show me an interactive graph of this project"* (or invoke `codebase_graph_visualize` with `mode: "interactive"`) and SocratiCode generates a self-contained HTML page and opens it in your default browser:

- **File view** — every source file as a node, imports as edges, language-coloured, circular deps in red.
- **Symbol view** — toggle to see functions/classes/methods as nodes with call edges (available when the symbol graph fits within the embed cap; above that threshold the file view remains and the banner points at `codebase_impact` for symbol-level queries).
- **Sidebar** — click a node to see imports / dependents / symbols-in-file / line numbers, wit
