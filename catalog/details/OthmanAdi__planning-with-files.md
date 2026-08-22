# OthmanAdi/planning-with-files

Persistent file-based planning for AI coding agents and long-running tasks. Crash-proof markdown plans, session recovery after /clear and compaction, per-turn re-injection against context rot, determi

## features

On December 29, 2025, [Meta acquired Manus for $2 billion](https://techcrunch.com/2025/12/29/meta-just-bought-manus-an-ai-startup-everyone-has-been-talking-about/). In just 8 months, Manus went from launch to $100M+ revenue. Their secret? **Context engineering.**

> "Markdown is my 'working memory' on disk. Since I process information iteratively and my active context has limits, Markdown files serve as scratch pads for notes, checkpoints for progress, building blocks for final deliverables."
> — Manus AI

This skill packages that exact pattern for your coding agent.

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
