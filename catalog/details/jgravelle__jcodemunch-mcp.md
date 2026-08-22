# jgravelle/jcodemunch-mcp

Cut AI token costs 95%+ on code exploration. The leading MCP server for precise, symbol-level GitHub code retrieval via tree-sitter AST. Works with Claude Code, Cursor & any MCP client. 313B+ tokens s

## features

Most AI agents explore repositories the expensive way: open entire files, skim thousands of irrelevant lines, repeat. That is not "a little inefficient." That is a **token incinerator**.

**jCodeMunch indexes a codebase once and lets agents retrieve only the exact code they need**: functions, classes, methods, constants, outlines, and tightly scoped context bundles, with byte-level precision. It parses source with tree-sitter, stores structured symbol metadata (signature, kind, qualified name, summary, byte offsets) alongside raw file content in a local index, and fetches exact implementations on demand instead of re-reading files over and over.

| Task | Traditional approach | With jCodeMunch |
| --- | --- | --- |
| Find a function | Open and scan large files | Search symbol, fetch exact implementation |
| Understand a module | Read broad file regions | Pull only relevant symbols and imports |
| Explore repo structure | Traverse file after file | Query outlines, trees, and targeted bundles |
| "What breaks if I change X?" | Not possible | `get_blast_radius` |

Index once. Query cheaply. Keep moving. **Precision context beats brute-force context.**

---

## Evidence

### Reproducible token efficiency benchmark

Measured with `tiktoken cl100k_base` across three public repos pinned to upstream commits, run 2026-08-03 on v1.108.233. Workflow: `search_symbols` (top 5) + `get_symbol_source` × 3 per query. Two baselines, same run, same corpus, same file reader:

- **Grep-top-3**: `rg -l` the query terms, rank files by match count, open the top 3 whole. This is what a competent agent without the tool actually does, and it is the number to quote.
- **Read-all**: every indexed source file concatenated. A ceiling nobody pays; retained for continuity with previously published figures.

| Repository | Files | Symbols | Grep-top-3 baseline | jCodeMunch | vs grep | vs read-all |
|------------|------:|--------:|--------------------:|-----------:|--------:|------------:|
| expressjs/express | 182 | 200 | 15,724 avg | 1,007 avg | **15.6x** | 153.2x |
| fastapi/fastapi | 1,182 | 6,841 | 85,296 avg | 2,209 avg | **38.6x** | 372.9x |
| gin-gonic/gin | 98 | 1,179 | 31,975 avg | 1,545 avg | **20.7x** | 98.3x |
| **Grand total (15 task-runs)** | | | **664,975** | **23,805** | **27.9x** | 237.3x |

**Against a grep-and-read agent: 96.4% reduction, 27.9x fewer tokens.** Per-query results range from 7.3x to 84.3x (median 25.5x); no single multiple describes every query. Against read-all the figure is 99.6%, but nobody pays that ceiling. Compact [MUNCH](SPEC_MUNCH.md) wire encoding then trims a median 45.5% more bytes off responses.

Full methodology, pinned commits, harness, and known caveats: [benchmarks/METHODOLOGY.md](benchmarks/METHODOLOGY.md) · [Reproduce it yourself](benchmarks/REPRODUCING.md) · [TOKEN_SAVINGS.md](TOKEN_SAVINGS.md)

### Independent A/B test on a production codebase

50-iteration A/B test on a real Vue 3 + Firebase production codebase, jCodeMunch vs native tools (Grep/Glob/Read), Claude Sonnet 4.6, fresh session per iteration: success rate 80% vs 72%, timeout rate 32% vs 40%, mean cache creation down 10.5%. Tool-layer savings isolated from fixed overhead: 15-25%. One finding category appeared exclusively in the jCodeMunch variant: orphaned file detection via `find_importers`, a structural query native tools cannot answer without scripting. Full report: [benchmarks/ab-test-naming-audit-2026-03-18.md](benchmarks/ab-test-naming-audit-2026-03-18.md)

### Mentioned by

- **Artur Skowroński** (VirtusLab): *"roughly 80% fewer tokens, or 5× more efficient — index once, query cheaply forever"* · [GitHub All-Stars #15](https://virtuslab.com/blog/ai/code-munch-mcp-your-agent-starts-navigating)
- **Traci Lim** (AWS · ASEAN AI Lead): *"structural queries that native tools can't answer: find_importers, get_blast_radius, get_class_hierarchy, find_dead_code"* · [5 Repos That Save Token Usage in Claude Code](https://www.tracilzw.com/posts/5-repos-

## installation

#### One-click installs

[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_jCodeMunch-007ACC?style=for-the-badge&logo=visualstudiocode&logoColor=white)](vscode:mcp/install?%7B%22name%22%3A%20%22jcodemunch%22%2C%20%22command%22%3A%20%22uvx%22%2C%20%22args%22%3A%20%5B%22jcodemunch-mcp%22%5D%7D)
[![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install-24bfa5?style=for-the-badge&logo=visualstudiocode&logoColor=white)](vscode-insiders:mcp/install?%7B%22name%22%3A%20%22jcodemunch%22%2C%20%22command%22%3A%20%22uvx%22%2C%20%22args%22%3A%20%5B%22jcodemunch-mcp%22%5D%7D)
[![Install in Cursor](https://img.shields.io/badge/Cursor-Install_jCodeMunch-122122?style=for-the-badge&logo=cursor&logoColor=white)](cursor://anysphere.cursor-deeplink/mcp/install?name=jcodemunch&config=eyJjb21tYW5kIjogInV2eCIsICJhcmdzIjogWyJqY29kZW11bmNoLW1jcCJdfQ==)

#### Recommended: one command

```bash
uv tool install jcodemunch-mcp
jcodemunch-mcp init
```

No virtualenv to manage, nothing written into system Python, and it works as-is on PEP 668 distros (Ubuntu 24.04+, Debian 12+) where bare `pip install` is refused. [Don't have `uv` yet?](https://docs.astral.sh/uv/getting-started/installation/)

`init` auto-detects your MCP clients (Claude Code, Claude Desktop, Cursor, Windsurf, Continue), writes their config entries, installs the CLAUDE.md prompt policy so your agent actually uses jCodeMunch, optionally installs enforcement hooks, optionally indexes your project, and audits your agent config files for token waste.

<details>
<summary><b>Other install paths</b></summary>

| Command | Use it when |
|---|---|
| `uvx jcodemunch-mcp` | **Zero install.** Runs from an ephemeral environment — nothing lands on disk permanently. The client entries `init` writes already invoke the server this way, so for most setups this is all that ever runs. ⚠ Enforcement hooks are the exception: they're spawned by a minimal-PATH subshell and resolve the executable by name, so they need `uv tool install` (or `pipx`/`pip`) to work. |
| `pipx install jcodemunch-mcp` | You already standardise on pipx |
| `pip install jcodemunch-mcp` | Inside a virtualenv you manage yourself |

</details>

Verify:

```bash
jcodemunch-mcp --version
```

#### Manual Claude Code setup

```bash
claude mcp add -s user jcodemunch -- uvx jcodemunch-mcp
```

No install step — `uvx` fetches and runs the server on demand. Prefer it on your PATH (and required for enforcement hooks)? `uv tool install jcodemunch-mcp`, then `claude mcp add -s user jcodemunch jcodemunch-mcp`.

Then tell the agent to prefer the tools. This matters more than people think; installation makes the tools available but does not break the agent's brute-reading habit. One line in your CLAUDE.md does it:

```markdown
Call the jcodemunch_guide tool and strictly follow its instructions.
```

Using Cursor, Windsurf, Codex CLI, Antigravity, Gemini CLI, Qwen Code, Kiro, Cline, Zed, Goose, Hermes, Odysseus, or Paperclip? Every tested client configuration lives in **[CLIENTS.md](CLIENTS.md)**. Optional extras (local semantic search, AI summaries per provider) are in [QUICKSTART.md](QUICKSTART.md); the system surfaces each extra pulls in are documented in [SECURITY.md](SECURITY.md#optional-extras--system-surfaces-each-pulls-in).

---

## Quickstart

Full walkthrough: **[QUICKSTART.md](QUICKSTART.md)**. The two-minute version, inside your agent after `init`:

1. Ask: *"Index this repo with jcodemunch."*
2. Ask: *"Using jcodemunch, find the function that handles authentication and show me its source."*

The agent should answer via `search_symbols` and `get_symbol_source`, returning tens of lines instead of whole files. Confirm with `get_session_stats`: it reports tokens served and savings for the session. That is where the numbers on the meter come from.

Want to skip initial indexing for popular frameworks? Pre-built **starter packs**: `jcodemunch-mcp install-pack --list` (free packs need no license).

---

## 
