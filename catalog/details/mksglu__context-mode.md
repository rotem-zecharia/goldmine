# mksglu/context-mode

Context window optimization for AI coding agents. Sandboxes tool output (98% reduction), persists session memory, and enforces routing across 17 platforms via MCP + hooks.

## installation

Platforms are grouped by install complexity. Hook-capable platforms get automatic routing enforcement. Non-hook platforms need a one-time routing file copy.

<details open>
<summary><strong>Claude Code</strong> — plugin marketplace, fully automatic</summary>

**Prerequisites:** Claude Code v1.0.33+ (`claude --version`). If `/plugin` is not recognized, update first: `brew upgrade claude-code` or `npm update -g @anthropic-ai/claude-code`.

**Install:**

```bash
/plugin marketplace add mksglu/context-mode
/plugin install context-mode@context-mode
```

Restart Claude Code (or run `/reload-plugins`).

**Verify:**

```
/context-mode:ctx-doctor
```

All checks should show `[x]`. The doctor validates runtimes, hooks, FTS5, and plugin registration.

**Routing:** Automatic. The SessionStart hook injects routing instructions at runtime — no file is written to your project. The plugin registers all hooks (PreToolUse, PostToolUse, UserPromptSubmit, PreCompact, SessionStart, Stop) and 11 MCP tools — six sandbox tools (`ctx_batch_execute`, `ctx_execute`, `ctx_execute_file`, `ctx_index`, `ctx_search`, `ctx_fetch_and_index`) plus five meta-tools (`ctx_stats`, `ctx_doctor`, `ctx_upgrade`, `ctx_purge`, `ctx_insight`).

| Slash Command | What it does |
|---|---|
| `/context-mode:ctx-stats` | Context savings — per-tool breakdown, tokens consumed, savings ratio. |
| `/context-mode:ctx-doctor` | Diagnostics — runtimes, hooks, FTS5, plugin registration, versions. |
| `/context-mode:ctx-index` | Index a local file or directory into the persistent FTS5 knowledge base. |
| `/context-mode:ctx-search` | Search previously indexed content. |
| `/context-mode:ctx-upgrade` | Pull latest, rebuild, migrate cache, fix hooks. |
| `/context-mode:ctx-purge` | Permanently delete all indexed content from the knowledge base. |
| `/context-mode:ctx-insight` | Opens the hosted Insight dashboard ([context-mode.com/insight](https://context-mode.com/insight)) in your browser — org analytics for AI-assisted engineering teams. |

> **Note:** Slash commands are a Claude Code plugin feature. On other platforms, type `ctx stats`, `ctx doctor`, `ctx index`, `ctx search`, `ctx upgrade`, or `ctx insight` in the chat — the model calls the MCP tool automatically. See [Utility Commands](#utility-commands).

**Status line (optional):** Claude Code's plugin manifest cannot declare a status line, so this is a one-time manual edit to `~/.claude/settings.json`:

```json
{
  "statusLine": {
    "type": "command",
    "command": "context-mode statusline"
  }
}
```

After saving, restart Claude Code. The bar shows `$ saved this session · $ saved across sessions · % efficient` so you can see savings accumulate in real time. The wiring is path-free — `context-mode statusline` resolves through the bundled CLI regardless of where the plugin cache lives.

<details>
<summary>Alternative — MCP-only install (no hooks or slash commands)</summary>

```bash
claude mcp add context-mode -- npx -y context-mode
```

This gives you all 11 MCP tools without automatic routing. The model can still use them — it just won't be nudged to prefer them over raw Bash/Read/WebFetch. Good for trying it out before committing to the full plugin.

</details>

</details>

<details>
<summary><strong>Gemini CLI</strong> — one config file, hooks included</summary>

**Prerequisites:** Node.js >= 22.5 (or Bun), Gemini CLI installed.

**Install:**

1. Install context-mode globally:

   ```bash
   npm install -g context-mode
   ```

2. Add the following to `~/.gemini/settings.json`. This single file registers the MCP server and all four hooks:

   ```json
   {
     "mcpServers": {
       "context-mode": {
         "command": "context-mode"
       }
     },
     "hooks": {
       "BeforeTool": [
         {
           "matcher": "run_shell_command|read_file|read_many_files|grep_search|search_file_content|web_fetch|activate_skill|mcp__plugin_context-mode|mcp__context-mode|mcp__(?!.*context-mode)",
           "hooks": [{ "type": "com

## tools

| Tool | What it does | Context saved |
|---|---|---|
| `ctx_batch_execute` | Run multiple commands + search multiple queries in ONE call. Opt-in `concurrency: 1-8` for I/O-bound batches. | 986 KB → 62 KB |
| `ctx_execute` | Run code in 12 languages. Only stdout enters context. | 56 KB → 299 B |
| `ctx_execute_file` | Process files in sandbox. Raw content never leaves. | 45 KB → 155 B |
| `ctx_index` | Chunk markdown into FTS5 with BM25 ranking. | 60 KB → 40 B |
| `ctx_search` | Query indexed content with multiple queries in one call. | On-demand retrieval |
| `ctx_fetch_and_index` | Fetch URL, chunk and index. Cache reuses content within TTL (default 24h, override per-call with `ttl: <ms>`). `ttl: 0` or `force: true` to bypass. Pass `requests: [{url, source}, ...]` + `concurrency: 1-8` for parallel multi-URL. | 60 KB → 40 B |
| `ctx_stats` | Show context savings, call counts, and session statistics. | — |
| `ctx_doctor` | Diagnose installation: runtimes, hooks, FTS5, versions. | — |
| `ctx_upgrade` | Upgrade to latest version from GitHub, rebuild, reconfigure hooks. | — |
| `ctx_purge` | Permanently deletes all indexed content from the knowledge base. | — |

## How the Sandbox Works

Each `ctx_execute` call spawns an isolated subprocess with its own process boundary. Scripts can't access each other's memory or state. The subprocess runs your code, captures stdout, and only that stdout enters the conversation context. The raw data — log files, API responses, snapshots — never leaves the sandbox.

Twelve language runtimes are available: JavaScript, TypeScript, Python, Shell, Ruby, Go, Rust, PHP, Perl, R, Elixir, and C#. Bun is auto-detected for 3-5x faster JS/TS execution.

Authenticated CLIs work through credential passthrough — `gh`, `aws`, `gcloud`, `kubectl`, `docker` inherit environment variables and config paths without exposing them to the conversation.

When output exceeds 5 KB and an `intent` is provided, Context Mode switches to intent-driven filtering: it indexes the full output into the knowledge base, searches for sections matching your intent, and returns only the relevant matches with a vocabulary of searchable terms for follow-up queries.

## How the Knowledge Base Works

The `ctx_index` tool chunks markdown content by headings while keeping code blocks intact, then stores them in a **SQLite FTS5** (Full-Text Search 5) virtual table. The SQLite backend is selected automatically at runtime: `bun:sqlite` on Bun, `node:sqlite` on Node.js >= 22.5, and `better-sqlite3` everywhere else. Search uses **BM25 ranking** — a probabilistic relevance algorithm that scores documents based on term frequency, inverse document frequency, and document length normalization. **Porter stemming** is applied at index time so "running", "runs", and "ran" match the same stem. Titles and headings are weighted **5x** in BM25 scoring for precise navigational queries.

When you call `ctx_search`, it returns relevant content snippets focused around matching query terms — not full documents, not approximations, the actual indexed content with smart extraction around what you're looking for. `ctx_fetch_and_index` extends this to URLs: fetch, convert HTML to markdown, chunk, index. The raw page never enters context. Use the `contentType` parameter to filter results by type (e.g. `code` or `prose`).

### Ranking: Reciprocal Rank Fusion

Search runs two parallel strategies and merges them with **Reciprocal Rank Fusion (RRF)**:

- **Porter stemming** — FTS5 MATCH with porter tokenizer. "caching" matches "cached", "caches", "cach".
- **Trigram substring** — FTS5 trigram tokenizer matches partial strings. "useEff" finds "useEffect", "authenticat" finds "authentication".

RRF merges both ranked lists into a single result set, so a document that ranks well in both strategies surfaces higher than one that ranks well in only one. This replaces the old cascading fallback approach where trigram results were only used if porter returned nothing.

### Proxim

## configuration

| Variable | Default | Purpose |
|---|---|---|
| `CONTEXT_MODE_DIR` | Adapter default, for example `~/.codex/context-mode` or `~/.claude/context-mode` | Since v1.0.147. Absolute writable root for context-mode storage. Sessions and stats use `<root>/sessions`; indexed content uses `<root>/content`. Empty or whitespace-only values are treated as unset and shown by `ctx_doctor`; non-empty values must be absolute. `~` is not expanded. |

### Routing-guidance environment variables

| Variable | Default | Purpose |
|---|---|---|
| `CONTEXT_MODE_EXTERNAL_MCP_NUDGE_EVERY` | `10` | Cadence (in tool calls) at which the PreToolUse hook re-injects the "wrap large external-MCP payloads in `ctx_execute`" guidance. The original implementation ([#529](https://github.com/mksglu/context-mode/pull/529)) fired only once per session, which got lost after context compaction in MCP-heavy sessions (e.g. 50+ Jira/Slack/Notion calls — see [#567](https://github.com/mksglu/context-mode/issues/567) follow-up). The default re-fires every 10th matching call, keeping the guidance in the model's recent window. Range `[1, 100]`; invalid values fall back to `10`. Set to `1` for "every call" (most aggressive — adds ~250 tokens/call) or to a larger value for less frequent reminders. |

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for the development workflow and TDD guidelines.

```bash
git clone https://github.com/mksglu/context-mode.git
cd context-mode && npm install && npm test
```

## License

Licensed under [Elastic License 2.0](LICENSE) (source-available). You can use it, fork it, modify it, and distribute it. Two things you can't do: offer it as a hosted/managed service, or remove the licensing notices. We chose ELv2 over MIT because MIT permits repackaging the code as a competing closed-source SaaS — ELv2 prevents that while keeping the source available to everyone.
