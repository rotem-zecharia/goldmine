# tirth8205/code-review-graph

Local-first code intelligence graph for MCP and CLI. Builds a persistent map of your codebase so AI coding tools read only what matters, with benchmarked context reductions on reviews and large-repo w

## installation

```bash
pip install code-review-graph                     # or: pipx install code-review-graph
code-review-graph install          # auto-detects and configures all supported platforms
code-review-graph build            # parse your codebase
```

One command sets up everything. `install` detects which AI coding tools you have, writes the correct MCP configuration for each one, installs platform-native hooks/skills where supported, and injects graph-aware instructions into your platform rules. It auto-detects whether you installed via `uvx` or `pip`/`pipx` and generates the right config. Restart your editor/tool after installing.

<p align="center">
  <img src="diagrams/diagram8_supported_platforms.png" alt="One Install, Every Platform: auto-detects Codex, Claude Code, CodeBuddy Code, Cursor, Windsurf, Zed, Continue, OpenCode, Antigravity, Gemini CLI, Qwen, Qoder, Kiro, GitHub Copilot, and GitHub Copilot CLI" width="85%" />
</p>

To target a specific platform:

```bash
code-review-graph install --platform codex       # configure only Codex
code-review-graph install --platform cursor      # configure only Cursor
code-review-graph install --platform claude-code  # configure only Claude Code
code-review-graph install --platform gemini-cli   # configure only Gemini CLI
code-review-graph install --platform antigravity   # configure only Antigravity
code-review-graph install --platform windsurf     # configure only Windsurf
code-review-graph install --platform zed          # configure only Zed
code-review-graph install --platform continue     # configure only Continue
code-review-graph install --platform opencode     # configure only OpenCode
code-review-graph install --platform qwen         # configure only Qwen
code-review-graph install --platform qoder        # configure only Qoder
code-review-graph install --platform kiro         # configure only Kiro
code-review-graph install --platform copilot      # configure only GitHub Copilot (VS Code)
code-review-graph install --platform copilot-cli  # configure only GitHub Copilot CLI
code-review-graph install --platform codebuddy    # configure only CodeBuddy Code
code-review-graph install --platform hermes       # configure only Hermes Agent
```

Requires Python 3.10+. For the best experience, install [uv](https://docs.astral.sh/uv/) (the MCP config will use `uvx` if available, otherwise falls back to the `code-review-graph` command directly).

To remove CRG from a Git or SVN project, use the symmetric uninstall command
from anywhere inside its working tree. The target is normalized to the working
tree root, and non-repository directories are refused. It removes only
CRG-owned files and entries; unrelated MCP servers, hooks, skills, and JSONC
comments remain untouched. Shared configuration changes use atomic replacement
so a failed write leaves the original file intact.

```bash
code-review-graph uninstall --dry-run    # preview every action; write nothing
code-review-graph uninstall              # preview, ask for confirmation, then apply
code-review-graph uninstall --yes        # apply without prompting
code-review-graph uninstall --all-repos  # also clean every registered repository
code-review-graph uninstall --keep-data  # remove integrations but keep graph databases
code-review-graph uninstall --keep-user-configs --repo .  # clean this project only
```

Then open your project and ask your AI assistant:

```
Build the code review graph for this project
```

The initial build takes ~10 seconds for a 500-file project. After that, watch mode and supported hooks can keep the graph updated automatically.

## limitations

- **Impact "recall 1.0" is graph-derived and circular:** the historical ground truth comes from the same graph edges the predictor walks, so it is an upper bound by construction. The honest co-change mode (grade against files actually co-changed in the same commit) is measured alongside it; expect those numbers to be substantially lower.
- **Small single-file changes:** Graph context can exceed naive file reads for trivial edits (see express results above). The overhead is the structural metadata that enables multi-file analysis.
- **Search quality (MRR 0.35):** Keyword search finds the right result in the top-4 for most queries, but ranking needs improvement. Express queries return 0 hits due to module-pattern naming.
- **Flow detection (33% recall):** Framework and conventional entry patterns are strongest for Python and PHP/Laravel. JavaScript and Go flow detection needs work.
- **Precision vs recall trade-off:** Impact analysis is deliberately conservative. It flags files that *might* be affected, which means some false positives in large dependency graphs.

---

## features

| Feature | Details |
|---------|---------|
| **Incremental updates** | Re-parses only the files whose hash changed. On a ~3,000-file repo a two-file edit takes ~2.5s on the hook path ([measured](docs/REPRODUCING.md#incremental-update-latency)). |
| **Broad language + notebook support** | Python, JavaScript/TypeScript/TSX, Go, Rust, Java, C/C++, C#, VB.NET, Ruby, Kotlin, Swift, PHP, Scala, Solidity, Dart, R, Perl, Lua/Luau, Objective-C, shell scripts, Elixir, Zig, PowerShell, Julia, ReScript, GDScript, Nix, Verilog/SystemVerilog, SQL, Terraform/OpenTofu structure (`.tf`; generic `.hcl` files are file-only), Ansible playbooks/roles/tasks, Vue/Svelte SFCs, Astro files parsed through the TypeScript parser, Jupyter/Databricks (.ipynb), and Perl XS (.xs) |
| **Framework-aware PHP parsing** | Repository-bounded Composer PSR-4 imports, Blade template references, and evidence-gated Laravel Route-to-controller and Eloquent relationship edges |
| **Blast-radius analysis** | Shows which functions, classes, and files are likely affected by a change |
| **Auto-update hooks** | Hooks and watch mode can update the graph on file saves and supported commit hooks |
| **Semantic search** | Optional vector embeddings via sentence-transformers, Google Gemini, MiniMax, or any OpenAI-compatible endpoint (real OpenAI, Azure, new-api, LiteLLM, vLLM, LocalAI) |
| **Interactive visualisation** | D3.js force-directed graph with search, community legend toggles, and degree-scaled nodes |
| **Hub & bridge detection** | Find most-connected nodes and architectural chokepoints via betweenness centrality |
| **Surprise scoring** | Detect unexpected coupling: cross-community, cross-language, peripheral-to-hub edges |
| **Knowledge gap analysis** | Identify isolated nodes, untested hotspots, thin communities, and structural weaknesses |
| **Suggested questions** | Auto-generated review questions from graph analysis (bridges, hubs, surprises) |
| **Edge confidence** | Three-tier confidence scoring (EXTRACTED/INFERRED/AMBIGUOUS) with float scores on edges |
| **Graph traversal** | Free-form BFS/DFS exploration from any node with configurable depth and token budget |
| **Export formats** | GraphML (Gephi/yEd), Neo4j Cypher, Obsidian vault with wikilinks, SVG static graph |
| **Graph diff** | Compare graph snapshots over time: new/removed nodes, edges, community changes |
| **Token benchmarking** | Measure naive full-corpus tokens vs graph query tokens with per-question ratios |
| **Estimated context savings** | Compact `context_savings` metadata on relevant MCP/CLI review outputs, labelled as estimated and kept to three small fields |
| **Memory loop** | Persist Q&A results as markdown for re-ingestion, so the graph grows from queries |
| **Community auto-split** | Oversized communities (>25% of graph) are recursively split via Leiden |
| **Execution flows** | Trace call chains from entry points, sorted by weighted criticality |
| **Community detection** | Cluster related code via Leiden algorithm with resolution scaling for large graphs |
| **Architecture overview** | Auto-generated architecture map with coupling warnings |
| **Risk-scored reviews** | `detect_changes` maps diffs to affected functions, flows, and test gaps |
| **Custom languages** | Add new languages via `.code-review-graph/languages.toml` — no fork or code changes needed |
| **GitHub Action** | Sticky risk-scored PR review comments in CI, with an optional `fail-on-risk` merge gate |
| **Refactoring tools** | Rename preview, framework-aware dead code detection, community-driven suggestions |
| **Wiki generation** | Auto-generate markdown wiki from community structure |
| **Multi-repo registry** | Register multiple repos, search across all of them |
| **Multi-repo daemon** | `crg-daemon` watches multiple repos as child processes, with health checks and auto-restart |
| **MCP prompts** | 5 workflow templates: review, architecture, debug, onboard, pre-merge |
| **Full-text search** | FTS5-powered hybr

## tools

<details>
<summary><strong>Slash commands</strong></summary>
<br>

| Command | Description |
|---------|-------------|
| `/code-review-graph:build-graph` | Build or rebuild the code graph |
| `/code-review-graph:review-delta` | Review changes since last commit |
| `/code-review-graph:review-pr` | Full PR review with blast-radius analysis |

</details>

<details>
<summary><strong>CLI reference</strong></summary>
<br>

```bash
code-review-graph install          # Auto-detect and configure all platforms
code-review-graph install --platform <name>  # Target a specific platform
code-review-graph uninstall --dry-run  # Preview safe removal of installed artifacts
code-review-graph build            # Parse entire codebase
code-review-graph update           # Incremental update (changed files only)
code-review-graph status           # Graph statistics
code-review-graph watch            # Auto-update on file changes
code-review-graph visualize        # Generate interactive HTML graph
code-review-graph visualize --format json      # Export local graph data as JSON
code-review-graph visualize --format graphml   # Export as GraphML
code-review-graph visualize --format svg       # Export as SVG
code-review-graph visualize --format obsidian  # Export as Obsidian vault
code-review-graph visualize --format cypher    # Export as Neo4j Cypher
code-review-graph wiki             # Generate markdown wiki from communities
code-review-graph detect-changes --brief         # Risk panel + token savings (read-only)
code-review-graph update --brief                 # Refresh graph + same panel
code-review-graph detect-changes --brief --verify  # Cross-check vs tiktoken
code-review-graph register <path>  # Register repo in multi-repo registry
code-review-graph unregister <id>  # Remove repo from registry
code-review-graph repos            # List registered repositories
code-review-graph daemon start     # Start multi-repo watch daemon
code-review-graph daemon stop      # Stop the daemon
code-review-graph daemon status    # Show daemon status and repos
code-review-graph eval             # Run evaluation benchmarks
code-review-graph serve            # Start MCP server
```

JSON exports stay inside the local graph data directory, which Git ignores by
default. They can contain absolute paths and code-structure metadata, so inspect
and sanitize an export before publishing it outside your machine.

</details>

<details>
<summary><strong>Token Savings panel: <code>detect-changes --brief</code> vs <code>update --brief</code></strong></summary>
<br>

Both commands print the same compact panel showing how many tokens the
graph saved you compared to handing the changed files to an agent raw.
They differ in **one** thing: whether the graph gets refreshed first.

```text
┌─────────────────────── Token Savings ────────────────────────┐
│ Full context would be:     12,921 tokens                     │
│ Graph context used:           762 tokens                     │
│ Saved:                     12,159 tokens (~94%)              │
│ Breakdown: Functions 244 · Tests 191 · Risk 244 · Other 83   │
└──────────────────────────────────────────────────────────────┘
```

| Command | What it does | When to use |
|---|---|---|
| `detect-changes --brief` | **Read-only.** Looks at your current changes, queries the **existing** graph, prints the panel. ~1 sec. | Most of the time — the hooks (or `crg-daemon`) keep the graph fresh in the background, so this is enough. |
| `update --brief` | **Re-parses your changed files into the graph first**, then prints the same panel. ~5 sec. | After a rebase, a large change set, or any time you suspect the graph is stale. |

Both end with the **same panel** because both call the same `analyze_changes()` step at the end. The difference is whether the graph itself got refreshed before that analysis ran.

Add `--verify` to either command to cross-check the displayed numbers against OpenAI's `cl100k_base` tokenizer (the GPT-4 family). Requires `pip instal

## configuration

| Variable | Description | Default |
|----------|-------------|---------|
| `CRG_GIT_TIMEOUT` | Timeout in seconds for Git operations | `30` |
| `CRG_DATA_DIR` | Override directory for graph databases and generated graph artefacts | - |
| `CRG_EMBEDDING_MODEL` | Default model for vector embeddings | `all-MiniLM-L6-v2` |
| `CRG_ACCEPT_CLOUD_EMBEDDINGS` | Suppress the cloud embedding egress warning after explicit acknowledgement | - |
| `CRG_ALLOW_REMOTE_CODE` | Allow HuggingFace models that require `trust_remote_code=True` | `0` |
| `CRG_MAX_IMPACT_NODES` | Maximum nodes to include in impact analysis | `500` |
| `CRG_MAX_IMPACT_DEPTH` | Search depth for blast-radius analysis | `2` |
| `CRG_MAX_BFS_DEPTH` | Maximum depth for graph traversal | `15` |
| `CRG_MAX_CHANGED_FUNCS` | Maximum changed functions analysed in one change report | `500` |
| `CRG_MAX_TRANSITIVE_FRONTIER` | Maximum frontier size for transitive caller/callee expansion | `50` |
| `CRG_TOOL_TIMEOUT` | Optional timeout in seconds for bounded MCP tools (`0` disables timeout) | `0` |
| `CRG_RECURSE_SUBMODULES` | Include git submodules in file collection when set to `1`, `true`, or `yes` | - |
| `CRG_TOOLS` | Comma-separated allowlist of MCP tools to expose when serving | - |
| `GOOGLE_API_KEY` | API key for Google Gemini embeddings | - |
| `MINIMAX_API_KEY` | API key for MiniMax embeddings | - |
| `VOYAGE_API_KEY` | API key for Voyage embeddings | - |
| `CRG_VOYAGE_MODEL` | Model name for Voyage embeddings | `voyage-code-3` |
| `CRG_VOYAGE_OUTPUT_DIMENSION` | Output dimension for Voyage embeddings | `1024` |
| `CRG_VOYAGE_OUTPUT_DTYPE` | Output dtype for Voyage embeddings | `float` |
| `CRG_VOYAGE_BASE_URL` | Voyage embeddings endpoint | `https://api.voyageai.com/v1` |
| `CRG_VOYAGE_BATCH_SIZE` | Batch size for Voyage embedding requests | `100` |
| `CRG_VOYAGE_MIN_INTERVAL_SEC` | Minimum delay between Voyage requests | `0` |
| `CRG_OPENAI_BASE_URL` | OpenAI-compatible embeddings endpoint | - |
| `CRG_OPENAI_API_KEY` | API key for OpenAI-compatible embeddings | - |
| `CRG_OPENAI_MODEL` | Model name for OpenAI-compatible embeddings | - |
| `CRG_OPENAI_DIMENSION` | Pin embedding dimension (v3 models support reduction) | - |
| `NO_COLOR` | If set, disables ANSI colors in terminal | - |
| `CRG_SERIAL_PARSE` | If `1`, disables parallel parsing (use for debugging) | - |

OpenAI-compatible embeddings (real OpenAI, Azure, or any self-hosted gateway like
new-api / LiteLLM / vLLM / LocalAI / Ollama in openai mode) need no extra install —
just set the environment variables and pass `provider="openai"` to `embed_graph`:

```bash
export CRG_OPENAI_BASE_URL=http://127.0.0.1:3000/v1     # or https://api.openai.com/v1
export CRG_OPENAI_API_KEY=sk-...
export CRG_OPENAI_MODEL=text-embedding-3-small          # whatever your gateway serves
