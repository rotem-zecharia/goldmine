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
