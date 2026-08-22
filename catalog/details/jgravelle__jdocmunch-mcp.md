# jgravelle/jdocmunch-mcp

The leading, most token-efficient MCP server for documentation exploration and retrieval via structured section indexing

## features

**The problem.** An agent asked "how do I configure authentication?" opens a documentation file, skims hundreds of paragraphs it does not need, opens another, and repeats. Large context windows do not fix this. They just make the waste affordable enough to ignore until the bill arrives, and they crowd out the context the model actually needed.

**The mechanism.** jDocMunch parses a documentation set into a section tree keyed by heading hierarchy, stores each section's byte offsets into the original file, and exposes retrieval over MCP. Sections keep durable identities across re-indexing as long as path, heading text, and heading level are unchanged.

**The outcome.** The unit of access changes from *file* to *section*. An agent retrieves the installation section, one configuration block, or a specific heading subtree — and nothing else.

---

## installation

**Requirements:** Python 3.10+, any MCP-compatible client.

```bash
uv tool install jdocmunch-mcp
jdocmunch-mcp init
```

No virtualenv to manage, nothing written into system Python, and it works as-is on PEP 668 distros (Ubuntu 24.04+, Debian 12+) where bare `pip install` is refused. [Don't have `uv` yet?](https://docs.astral.sh/uv/getting-started/installation/)

`init` detects your MCP clients, writes their config entries, installs the doc-exploration prompt policy so your agent actually reaches for the tools, and optionally installs hooks and indexes your docs.

<details>
<summary><b>Other install paths</b></summary>

| Command | Use it when |
|---|---|
| `uvx jdocmunch-mcp` | **Zero install.** Runs from an ephemeral environment — nothing lands on disk permanently. The client entries `init` writes already invoke the server this way, so for most setups this is all that ever runs. ⚠ Hooks are the exception: they're spawned by a minimal-PATH subshell and resolve the executable by name, so they need `uv tool install` (or `pipx`/`pip`) to work. |
| `pipx install jdocmunch-mcp` | You already standardise on pipx |
| `pip install jdocmunch-mcp` | Inside a virtualenv you manage yourself |

</details>

Verify:

```bash
jdocmunch-mcp --version
```

**Manual Claude Code setup:**

```bash
claude mcp add -s user jdocmunch -- uvx jdocmunch-mcp
```

No install step — `uvx` fetches and runs the server on demand. Prefer it on your PATH (and required for hooks)? `uv tool install jdocmunch-mcp`, then `claude mcp add -s user jdocmunch jdocmunch-mcp`.

Installing the server makes the tools available; it does not break an agent's habit of brute-reading files. One line in your `CLAUDE.md` does that:

```markdown
Call the jdocmunch_guide tool and strictly follow its instructions.
```

---

## limitations

- **Section retrieval helps least on small files.** If a document has one heading and 40 lines, retrieving the section and reading the file cost about the same.
- **Semantic search requires an embedding provider.** Without one, search is lexical only — good for identifiers and exact phrasing, weaker for paraphrased questions.
- **Office formats need the optional `[office]` extra** and are supported for local indexing only.
- **Freshness is disclosed, not guaranteed.** A section whose source cannot be checked is reported as `unknown` rather than assumed current.
- **jDocMunch does not parse code.** Symbols, signatures, and call graphs belong to [jcodemunch-mcp](https://github.com/jgravelle/jcodemunch-mcp); tabular data belongs to [jdatamunch-mcp](https://github.com/jgravelle/jdatamunch-mcp).

---
