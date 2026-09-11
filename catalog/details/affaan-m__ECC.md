# affaan-m/ECC

The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.

## installation

Use the [guided setup](#install-ecc) or [native plugin commands](#claude-code-details). Both install the same `ecc@ecc` plugin. Choose one and do not stack a full manual Claude install on top.

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
  <a href="https://platform.kimi.ai?aff=ecc" title="Moonshot AI - Kimi"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/images/sponsors/moonshot-dark.png" /><img src="assets/images/sponsors/moonshot.png" width="132" alt="Moonshot AI - Kimi" /></picture></a>&nbsp;&nbsp;&nbsp;
  <a href="https://compute.itomarkets.com" title="Itô Markets"><picture><source media="(prefers-color-scheme: light)" srcset="assets/images/sponsors/ito-transparent-light.png" /><img src="assets/images/sponsors/ito-transparent.png" width="96" alt="Itô Markets" /></picture></a>
</p>

<sub><strong>Community sponsors:</strong> <a href="https://github.com/mikejmorgan-ai">Mike Morgan</a> · <a href="https://github.com/jasonwu513">@jasonwu513</a> · <a href="https://github.com/1anter">@1anter</a> · <a href="https://github.com/massimotodaro">@massimotodaro</a> · <a href="https://github.com/meadmccabe">@meadmccabe</a></sub>

<sub><a href="https://github.com/sponsors/affaan-m"><strong>Become a Sponsor</strong></a> · <a href="SPONSORS.md">Sponsor Tiers</a> · <a href="SPONSORING.md">Sponsorship Program</a></sub>

</div>

<p align="center"><a href="#install-ecc">Jump to install ↓</a></p>

# ECC

Your agent can write code, but ECC gives it a coordinated engineering system and toolbox: it plans before it builds, verifies changes with tests, reviews its own work from a fresh context, remembers what matters, and turns repeated wins into reusable skills and workflows.

```text
plan -> test -> implement -> review -> verify -> remember -> improve
```

Instead of rebuilding that process in every prompt, you install it once and make it part of how your agent works.

> Optimize the context window. Persist everything else.

ECC 

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

Skill-only, minimal, manual, and Claude plugin installs do not put the Memory Vault runtime on `PATH`. Install the npm runtime separately before using the CLI or optional MCP server:

```bash
npm install -g ecc-universal@2.2.1
ecc memory init --scope project
ecc memory search "authentication migration" --target-harness codex
ecc memory doctor
```

Memory is unreviewed context, not executable policy. Verify important claims against authoritative sources and promote accepted knowledge into governed project documentation. The optional `ecc-memory-mcp` server exposes the same bounded save, search, read, and doctor surface without enabling itself by default.

[Open the Unified Memory workflow →](skills/unified-memory/SKILL.md)

<details>
<summary><strong>Memory Vault in depth: scopes, handoffs, and trust boundaries</strong></summary>

The Memory Vault stores portable `ecc.memory.v1` Markdown documents instead of copying vendor transcripts or emailing context between agents. Project memories are protected by a fail-closed `.gitignore`; use the team scope only for human-inspected, version-controlled sharing. Team memories remain unreviewed context even after they are committed.

After installing the runtime above, check that the CLI and optional MCP entry point are available:

```bash
ecc memory --help
command -v ecc-memory-mcp
```

```bash
# Initialize the project vault.
ec

## configuration

export CLAUDE_PACKAGE_MANAGER=pnpm

# Via global config
node scripts/setup-package-manager.js --global pnpm

# Via project config
node scripts/setup-package-manager.js --project bun

# Detect current setting
node scripts/setup-package-manager.js --detect
```

Or use the `/setup-pm` command.
</details>

<details>
<summary><strong>Hook runtime controls (env vars)</strong></summary>

Use runtime flags to tune strictness or disable specific hooks temporarily:

```bash
# Hook strictness profile (default: standard)
export ECC_HOOK_PROFILE=standard

# Comma-separated hook IDs to disable
export ECC_DISABLED_HOOKS="pre:bash:tmux-reminder,post:edit:typecheck"

# Cap SessionStart additional context (default: 8000 chars)
export ECC_SESSION_START_MAX_CHARS=4000

## tools

export ECC_CONTEXT_MONITOR_COST_WARNINGS=off
```

Windows PowerShell:

```powershell
[Environment]::SetEnvironmentVariable('ECC_CONTEXT_MONITOR_COST_WARNINGS', 'off', 'User')
[Environment]::SetEnvironmentVariable('ECC_SESSION_RETENTION_DAYS', '14', 'User')
```
</details>

<details>
<summary><strong>Agent data home (multi-harness isolation)</strong></summary>

Memory persistence hooks (session summaries, learned skills, session aliases, metrics) store data under a single agent data root. By default that root is `~/.claude`. When you use ECC in both Claude Code and Cursor on the same machine, set a separate root for Cursor so the two environments do not overwrite each other's session files:

```bash
# Cursor-only boundary (Claude Code keeps the default ~/.claude)
export ECC_AGENT_DATA_HOME="$HOME/.cursor/ecc"
```

Paths resolved under that root include:

- `$ECC_AGENT_DATA_HOME/session-data/`: session summaries
- `$ECC_AGENT_DATA_HOME/skills/learned/`: learned skills from evaluate-session
- `$ECC_AGENT_DATA_HOME/session-aliases.json`: session aliases
- `$ECC_AGENT_DATA_HOME/metrics/`: cost and activity metrics

See [affaan-m/ECC#2065](https://github.com/affaan-m/ECC/issues/2065).
</details>

<details>
<summary><strong>Cross-tool capability map and per-harness notes</strong></summary>

### Cross-tool capability map

| Capability | Claude Code | Codex | Cursor | OpenCode | GitHub Copilot |
|---|---|---|---|---|---|
| Instructions | Native | Native `AGENTS.md` | Project rules | Plugin instructions | Native instruction file |
| Skills | Native installed set | Native plugin set | Build-dependent/project set | Built subset | Prompt/instruction references only |
| Agents/delegation | Native agents | Codex multi-agent roles; Claude agent files are not installed as roles | Build-dependent project agents | Plugin agents | Not supported |
| ECC hooks | Native plugin hooks | Native reviewed subset with explicit trust | Cursor hook adapter; install-path differences remain | Plugin events | Not supported |
| MCP configuration | Available, explicit activation | Native plugin manifest; legacy sync can merge TOML | Explicit project/user config | Provider/plugin config | Not supplied by ECC |
| Parity with Claude Code | Primary reference | Partial | Partial | Partial | Not a parity target |

**Key architectural decisions:**
- **AGENTS.md** at root is the universal cross-tool file (read by Claude Code, Cursor, Codex, and OpenCode; GitHub Copilot uses `.github/copilot-instructions.md` instead)
- **DRY adapter pattern** lets Cursor reuse Claude Code's hook scripts without duplication
- **Skills format** (SKILL.md with YAML frontmatter) works across Claude Code, Codex, and OpenCode
- Codex's narrower native hook set is supplemented by `AGENTS.md`, optional `model_instructions_file` overrides, and sandbox permissions

<details>
<summary><strong>Cursor IDE support in depth</strong></summary>

ECC provides Cursor IDE support with hooks, rules, agents, skills, commands, and MCP configs adapted for Cursor's project layout.

```bash
# macOS/Linux
./install.sh --target cursor typescript
./install.sh --target cursor python golang swift php
```

```powershell
# Windows PowerShell
.\install.ps1 --target cursor typescript
.\install.ps1 --target cursor python golang swift php
```

#### What's included for Cursor

| Component | Count | Details |
|-----------|-------|---------|
| Hook Events | 15 | sessionStart, beforeShellExecution, afterFileEdit, beforeMCPExecution, beforeSubmitPrompt, and 10 more |
| Hook Scripts | 16 | Thin Node.js scripts delegating to `scripts/hooks/` via shared adapter |
| Rules | 34 | 9 common (alwaysApply) + 25 language-specific (TypeScript, Python, Go, Swift, PHP) |
| Agents | 48 | `.cursor/agents/ecc-*.md` when installed; prefixed to avoid collisions with user or marketplace agents |
| Skills | Shared + Bundled | `.cursor/skills/` for translated additions |
| Commands | Shared | `.cursor/commands/` if installed |
| MCP Config | Shared |

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

Scan a project with an already installed, reviewed AgentShield binary (see [runner provenance](#agentshield-runner-provenance)):

```bash
agentshield scan --path .
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
