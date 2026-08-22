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

### No LLM handy? Type the command yourself

You don't need an AI to install this — a terminal and one pasted line is
enough. New to terminals? Follow your OS below.

**On Windows — open Git Bash:**

1. **Do you already have Git Bash?** Click the search icon (or press the
   **Windows key**) in your taskbar and type **`git bash`**.
   - If **"Git Bash"** shows up in the results, click it and skip to step 3.
   - If nothing shows up, you need to install Git for Windows first: go to
     **[git-scm.com/download/win](https://git-scm.com/download/win)**,
     download it, and run the installer (default options are fine — keep
     clicking **Next**, then **Install**).
2. After installing, search **`git bash`** again (same as step 1) and click
   the **"Git Bash"** result.
3. A black window opens — this is Git Bash. Click inside it, **paste** the
   command below (right-click → Paste, or `Shift+Insert`), then press
   **Enter**:
   ```bash
   curl -fsSL https://raw.githubusercontent.com/agentlas-ai/Agentlas-OS/main/scripts/install-all-runtimes.sh | HEPHAESTUS_INSTALL_GLOBAL_ROUTER=1 bash
   ```
4. Wait for it to finish (it prints its own progress). When it stops and
   gives you the prompt back, close and reopen your AI tool (Claude Code,
   Codex, etc.) so it picks up the new commands.

**On macOS — open Terminal:**

1. Press **`Cmd + Space`** to open Spotlight search, type **`terminal`**,
   and press **Enter**.
2. A window opens (Terminal, built into macOS — nothing to install). Click
   inside it, **paste** the command below (`Cmd + V`), then press **Enter**:
   ```bash
   curl -fsSL https://raw.githubusercontent.com/agentlas-ai/Agentlas-OS/main/scripts/install-all-runtimes.sh | HEPHAESTUS_INSTALL_GLOBAL_ROUTER=1 bash
   ```
   The first time you run `curl`/`git` on a fresh Mac, macOS may ask to
   install "Command Line Tools" — click **Install** and wait, then run the
   command again.
3. Wait for it to finish, then close and reopen your AI tool so it picks up
   the new commands.

If you'd rather read the script before running it (recommended if you're
security-conscious), open this link in your browser first:
[install-all-runtimes.sh](https://raw.githubusercontent.com/agentlas-ai/Agentlas-OS/

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

## Why Not Just Make A Claude Agent?

Claude subagents and custom agents are useful. They give a task its own prompt,
tools, and context window. Agentlas starts after that point.

An LLM can draft an agent. Agentlas turns it into an operating unit:

| Layer | A prompt-made agent | An Agentlas package |
| --- | --- | --- |
| Definition | Role prompt, markdown, tool list | Manifest, agent card, mode map, package contract |
| Invocation | Manual mention or simple trigger | Routing card, triggers, anti-triggers, benchmarks, receipts |
| Browser | Ad hoc browsing or screenshots | Real browser hardpoint with visible clicks, forms, waits, and snapshots |
| Memory | Copied context or chat history | Memory map, memory tickets, Memory Curator, Policy Gate |
| Runtime | One LLM session or one vendor runtime | Adapters across Claude Code, Codex, Gemini, Cursor, Antigravity, and local runtime |
| Teams | Another prompt layer | Orchestrator, PM Soul, Memory Curator, Policy Gate, eval judge, QA gate |
| Verification | User checks manually | Package checks, receipts, Stormbreaker final gate |
| Ownership and portability | Trapped in the chat or vendor workspace where it was created | Portable package that can remain local or be retrieved from the owner's Agent Cloud on another supported, installed, signed-in host |
| Distribution | Copy the prompt | Explicit choice between public Hub publishing and private owner-scoped Cloud storage |

That is the product boundary: Agentlas does not compete on "better prompt." It
gives agents the architecture to keep working outside one chat.

## The Agent OS Stack

Agentlas maps agent work to operating-system-like responsibilities without
forcing your work into one model provider:

| OS Abstraction | Implementation in Hephaestus |
| :--- | :--- |
| **Kernel / Policy Gate** | Deterministic router + security gates. Every routing action yields an auditable receipt; tool execution permissions are enforced by the active host and runtime. |
| **Processes / Threads** | Independent agents and multi-agent teams compiled as packages with explicit, typed contracts (Routing Cards, anti-scopes, memory boundaries, and verification shims). |
| **Process Scheduler** | Network 2.0 routing (local-first, quality-gated, and benchmark-gated dispatch) combined with Stormbreaker's parallel execution fabric and append-only run journals. |
| **Memory Management (MMU)** | Two-boundary governed memory: local project memory remains isolated on the machine, while durable promotions are gated by a local Memory Curator. |
| **Virtual File System** | Production Ontology Runtime: local-first source ingestion, CJK trigram FTS5
