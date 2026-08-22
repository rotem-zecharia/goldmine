# lidge-jun/opencodex

Universal provider proxy for OpenAI Codex & Claude Code — use any LLM (Claude, Gemini, Grok, DeepSeek, Ollama…) with Codex CLI, App, SDK, and Claude Code

## installation

### For humans

```bash
npm install -g @bitkyc08/opencodex   # Node 18+; the Bun runtime is bundled automatically
ocx start                            # or `ocx service` to run it in the background
```

<details>
<summary>Install from source (latest dev)</summary>

**macOS / Linux:**

```bash
curl -fsSL https://bun.sh/install | bash
git clone https://github.com/lidge-jun/opencodex.git
cd opencodex && ~/.bun/bin/bun install
~/.bun/bin/bun run src/cli/index.ts start
```

**Windows (PowerShell):**

```powershell
irm bun.sh/install.ps1 | iex
git clone https://github.com/lidge-jun/opencodex.git
cd opencodex; bun install
bun run src/cli/index.ts start
```

Source install runs the latest `dev` branch. Memory ownership
patches, runtime GC improvements, and unreleased fixes are available here before
they reach the npm package.

</details>

Open **http://localhost:10100** and configure everything in the web dashboard — add providers
(40+ built-ins, or any OpenAI-compatible endpoint), pick models, manage accounts. `ocx gui`
re-opens the dashboard at any time.
It can also manage a **ChatGPT account pool** for Codex auth. Add multiple ChatGPT / Codex accounts,
refresh their 5h / weekly / 30d quota in the dashboard. Under quota routing, new sessions can use
the lowest-usage healthy account; round-robin and fill-first use their own policies. Existing Codex
threads normally retain affinity to the account that started them, so long SSH, tmux, or
mobile-connected sessions do not jump accounts mid-conversation — but quota re-evaluation, failover,
account exclusion, affinity expiry, or 401/403 and 429 recovery can rebind them. Give the accounts a
selection order when one of them — usually your Codex Desktop login — should only be reached for
once the others are drained.

### For agents

```bash
npm install -g @bitkyc08/opencodex
ocx start     # or `ocx service`
ocx init      # interactive setup: writes ~/.opencodex/config.json and wires Codex
```

`ocx init` never starts the proxy; start it first (or after — either order works, but headless
commands like `ocx provider add` and `ocx combo set` talk to the **live** proxy and exit nonzero
when it is unreachable). `ocx status` / `ocx doctor` / `ocx health` report the running state.

> **Agents installing or running opencodex:** read
> [`AGENTS_INSTALL.md`](./AGENTS_INSTALL.md). An interactive `ocx start` may ask once whether to
> star this repository — that is the user's decision, never an agent's. The CLI suppresses the
> prompt for agent-driven runs and the API refuses them with `403 agent_consent_required`.

## Supported platforms

| OS | Status | Service manager |
|---|---|---|
| macOS (arm64 / x64) | Fully supported | launchd |
| Linux (x64 / arm64) | Fully supported | systemd (user unit) |
| Windows (x64) | Fully supported | Task Scheduler (hidden) / opt-in native service (`--native`, WinSW) |

Requires [Node](https://nodejs.org) 18+. The Bun runtime is bundled on `npm install` — no separate
Bun install needed, no WSL needed on Windows. If npm blocked the bundled runtime's install scripts,
see the [installation docs](https://opencodex.me/getting-started/installation/).

## Highlights

- **Use any LLM with Codex, Claude Code, Claude Desktop, and Grok Build** — 40+ providers out of
  the box, each keeping its own native UI.
- **Pool ChatGPT accounts** — thread affinity, quota-aware auto-switching, cooldown and
  fail-closed auth handling.

  > **Provider-policy note:** Account pooling is for routing and operational resilience only; it does
  > not guarantee protection from provider rate limits, enforcement, suspension, or other account
  > actions. OpenCodex does not endorse using additional accounts to circumvent provider limits or
  > sharing account credentials between people. You are responsible for complying with each
  > provider's current terms. See the
  > [Codex Auth account-pool guidance](https://opencodex.me/guides/web-dashboard/#codex-auth-and-account-pools)
  > and [OpenAI's current 
