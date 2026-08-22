# unohee/OpenSwarm

OpenSwarm — Autonomous AI dev team orchestrator powered by Claude Code CLI. Discord control, Linear integration, cognitive memory.

## installation

```bash
npm install -g @intrect/openswarm
openswarm init         # interactive setup wizard — provider auth + Linear OAuth + config
openswarm doctor       # verify your environment (runtime, native deps, providers, ports)
openswarm              # launches the TUI chat
```

`openswarm init` walks you through provider authentication, optional Linear OAuth (team/project picker), and writes a validated `config.yaml`. Prefer wiring a provider by hand? You need **one** first: `openswarm auth login` (ChatGPT OAuth, used by `codex`/`gpt`), `openswarm auth login --provider openrouter` (or `export OPENROUTER_API_KEY=…`), or just have an authenticated `claude` on PATH. Check what's wired with `openswarm auth status`, and diagnose any gaps with `openswarm doctor`.

## tools

```bash
openswarm                        # TUI chat (default)
openswarm chat [session]         # Simple readline chat
openswarm resume                 # Reopen the most recent chat session (conversation + goal)
openswarm start                  # Start full daemon (requires config.yaml)
openswarm run "Fix the bug" -p ~/my-project   # Run a single task
openswarm exec "Run tests" --local --pipeline # Execute via daemon
openswarm init                   # Interactive setup wizard (provider auth, Linear OAuth, config)
openswarm provider               # Show/switch the active provider (interactive picker)
openswarm provider claude        # Switch straight to a provider — a running daemon switches in place
openswarm doctor                 # Diagnose environment (runtime, native deps, providers, ports)
openswarm validate               # Validate config.yaml

## configuration

| Option | Description |
|--------|-------------|
| `--path <path>` | Project path (default: cwd) |
| `--timeout <seconds>` | Timeout in seconds (default: 600) |
| `--local` | Execute locally without daemon |
| `--pipeline` | Full pipeline: worker + reviewer + tester + documenter |
| `--worker-only` | Worker only, no review |
| `-m, --model <model>` | Model override for worker |

Exit codes: `0` success · `1` failure · `2` timeout

---

## requirements

- **Node.js** >= 22
- **At least one LLM provider**:
  - **OpenAI Codex** — `codex-responses` (ChatGPT OAuth, native loop, no extra binary) is the smoothest start; `codex` delegates to the external Codex CLI. `openswarm auth login` handles the ChatGPT OAuth
  - **OpenRouter** — any model; `OPENROUTER_API_KEY` or `openswarm auth login --provider openrouter`
  - **OpenAI GPT** — `openswarm auth login --provider gpt`
  - **Local** — LM Studio (`lmstudio`, `:1234`) or Ollama (`local`, `:11434`), auto-detected, no auth
  - **Claude Code CLI** (`claude -p`) — opt-in fallback; an authenticated `claude` on PATH
- **Native build toolchain** — `better-sqlite3` and `@lancedb/lancedb` are native modules. Prebuilt binaries cover common platforms; if yours lacks one, `npm install` builds from source and needs `python3` + a C/C++ toolchain (`build-essential` on Linux, Xcode Command Line Tools on macOS)
- **For autonomous mode only** (optional): **Linear** — sign in with `openswarm auth login --provider linear` (OAuth PKCE) or use an API key + team ID; **Discord** bot token (message content intent); **GitHub CLI** (`gh`) for CI monitoring

## features

- **Multi-Provider Adapters** — Pluggable adapter system: **OpenAI Codex/GPT**, **OpenRouter** (any model, native agentic loop), **local models** (Ollama, LM Studio), and **Claude Code** (`claude -p`, opt-in) with runtime provider switching
- **Code Registry** — SQLite-backed entity registry tracking every function/class/type across 8 languages, with complexity scoring, test mapping, and risk assessment
- **BS Detector** — Built-in static analysis engine that detects bad code patterns (empty catch, hardcoded secrets, `as any`, etc.) with pipeline guard integration
- **Autonomous Pipeline** — Cron-driven heartbeat fetches Linear issues, runs Worker/Reviewer pair loops, and updates issue state automatically
- **Worker/Reviewer Pairs** — Multi-iteration code generation with automated review, testing, and documentation stages
- **Codebase Audit (`review --max`)** — fans reviewer subagents out over directory-shaped areas (auto-split to fill `--concurrency`), aggregates a deduped verdict into a markdown report, and synthesizes ≤10 cohesive Linear issues via a PM agent. Both `review` modes consult repository-local prior review logs; resolved/stale findings are not repeated, and byte-identical duplicate follow-ups are suppressed while unresolved issues remain visible. `--fix` groups findings by repository dependency closure, injects the package manager/manifests/verification contract and repo knowledge, runs only independent fix units concurrently in isolated sandboxes, and promotes disjoint in-scope diffs into an audit worktree. It publishes the PR only when every area re-approves and trusted deterministic verification passes; unavailable dependencies/checks fail closed. `--in-place` keeps edits in the current working tree but uses the same gates. Language-agnostic; codex usage-limit aware with automatic `claude` fallback
- **CI / test gate auto-fix (`openswarm fix`)** — runs the project's objective checks (lint / typecheck / build / test), groups the failures by file into areas, fans a fix-worker out over each, then **re-runs the checks and repeats until green** (or the round budget). Deterministic convergence — unlike the review fix pass, it verifies its own work. Multi-language: auto-detects npm scripts, `Cargo.toml` (`cargo check`/`test`, clippy on request), and Python tooling (`ruff`/`mypy`/`pytest`, gated on the repo's config); any other toolchain via a `"checks"` map in `openswarm.json`
- **PR autopilot (`openswarm pr`)** — on-demand surface over the daemon's PRProcessor + `commitAndCreatePR`. `status` reports conflicts / review feedback / CI; `fix` runs one autopilot pass (conflict → comments → CI); `review` re-applies reviewer feedback only, skipping conflict/CI work — recognizes Claude, Codex, and any formal `CHANGES_REQUESTED` review; `review --fresh` instead runs a brand-new code review of the PR's current diff (the same reviewer `openswarm review` uses) and posts the verdict as a PR comment, independent of any existing feedback; `review --all` reviews every open PR in the repo sequentially (combine with `--fresh`) instead of just the current branch's PR or `--number`; `watch` loops until merge-ready; `create` publishes the current feature branch (local fix → commit → push → `gh pr create`). Never merges or enables auto-merge.
- **Decision Engine** — Scope validation, rate limiting, priority-based task selection, and workflow mapping
- **Cognitive Memory** — LanceDB vector store with Xenova/multilingual-e5-base embeddings for long-term recall across sessions
- **Repo Knowledge Loop** — workers learn each repository over time: task outcomes (success patterns, review-rejection pitfalls) are stored per-repo and recalled into the next worker prompt
- **SWE-bench Verified** — the agentic harness solves real SWE-bench Lite issues, graded by the official harness; hybrid mode (frontier diagnosis + lightweight implementer) resolved 3/3 attempted instances ([benchmarks/RUBRIC.md](benchmarks/RUBRIC.md))
- **Knowledge Graph** — Stati
