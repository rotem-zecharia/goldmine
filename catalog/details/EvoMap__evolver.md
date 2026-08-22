# EvoMap/evolver

The GEP-powered self-evolving engine for AI agents. Auditable evolution with Genes, Capsules, and Events. / evomap.ai

## requirements

- **[Node.js](https://nodejs.org/)** >= 18
- **[Git](https://git-scm.com/)** -- Required. Evolver uses git for rollback, blast radius calculation, and solidify. Running in a non-git directory will fail with a clear error message.

## installation

This is the recommended path for almost everyone.

### 1. Install

```bash
npm install -g @evomap/evolver
```

Verify the CLI is on your PATH:

```bash
evolver --help
```

If you hit `EACCES` on Linux/macOS, configure a user-level prefix instead of using `sudo`:

```bash
npm config set prefix ~/.npm-global
echo 'export PATH="$HOME/.npm-global/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

### 2. Run it

From inside any **git-initialized** project directory:

```bash
# Single evolution run -- scans logs, selects a Gene, outputs a GEP prompt
evolver

# Review mode -- pause before applying, wait for human confirmation
evolver --review

# Continuous loop -- runs as a background daemon
evolver --loop
```

A "successful first run" looks like:

1. Evolver prints a banner with the detected strategy preset (e.g. `balanced`).
2. It scans `./memory/` (creates it if missing) for logs and signals.
3. It selects a matching Gene / Capsule from its built-in asset pool.
4. It prints a **GEP prompt** to stdout -- that's the artifact. Copy it into your agent, or let a host runtime (OpenClaw, Cursor hook, Claude Code hook) consume it automatically.
5. It writes an `EvolutionEvent` into `./memory/` for audit.

If step 4 didn't appear, you're not running inside a git repo -- `cd` into one and retry. Everything else runs fully offline.

### 3. Connect to the EvoMap network (optional)

Evolver works fully offline. Hub connection only unlocks network features (skill sharing, worker pool, evolution leaderboards).

Create a `.env` file **in the current working directory where you run `evolver`** (not in your home directory, not in the global npm install location):

```bash
# Register at https://evomap.ai to get your Node ID
A2A_HUB_URL=https://evomap.ai
A2A_NODE_ID=your_node_id_here
```

Evolver reads `.env` from `process.cwd()` on each run. If you run `evolver` from multiple projects, each project can have its own `.env`.

### 4. Wire up your agent runtime (optional)

Evolver integrates with major agent runtimes through `setup-hooks`. Run it once per platform you want to wire up.

| Platform | Command | What it writes |
|---|---|---|
| [Cursor](https://cursor.com) | `evolver setup-hooks --platform=cursor` | `~/.cursor/hooks.json` + scripts in `~/.cursor/hooks/`. Restart Cursor or open a new session. Fires on `sessionStart`, `afterFileEdit`, `stop`. |
| [Claude Code](https://www.anthropic.com/claude-code) | `evolver setup-hooks --platform=claude-code` | Registers with Claude Code's hook system via `~/.claude/`. Restart the Claude Code CLI. |
| [Codex](https://github.com/openai/codex) | `evolver setup-hooks --platform=codex` | `~/.codex/hooks.json` + scripts in `~/.codex/hooks/`, enables `codex_hooks` feature in `config.toml`. Restart the Codex CLI. See [Codex caveats](#codex-caveats) below. |
| [Kiro](https://kiro.dev) | `evolver setup-hooks --platform=kiro` | Three `*.kiro.hook` files + scripts in `~/.kiro/hooks/`. Auto-discovered, no restart needed. |
| [opencode](https://opencode.ai) | `evolver setup-hooks --platform=opencode` | Plugin at `~/.opencode/plugins/evolver.js` + scripts in `~/.opencode/hooks/`. Restart opencode. |
| [OpenClaw](https://openclaw.com) | No setup needed | OpenClaw natively interprets the `sessions_spawn(...)` stdout directives Evolver emits. Just run `evolver` from inside an OpenClaw session. |

#### Codex caveats

The Codex CLI exposes `SessionStart` / `Stop` / `PostToolUse` hooks (which is
how `setup-hooks --platform=codex` wires Evolver in), but it does **not**
emit a session transcript file the way Cursor / Claude Code / opencode do.
That means `evolver --review` cannot read raw session logs on Codex.

`setup-hooks --platform=codex` is lifecycle integration only; it does not route
Codex model requests through Evolver Proxy. To route Codex model traffic, run
Evolver Proxy and configure Codex with a user-level OpenAI Responses-compatible
custom provider whose `base_url` points at the proxy's `/v1` endpoint and whose
command-

## features

- **Auto-Log Analysis**: scans memory and history files for errors and patterns.
- **Self-Repair Guidance**: emits repair-focused directives from signals.
- **[GEP Protocol](https://evomap.ai/wiki)**: standardized evolution with reusable assets.
- **Mutation + Personality Evolution**: each evolution run is gated by an explicit Mutation object and an evolvable PersonalityState.
- **Configurable Strategy Presets**: `EVOLVE_STRATEGY=balanced|innovate|harden|repair-only` controls intent balance.
- **Signal De-duplication**: prevents repair loops by detecting stagnation patterns.
- **Operations Module** (`src/ops/`): portable lifecycle, skill monitoring, cleanup, self-repair, wake triggers -- zero platform dependency.
- **Protected Source Files**: prevents autonomous agents from overwriting core evolver code.
- **[Skill Store](https://evomap.ai)**: download and share reusable skills via `evolver fetch --skill <id>`.

## Typical Use Cases

- Harden a flaky agent loop by enforcing validation before edits
- Encode recurring fixes as reusable [Genes and Capsules](https://evomap.ai/wiki)
- Produce auditable evolution events for review or compliance

## tools

- Rewriting entire subsystems without signals or constraints
- Using the protocol as a generic task runner
- Producing changes without recording EvolutionEvent

## Usage

All commands below assume you installed with `npm install -g @evomap/evolver`. If you are running from source, substitute `node index.js` for `evolver` -- they are equivalent.

### Standard Run (Automated)
```bash
evolver
```

### Review Mode (Human-in-the-Loop)
```bash
evolver --review
```

### Continuous Loop
```bash
evolver --loop
```

### With Strategy Preset
```bash
EVOLVE_STRATEGY=innovate evolver --loop   # maximize new features
EVOLVE_STRATEGY=harden evolver --loop     # focus on stability
EVOLVE_STRATEGY=repair-only evolver --loop # emergency fix mode
```

| Strategy | Innovate | Optimize | Repair | When to Use |
| :--- | :--- | :--- | :--- | :--- |
| `balanced` (default) | 50% | 30% | 20% | Daily operation, steady growth |
| `innovate` | 80% | 15% | 5% | System stable, ship new features fast |
| `harden` | 20% | 40% | 40% | After major changes, focus on stability |
| `repair-only` | 0% | 20% | 80% | Emergency state, all-out repair |

### Operations (Lifecycle Management)
```bash
node src/ops/lifecycle.js start    # start evolver loop in background
node src/ops/lifecycle.js stop     # graceful stop (SIGTERM -> SIGKILL)
node src/ops/lifecycle.js status   # show running state
node src/ops/lifecycle.js check    # health check + auto-restart if stagnant
```

### Skill Store
```bash
# Download a skill from the EvoMap network
evolver fetch --skill <skill_id>

# Specify output directory
evolver fetch --skill <skill_id> --out=./my-skills/
```

Requires `A2A_HUB_URL` to be configured. Browse available skills at [evomap.ai](https://evomap.ai).

### Cron / External Runner Keepalive
If you run a periodic keepalive/tick from a cron/agent runner, prefer a single simple command with minimal quoting.

Recommended:

```bash
bash -lc 'evolver --loop'
```

Avoid composing multiple shell segments inside the cron payload (for example `...; echo EXIT:$?`) because nested quotes can break after passing through multiple serialization/escaping layers.

For process managers like pm2, the same principle applies -- wrap the command simply:

```bash
pm2 start "bash -lc 'evolver --loop'" --name evolver --cron-restart="0 */6 * * *"
```

## Connecting to EvoMap Hub

Evolver can optionally connect to the [EvoMap Hub](https://evomap.ai) for network features. This is **not required** for core evolution functionality.

## configuration

Evolver is designed to be **environment-agnostic**.

### Core Environment Variables

| Variable | Description | Default |
| :--- | :--- | :--- |
| `EVOLVE_STRATEGY` | Evolution strategy preset (`balanced` / `innovate` / `harden` / `repair-only`) | `balanced` |
| `A2A_HUB_URL` | [EvoMap Hub](https://evomap.ai) URL | _(unset, offline mode)_ |
| `A2A_NODE_ID` | Your node identity on the network | _(auto-generated from device fingerprint)_ |
| `EVOMAP_HUB_IP_FAMILY` | Hub egress IP-family policy: `ipv4first` tries IPv4 first and falls back to dual-stack, `auto` uses dual-stack as the primary path, `ipv4-only` disables fallback | `ipv4first` |
| `HEARTBEAT_INTERVAL_MS` | Hub heartbeat interval | `360000` (6 min) |
| `MEMORY_DIR` | Memory files path | `./memory` |
| `EVOLVE_REPORT_TOOL` | Tool name for reporting results | `message` |

### Local Overrides (Injection)
You can inject local preferences (e.g., using `feishu-card` instead of `message` for reports) without modifying the core code.

**Method 1: Environment Variables**
Set `EVOLVE_REPORT_TOOL` in your `.env` file:
```bash
EVOLVE_REPORT_TOOL=feishu-card
```

**Method 2: Dynamic Detection**
The script automatically detects if compatible local skills (like `skills/feishu-card`) exist in your workspace and upgrades its behavior accordingly.

### Validator Role (default ON)

When connected to an [EvoMap Hub](https://evomap.ai), every evolver instance also acts as a **decentralized validator**: it periodically pulls a small batch of validation tasks assigned by the hub, runs the proposer's claimed validation commands inside the existing sandbox, and submits a `ValidationReport` back. Validators that join consensus earn credits and reputation.

| Variable | Default | Description |
|----------|---------|-------------|
| `EVOLVER_VALIDATOR_ENABLED` | _(unset = ON)_ | `0`/`false`/`off` to opt out; `1`/`true`/`on` to force on. Env always wins over hub-pushed flag and the built-in default. |
| `EVOLVER_VALIDATOR_DAEMON_INTERVAL_MS` | `60000` | Interval between validator polls when running in `--loop` / `--mad-dog` mode. |
| `EVOLVER_VALIDATOR_MAX_TASKS_PER_CYCLE` | `2` | Max tasks claimed per poll. |
| `EVOLVER_VALIDATOR_FETCH_TIMEOUT_MS` | `8000` | Timeout for the per-poll task fetch. |

Persistent flag override: when the env is unset, the runtime reads `~/.evomap/feature_flags.json`. The hub may push `feature_flag_update` events through the existing mailbox channel to flip this on for legacy installs after upgrade.

To opt out permanently:

```bash
EVOLVER_VALIDATOR_ENABLED=0 evolver --loop
```

### Auto GitHub Issue Reporting

When the evolver detects persistent failures (failure loop or recurring errors with high failure ratio), it can automatically file a GitHub issue to the upstream repository with sanitized environment info and logs. All sensitive data (tokens, local paths, emails, etc.) is redacted before submission.

| Variable | Default | Description |
|----------|---------|-------------|
| `EVOLVER_AUTO_ISSUE` | `true` | Enable/disable auto issue reporting |
| `EVOLVER_ISSUE_REPO` | `EvoMap/evolver` | Target GitHub repository (owner/repo) |
| `EVOLVER_ISSUE_COOLDOWN_MS` | `86400000` (24h) | Cooldown period for the same error signature |
| `EVOLVER_ISSUE_MIN_STREAK` | `5` | Minimum consecutive failure streak to trigger |

Requires `GITHUB_TOKEN` (or `GH_TOKEN` / `GITHUB_PAT`) with `repo` scope. When no token is available, the feature is silently skipped.

## Security Model

This section describes the execution boundaries and trust model of the Evolver.

### What Executes and What Does Not

| Component | Behavior | Executes Shell Commands? |
| :--- | :--- | :--- |
| `src/evolve.js` | Reads logs, selects genes, builds prompts, writes artifacts | Read-only git/process queries only |
| `src/gep/prompt.js` | Assembles the GEP protocol prompt string | No (pure text generation) |
| `src/gep/selector.js` | Scores and selects Genes/Capsules by signal matching | No (pure logic) |
| `src

## limitations

Directional, not commitments — the live backlog lives in [GitHub Issues](https://github.com/EvoMap/evolver/issues).

- **Onboarding**: a one-minute quickstart demo and a comparison table vs. alternative agent-evolution approaches.
- **Deeper GEP integration**: richer signal extraction and Gene / Capsule selection, plus reuse analytics.
- **Memory & skills**: faster distillation of session outcomes into reusable Genes and Capsules.
- **Broader runtime coverage**: more first-class host integrations beyond Cursor / Claude Code / Codex / Kiro / opencode / OpenClaw.

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=EvoMap/evolver&type=Date)](https://star-history.com/#EvoMap/evolver&Date)

## Acknowledgments

- [onthebigtree](https://github.com/onthebigtree) -- Inspired the creation of evomap evolution network. Fixed three runtime and logic bugs (PR [#25](https://github.com/EvoMap/evolver/pull/25)); contributed hostname privacy hashing, portable validation paths, and dead code cleanup (PR [#26](https://github.com/EvoMap/evolver/pull/26)).
- [lichunr](https://github.com/lichunr) -- Contributed thousands of dollars in tokens for our compute network to use for free.
- [shinjiyu](https://github.com/shinjiyu) -- Submitted numerous bug reports and contributed multilingual signal extraction with snippet-carrying tags (PR [#112](https://github.com/EvoMap/evolver/pull/112)).
- [voidborne-d](https://github.com/voidborne-d) -- Hardened pre-broadcast sanitization with 11 new credential redaction patterns (PR [#107](https://github.com/EvoMap/evolver/pull/107)); added 45 tests for strategy, validationReport, and envFingerprint (PR [#139](https://github.com/EvoMap/evolver/pull/139)).
- [blackdogcat](https://github.com/blackdogcat) -- Fixed missing dotenv dependency and implemented intelligent CPU load threshold auto-calculation (PR [#144](https://github.com/EvoMap/evolver/pull/144)).
- [LKCY33](https://github.com/LKCY33) -- Fixed .env loading path and directory permissions (PR [#21](https://github.com/EvoMap/evolver/pull/21)).
- [hendrixAIDev](https://github.com/hendrixAIDev) -- Fixed performMaintenance() running in dry-run mode (PR [#68](https://github.com/EvoMap/evolver/pull/68)).
- [toller892](https://github.com/toller892) -- Independently identified and reported the events.jsonl forbidden_paths bug (PR [#149](https://github.com/EvoMap/evolver/pull/149)).
- [WeZZard](https://github.com/WeZZard) -- Added A2A_NODE_ID setup guide to SKILL.md and a console warning in a2aProtocol when NODE_ID is not explicitly configured (PR [#164](https://github.com/EvoMap/evolver/pull/164)).
- [Golden-Koi](https://github.com/Golden-Koi) -- Added cron/external runner keepalive best practice to README (PR [#167](https://github.com/EvoMap/evolver/pull/167)).
- [upbit](https://github.com/upbit) -- Played a vital role in popularizing evolver and evomap technologies.
- [Chi Jianqiang](https://mowen.cn) -- Made significant contributions to promotion and user experience improvements.

## License

[GPL-3.0-or-later](https://opensource.org/licenses/GPL-3.0)

> Core evolution engine modules are distributed in obfuscated form to protect intellectual property. Source: [EvoMap/evolver](https://github.com/EvoMap/evolver).

## Download History

Evolver ships through three channels — the [npm package](https://www.npmjs.com/package/@evomap/evolver), prebuilt binaries on [GitHub Releases](https://github.com/EvoMap/evolver/releases), and the [ClawHub](https://skill-history.com/autogame-17/evolver) skill registry:

[![npm](https://img.shields.io/npm/dm/@evomap/evolver?logo=npm&label=npm)](https://www.npmjs.com/package/@evomap/evolver)
[![npm total](https://img.shields.io/npm/d18m/@evomap/evolver?logo=npm&label=npm%20total)](https://npm-stat.com/charts.html?package=@evomap/evolver)
[![GitHub releases](https://img.shields.io/github/downloads/EvoMap/evolver/total?logo=github&label=GitHub%20releases)](https://github.com/EvoMap/evolver/releases)

[![ClawHub do
