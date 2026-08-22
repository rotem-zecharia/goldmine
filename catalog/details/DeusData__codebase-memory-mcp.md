# DeusData/codebase-memory-mcp

High-performance code intelligence MCP server. Indexes codebases into a persistent knowledge graph — average repo in milliseconds. 158 languages, sub-ms queries, 99% fewer tokens. Single static binary

## features

- **Extreme indexing speed** — Linux kernel (28M LOC, 75K files) in 3 minutes. RAM-first pipeline: LZ4 compression, in-memory SQLite, fused Aho-Corasick pattern matching. Memory released after indexing.
- **Plug and play** — native executable plus authenticated release-owned assets for macOS (arm64/amd64), Linux (arm64/amd64), and Windows (amd64). The native install needs no Docker, language runtime, or API keys. Download → `install` → restart agent → done.
- **158 languages** — vendored tree-sitter grammars compiled into the binary. Nothing to install, nothing that breaks.
- **120x fewer tokens** — 5 structural queries: ~3,400 tokens vs ~412,000 via file-by-file search. One graph query replaces dozens of grep/read cycles.
- **43 supported automatic/conditional client surfaces** — `install` configures detected clients and safely activates conditional clients only when their documented platform, marker, or explicit existing config path is present. See [Multi-Agent Support](#multi-agent-support) for the complete matrix and manual/UI-only boundaries.
- **Built-in graph visualization** — 3D interactive UI at `localhost:9749`, served from the binary itself.
- **Infrastructure-as-code indexing** — Dockerfiles, Kubernetes manifests, and Kustomize overlays indexed as graph nodes with cross-references. `Resource` nodes for K8s kinds, `Module` nodes for Kustomize overlays with `IMPORTS` edges to referenced resources.
- **15 MCP tools** — search, trace, architecture, impact analysis, targeted index-coverage checks, Cypher queries, dead code detection, cross-service HTTP linking, ADR management, and more.

## installation

**One-line install** (macOS / Linux):
```bash
curl -fsSL https://raw.githubusercontent.com/DeusData/codebase-memory-mcp/main/install.sh | bash
```

With graph visualization UI:
```bash
curl -fsSL https://raw.githubusercontent.com/DeusData/codebase-memory-mcp/main/install.sh | bash
```

**Windows** (PowerShell):
```powershell

## configuration

<details>
<summary>If you prefer not to use the install command</summary>

Add to `~/.claude.json` (user scope) or project `.mcp.json`:

```json
{
  "mcpServers": {
    "codebase-memory-mcp": {
      "command": "/path/to/codebase-memory-mcp",
      "args": []
    }
  }
