# OthmanAdi/planning-with-files

Persistent file-based planning for AI coding agents and long-running tasks. Crash-proof markdown plans, session recovery after /clear and compaction, per-turn re-injection against context rot, determi

## features

On December 29, 2025, [Meta acquired Manus for $2 billion](https://techcrunch.com/2025/12/29/meta-just-bought-manus-an-ai-startup-everyone-has-been-talking-about/). In just 8 months, Manus went from launch to $100M+ revenue. Their secret? **Context engineering.**

> "Markdown is my 'working memory' on disk. Since I process information iteratively and my active context has limits, Markdown files serve as scratch pads for notes, checkpoints for progress, building blocks for final deliverables."
> — Manus AI

This skill packages that exact pattern for your coding agent.

### The Manus Principles

| Principle | Implementation |
|-----------|----------------|
| Filesystem as memory | Store in files, not context |
| Attention manipulation | Re-read plan before decisions (hooks) |
| Error persistence | Log failures in plan file |
| Goal tracking | Checkboxes show progress |
| Completion verification | Stop hook checks all phases |

## Benchmark Results

> **Methodology note:** the 96.7% figure comes from the v2.21.0 evaluation run on `claude-sonnet-4-6` (2026-03-06). It measures file-pattern fidelity (does the agent create and maintain the 3-file structure), not goal-drift over long autonomous runs. Newer models and the autonomous-mode work are not yet covered by this number. Full methodology, dataset, and assertion list: [docs/evals.md](docs/evals.md).

Evaluated with Anthropic's [skill-creator](https://github.com/anthropics/skills/tree/main/skills/skill-creator) framework: skill v2.21.0, model `claude-sonnet-4-6`, 2026-03-06. 10 parallel subagents, 5 task types, 30 objectively verifiable assertions, 3 blind A/B comparisons.

<p align="center">
  <img src="media/benchmark-skill-vs-baseline.svg" width="860" alt="Eval results, with skill vs without: assertions passed 29 of 30 vs 2 of 30, 3-file pattern followed 5 of 5 vs 0 of 5, blind A/B wins 3 of 3 vs 0 of 3, average rubric score 10.0 vs 6.8">
</p>

| Test | with_skill | without_skill |
|------|-----------|---------------|
| Pass rate (30 assertions) | **96.7%** (29/30) | 6.7% (2/30) |
| 3-file pattern followed | 5/5 evals | 0/5 evals |
| Blind A/B wins | **3/3 (100%)** | 0/3 |
| Avg rubric score | **10.0/10** | 6.8/10 |

### Recovery after a context wipe

> **Internal benchmark, v1 (2026-07-06).** Author-run against v3.4.0, harness-authored tasks, deterministic grading, no LLM grades anything. Treat it as the project's own measurement, not an independent comparison. Full method, arms, disclosed limits, and grader validation: [docs/evals.md](docs/evals.md#test-5-competitive-benchmark-v1-seven-planning-methods-head-to-head-2026-07-06-internal).

Protocol: the session is hard-stopped at roughly half done, and a fresh session is told only "Continue the work in this directory." Every graded run across every arm ended pytest-green (77/77), so the difference is re-orientation cost, not correctness.

<p align="center">
  <img src="media/recovery-turns.svg" width="860" alt="Turns to resume after a context wipe, internal benchmark v1: 5.0 with planning-with-files, 13.3 for a raw agent with no planning method">
</p>

**With the planning files on disk, a resume took 5.0 turns on average; a raw agent took 13.3.** Session catchup plus hook injection put phase state in front of the model before its first tool call, and the same run found no correctness penalty anywhere. An animated summary lives at [docs/benchmark/index.html](docs/benchmark/index.html) ([rendered view](https://htmlpreview.github.io/?https://github.com/OthmanAdi/planning-with-files/blob/master/docs/benchmark/index.html)).

[Full methodology and results](docs/evals.md) · [Technical write-up](docs/article.md)

## installation

**Claude Code, plugin route** (ships everything: skill, hooks, slash commands):

```
/plugin marketplace add OthmanAdi/planning-with-files
/plugin install planning-with-files@planning-with-files
```

**Every other agent**, one line, 60+ agents via the [Agent Skills](https://agentskills.io) standard:

```bash
npx skills add OthmanAdi/planning-with-files --skill planning-with-files -g
```

**npm**, to pin an exact version into a project or vendor it:

```bash
npm install planning-with-files
```

The package carries `SKILL.md`, `scripts/` and `templates/`, so this is the route for locking a version into a repo's dependencies or copying the skill in yourself. It does not register hooks on its own.

**Pi Coding Agent**, same npm package, wired up for you (skill, extension, status bar):

```bash
pi install npm:planning-with-files
```

Under a minute. Safe to re-run. Trigger it by typing `/plan` (plugin) or asking the agent to "plan this task"; the skill also self-triggers on multi-step tasks.

What each route actually ships:

| Route | Skill + scripts + templates | Slash commands | Hooks |
|---|---|---|---|
| Claude Code plugin | yes | **yes** | **yes** |
| `npx skills add` | yes | no | frontmatter hooks, see note |
| `npm install` | yes, under `node_modules/` | no | no, copy the skill in yourself |
| `pi install npm:` | yes | **yes**, Pi commands | **yes**, via the Pi extension |
| ClawHub / manual copy | yes | no | frontmatter hooks, see note |

Skill-route installs can end up silently hook-less (project trust not accepted, or frontmatter hooks not registering on project-level installs). The hooks are the differentiating mechanism, so if they matter to you, use the plugin route, then verify with `/plan-doctor`. Full matrix and the two silent killers: [docs/installation.md](docs/installation.md#what-each-install-route-actually-ships).

Install acting up? Open your agent and say: *"Read docs/installation.md and docs/troubleshooting.md from OthmanAdi/planning-with-files and fix my install."* Then run `/plan-doctor`.

<details>
<summary><strong>🌐 Available in 5 other languages</strong></summary>

**🇸🇦 العربية / Arabic**
```bash
npx skills add OthmanAdi/planning-with-files --skill planning-with-files-ar -g
```

**🇩🇪 Deutsch / German**
```bash
npx skills add OthmanAdi/planning-with-files --skill planning-with-files-de -g
```

**🇪🇸 Español / Spanish**
```bash
npx skills add OthmanAdi/planning-with-files --skill planning-with-files-es -g
```

**🇨🇳 中文版 / Chinese (Simplified)**
```bash
npx skills add OthmanAdi/planning-with-files --skill planning-with-files-zh -g
```

**🇹🇼 正體中文版 / Chinese (Traditional)**
```bash
npx skills add OthmanAdi/planning-with-files --skill planning-with-files-zht -g
```

These are real translations, not an English body with a translated description: the SKILL.md prose, the templates, and the user-facing output of `check-complete`, `init-session` and `session-catchup` are all localized. The status tokens stay literal English (`**Status:** complete`) on purpose, because `check-complete.sh` matches them with `grep -F`, so translating them would disable the completion gate.

Since v3.10.0 the variants also ship the full script surface: attestation, the Stop gate, the ledger, phase status and plan-doctor used to be canonical-only, which quietly made every non-English install a subset install. Full details, including what changed on the plugin route in v3.11.0, are in [docs/languages.md](docs/languages.md).

They live under `skills/i18n/`, one directory deeper than the canonical skill. The install commands above are unchanged, because `npx skills add` resolves `--skill` by skill name across the whole repository. The Claude Code plugin scan reads `skills/*/SKILL.md` without recursing, so the plugin route registers the canonical skill alone and no longer carries five extra descriptions in every session's system prompt. On that route the `/plan-ar`, `/plan-de`, `/plan-es`, `/plan-zh` and `/plan-zht` commands read the transla

## tools

Slash commands ship with the Claude Code plugin route (see the install matrix above).

| Command | Autocomplete | What you get |
|---------|--------------|--------------|
| `/planning-with-files:plan` | type `/plan` | Creates the three planning files and starts the session (v2.11.0+) |
| `/planning-with-files:pwf` | type `/pwf` | Short alias for `/plan`; `--autonomous` / `--gated` init (v3.0.0+) |
| `/planning-with-files:status` | type `/status` | One-glance report: current phase and phase totals (v2.15.0+) |
| `/planning-with-files:plan-doctor` | type `/plan-doctor` | Self-check for the failure modes that are silent by design: one PASS/WARN/FAIL line each for resolution, injection, attestation, install surfaces, and per-fire latency (v3.6.0+) |
| `/planning-with-files:plan-attest` | type `/plan-attest` | Locks `task_plan.md` with a SHA-256; hooks refuse a tampered plan body; `--show` / `--clear` (v2.37.0+) |
| `/planning-with-files:plan-goal` | type `/plan-goal` | Runs until the plan reports complete, composing with Claude Code `/goal` (v2.38.0+) |
| `/planning-with-files:plan-loop` | type `/plan-loop` | Planning-aware cadence on `/loop`, default 10 minute tick (v2.38.0+) |
| `/planning-with-files:plan-de` | type `/plan-de` | Start planning in German; also `-ar`, `-es`, `-zh`, `-zht` (v2.33.0+) |
| `/planning-with-files:start` | type `/planning` | Original start command |

Typing `/plan` prefix-matches every `plan*` command in autocomplete; `/planning-with-files:status` autocompletes as `/status` (the older `/plan:status` label predates the rename).

### Pi extension commands

Install the Pi extension with `pi install npm:planning-with-files`; it registers these commands, typed with no `/planning-with-files:` prefix.

| Command | What it does | Version |
|---------|--------------|---------|
| `/plan-execute` | Pi only. Approve the active plan to ACTIVATE all Pi hooks; hooks stay passive until you run this; `reset` returns to passive review | v3.3.0+ |
| `/plan-status` | Active plan path, scope, and phase totals | v2.39.0+ |
| `/plan-goal <text\|default\|clear>` | Set or clear the goal string appended to auto-continue prompts | v2.39.0+ |
| `/plan-loop [interval] [prompt\|stop]` | Start or stop a planning tick (default 10m) that re-reads the plan and nudges progress | v2.39.0+ |
| `/plan-attest [--show\|--clear]` | Run the attest-plan helper; shares the `.attestation` file with Claude Code | v2.39.0+ |

On Pi there is no `/plan` command to create the files; the skill creates them, then `/plan-execute` approves and activates the hooks. Pi `plan-goal`/`plan-loop` run their own logic, while the Claude Code commands of the same name forward to native `/goal` and `/loop`. The doctor ships as a script in every mirror since v3.7.0: run `sh scripts/plan-doctor.sh` directly on platforms without the command.

### Command names vs skill names

| Platform | You type | Examples |
|----------|----------|----------|
| Claude Code | `/planning-with-files:<verb>`, autocompletes from the short form | `/plan`, `/pwf`, `/plan-attest`, `/plan-de` |
| Pi | bare form, no prefix | `/plan-status`, `/plan-execute`, `/plan-goal` |
| Continue.dev | `/planning-with-files` | |

On the plugin route the model-invocable SKILL is `planning-with-files:planning-with-files`; the doubled form is the skill id, not a command you type. The five language variants live under `skills/i18n/`, which the plugin scan does not reach, so there is no `planning-with-files:planning-with-files-de` to invoke by name — reach a translation through its `/plan-ar`, `/plan-de`, `/plan-es`, `/plan-zh` or `/plan-zht` command, or install it as its own skill with `npx skills add OthmanAdi/planning-with-files --skill planning-with-files-de -g`, which registers it under its own name. There is no `/pwf-de` and no `/planning-with-files:planning-with-files-goal`; `/pwf` is just a short alias for `/plan`.

## Works across 18+ platforms

One skill, three integration tiers. Know what your agent ge

## configuration

| Variable | Since | What it does |
|---|---|---|
| `PLANNING_DISABLED=1` | v3.4.0 | Skips all plan reading for this invocation. For one-shot or CI sessions that share a cwd with a plan they never opted into. |
| `PLAN_ID=<slug>` | v2.36.0 | Pins the terminal to one plan under `$(pwd)/.planning`. Slug only, resolved against the current directory. |
| `PWF_PLAN_ROOT=<abs path>` | v3.9.0 | Pins the thread to a project root by absolute path, which `PLAN_ID` cannot express. Use it when the agent's cwd is a shared parent such as `/workspace` while the work lives in `/workspace/project`. A pin that does not resolve stops injection instead of falling back. |
| `PWF_SESSION_ID=<id>` | v2.36.0 | Identifies the session for plan attachment. Only consulted when `.planning/sessions/` exists, in which case a session sees plan context only if `.planning/sessions/<id>.attached` exists. Delete that directory to turn session isolation off. |
| `PWF_INJECT=smart` | v3.8.0 | Replaces the fixed `head -50` injection window with the goal, next step, current phase, the full in-progress phase, and the last three decisions. |
| `PWF_PLAN_GUARD=0` | v3.10.0 | Turns off the parallel-write guard, which is on by default. The guard compares checked items and completed phases against the previous hook fire and prints one advisory line when they go DOWN, meaning a second session overwrote work. A `plan-guard-off` token in `.mode` does the same. |
| `PWF_MODE` | v2.39.0 | Pi extension runtime mode: `auto`, `parity`, `cache-safe`, `notify`. Also settable in `.pi/settings.json` under `planningWithFiles.mode`. |
| `PWF_GATE_CAP` | v3.0.0 | Maximum consecutive Stop-gate blocks in gated mode. Default 20. |

### Hooks and modes reference

| Platform | Lifecycle hooks | Where registered |
|----------|-----------------|------------------|
| Claude Code | 5: UserPromptSubmit, PreToolUse, PostToolUse, Stop, PreCompact | The skill's `SKILL.md` frontmatter (not `plugin.json`), so they ship with the bundled skill |
| Codex CLI | 7: SessionStart, UserPromptSubmit, PreToolUse, PermissionRequest, PostToolUse, PreCompact, Stop | `.codex/hooks.json`, with event-aware adapters on every platform and `commandWindows` on Windows |
| Pi | 8 lifecycle handlers in the bundled extension | The injection and recitation handlers stay passive until `/plan-execute` |

Pi runtime modes:

| Pi mode | Behavior |
|---------|----------|
| `auto` | Detects the model and picks `parity` or `cache-safe` |
| `parity` | Full plan injection, mirrors the Claude Code skill |
| `cache-safe` | A stable reminder instead of full injection, for KV-cache-sensitive models like DeepSeek |
| `notify` | Status-line only, no model injection |

## Key Rules

1. **Create Plan First** — Never start without `task_plan.md`
2. **The 2-Action Rule** — Save findings after every 2 view/browser operations
3. **Log ALL Errors** — They help avoid repetition
4. **Never Repeat Failures** — Track attempts, mutate approach

## When to Use

**Use this pattern for:**
- Multi-step tasks (3+ steps)
- Research tasks
- Building/creating projects
- Tasks spanning many tool calls
- Long-running agent sessions that must survive `/clear` and compaction

## File Structure

What the skill writes into your project is three markdown files (see [the 3-file pattern](#the-solution-3-file-pattern)). What the repository ships:

<details>
<summary><strong>Repository layout</strong></summary>

```
planning-with-files/
├── skills/planning-with-files/   # canonical skill: SKILL.md, scripts/, templates/, reference.md, examples.md
├── skills/i18n/                  # 5 translated variants: -ar / -de / -es / -zh / -zht
├── .agents/skills/planning-with-files/   # Agent Skills standard path, full surface (v3.7.0+)
├── commands/                     # 13 slash commands (plugin route only)
├── scripts/ · templates/        # root-level copies for CLAUDE_PLUGIN_ROOT
├── .claude-plugin/               # plugin + marketplace manifests
├── .codex/ .cursor/ .github/ .g
