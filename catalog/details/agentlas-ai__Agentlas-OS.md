# agentlas-ai/Agentlas-OS

Agent OS: keep specialist agents in a hub, spin up a temporary orchestrator per task. Local-first, works with any model.

## installation

Paste this into the LLM you are using now, such as Claude Code, Codex,
Gemini CLI, Antigravity, or Cursor. It is written so you (the LLM reading it)
can verify what you're running before you run it, rather than being asked to
trust it blindly:

```text
I want to install Agentlas OS / Hephaestus from this open-source GitHub repo:
https://github.com/agentlas-ai/Agentlas-OS

Before running anything, fetch and read the installer script so you know what
it does:
https://raw.githubusercontent.com/agentlas-ai/Agentlas-OS/main/scripts/install-all-runtimes.sh

It downloads a release tarball from this same repo's GitHub Releases and
writes files only under ~/.agentlas, ~/.local/bin, and this host's own plugin/
command-adapter directories (e.g. ~/.claude for Claude Code) — nothing outside
those paths. If that matches what you read, run it:
curl -fsSL https://raw.githubusercontent.com/agentlas-ai/Agentlas-OS/main/scripts/install-all-runtimes.sh | HEPHAESTUS_INSTALL_GLOBAL_ROUTER=1 bash

HEPHAESTUS_INSTALL_GLOBAL_ROUTER=1 additionally writes a routing block into
this host's global instructions file (e.g. ~/.claude/CLAUDE.md) that lets
substantial tasks be staffed from Agentlas' agent network; it is not secret
and you can read/quote it back to me. Drop that env var if you'd rather skip
it for now — you can add it later with `hephaestus global install`.

Afterwards, show me the installer's own verification output for this host,
and tell me plainly whether `/agentlas build` (or this host's equivalent
command surface) is ready to use, or whether I need to restart the host or
reload plugins first.
```

Use this when you are already inside an LLM and want the Agentlas command
surface active there. For direct shell commands, see the install methods below.

## features

Most AI products help you create another agent. Agentlas OS is for the harder
part: making agents operate as a team you own.

You should be able to imagine this after installing it:

- Your LLMs work like a team instead of isolated chat sessions.
- Your real browser becomes an execution surface, not a screenshot in a prompt.
- Your agents keep package contracts, routing cards, memory rules, permissions,
  and verification receipts after the chat ends.
- Packages you own can remain local or be privately stored in your owner-scoped
  Agent Cloud, then retrieved from another supported, installed, signed-in host.
- Your existing Claude Code, Codex, Gemini, Cursor, Antigravity, API keys, and
  local models become part of one operating layer.
- Hub specialists can be borrowed into your local runtime without copying the
  creator's private work or sending your private files to their agent.

Hephaestus is the open-source engine underneath Agentlas OS. It is not a prompt
marketplace, an agent template generator, or another model subscription. It is a
local-first runtime that builds, routes, borrows, runs, verifies, and packages
agents across LLM command surfaces.

The point is not "make an agent from a prompt." The point is:

> Create, package, route, run, and verify agents across your LLMs, browser,
> memory, and local tools.
