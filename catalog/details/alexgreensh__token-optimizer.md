# alexgreensh/token-optimizer

Find the ghost tokens. Fix them. Survive compaction. Avoid context quality decay.

## installation

**Claude Code (recommended):**

```
/plugin marketplace add alexgreensh/token-optimizer
/plugin install token-optimizer@alexgreensh-token-optimizer
```

Then in Claude Code: `/token-optimizer`

> **Enable auto-update after installing.** Claude Code ships third-party marketplaces with auto-update off by default. `/plugin` → **Marketplaces** tab → select `alexgreensh-token-optimizer` → **Enable auto-update**. One-time, 10 seconds.
>
> After install, run `/token-optimizer` once to set up hooks. From there, everything runs automatically: compression, checkpoints, quality scoring, dashboard updates. You don't need to run any command again unless you want an audit.

> **Claude Code cloud sessions (claude.ai/code).** A cloud session runs in a fresh container and never reads the plugins installed on your machine, so the two commands above are not enough there (`/plugin` itself is not available in cloud sessions). Either enable Token Optimizer for your claude.ai account (Desktop app → **Customize** → plugins), or commit this to the repo's `.claude/settings.json` so every cloud session on that repo installs it at start:
>
> ```json
> {
>   "extraKnownMarketplaces": {
>     "alexgreensh-token-optimizer": { "source": { "source": "github", "repo": "alexgreensh/token-optimizer" } }
>   },
>   "enabledPlugins": { "token-optimizer@alexgreensh-token-optimizer": true }
> }
> ```
>
> Hooks, compression and redaction behave the same inside the container. Each cloud session starts with an empty state directory, so the dashboard and audit history there cover that session only.

<details>
<summary><b>Other platforms and install methods</b></summary>

**Codex:**
```bash
codex plugin marketplace add alexgreensh/token-optimizer
```
Then in the Codex TUI: `/plugins` and install Token Optimizer. See [`docs/codex.md`](docs/codex.md).

**OpenCode:** add `token-optimizer-opencode` to the `plugin` array in your `opencode.json`:
```jsonc
{ "$schema": "https://opencode.ai/config.json", "plugin": ["token-optimizer-opencode"] }
```
See [`opencode/README.md`](opencode/README.md).

**OpenClaw:**
```bash
openclaw plugins install github:alexgreensh/token-optimizer
```
See [`openclaw/README.md`](openclaw/README.md).

**Hermes:**
```bash
git clone https://github.com/alexgreensh/token-optimizer.git
token-optimizer/install.sh --hermes
```
See [`hermes/README.md`](hermes/README.md).

**GitHub Copilot:**
```bash
git clone --depth 1 https://github.com/alexgreensh/token-optimizer.git
cd token-optimizer
bash install.sh --copilot
```
See [`docs/copilot.md`](docs/copilot.md).

**Cursor:**
```bash
git clone --depth 1 https://github.com/alexgreensh/token-optimizer.git
cd token-optimizer
bash install.sh --cursor
```
See [`docs/cursor.md`](docs/cursor.md).

**Google Antigravity:**
```bash
git clone --depth 1 https://github.com/alexgreensh/token-optimizer.git
cd token-optimizer
bash install.sh --antigravity
```
See [`docs/antigravity.md`](docs/antigravity.md).

**Grok Build (beta, contract-only):**
```bash
git clone --depth 1 https://github.com/alexgreensh/token-optimizer.git
cd token-optimizer
bash install.sh --grok
```
See [`docs/grok.md`](docs/grok.md).

**macOS/Linux script install (alternative to plugin):**
```bash
tmp="$(mktemp -d)"
release_json="$(curl -fsSL https://api.github.com/repos/alexgreensh/token-optimizer/releases/latest)"
tag="$(python3 -c 'import json,sys; print(json.load(sys.stdin)["tag_name"])' <<<"$release_json")"
git clone --branch "$tag" --depth 1 https://github.com/alexgreensh/token-optimizer.git ~/.claude/token-optimizer
bash ~/.claude/token-optimizer/install.sh
rm -rf "$tmp"
```

**Windows users:** Use the plugin install only. Do not run `install.sh` on Windows. If you hit `EBUSY` errors, close all Claude Code and Git Bash windows, kill lingering `git.exe` processes, delete `C:\Users\<you>\.claude\token-optimizer` and `C:\Users\<you>\.claude\plugins\marketplaces\alexgreensh-token-optimizer`, then retry.

**If `install.sh` fails with `$'\r': command not fou

## tools

[filters.exclude]
commands = ["git status", "ls -la"]
```

Safety is immutable: the loader rejects `add` entries that name a shell
interpreter (`bash`, `python`, `node`, ...), a privilege-escalation wrapper
(`sudo`, `su`, `doas`), a destructive write subcommand (`rm`, `chmod`, `dd`,
...), or any command containing shell metacharacters (`;`, `|`, `$`, ...).
Categorical exclusions (dangerous chars, git write subcommands, interpreters)
are enforced in the hook and dispatch code and cannot be overridden by user
config. Built-in detection always runs first, so a user `add` only extends
the set, never replaces a built-in handler for the same command.

### Search Result Compression

When the AI runs grep, rg, or web searches that return long result lists, the output is condensed to the top hits plus a count. A 500-line grep result becomes 20 lines plus a summary.

Disable: `TOKEN_OPTIMIZER_BASH_COMPRESS=0` (search compression is part of bash compression; it has no separate switch)

### Lean-Output Nudges

When context fills past 25%, a short nudge tells the model to reason deeply but keep visible output lean. Fill is the only condition — quality no longer gates it, so an ordinary healthy session gets the nudge too, not just a long degraded one. The saving is **estimated at 10-15%, not measured**: the counterfactual (what the model would have written without the nudge) cannot be observed, so Token Optimizer reports this in the estimated tier and never folds it into metered savings. Cache-safe: injected as `additionalContext`, never modifies the existing prefix.

No on/off switch today (not a `v5` feature). Tune the trigger point with `TOKEN_OPTIMIZER_VERBOSITY_MIN_FILL` (default `25`).

### Quality Nudges

Watches context quality in real time. When the score drops more than 15 points or crosses below 60, an inline note enters the context. Claude sees it on the next turn and surfaces the warning or adjusts behavior. Cooldown of 5 minutes, max 3 per session.

Disable: `TOKEN_OPTIMIZER_QUALITY_NUDGES=0`

### Loop Detection

Catches the AI getting stuck on a retry loop. Compares the last 4 user messages and last 5 tool results for similarity. Fires at confidence ≥0.7, session cap of 2 notes. Savings measured from actual loop turn content.

Also catches the edit-compile-fail cycle: when the same command fails 3 times in a row with different output, a nudge suggests changing approach instead of re-running. Tunable with `TOKEN_OPTIMIZER_FAIL_STREAK_THRESHOLD` (default `3`).

Also catches inline-script repeats: when a command with a heredoc body >= 300 chars has been run 8 times in a session, a nudge suggests saving the script to a file and running that instead, so the body is not re-sent as input tokens every turn. Tunable with `TOKEN_OPTIMIZER_INLINE_SCRIPT_THRESHOLD` (default `8`).

Disable: `TOKEN_OPTIMIZER_LOOP_DETECTION=0`

### UserPromptSubmit Hook

Every prompt fires the `UserPromptSubmit` hook, which runs the per-turn work: prompt-continuity hint, verbosity steer, quality-cache warn tick, and (in harness/container/Cowork contexts) the once-per-session ensure-health, forced cache warm, and compact-restore pointer. These six subcommands share one `measure.py` import inside a single dispatcher (`hooks/userpromptsubmit_runner.py`), so one prompt spawns three processes, not eighteen. The dispatcher uses one shared deadline (18s, 2s margin under the 20s hooks.json timeout) with fair-share budgeting across subcommands, and buffers all stdout through a single emitter for controlled, host-consumable output.

Disable the entire `UserPromptSubmit` path: `TOKEN_OPTIMIZER_HOOKS_USERPROMPTSUBMIT=0`. Checked before `measure.py` is imported, so the opt-out costs zero per prompt. The other hook events (PreToolUse, PostToolUse, SessionStart, Stop, etc.) are unaffected.

### Activity Mode Detection

Classifies your session into one of five modes (code, debug, review, infra, general) using the last 10 tool calls. The mode feeds into compaction guidance 
