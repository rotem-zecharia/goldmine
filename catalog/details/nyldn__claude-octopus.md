# nyldn/claude-octopus

Run multiple AI models against the same research, design, or coding task. Surface disagreements before you ship.

## configuration

Model configuration rejects unsafe names while preserving supported Antigravity
display labels. Concurrent provider-history updates retain entries even when a
directory utility reports success to multiple writers. Optional history recording
requires Python 3 and skips the write if it cannot acquire the lock.

The MCP SDK is updated to 1.31.0, including an upstream OAuth client security fix.
See [the changelog](CHANGELOG.md) for details.

### Parallel work, reliable reviews and Codex startup

Parallel work packages now use separate branches. Completed commits remain
available after cleanup, and worktrees with uncommitted edits are kept for
recovery. Failed packages record their completion status so the wave can finish.

Reviews and research retain provider stdout longer than the configured threshold,
even when it contains a context-limit rejection phrase. Short stdout-only
rejections and stderr rejection signatures still fail the affected seat. The new
`OCTO_PROVIDER_REJECTION_MAX_OUTPUT_BYTES` setting adjusts the output-size
threshold, with a default of 4096 bytes. See [provider rejection handling](docs/PROVIDERS.md#provider-rejection-handling).

Codex can create its thread-coordination and plugin-sync locks inside the Linux
Tangle execution boundary. The locks use private temporary storage, while
configuration and extension inputs remain read-only. See [bounded Codex runs](docs/PROVIDERS.md#codex-in-bounded-tangle-runs)
for host requirements and temporary-directory configuration.

### Engineering methods

Octopus includes eight engineering methods adapted from
[Matt Pocock's skills](THIRD_PARTY_NOTICES.md). Routine architecture, TDD, and
debugging use your current host. Ask for an independent opinion when a reviewer
would help. Plans capture domain terms and blocking decisions, compare interface
designs, and can propose a time-limited prototype.

Setup can resume an interrupted configuration and rechecks readiness before
reporting success. See [workflow methods](docs/WORKFLOW-METHODS.md)
for usage and [the changelog](CHANGELOG.md) for release details.

Premium `/octo:auto` routes also run one bounded cross-provider peer check after
an eligible single-owner result, without requiring a second command or flag.
Budget and Standard routes do not add the check, and existing multi-model
workflows are not double-reviewed. Set `OCTOPUS_PREMIUM_PEER_CHECK=off` to
disable it.

<!-- BEGIN CURRENT RELEASE -->
> 🆕 **v11.13.1 — Safer model configuration, reliable provider history and an MCP dependency security update.**
>
> **Default roster:** Claude Opus 5.5 leads architecture, planning, security reasoning, and final judgment; GPT-5.6 Sol is the independent implementation/review peer; Claude Sonnet 5.5 is the standard Claude seat; Fable 5.1 remains an opt-in judgment escalation. Existing model pins and provider configuration still win. See [the routing strategy](docs/MODEL-ROUTING-STRATEGY.md).
<!-- END CURRENT RELEASE -->
>
> ```bash
> /octo:model-config                         # inspect or override the frontier roster
> OCTOPUS_OPUS5_AUTO_XHIGH=1                 # opt in to automatic xhigh Opus 5 phases
> OCTOPUS_OPUS_MODEL=claude-fable-5-1        # explicitly opt in to Fable 5.1
> OCTOPUS_CODEX_MODEL=gpt-6-astra            # explicitly opt in to Astra
> /octo:model-config tier premium claude claude-fable-5-1  # one bounded Fable judgment seat
> /octo:model-config tier premium codex gpt-6-astra        # one bounded Astra judgment seat
> ```

> 🆕 **v9.41 — Multi-LLM Council.** `/octo:council` runs a structured 3/5/7-persona deliberation across Claude, Codex, Antigravity, and OpenCode with goal modes (`advice`, `decision`, `plan`, `implement`, `review`), styles (`balanced`, `adversarial`, `red-team`, `executive`, `implementation`), benchmark-aware role routing, quorum + critical-veto gates, budget caps, and gated worktree handoff for approved plans. Use it when one model's opinion isn't enough.
>
> ```bash
> /octo:council --goal decision -

## installation

```bash
# Terminal (not inside a Claude Code session):
claude plugin marketplace add https://github.com/nyldn/plugins.git
claude plugin install octo@nyldn-plugins

# Then inside Claude Code:
/octo:setup
```

That's it. Setup detects installed providers, shows what's missing, and walks you through configuration. You need **zero** external providers to start — Claude is built in.

**Supported platforms:** Linux and macOS run natively. For Windows, use the
[Claude Code CLI inside WSL or a desktop SSH session](#using-claude-code-from-windows).
Native Git Bash, MSYS2, and Cygwin are unsupported. Octopus hooks exit immediately
on those hosts in Claude Code and Codex, without writing install or session state.

### Dormant by default

Installing Octopus does not route ordinary prompts, launch provider workflows,
or delegate to Octopus agents. Every shipped command and skill uses Claude
Code's native manual-invocation gate. Start it with `/octo:*`.

> **Seeing `cannot be used with Skill tool due to disable-model-invocation`?**
> That is the gate working as intended — the model tried to auto-invoke an
> Octopus skill. Invoke it explicitly instead: type `/octo:skill-doctor` (the
> manually invokable skill), not a model call to the `skill-doctor` skill. Slash skills are
> user-invoked, so they bypass this invocation gate; the model will not call
> Octopus skills on its own unless you opt into the router below. Rule of thumb:
> **invoke Octopus with
> `/octo:…`, don't expect Claude to reach for it for you.**

Optional automation remains available, but it is explicit opt-in:

```bash
export OCTOPUS_AUTO_ROUTER_MODE=suggest  # suggest a route for plain prompts
# or: OCTOPUS_AUTO_ROUTER_MODE=invoke    # load the matched command route
export OCTO_DONE_CRITERIA=on             # compound-task completion coaching
export OCTOPUS_COMPRESS_ENABLED=true     # PostToolUse output compression
export OCTO_STRATEGY_ROTATION=on         # failure strategy rotation
export OCTOPUS_CONTEXT_AWARENESS=on      # statusline-to-context reinforcement
export OCTOPUS_SESSION_MEMORY=on         # SessionStart preference restoration
```

This legacy opt-in examines ordinary prompts. `invoke` can start paid
external-provider workflows and share the routed prompt context with configured
providers; prefer `suggest` unless that behavior is intentional. Provider-side
retention follows each provider account's policy. Unset the variable (or set it
to `off`) to opt out without disabling direct `/octo:*` commands.

Safety guards that prevent invalid direct Codex, Qwen, or retired Gemini CLI
dispatch remain available, but host-side command filters keep them out of
unrelated tool calls.

### Installation health

Not sure which command to use? Run `/octo:guide` or `/octo:auto help` to browse
the commands in your installed version. Neither starts a provider workflow.

Octopus records non-secret install metadata for each host. Claude Code and
Codex keep separate entries, so switching hosts or updating one cache does not
make the other look current. SessionStart refreshes the active host entry when
the loaded root, version, scope, or profile changes.

```bash
octopus capabilities --json    # provider readiness and supported interfaces
octopus doctor installation    # loaded root, stable root, and saved metadata
octopus cache-check --json     # active, newest, stale, and stable plugin roots
octopus repair --dry-run       # explain a broken or stale stable link
octopus repair --apply         # repair that link and refresh install metadata
octopus security-audit --json  # offline checks of the installed plugin files
octopus handoff export --json  # redacted checkpoint for another supported host
```

`repair --apply` changes only the Octopus-owned stable plugin root and install
metadata. On platforms without symlink support, the stable root contains
generated wrappers for Octopus script entry points. Repair does not delete host
caches. The security audit checks the plugin itself; use `/oct

## tools

~/.claude-octopus/plugin/scripts/orchestrate.sh update-plugin
