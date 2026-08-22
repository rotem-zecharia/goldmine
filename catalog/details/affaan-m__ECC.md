# affaan-m/ECC

The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.

## installation

Run these commands inside Claude Code:

```text
/plugin marketplace add https://github.com/affaan-m/ECC
/plugin install ecc@ecc
```

That installs ECC's skills, agents, commands, and plugin-managed hooks. If you choose this path, stop there. Do not also run a full manual install into Claude Code.

> Guided package setup is coming in `ecc-universal` 2.2.0. Use the native
> Claude plugin commands above while npm remains on 2.1.0.

<div align="center">

<table aria-label="ECC primary links">
<tr>
<td width="33%" align="center">
  <a href="https://ecc.tools/pricing">
    <img src="assets/images/community/ecc-tools-mark.svg" height="42" alt="ECC Tools" /><br />
    <strong>ECC Pro + GitHub App</strong>
  </a><br />
  <sub><a href="https://github.com/apps/ecc-tools">Install free</a> · <a href="https://ecc.tools/pricing">Private repos from $19/seat/mo</a></sub>
</td>
<td width="33%" align="center">
  <a href="https://github.com/sponsors/affaan-m">
    <img src="assets/images/community/heart.svg" height="42" alt="" /><br />
    <strong>Sponsor ECC</strong>
  </a><br />
  <sub>Fund the open-source project</sub>
</td>
<td width="33%" align="center">
  <a href="https://discord.gg/36yGMHGFbR">
    <img src="assets/images/community/discord.svg" height="42" alt="Discord" /><br />
    <strong>Community</strong>
  </a><br />
  <sub>Discord · Q&amp;A · Show and Tell</sub>
</td>
</tr>
</table>

</div>

<sub>**OSS stays free.** This repo is MIT-licensed forever. ECC Pro is the hosted GitHub App for private repos. <a href="https://github.com/sponsors/affaan-m">Sponsors</a> and <a href="https://ecc.tools/pricing">Pro subscribers</a> fund the work. That's why a single maintainer ships weekly across 7 harnesses.</sub>

<div align="center">

<sub><strong>Partners &amp; sponsors</strong></sub>

<p align="center" aria-label="Partners and sponsors">
  <a href="https://www.coderabbit.ai" title="CodeRabbit"><img src="assets/images/sponsors/coderabbit.png" height="54" alt="CodeRabbit" /></a>&nbsp;&nbsp;&nbsp;
  <a href="https://www.greptile.com/go/ecc" title="Greptile"><img src="assets/images/sponsors/greptile.png" height="54" alt="Greptile" /></a>&nbsp;&nbsp;&nbsp;
  <a href="https://www.atlascloud.ai/?utm_source=github&amp;utm_medium=link&amp;utm_campaign=ECC" title="Atlas Cloud"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/images/sponsors/atlascloud-dark.svg" /><img src="assets/images/sponsors/atlascloud.svg" width="154" alt="Atlas Cloud" /></picture></a>&nbsp;&nbsp;&nbsp;
  <a href="https://www.moonshot.ai" title="Moonshot AI - Kimi"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/images/sponsors/moonshot-dark.png" /><img src="assets/images/sponsors/moonshot.png" width="132" alt="Moonshot AI - Kimi" /></picture></a>&nbsp;&nbsp;&nbsp;
  <a href="https://compute.itomarkets.com" title="Itô Markets"><picture><source media="(prefers-color-scheme: light)" srcset="assets/images/sponsors/ito-transparent-light.png" /><img src="assets/images/sponsors/ito-transparent.png" width="96" alt="Itô Markets" /></picture></a>
</p>

<sub><strong>Community sponsors:</strong> <a href="https://github.com/mikejmorgan-ai">Mike Morgan</a> · <a href="https://github.com/jasonwu513">@jasonwu513</a> · <a href="https://github.com/1anter">@1anter</a> · <a href="https://github.com/massimotodaro">@massimotodaro</a> · <a href="https://github.com/meadmccabe">@meadmccabe</a></sub>

<sub><a href="https://github.com/sponsors/affaan-m"><strong>Become a Sponsor</strong></a> · <a href="SPONSORS.md">Sponsor Tiers</a> · <a href="SPONSORING.md">Sponsorship Program</a></sub>

</div>

<p align="center"><a href="#install-ecc">Jump to install ↓</a></p>

# ECC

Your agent can write code, but ECC gives it a coordinated engineering system and toolbox: it plans before it builds, verifies changes with tests, reviews its own work from a fresh context, remembers what matters, and turns repeated wins into reusable skills and workflows.

```text
plan -> test -> impl

## tools

- **Python/Django support**: Django patterns, security, TDD, and verification skills
- **Java Spring Boot skills**: Patterns, security, TDD, and verification for Spring Boot
- **Session management**: `/sessions` command for session history
- **Continuous learning v2**: Instinct-based learning with confidence scoring, import/export, evolution

See the full changelog in [Releases](https://github.com/affaan-m/ECC/releases).
</details>

## features

| Without a system                                        | With ECC                                                              |
| ------------------------------------------------------- | --------------------------------------------------------------------- |
| Plans disappear into chat history                       | Plans become editable artifacts before implementation starts          |
| "Please use TDD" is an instruction the model may forget | TDD becomes a gated RED -> GREEN -> REFACTOR workflow with evidence   |
| The same context writes and reviews the code            | A fresh-context reviewer looks for regressions and blind spots        |
| Memory means saving an enormous transcript              | Sessions are distilled into summaries, instincts, and reusable skills |
| Quality checks depend on reminders                      | Hooks can enforce deterministic checks outside the prompt             |
| Agent configuration is trusted by default               | AgentShield scans the harness itself as an attack surface             |

### TDD: Test-Driven Development

```text
/ecc:plan "Add usage-based billing alerts"
  -> confirm or edit the plan
  -> activate tdd-workflow
  -> capture RED evidence before implementation
  -> implement until GREEN
  -> review from fresh context
  -> fix findings with regression tests
  -> verify build, lint, types, and tests
```

A result is not just code. It's a trail of evidence: the plan, the failing test, the passing test, the review findings, and the final verification.

### Skills keep the context focused

Rules, skills, agents, and hooks solve different problems. Keeping those jobs separate is how ECC adds capability without dumping the entire repository into every session.

| Concept | What it does | Context behavior |
|---|---|---|
| Skills | Reusable workflows such as TDD, security review, or deep research | Loaded when the task needs them |
| Agents | Scoped workers with their own context and tool permissions | Isolate planning, implementation, and review |
| Rules | Durable project or language standards | Always loaded, so install them selectively |
| Hooks | Scripts triggered by harness events | Run outside the model context |
| Instincts | Patterns learned from real sessions with confidence scores | Recalled when relevant |

### Share context between harnesses

ECC's Memory Vault gives Claude, Codex, Hermes, OpenClaw, Kimi, and other harnesses one local, inspectable Markdown format for durable context and handoffs. Project and team memories live under `.ecc/memory/`; user memories live under `~/.ecc/memory/`.

```bash
npm install -g ecc-universal
ecc memory init --scope project
ecc memory search "authentication migration" --target-harness codex
ecc memory doctor
```

Memory is unreviewed context, not executable policy. Verify important claims against authoritative sources and promote accepted knowledge into governed project documentation. The optional `ecc-memory-mcp` server exposes the same bounded save, search, read, and doctor surface without enabling itself by default.

[Open the Unified Memory workflow →](skills/unified-memory/SKILL.md)

<details>
<summary><strong>Memory Vault in depth: scopes, handoffs, and trust boundaries</strong></summary>

The Memory Vault stores portable `ecc.memory.v1` Markdown documents instead of copying vendor transcripts or emailing context between agents. Project memories are protected by a fail-closed `.gitignore`; use the team scope only for human-inspected, version-controlled sharing. Team memories remain unreviewed context even after they are committed.

Skill-only, minimal, manual, and Claude plugin installs do not put the Memory Vault runtime on `PATH`. Install the npm runtime separately before using the CLI or optional MCP server:

```bash
npm install -g ecc-universal
ecc memory --help
command -v ecc-memory-mcp
```

```bash
# Initialize the project vault.
ecc memory init --scope project

# Write a handoff body to a regular file, then

## configuration

npx ecc-agentshield init
```

**What it scans:** CLAUDE.md, settings.json, MCP configs, hooks, agent definitions, and skills across 5 categories: secrets detection (14 patterns), permission auditing, hook injection analysis, MCP server risk profiling, and agent config review.

**The `--opus` flag** runs three Claude Opus 4.6 agents in a red-team/blue-team/auditor pipeline. The attacker finds exploit chains, the defender evaluates protections, and the auditor synthesizes both into a prioritized risk assessment. Adversarial reasoning, not just pattern matching.

**Output formats:** Terminal (color-graded A-F), JSON (CI pipelines), Markdown, HTML. Exit code 2 on critical findings for build gates.

Use `/security-scan` in Claude Code to run it, or add to CI with the [GitHub Action](https://github.com/affaan-m/agentshield).

[GitHub](https://github.com/affaan-m/agentshield) | [npm](https://www.npmjs.com/package/ecc-agentshield)
</details>

<details>
<summary><strong>Continuous Learning v2: instincts</strong></summary>

The instinct-based learning system automatically learns your patterns:

```bash
/instinct-status        # Show learned instincts with confidence
/instinct-import <file> # Import instincts from others
/instinct-export        # Export your instincts for sharing
/evolve                 # Cluster related instincts into skills
```

See `skills/continuous-learning-v2/` for full documentation. Keep `continuous-learning/` only when you explicitly want the legacy v1 Stop-hook learned-skill flow.
</details>

## Key Concepts

<details>
<summary><strong>Agents, skills, hooks, and rules explained</strong></summary>

### Agents

Subagents handle delegated tasks with limited scope. Example:

```markdown
---
name: code-reviewer
description: Reviews code for quality, security, and maintainability
tools: Read, Grep, Glob, Bash
model: opus
---

You are a senior code reviewer...
```

### Skills

Skills are the primary workflow surface. They can be invoked directly, suggested automatically, and reused by agents. ECC still ships maintained `commands/` during migration, while retired short-name shims live under `legacy-command-shims/` for explicit opt-in only. New workflow development should land in `skills/` first.

```markdown
# TDD Workflow

1. Define interfaces first
2. Write failing tests (RED)
3. Implement minimal code (GREEN)
4. Refactor (IMPROVE)
5. Verify 80%+ coverage
```

### Hooks

Hooks fire on tool events. Example: warn about console.log:

```json
{
  "matcher": "tool == \"Edit\" && tool_input.file_path matches \"\\\\.(ts|tsx|js|jsx)$\"",
  "hooks": [{
    "type": "command",
    "command": "#!/bin/bash\ngrep -n 'console\\.log' \"$file_path\" && echo '[Hook] Remove console.log' >&2"
  }]
}
```

### Rules

Rules are always-follow guidelines, organized into `common/` (language-agnostic) + language-specific directories:

```
rules/
  common/          # Universal principles (always install)
  typescript/      # TS/JS specific patterns and tools
  python/          # Python specific patterns and tools
  golang/          # Go specific patterns and tools
  swift/           # Swift specific patterns and tools
  php/             # PHP specific patterns and tools
  arkts/           # HarmonyOS / ArkTS patterns and constraints
```

See [`rules/README.md`](rules/README.md) for installation and structure details.
</details>

## Cross-Platform Support

ECC's core Node.js CLI and managed installers run on **Windows, macOS, and Linux**, but optional capabilities are not at full parity. Some continuous-learning, GAN, and orchestration paths still require Bash or Python; harnesses also expose different hook, agent, and skill APIs.

| Platform | Status | Current limitation |
|---|---|---|
| Linux | Supported core | Optional features may require Bash, Python, or provider-specific tools. |
| macOS | Supported core | The standalone GAN shell path is not compatible with the system Bash 3.2 and currently has a score-parsing defect ([#2674](https://git

## requirements

<details>
<summary><strong>Claude Code CLI version + hooks auto-loading behavior</strong></summary>

### Claude Code CLI version

**Minimum version: v2.1.0 or later.** The plugin requires Claude Code CLI v2.1.0+ due to changes in how the plugin system handles hooks.

Check your version:
```bash
claude --version
```

### Important: hooks auto-loading behavior

> WARNING: **For Contributors:** Do NOT add a `"hooks"` field to `.claude-plugin/plugin.json`. This is enforced by a regression test.

Claude Code v2.1+ **automatically loads** `hooks/hooks.json` from any installed plugin by convention. Explicitly declaring it in `plugin.json` causes a duplicate detection error:

```
Duplicate hooks file detected: ./hooks/hooks.json resolves to already-loaded file
```

**History:** This has caused repeated fix/revert cycles in this repo ([#29](https://github.com/affaan-m/ECC/issues/29), [#52](https://github.com/affaan-m/ECC/issues/52), [#103](https://github.com/affaan-m/ECC/issues/103)). The behavior changed between Claude Code versions, leading to confusion. There is now a regression test to prevent this from being reintroduced.
</details>

## Security

Install ECC only from official sources:

- GitHub repository: <https://github.com/affaan-m/ECC>
- Claude Code plugin: `ecc@ecc`
- npm packages: [`ecc-universal`](https://www.npmjs.com/package/ecc-universal) and [`ecc-agentshield`](https://www.npmjs.com/package/ecc-agentshield)
- GitHub App: <https://github.com/apps/ecc-tools>
- Website: <https://ecc.tools>

Scan a project with AgentShield:

```bash
npx -y ecc-agentshield scan --path .
```

- **Report a vulnerability.** Use the private process in [SECURITY.md](SECURITY.md) (GitHub private vulnerability reporting). Please do not open public issues for security reports.
- **Built-in guardrails.** GateGuard gates destructive shell commands (including `rm`, force/path `git checkout`, and destructive `find -exec`) before they run; the supply-chain IOC scanner runs in CI; and AgentShield audits your own agent, hook, MCP, permission, and secret surfaces (`/security-scan`).

<details>
<summary><strong>Hooks, MCP servers, and context controls</strong></summary>

Hooks can run shell commands, MCP servers can hold credentials, and project instructions can enter an agent's context. Treat all three as executable configuration.

Do not copy raw `hooks/hooks.json` into `~/.claude/settings.json` after a plugin install. Modern Claude Code versions load plugin hooks automatically, and a second copy can make them fire twice.

Use `/mcp` for Claude Code runtime disables; Claude Code persists those choices in `~/.claude.json`.

`ECC_DISABLED_MCPS` is an ECC install/sync filter, not a live Claude Code toggle.

If context is getting heavy, run `/context-budget`, remove rules you do not need, and disable unused MCP servers. See the [token optimization guide](docs/token-optimization.md).
</details>

Security references:

- [Security policy](SECURITY.md)
- [Security guide](./the-security-guide.md)
- [MCP connector policy](docs/MCP-CONNECTOR-POLICY.md)
- [Supply-chain incident response](docs/security/supply-chain-incident-response.md)

## Troubleshooting

<details>
<summary><strong>ECC appears twice or hooks fire twice</strong></summary>

The usual cause is installing the Claude plugin and then running `./install.sh --profile full` on top of it.

1. Remove the Claude Code plugin install.
2. Run `node scripts/ecc.js uninstall --dry-run` from the ECC checkout.
3. Remove extra rule folders you manually copied and no longer want.
4. Reinstall once, using one path.

For hook-specific checks, see the [hooks README](hooks/README.md).
</details>

<details>
<summary><strong>My hooks aren't working / "Duplicate hooks file" errors</strong></summary>

**Do NOT add a `"hooks"` field to `.claude-plugin/plugin.json`.** Claude Code v2.1+ automatically loads `hooks/hooks.json` from installed plugins. Explicitly declaring it causes duplicate detection errors. See [#29](https://github
