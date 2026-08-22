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

### What `openswarm init` sets up

The wizard asks three questions, detects what you already have, and writes the config for you:

1. **AI provider** (worker/reviewer) — it auto-detects existing auth and offers inline login:
   - `codex-responses` — ChatGPT subscription via OAuth (Codex models, native loop) — **easiest start**
   - `codex` — external `codex` CLI · `openrouter` — any model (API key/OAuth) · `gpt` — OpenAI OAuth
   - `lmstudio` / `local` — local servers, no account · `claude` — `claude -p` CLI (opt-in fallback)
2. **Task backend** — `local` SQLite issue store (no account) **or** `linear` (OAuth browser login or API key, then an arrow-key **team → project** picker for this repo)
3. **Notification channel** (optional) — `none` / `discord` / `slack` / `telegram` / `webhook`

It then writes **`.env`** (secrets, `chmod 600`), **`config.yaml`** (validated), and — if you mapped a Linear project — **`openswarm.json`** (this repo → Linear team/project). Finally it prints next steps and can launch browser OAuth.

> Re-running in a repo that already has `config.yaml` is refused unless you pass `--force`, and `init` refuses to overwrite a `config.yaml` that symlinks into the daemon's global config. For CI / non-interactive use, `openswarm init --yes` writes a sample config only.

![TUI Chat Interface](screenshots/tui.png)

### TUI keyboard shortcuts

| Key | Action |
|-----|--------|
| `Tab` | Switch tabs (Chat / Projects / Tasks / Stuck / Issues / Logs) |
| `Enter` | Send message |
| `Shift+Enter` | Newline |
| `i` | Focus input |
| `Esc` | Exit input focus |
| `Ctrl+C` | Quit |

Status bar shows: provider · model · message count · cumulative cost

---

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

# Code review
openswarm review                 # Review the working-tree changes
openswarm review --max           # Full-codebase audit: fan reviewer subagents over areas
                                 #   → report at .openswarm/audit/ + PM-synthesized Linear
                                 #   issues by default (≤10 cohesive, master + sub-issues)
openswarm review --max --fix     # after the audit, dependency-related findings are grouped;
                                 #   independent fix units run in isolated sandboxes, then
                                 #   a PR is published only after every re-review and trusted
                                 #   deterministic repository check passes
                                 #   add --in-place to edit the current working tree instead
openswarm review --max --concurrency 8   # widen the fan-out — areas auto-split to fill the pool
                                 # more --max flags: --no-linear (report only) · --issues-per-area
                                 #   (legacy spray) · --issues <id> (set parent) · --fallback
                                 #   <adapter> · --out <file> · --dry-run (print the plan)

# CI / test gate auto-fix (npm / Cargo / Python auto-detected)
openswarm fix                    # Run the checks (package.json scripts, or cargo check+test,
                                 #   or ruff/mypy/pytest), fan a fix-worker out over the
                                 #   failures, re-run until green
openswarm fix --checks lint,test # only these checks · --concurrency <n> · --rounds <n> (default 3)
                                 # any language: put {"checks": {"test": "pytest -x"}} in openswarm.json

# PR autopilot (on-demand — conflict → comments → CI; does not merge)
openswarm pr status              # Snapshot: conflicts, CI, CHANGES_REQUESTED / critical comments
openswarm pr status --json       # Machine-readable; exit 0 only when merge-ready
openswarm pr fix                 # One-shot fix for the current branch's open PR (or --number N)
openswarm pr review              # Re-apply reviewer feedback only (Claude, Codex, or CHANGES_REQUESTED) — no conflict/CI work
openswarm pr review --fresh      # Run a brand-new code review of the PR diff and post it as a comment
openswarm pr review --all        # Review every open PR in the repo instead of just one (combine with --fresh)
openswarm pr watch               # Loop fix until merge-ready or --rounds exhausted (default 5)
openswarm pr create              # Local fix → commit → push → gh pr create (from feature branch)
openswarm pr create --no-fix --issue INT-123 --title "feat: …"  # skip local fix; set issue id

# Code Registry & BS Detector
openswarm check --scan           # Scan repo → register all entities
openswarm check src/foo.ts       # File brief (entities, tests, risk)
openswarm check --bs             # BS pattern scan (bad code smells)
openswarm check --stats          # Registry statistics
openswarm check --high-risk      # High-risk entities
openswarm check --search "name"  # Full-text search
openswarm annotate "funcName" --deprecate "reason"
openswarm a

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
