# thedotmack/claude-mem

Persistent Context Across Sessions for Every Agent – Captures everything your agent does during sessions, compresses it with AI, and injects relevant context back into future sessions. Works with Clau

## installation

**Installing for someone as an AI agent?** If the user is available, run `npx claude-mem install --setup browser` on their computer and keep it running. It prepares the local runtime, then opens setup in their browser; if the page doesn't open, give them the printed URL. Every choice (agents, integrations, skills, model, usage analytics, the optional email) is made by the user on that page, so there are no terminal questions to relay. If the user is away, run `npx claude-mem install --setup defer`: it prepares the runtime and leaves setup waiting for their first visit, and their next session shows them the link. Don't make their choices for them.

```bash
npx claude-mem install
```

The installer finds the agents on your machine and asks which ones to set up. Then just start working: observations stream in from your first prompt, and your second session in a project opens with memory from the first. (Copilot CLI, Goose, Roo Code and Warp get memory search only, so their sessions don't add to it.)

The installer sets everything up first, then asks you to sign in to claude-mem in your browser (email magic link, no card required to sign in). Choosing the **claude-mem observer** then starts its **30 Day Free Trial** on a checkout page that asks for a payment method; once it completes, the installer saves your memory key. With the observer, memory runs off-plan, so you get up to 100% more usage from your plan. When the free trial ends, memory automatically falls back to your Anthropic plan unless you subscribe. After sign-in you pick your memory provider: the claude-mem observer, your own OpenRouter or Gemini key, or your Anthropic plan.

Prefer to skip the sign-in? Pass an explicit `--provider` flag, set `CLAUDE_MEM_ONLINE_OPTIN=false`, or run in CI/non-interactive shells — the installer completes without any account interaction.

Your memory lives in `~/.claude-mem` on your machine. Cloud sync is opt-in. Anonymous usage analytics are on by default; `npx claude-mem telemetry disable` turns them off ([what's collected](https://docs.claude-mem.ai/telemetry)).

Or install from the plugin marketplace inside Claude Code:

```bash
/plugin marketplace add thedotmack/claude-mem

/plugin install claude-mem
```

Restart Claude Code. Context from previous sessions will automatically appear in new sessions.

> **Note:** Claude-Mem is also published on npm, but `npm install -g claude-mem` installs the **SDK/library only** — it does not register the plugin hooks or set up the worker service. Always install via `npx claude-mem install` or the `/plugin` commands above.

### Other agents

`npx claude-mem install` covers every supported agent. To set up one agent directly, pass `--ide`.

**OpenCode** (1.3.4 or later, including OpenCode 2). Restart OpenCode after installing.

```bash
npx claude-mem install --ide opencode
```

**T3 Code** (Codex and Claude Code providers). The installer discovers T3 Code's enabled providers, registers native Claude-Mem plugins in their configured homes, and supports T3-managed Codex. Restart T3 Code, trust the provider's hooks when prompted, and start a new thread. See the [T3 Code integration guide](https://docs.claude-mem.ai/t3code-integration) for custom server settings, status, and removal.

```bash
npx claude-mem install --ide t3code
```

**Antigravity CLI** ([setup guide](https://docs.claude-mem.ai/antigravity-cli/setup)):

```bash
npx claude-mem install --ide antigravity
```

**OMP (Oh My Pi):**

```bash
npx claude-mem install --ide omp
```

**Pi and DeepSeek Harness** use the worker runtime. See [native harness setup](docs/native-harness-integrations.md) for capture, recall, and troubleshooting.

```bash
npx claude-mem install --ide pi
npx claude-mem install --ide dsh --dsh-profile tui
```

**Grok Bot:** see [Grok Bot](#grok-bot) below.

```bash
npx claude-mem install --ide grok-bot
```

The full list of `--ide` values is in `npx claude-mem --help`.

#### Grok Bot

Grok Bot has no host hooks, so we watch the 

## configuration

- **[Configuration](https://docs.claude-mem.ai/configuration)** - Environment variables & settings
- **[Development](https://docs.claude-mem.ai/development)** - Building, testing, contributing
- **[Troubleshooting](https://docs.claude-mem.ai/troubleshooting)** - Common issues & solutions

---

## How It Works

1. **Your agent works.** Hooks in your agent hand each tool call (what it reads, edits and runs) to a small local worker.
2. **The observer takes notes.** A second agent turns that activity into short observations, and writes a summary when the session ends.
3. **The next session starts with them.** When a session starts, your agent gets a compact index of the observations that matter for this project, and fetches full details only when it needs them.

Memory injection starts on your second session in a project. To front-load a whole repo instead, run `/learn-codebase` (~5 minutes on a typical repo, optional).

See [Architecture Overview](https://docs.claude-mem.ai/architecture/overview) for details.

### How it fits together

For contributors, the main parts and where they live:

- **The `claude-mem` command** (`src/npx-cli/index.ts`): install, repair, doctor, start, search and the rest. The installer puts a small launcher on PATH so hooks can run `claude-mem` directly.
- **Hooks** (`src/cli/hook-command.ts`, one adapter per agent in `src/cli/adapters/`): each agent event runs one shell-free command, such as `claude-mem hook claude-code <event>`. For Claude Code that's Setup (`claude --init` / `--maintenance`), SessionStart, UserPromptSubmit, PreToolUse, PostToolUse, PostToolUseFailure, Stop, SubagentStop and SessionEnd.
- **The worker** (`src/services/worker-service.ts`, routes in `src/services/worker/http/routes/`): a local HTTP service managed by Bun. It takes tool activity from the hooks, runs the observer, and serves the viewer and search.
- **The observer** (prompts in `src/sdk/`, one provider per model source in `src/services/worker/`, such as `ClaudeProvider.ts` and `OpenRouterProvider.ts`): turns tool activity into observations and summaries.
- **Storage** (`src/services/sqlite/`): SQLite at `~/.claude-mem/claude-mem.db` holds sessions, observations and summaries. Chroma adds semantic search on top of SQLite's keyword search (`src/services/worker/search/`).
- **Context** (`src/services/context/`): builds the block a new session starts with.
- **Search** (`src/servers/mcp-server.ts`, `plugin/skills/mem-search/`): the MCP tools and the mem-search skill that drives them.
- **The viewer** (`src/ui/viewer/` at `/viewer`, `src/ui/my-work/` at `/`): memory, sessions and settings, plus My Work.
- **The built plugin** (`plugin/`): written by `npm run build`; edit `src/`, not the generated scripts.

The words we use for each of these, and the story they tell, are in [docs/story.md](docs/story.md).

---

## tools

Search runs through three MCP tools in a token-efficient three-step workflow. The mem-search skill drives it for you:

**The three steps:**

1. **`search`** - Get compact index with IDs (~50-100 tokens/result)
2. **`timeline`** - Get chronological context around interesting results
3. **`get_observations`** - Fetch full details ONLY for filtered IDs (~500-1,000 tokens/result)

**Step by step:**
- Your agent uses MCP tools to search your memory
- Start with `search` to get an index of results
- Use `timeline` to see what was happening around specific observations
- Use `get_observations` to fetch full details for relevant IDs
- **Index rows are about a tenth the size of a full record**: ~50-100 tokens versus ~500-1,000. Filtering decides how many records you pay to fetch, not how large each one is; the workflow's total cost also includes the timeline and the selected details. The ratio is not a measured recall or end-to-end saving ([#4138](https://github.com/thedotmack/claude-mem/issues/4138)).

**Available MCP Tools:**

1. **`search`** - Search memory index with full-text queries, filters by type/date/project
2. **`timeline`** - Get chronological context around a specific observation or query
3. **`get_observations`** - Fetch full observation details by IDs (always batch multiple IDs)

**Example Usage:**

```typescript
// Step 1: Search for index
search(query="authentication bug", type="bugfix", limit=10)

// Step 2: Review index, identify relevant IDs (e.g., #123, #456)

// Step 3: Fetch full details
get_observations(ids=[123, 456])
```

The worker also offers tools for code navigation (`smart_search`, `smart_outline`, `smart_unfold`), saving a note on purpose (`save_memory`) and tracking work in progress. See [Search Tools Guide](https://docs.claude-mem.ai/usage/search-tools) for detailed examples.

---

## requirements

- **Node.js**: 20.19 or later in the 20.x line, or 22.12 or later
- **A supported agent**: Claude Code (latest, with plugin support) or any agent in [Other agents](#other-agents)
- **Bun**: JavaScript runtime and process manager (auto-installed if missing)
- **uv**: Python package manager for vector search (auto-installed if missing)
- **SQLite 3**: For persistent storage (bundled)

---
