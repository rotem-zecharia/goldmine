# Gitlawb/openclaude

runs anywhere. uses anything

## features

- One CLI across cloud APIs and local model backends — no per-provider tooling
- Guided provider setup and saved profiles with `/provider`
- Coding-agent workflows in one place: bash, file tools, grep, glob, agents, tasks, MCP, and web tools
- A bundled VS Code extension for launch integration and theme support
- A pixel-art hero companion who fires an arrow every time you press Enter (really — see [Meet your buddy](#meet-your-buddy))

## installation

### Install

OpenClaude requires Node.js `>=22.0.0` for npm installs and runtime. Bun is
only needed for source builds and local development.

```bash
npm install -g @gitlawb/openclaude@latest
```

If you're on Arch Linux, you can install OpenClaude from the community-maintained [AUR package](https://aur.archlinux.org/packages/openclaude):
```bash
paru -S openclaude
```

If the install later reports `ripgrep not found`, install ripgrep system-wide and confirm `rg --version` works in the same terminal before starting OpenClaude.

**Verify / troubleshoot installed version:**

```bash
openclaude --version
npm view @gitlawb/openclaude dist-tags
npm install -g @gitlawb/openclaude@latest
```

### Start

```bash
openclaude
```

Inside OpenClaude:

- run `/provider` for guided provider setup and saved profiles
- run `/onboard-github` for GitHub Models onboarding

> **Note:** OpenClaude does not automatically load project `.env` files. We recommend using the `/provider` command for setup, which saves provider profiles and credentials in `.openclaude-profile.json`. If you prefer environment variables, export them explicitly or run `openclaude --provider-env-file .env` for provider/setup variables. Export runtime/debug knobs from your shell or launcher.

### Resume or fork a conversation

Resume an existing conversation by session ID, or continue the most recent
conversation in the current directory:

```bash
openclaude --resume <session-id>
openclaude --continue
```

Add `--fork-session` to branch the conversation history into a new session ID
instead of reusing the original transcript:

```bash
openclaude --resume <session-id> --fork-session
openclaude --continue --fork-session
```

Forking is conversation branching only. It does not create filesystem isolation,
copy your working tree, or create a git worktree branch.

### Background sessions

Run long non-interactive prompts detached from the current terminal:

```bash
openclaude --bg "fix failing tests"
openclaude --bg --name auth-refactor "refactor auth middleware"
openclaude ps
openclaude logs auth-refactor
openclaude logs auth-refactor -f
openclaude kill auth-refactor
```

Background sessions are local child processes. OpenClaude does not start a daemon
or network service, and permission/provider/model/settings flags are passed to
the child process the same way they are for a foreground `--print` run. Session
metadata and logs are stored under the resolved OpenClaude config directory,
usually `~/.openclaude/bg-sessions/`; `OPENCLAUDE_CONFIG_DIR` can point
OpenClaude somewhere else. `CLAUDE_CONFIG_DIR` is ignored for OpenClaude
background-session storage. Session names can be reused after older sessions
reach a terminal state; use the session ID to inspect older logs with the same
name. A naturally finished session is recorded as `exited` when its process
returns zero and `failed` when it returns nonzero or handles a termination
signal. `stale` remains the conservative result when the process disappears
without an observed outcome; an explicit successful `openclaude kill` is
recorded as `killed`, and `killed` takes precedence over a natural `exited` or
`failed` outcome for the same process. Terminal outcomes are stored separately
under `bg-sessions/terminal/`; deleting that directory makes finished sessions
fall back to liveness-derived status. OpenClaude does not infer POSIX signal
names on Windows.
Unobservable force termination, host crashes, and power loss remain `stale` on
every platform.

`openclaude attach <id-or-name>` currently reports the matching session and
points to `openclaude logs <id> -f`; full terminal reattach is not implemented
for local background sessions yet.

## configuration

OpenClaude stores its own config under `~/.openclaude` and `~/.openclaude.json`
by default. It does not read `~/.claude`, project `.claude/` directories, or
`CLAUDE_CONFIG_DIR`; new users can start with an empty OpenClaude config and do
not need Claude Code installed.

If you previously used OpenClaude with `.claude` paths, migrate intentionally:
copy only the settings, commands, agents, skills, scheduled tasks, or other files
you personally created for OpenClaude into the matching `.openclaude` location.
Do not blanket-copy `.claude`, and do not copy Claude Code credentials or auth
files. For provider authentication, prefer running OpenClaude's provider setup
again or exporting provider-specific environment variables.
