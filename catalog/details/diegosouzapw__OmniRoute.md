# diegosouzapw/OmniRoute

Never stop coding. Free MIT AI gateway: one endpoint, 340 providers (90+ free), 1200+ models — Kimi, Claude, GPT, Gemini, GLM, DeepSeek, MiniMax. Works with Claude Code, Codex, Cursor, OpenCode, Cline

## installation

</div>

<img src="./docs/diagrams/works-zero-config.svg" width="100%" alt="Works the second you install it — zero config. Three steps: 1. Install — npm i -g omniroute, server boots on localhost:20128. 2. Point your tool at http://localhost:20128/v1 — any OpenAI-compatible tool (Claude Code, Cursor, Cline). 3. It answers — call model auto for an instant reply, with no API key, no signup, no configuration. Keyless free providers OpenCode Free and Felo are pre-wired into the auto combo, so a fresh install responds out of the box."/>

```bash

## features

</div>

<img src="./docs/diagrams/why-pain-fix.svg" width="100%" alt="Why OmniRoute — stop juggling 10 dashboards, dead API keys and surprise bills. Ten daily pains vs fixes: quota expiring unused → maximize subscriptions; rate limits mid-coding → 4-tier auto-fallback (Subscription → API → Cheap → Free); tool outputs burning tokens → RTK + Caveman compression (15–95%); expensive APIs → cost-optimized routing; every tool its own setup → one endpoint, one dashboard; AI blocked → 3-level proxy + TLS stealth; dead keys → 3-layer resilience (circuit breakers, key cooldown, model lockout); team sharing one subscription → key pools with fair-share quotas; prompts through someone's cloud → local-first with AES-256-GCM encrypted keys; no spend visibility → live analytics (usage, quota, savings, p95 latency)."/>

<div align="center">

<img src="./docs/diagrams/tier-cascade.svg" width="100%" alt="OmniRoute request flow: your IDE or CLI (Claude Code, Cursor, Cline…) calls one local endpoint (http://localhost:20128/v1); the OmniRoute Smart Router (RTK + Caveman compression, 19 routing strategies, circuit breakers, TLS stealth, MCP, A2A, guardrails) auto-falls back across 4 provider tiers — Tier 1 Subscription (Claude Code, Codex, Copilot), quota out? Tier 2 API Key (DeepSeek, Groq, xAI), budget hit? Tier 3 Cheap (GLM $0.5, MiniMax $0.2), budget hit? Tier 4 Free (Kiro, Qoder, Pollinations) — always on."/>

</div>

<br/>

<div align="center">

## configuration

No combo to create. Set your model to `auto` (or a variant) and OmniRoute builds a virtual combo from your connected providers, scored live:

<table>
  <tr><th align="left">Model ID</th><th align="left">What it optimizes for</th></tr>
  <tr><td align="left" nowrap><code>auto</code></td><td align="left">🎯 Balanced default (LKGP — sticks to your last good provider)</td></tr>
  <tr><td align="left" nowrap><code>auto/coding</code></td><td align="left">🧑‍💻 Quality-first weights for code generation</td></tr>
  <tr><td align="left" nowrap><code>auto/fast</code></td><td align="left">⚡ Lowest latency first</td></tr>
  <tr><td align="left" nowrap><code>auto/cheap</code></td><td align="left">💰 Cheapest per token first</td></tr>
  <tr><td align="left" nowrap><code>auto/offline</code></td><td align="left">🔋 Most quota / rate-limit headroom first</td></tr>
  <tr><td align="left" nowrap><code>auto/smart</code></td><td align="left">🔭 Quality-first + 10% exploration to discover better models</td></tr>
</table>

##

## tools

claude mcp add-server omniroute --type http --url http://localhost:20128/api/mcp/stream
```

<sub>📖 [MCP Server](docs/frameworks/MCP-SERVER.md) · [A2A Server](docs/frameworks/A2A-SERVER.md) · [Agent Protocols](docs/frameworks/AGENT_PROTOCOLS_GUIDE.md)</sub>

<br/>

<div align="center">
