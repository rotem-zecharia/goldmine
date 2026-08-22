# kenryu42/cc-safety-net

An AI coding agent guardrail — a CLI hook that blocks destructive git and filesystem commands and secret file access before they execute. Supports Amp Code, Antigravity CLI, Claude Code, Codex, Copilo

## features

We built CC Safety Net after an agent [wiped hours of work](https://www.reddit.com/r/ClaudeAI/comments/1pgxckk/claude_cli_deleted_my_entire_home_directory_wiped/) with one `rm -rf ~/` or `git checkout --`. Instructions did not stop it. Rules in `CLAUDE.md` or `AGENTS.md` can guide an agent, but they cannot enforce a technical limit. CC Safety Net watches relevant tool calls and blocks destructive commands and secret access before they reach the shell. See [What is CC Safety Net](https://ccsafetynet.com/docs/introduction) for the full background.

## What's new in v2.0.0

> [!TIP]
> **Already running v1?** Run `npx -y cc-safety-net@latest update` to upgrade every installed integration to v2. If you defined custom rules under v1, also read [Upgrading from an older version](#upgrading-from-an-older-version).

- **Evaluation engine.** A canonical command IR, policy snapshots that remain immutable at every nested level, and an ordered guard pipeline now support decision tracing through `explain`.
- **Secret protection.** Built-in rules block content access to SSH keys, `.env` files, cloud credentials, and coding-CLI credential stores through shell commands and file tools.
- **Always-on protections.** Every mode blocks recursive deletion of root or home, Git metadata changes to the `.git` control plane, hooks, worktrees, or submodules, and changes to the user policy file. Overrides do not disable these rules.
- **Safety presets.** The `standard`, `strict`, and `paranoid` levels support per-rule overrides and trusted delete allow-paths. Safety-level and capability environment variables can only raise protection. `CC_SAFETY_NET_WORKTREE` is the one exception. It allows local Git discards in linked worktrees.
- **Policy GUI.** `cc-safety-net gui` runs a local, token-authenticated editor with a live preset preview.
- **Universal installer.** Interactive `install` and `uninstall` commands support all twelve coding CLIs. The `update` command updates installed integrations.
- **Command-decision audit trail.** CC Safety Net records allowed and blocked decisions in local per-project JSONL. It redacts secrets, keeps records for 30 days by default, and shows them through `cc-safety-net logs`.
- **Threat model.** [SECURITY.md](SECURITY.md) defines the mode contract and resource limits. Its residual-risk registry records decisions for bypass families.

## installation

You need Node.js 18 or higher.

Run the interactive selector to install CC Safety Net into one or more installed coding CLIs:

```bash
npx -y cc-safety-net@latest install
```

To update every installed integration:

```bash
npx -y cc-safety-net@latest update
```

Keep the `@latest` qualifier. A bare `cc-safety-net` spec can run an older cached
copy from the npx cache instead of the current release.

To remove integrations interactively:

```bash
npx -y cc-safety-net uninstall
```

If you use the CLI often, install it globally to get `ccsn`, a shorter alias for the same commands:

```bash
npm install -g cc-safety-net
ccsn doctor
```

## Supported coding CLIs

CC Safety Net supports the coding agent CLIs below on Windows, macOS, and Linux. Automated tests cover the analyzer and some Windows integrations. Other hosts have best-effort Windows support that has not been tested. Amp documents macOS, Linux, and WSL, but not native Windows.

<table align="center">
  <tr>
    <td align="center"><a href="https://ccsafetynet.com/docs/installation#amp-code-installation"><picture><source media="(prefers-color-scheme: dark)" srcset="./.github/assets/amp-dark.svg"><img alt="Amp Code" src="./.github/assets/amp-light.svg" height="32"></picture><br>Amp Code</a></td>
    <td align="center"><a href="https://ccsafetynet.com/docs/installation#antigravity-cli-installation"><img alt="Antigravity CLI" src="./.github/assets/antigravity-cli.png" height="32"><br>Antigravity CLI</a></td>
    <td align="center"><a href="https://ccsafetynet.com/docs/installation#claude-code-installation"><img alt="Claude Code" src="./.github/assets/claude-code.svg" height="32"><br>Claude Code</a></td>
    <td align="center"><a href="https://ccsafetynet.com/docs/installation#codex-installation"><img alt="Codex" src="./.github/assets/codex.svg" height="32"><br>Codex</a></td>
  </tr>
  <tr>
    <td align="center"><a href="https://ccsafetynet.com/docs/installation#cursor-installation"><picture><source media="(prefers-color-scheme: dark)" srcset="./.github/assets/cursor-dark.svg"><img alt="Cursor" src="./.github/assets/cursor-light.svg" height="32"></picture><br>Cursor</a></td>
    <td align="center"><a href="https://ccsafetynet.com/docs/installation#gemini-cli-installation"><img alt="Gemini CLI" src="./.github/assets/gemini-cli.svg" height="32"><br>Gemini CLI</a></td>
    <td align="center"><a href="https://ccsafetynet.com/docs/installation#github-copilot-cli-installation"><picture><source media="(prefers-color-scheme: dark)" srcset="./.github/assets/copilot-cli-dark.svg"><img alt="GitHub Copilot CLI" src="./.github/assets/copilot-cli-light.svg" height="32"></picture><br>GitHub Copilot CLI</a></td>
    <td align="center"><a href="https://ccsafetynet.com/docs/installation#hermes-agent-installation"><img alt="Hermes Agent" src="./.github/assets/hermes.png" height="32"><br>Hermes Agent</a></td>
  </tr>
  <tr>
    <td align="center"><a href="https://ccsafetynet.com/docs/installation#kimi-code-installation"><img alt="Kimi Code" src="./.github/assets/kimi-cli.png" height="32"><br>Kimi Code</a></td>
    <td align="center"><a href="https://ccsafetynet.com/docs/installation#openclaw-installation"><img alt="OpenClaw" src="./.github/assets/openclaw.png" height="32"><br>OpenClaw</a></td>
    <td align="center"><a href="https://ccsafetynet.com/docs/installation#opencode-installation"><picture><source media="(prefers-color-scheme: dark)" srcset="./.github/assets/opencode-dark.svg"><img alt="OpenCode" src="./.github/assets/opencode-light.svg" height="32"></picture><br>OpenCode</a></td>
    <td align="center"><a href="https://ccsafetynet.com/docs/installation#pi-installation"><picture><source media="(prefers-color-scheme: dark)" srcset="./.github/assets/pi-dark.svg"><img alt="Pi" src="./.github/assets/pi-light.svg" height="32"></picture><br>Pi</a></td>
  </tr>
</table>

## tools

npx cc-safety-net logs
# Review what was blocked and edit your policy in a local web GUI
npx cc-safety-net gui
```

`doctor`, `explain`, and `logs` support `--json` for machine-readable output. The audit trail stays on your machine. It records command decisions, but it does not record command output or prompts. Invalid configuration never blocks your agent. CC Safety Net drops unverifiable rule sources and reports each degraded state in the next block message, `doctor`, the status line, and the GUI banner.

Details: [CLI Commands](https://ccsafetynet.com/docs/reference/cli-commands) · [Explain Trace](https://ccsafetynet.com/docs/reference/explain-trace) · [Audit Log](https://ccsafetynet.com/docs/reference/audit-log) · [Dashboard](https://ccsafetynet.com/docs/guides/dashboard) · [Configuration Recovery](https://ccsafetynet.com/docs/configuration/recovery).

## limitations

CC Safety Net denies a tool call before it runs. It does not enforce filesystem permissions, inspect network egress, or contain a process. Two v2 limits matter. First, the policy and sensitive-path command extractors remain mainly POSIX-oriented. Native PowerShell path expressions such as `Get-Content $HOME\.ssh\id_rsa` can evade static path extraction. Second, policy-file protection is a best-effort exact-path guard. It does not emulate commands. Use operating-system permissions, a sandbox, or equivalent runtime controls when you need complete protection.

Codex has one integration-specific limit. Its unified exec path is the default on macOS and Linux. It sends a hook payload when a command starts a session, but it sends none for `write_stdin`. CC Safety Net can inspect and audit the command that opens the session. It cannot inspect or audit text that the model types into the running session. Codex emits no event for that call, so an adapter change cannot close this gap.

[SECURITY.md](SECURITY.md) contains the full residual-risk registry. [Known Limitations](https://ccsafetynet.com/docs/guides/known-limitations) explains what those risks mean in practice.

## Upgrading from an older version

Upgrade every installed integration to the current release with one command:

```bash
npx -y cc-safety-net@latest update
```

> [!WARNING]
> If you defined custom rules in a legacy inline config such as `.safety-net.json` or `~/.cc-safety-net/config.json`, CC Safety Net no longer loads those files at runtime. Their rules enforce nothing. Normal use does not show this failure because the commands now run. Run `npx -y cc-safety-net rule migrate` to convert the rules to the rulebook layout. Then run `npx -y cc-safety-net doctor` and confirm that the runtime is `ready`. See the [migration guide](https://ccsafetynet.com/docs/configuration/custom-rules#migrate-legacy-configuration).

## Full documentation

The **[ccsafetynet.com/docs](https://ccsafetynet.com/docs)** site contains the full documentation:

| Area | Pages |
|---|---|
| Get started | [Introduction](https://ccsafetynet.com/docs/introduction) · [Installation](https://ccsafetynet.com/docs/installation) · [Quickstart](https://ccsafetynet.com/docs/quickstart) · [How It Works](https://ccsafetynet.com/docs/guides/how-it-works) · [Dashboard](https://ccsafetynet.com/docs/guides/dashboard) |
| Configuration | [Modes](https://ccsafetynet.com/docs/configuration/modes) · [Policy](https://ccsafetynet.com/docs/configuration/policy) · [Environment](https://ccsafetynet.com/docs/configuration/environment) · [Custom Rules](https://ccsafetynet.com/docs/configuration/custom-rules) · [Status Line](https://ccsafetynet.com/docs/configuration/status-line) · [Configuration Recovery](https://ccsafetynet.com/docs/configuration/recovery) |
| Reference | [Blocked Commands](https://ccsafetynet.com/docs/reference/blocked-commands) · [Allowed Commands](https://ccsafetynet.com/docs/reference/allowed-commands) · [Secret Protection](https://ccsafetynet.com/docs/reference/secret-protection) · [Audit Log](https://ccsafetynet.com/docs/reference/audit-log) · [CLI Commands](https://ccsafetynet.com/docs/reference/cli-commands) · [Explain Trace](https://ccsafetynet.com/docs/reference/explain-trace) · [Glossary](https://ccsafetynet.com/docs/reference/glossary) |
| Guides | [Architecture](https://ccsafetynet.com/docs/guides/architecture) · [Analysis Engine](https://ccsafetynet.com/docs/guides/analysis-engine) · [Design Principles](https://ccsafetynet.com/docs/guides/design-principles) · [Security Model](https://ccsafetynet.com/docs/guides/security-model) · [vs Sandboxing](https://ccsafetynet.com/docs/guides/vs-sandboxing) · [Integration Architecture](https://ccsafetynet.com/docs/guides/integration-architecture) · [Known Limitations](https://ccsafetynet.com/docs/guides/known-limitations) · [Troubleshooting](https://ccsafetynet.com/docs/guides/troubleshooting) |
| Project | [Contributing](https://ccsafetynet.com/docs/contribu
