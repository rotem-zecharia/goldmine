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

## features

I built SocratiCode because I regularly work on existing, large, and complex codebases across different languages and need to quickly understand them and act. Existing solutions were either too limited, insufficiently tested for production use, or bloated with unnecessary complexity. I wanted a single focused tool that does deep codebase intelligence well — zero setup, no bloat, fully automatic — and gets out of the way.

## requirements

| Dependency | Purpose | Install |
|------------|---------|---------|
| [Docker](https://www.docker.com/products/docker-desktop/) | Runs Qdrant (vector DB) and by default Ollama (embeddings) | [docker.com](https://www.docker.com/products/docker-desktop/) |
| Node.js 18+ | Runs the MCP server | [nodejs.org](https://nodejs.org/) |

Docker must be **running** when you use the server in the default `managed` mode. 

The Qdrant container is managed automatically. If you set `QDRANT_MODE=external` and point `QDRANT_URL` at a remote or cloud Qdrant instance, Docker is only needed for Ollama (embeddings) in that case.

The Ollama container (embeddings) is also managed automatically in the default `auto` mode. SocratiCode first checks if Ollama is already running natively — if so it uses it. Otherwise it manages a Docker container for you. First-time download of the docker images or embedding models may take a few minutes, depending on your internet speed, and is required only at first launch.

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
