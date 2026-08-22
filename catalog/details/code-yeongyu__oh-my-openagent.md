# code-yeongyu/oh-my-openagent

omo/lazycodex: The coding agent for tokenmaxxers;the one and only agent harness for complex codebases. For your Codex, for your OpenCode

## installation

oh-my-openagent ships in three editions of the same product: two plugins that load into a host you already run, plus one standalone edition.

- **Ultimate Edition (omo for OpenCode)** — full omo. 11 agents, 54+ lifecycle hooks, 5 built-in MCPs, all slash commands, Team Mode, `/goal`, ultrawork — everything. Hashline edits are opt-in (`hashline_edit: true`).
- **Light Edition (omo for Codex CLI)** — the portable components that fit Codex's plugin system: `rules`, `comment-checker`, `git-bash`, `lsp`, `ultrawork`, `ulw-loop`, `start-work-continuation`, and `telemetry` at the core, plus `teammode` and supporting components (`bootstrap`, `codegraph`, `lcx`, and more), plugin-scoped MCPs for `grep_app`, `context7`, `codegraph`, `git_bash`, and `lsp`, and the shared `ast-grep` skill. It installs Codex agent TOMLs into `~/.codex/agents/`. No OpenCode `team_*` tools — Codex CLI's own spawn/collaboration surface does that work.
- **Senpi Edition (standalone, beta)** — the native `omo` command with the OMO extension built in. It installs from `omo-ai@beta` rather than loading into OpenCode or Codex.

Pick the edition(s) you want.

## limitations

We are restructuring the codebase to support multiple agent harnesses (OpenCode, Codex, Pi, Claude Code, and others). The most urgent work is the package layering refactor: separating pure TypeScript core logic, MCP servers, skills, and adapter shims into distinct layers so the same logic can be reused across harnesses without duplication.

If you want to contribute, read the [ROADMAP](./ROADMAP.md) first. PRs related to this refactor should use the `ROADMAP` label so we can track them.

## tools

LSP, AST-Grep, Tmux, and MCP, actually integrated, not duct-taped together.

- **LSP**: `lsp_rename`, `lsp_goto_definition`, `lsp_find_references`, `lsp_diagnostics`. IDE precision for every agent.
- **AST-Grep**: Pattern-aware code search and rewriting across 25 languages.
- **Tmux**: Full interactive terminal. REPLs, debuggers, TUI apps. Your agent stays in session.
- **MCP**: Web search, official docs, GitHub code search. All baked in.

## features

Features you'll think should've always existed. Once you use them, you can't go back.

See full [Features Documentation](docs/reference/features.md).

**Quick Overview:**
- **Agents**: Sisyphus (the main agent), Prometheus (planner), Oracle (architecture/debugging), Librarian (docs/code search), Explore (fast codebase grep), Multimodal Looker
- **Background Agents**: Run multiple agents in parallel like a real dev team
- **LSP & AST Tools**: Refactoring, rename, diagnostics, AST-aware code search
- **Hash-anchored Edit Tool** (opt-in via `hashline_edit: true`): `LINE#ID` references validate content before applying every change. Surgical edits, zero stale-line errors
- **Context Injection**: Auto-inject AGENTS.md, README.md, conditional rules
- **Claude Code Compatibility**: Full hook system, commands, skills, agents, MCPs
- **Built-in MCPs**: websearch (Exa), context7 (docs), grep_app (GitHub search) — injected at runtime by the plugin; not visible in `opencode mcp list` (see [MCP docs](docs/reference/features.md#native-vs-plugin-injected-mcps))
- **Session Tools**: List, read, search, and analyze session history
- **Productivity Features**: Goal, Todo Enforcer, Comment Checker, Think Mode, and more
- **Doctor Command**: Built-in diagnostics (`bunx oh-my-opencode doctor`) verify plugin registration, config, models, and environment
- **Model Fallbacks**: `fallback_models` can mix plain model strings with per-fallback object settings in the same array
- **File Prompts**: Load prompts from files with `file://` support in agent configurations
- **Session Recovery**: Automatic recovery from session errors, context window limits, and API failures
- **Model Setup**: Agent-model matching is built into the [Installation Guide](docs/guide/installation.md#step-5-understand-your-model-setup)

## configuration

Opinionated defaults, adjustable if you insist.

See [Configuration Documentation](docs/reference/configuration.md).

**Quick Overview:**
- **Config Locations**: User `~/.omo/omo.jsonc` plus walked project `.omo/omo.jsonc` configs up to `$HOME`; closest wins. Legacy `oh-my-*` files are migrated once into `omo.jsonc`.
- **JSONC Support**: Comments and trailing commas supported
- **Agents**: Override models, temperatures, prompts, and permissions for any agent
- **Built-in Skills**: `playwright` (browser automation), `git-master` (atomic commits)
- **Sisyphus Agent**: Main orchestrator with Prometheus (Planner) and Metis (Plan Consultant)
- **Background Tasks**: Configure concurrency limits per provider/model
- **Categories**: Domain-specific task delegation (`visual-engineering`, `ultrabrain`, `deep`, `artistry`, `quick`, `unspecified-low`, `unspecified-high`, `writing`, plus custom names)
- **Hooks**: 54+ lifecycle hooks (61 with Team Mode), all configurable via `disabled_hooks`
- **MCPs**: Built-in websearch (Exa), context7 (docs), grep_app (GitHub search) — runtime-injected, not shown in `opencode mcp list`
- **LSP**: Full LSP support with refactoring tools
- **Experimental**: Aggressive truncation, auto-resume, and more
