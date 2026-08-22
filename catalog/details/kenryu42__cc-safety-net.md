# kenryu42/cc-safety-net

An AI coding agent guardrail — a CLI hook that blocks destructive git and filesystem commands and secret file access before they execute. Supports Amp Code, Antigravity CLI, Claude Code, Codex, Copilo

## features

We built CC Safety Net after an agent [wiped hours of work](https://www.reddit.com/r/ClaudeAI/comments/1pgxckk/claude_cli_deleted_my_entire_home_directory_wiped/) with one `rm -rf ~/` or `git checkout --`. Instructions did not stop it. Rules in `CLAUDE.md` or `AGENTS.md` can guide an agent, but they cannot enforce a technical limit. CC Safety Net watches relevant tool calls and blocks destructive commands and secret access before they reach the shell. See [What is CC Safety Net](https://ccsafetynet.com/docs/introduction) for the full background.

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

## tools

npx cc-safety-net logs

## limitations

CC Safety Net denies a tool call before it runs. It does not enforce filesystem permissions, inspect network egress, or contain a process. Two v2 limits matter. First, the policy and sensitive-path command extractors remain mainly POSIX-oriented. Native PowerShell path expressions such as `Get-Content $HOME\.ssh\id_rsa` can evade static path extraction. Second, policy-file protection is a best-effort exact-path guard. It does not emulate commands. Use operating-system permissions, a sandbox, or equivalent runtime controls when you need complete protection.

Codex has one integration-specific limit. Its unified exec path is the default on macOS and Linux. It sends a hook payload when a command starts a session, but it sends none for `write_stdin`. CC Safety Net can inspect and audit the command that opens the session. It cannot inspect or audit text that the model types into the running session. Codex emits no event for that call, so an adapter change cannot close this gap.

[SECURITY.md](SECURITY.md) contains the full residual-risk registry. [Known Limitations](https://ccsafetynet.com/docs/guides/known-limitations) explains what those risks mean in practice.
