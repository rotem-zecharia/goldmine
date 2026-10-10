# diegosouzapw/OmniRoute

Never stop coding. Free MIT AI gateway: one endpoint, 359 providers (150+ free), 1200+ models Kimi, Claude, GPT, Gemini, GLM, DeepSeek, MiniMax. Works with Claude Code, Codex, Cursor, OpenCode, Cline 

## installation

</div>

<img src="./docs/diagrams/works-zero-config.svg" width="100%" alt="Three steps: install and start OmniRoute, connect an eligible provider with your own account or API key, then point your tool at localhost:20128/v1 using an OmniRoute API key and model auto. Routing depends on available eligible connections and provider limits."/>

```bash
# After connecting a provider, copy your OmniRoute key from Dashboard → Endpoints:
curl http://localhost:20128/v1/chat/completions \
  -H "Authorization: Bearer YOUR_OMNIROUTE_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model":"auto","messages":[{"role":"user","content":"Hello!"}]}'
```

<sub>`auto` needs an eligible route. A fresh installation can have no eligible keyless targets, and a keyless provider may reject third-party clients. Providers marked `tos: avoid`, including OpenCode Free and Kiro, are excluded from automatic routing by default; connecting an account does not override that setting. See the [Free Tiers Guide](docs/getting-started/FREE-TIERS-GUIDE.md) before choosing a provider.</sub>

<sub>📦 Copy-paste quickstart scripts for **Python, Node.js, PHP, and cURL** → [`examples/quickstart/`](examples/quickstart/)</sub>

<br/>

<div align="center">

# 💥 The Promise

</div>

<img src="./docs/diagrams/promise-pillars.svg" width="100%" alt="The Promise — One endpoint and 372 providers. Automatic fallback keeps routing while another healthy target is available. Six pillars: resilient fallback across 372 providers · up to 95% token savings on eligible workloads · $0 to start with 150+ free tiers and 54 recurring/keyless free-forever providers · 36 CLI/agent integrations through one config · OpenAI, Claude, Gemini and Responses API compatibility at /v1 · production controls including circuit breakers, TLS stealth, MCP 110 tools, A2A, memory, guardrails, evals and 39,000+ static test declarations across 5,100+ tracked test files."/>

<br/>
<br/>

<div align="center">

## features

</div>

<img src="./docs/diagrams/why-pain-fix.svg" width="100%" alt="Why OmniRoute — stop juggling 10 dashboards, dead API keys and surprise bills. Ten daily pains vs fixes: quota expiring unused → maximize subscriptions; rate limits mid-coding → 4-tier auto-fallback (Subscription → API → Cheap → Free); tool outputs burning tokens → RTK + Caveman compression (15–95%); expensive APIs → cost-optimized routing; every tool its own setup → one endpoint, one dashboard; AI blocked → 3-level proxy + TLS stealth; dead keys → 3-layer resilience (circuit breakers, key cooldown, model lockout); team sharing one subscription → key pools with fair-share quotas; prompts through someone's cloud → local-first with AES-256-GCM encrypted keys; no spend visibility → live analytics (usage, quota, savings, p95 latency)."/>

<div align="center">

<img src="./docs/diagrams/tier-cascade.svg" width="100%" alt="OmniRoute request flow: your IDE or CLI (Claude Code, Cursor, Cline…) calls one local endpoint (http://localhost:20128/v1); the OmniRoute Smart Router (RTK + Caveman compression, 19 routing strategies, circuit breakers, TLS stealth, MCP, A2A, guardrails) can fall back across 4 provider tiers while an eligible healthy target remains — Tier 1 Subscription, Tier 2 API Key, Tier 3 Cheap and Tier 4 Free."/>

</div>

<br/>

<div align="center">

## 🤝 Supported by our Open Source Friends

</div>

<p align="center">
  <a href="https://platform.kimi.ai?track_id=track-8197581fdd7d4139a0f562e4a03c3798&aff=omniroute">
    <img src="public/sponsors/kimi-k3-banner.png" width="100%" alt="Kimi K3 — Open Frontier Intelligence · 2.8T parameters · 1M-token context"/>
  </a>
</p>

> **Want to join as an Open Source Friend?** These are the companies that back open source and help keep OmniRoute moving — and we say publicly where every token they give us goes. Reach out: [diegosouza.pw@outlook.com](mailto:diegosouza.pw@outlook.com)

<table>
  <tr>
    <td align="center" width="150">
      <a href="https://platform.kimi.ai?track_id=track-8197581fdd7d4139a0f562e4a03c3798&aff=omniroute">
        <picture>
          <source media="(prefers-color-scheme: dark)" srcset="public/providers/kimi-logomark-dark.svg">
          <img src="public/providers/kimi-logomark-light.svg" width="64" alt="Kimi (Moonshot AI)"/>
        </picture>
      </a>
      <br/><b>Kimi</b><br/><sub>Moonshot AI</sub><br/><br/>
      <img src="https://img.shields.io/badge/Founding_Friend-1783FF?style=flat-square" alt="Founding Open Source Friend"/>
    </td>
    <td>
      Thanks to <b>Kimi (Moonshot AI)</b>, our founding Open Source Friend, for backing this project! Kimi is the AI lab behind the open-weight K2 and K3 model families — <b>Kimi K3</b> delivers a 1M-token context window, native vision and frontier-level coding at a fraction of closed-model prices, and works out of the box with Claude Code, Codex and every coding tool OmniRoute serves.
      <br/><br/>
      <b>What Kimi's support powers:</b> Kimi's API credits power OmniRoute's AI-validated release pipeline — the <i>merge validation powered by Kimi K3</i> stage that reviews every pull request before it ships — plus day-to-day feature development. First-class Kimi support ships on both rails: the direct <a href="https://platform.kimi.ai?track_id=track-8197581fdd7d4139a0f562e4a03c3798&aff=omniroute">Kimi API</a> (<code>kimi-k3</code>) and the <a href="https://www.kimi.ai/code?aff=omniroute">Kimi Code coding plan</a> (OAuth and API key). OmniRoute is also the first Brazilian open-source project in Kimi's support program. <a href="https://platform.kimi.ai?track_id=track-8197581fdd7d4139a0f562e4a03c3798&aff=omniroute"><b>Get a Kimi API key with 15% extra credits →</b></a>
    </td>
  </tr>
  <tr>
    <td align="center" width="150">
      <a href="https://cheaperinference.com/?utm_source=omniroute">
        <img src="./public/providers/cli-generic.svg" width="64" alt="Cheaper Inference"/>
      </a>
      <br/><b>Cheaper Inference</b><br/><sub>c

## configuration

No combo to create. Set your model to `auto` (or a variant) and OmniRoute builds a virtual combo from your connected providers, scored live:

<table>
  <tr><th align="left">Model ID</th><th align="left">What it optimizes for</th></tr>
  <tr><td align="left" nowrap><code>auto</code></td><td align="left">🎯 Balanced default (LKGP — sticks to your last good provider)</td></tr>
  <tr><td align="left" nowrap><code>auto/coding</code></td><td align="left">🧑‍💻 Quality-first weights for code generation</td></tr>
  <tr><td align="left" nowrap><code>auto/fast</code></td><td align="left">⚡ Lowest latency first</td></tr>
  <tr><td align="left" nowrap><code>auto/cheap</code></td><td align="left">💰 Cheapest per token first</td></tr>
  <tr><td align="left" nowrap><code>auto/subscription</code></td><td align="left">🎟️ Only the subscription quota you already pay for — fails closed, never a billable fallback (<a href="./docs/routing/SUBSCRIPTION_LADDER.md">guide</a>)</td></tr>
  <tr><td align="left" nowrap><code>auto/thrifty</code></td><td align="left">🪜 Plan quota first, then one rung at a time to the cheapest paid options — back on the plan after it resets (<a href="./docs/routing/SUBSCRIPTION_LADDER.md">guide</a>)</td></tr>
  <tr><td align="left" nowrap><code>auto/offline</code></td><td align="left">🔋 Most quota / rate-limit headroom first</td></tr>
  <tr><td align="left" nowrap><code>auto/smart</code></td><td align="left">🔭 Quality-first + 10% exploration to discover better models</td></tr>
  <tr><td align="left" nowrap><code>auto/lkgp</code></td><td align="left">📌 Explicit last-known-good-provider stickiness</td></tr>
  <tr><td align="left" nowrap><code>auto/chaos</code></td><td align="left">🧪 Parallel fan-out to a panel of models (one per provider, 5 by default), returns one answer; one upstream call per panel model, not fault injection</td></tr>
</table>

##

### 🔀 Or build your own — 19 routing strategies

All **19** strategies — mix & match per combo step:

<table>
  <tr>
    <th>#</th>
    <th align="left">Strategy</th>
    <th align="left">What it does</th>
  </tr>
  <tr>
    <td align="center">1</td>
    <td nowrap><code>priority</code></td>
    <td>First-target ordered list — drain each before the next 🥇</td>
  </tr>
  <tr>
    <td align="center">2</td>
    <td nowrap><code>fill-first</code></td>
    <td>Fill each target's quota fully before moving on</td>
  </tr>
  <tr>
    <td align="center">3</td>
    <td nowrap><code>weighted</code></td>
    <td>Weighted random by per-target weight</td>
  </tr>
  <tr>
    <td align="center">4</td>
    <td nowrap><code>round-robin</code></td>
    <td>Cycle through targets in order</td>
  </tr>
  <tr>
    <td align="center">5</td>
    <td nowrap><code>p2c</code></td>
    <td>Power-of-two-choices random load balancing</td>
  </tr>
  <tr>
    <td align="center">6</td>
    <td nowrap><code>least-used</code></td>
    <td>Pick the target with the lowest current load</td>
  </tr>
  <tr>
    <td align="center">7</td>
    <td nowrap><code>random</code></td>
    <td>Uniform random pick (deduplicated)</td>
  </tr>
  <tr>
    <td align="center">8</td>
    <td nowrap><code>strict-random</code></td>
    <td>Random without de-duplicating repeats 🎲</td>
  </tr>
  <tr>
    <td align="center">9</td>
    <td nowrap><code>cost-optimized</code></td>
    <td>Minimize $ per request from live catalog pricing 💸</td>
  </tr>
  <tr>
    <td align="center">10</td>
    <td nowrap><code>headroom</code></td>
    <td>Pick the target with the most remaining quota</td>
  </tr>
  <tr>
    <td align="center">11</td>
    <td nowrap><code>reset-window</code></td>
    <td>Prefer the target whose quota window resets soonest</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td nowrap><code>reset-aware</code></td>
    <td>Rank by quota reset time — short windows first 📊</td>
  </tr>
  <tr>
    <td align="center">13</td>
    <td nowrap><code>context-relay</code></td>
    <td>Hand off context across targets for long conversations 🧠</t

## tools

claude mcp add-server omniroute --type http --url http://localhost:20128/api/mcp/stream
```

<sub>📖 [MCP Server](docs/frameworks/MCP-SERVER.md) · [A2A Server](docs/frameworks/A2A-SERVER.md) · [Agent Protocols](docs/frameworks/AGENT_PROTOCOLS_GUIDE.md)</sub>

<br/>

<div align="center">

## 🗜️ Save 15–95% Tokens — Automatically

</div>

### 📖 How it works — pipeline, architecture & savings math

<img src="./docs/diagrams/compression-pipeline.svg" width="100%" alt="OmniRoute compression pipeline: an illustrative 10,000-token client request passes through 12 composable engines — Session-Dedup, CCR, Lite, RTK, Responses Tool Output, Headroom, Relevance, Caveman, Aggressive, LLMLingua-2, Ultra and OmniGlyph — and can reach the provider at about 1,080 tokens in the documented stacked example. Structured content is protected by preservation guards and per-step fidelity gates; explicit lossy or experimental modes may transform eligible content."/>

Default stacked combo runs `RTK → Caveman`. When both act on the same tool/context payload, savings compound:

```txt
combined = 1 − (1 − RTK) × (1 − Caveman_input)
average  = 1 − (1 − 0.80) × (1 − 0.46) = 89.2%
range    = 78.4 – 94.6%
```

Code blocks, URLs, JSON and structured data are **always protected** by the preservation engine.

> **Why use many tokens when few tokens do the trick?** Every request passes through OmniRoute's compression pipeline **transparently** — no client changes. It's now a **stack of 12 composable engines** that run in order and mix & match per routing combo — building on ideas from [RTK](https://github.com/rtk-ai/rtk), [Caveman](https://github.com/JuliusBrussee/caveman) (⭐ 90K+), [LLMLingua-2](https://github.com/microsoft/LLMLingua), and [Troglodita](https://github.com/leninejunior/troglodita) (PT-BR).

### 🧱 The 12-engine stack

Engines run in pipeline order; each is independently toggleable and configurable per combo:

<table>
  <tr><th align="center">#</th><th align="left">Engine</th><th align="left">What it does</th></tr>
  <tr><td align="center" nowrap>1</td><td align="left" nowrap><b>Session-Dedup</b></td><td align="left">Drops content repeated across turns (content-addressed, cross-turn)</td></tr>
  <tr><td align="center" nowrap>2</td><td align="left" nowrap><b>CCR</b></td><td align="left">Archives large blocks behind retrieve markers, fetched on demand</td></tr>
  <tr><td align="center" nowrap>3</td><td align="left" nowrap><b>Lite</b></td><td align="left">Whitespace + image-URL trimming (latency-light baseline)</td></tr>
  <tr><td align="center" nowrap>4</td><td align="left" nowrap><b>RTK</b></td><td align="left">Smart tool-result filtering, dedup & truncation (command-aware)</td></tr>
  <tr><td align="center" nowrap>5</td><td align="left" nowrap><b>Responses Tool Output</b></td><td align="left">Lossless-first JSON + bounded diagnostic compression for shell/patch/search/build outputs (Responses API)</td></tr>
  <tr><td align="center" nowrap>6</td><td align="left" nowrap><b>Headroom</b></td><td align="left">Lossless tabular compaction of JSON arrays (~30%) via a vendored <b>GCF</b> codec</td></tr>
  <tr><td align="center" nowrap>7</td><td align="left" nowrap><b>Relevance</b></td><td align="left">Extractive sentence scoring against the last user query</td></tr>
  <tr><td align="center" nowrap>8</td><td align="left" nowrap><b>Caveman</b></td><td align="left">Rule-based prose compression (~65–75% on output)</td></tr>
  <tr><td align="center" nowrap>9</td><td align="left" nowrap><b>Aggressive</b></td><td align="left">Summarization + progressive aging of old turns</td></tr>
  <tr><td align="center" nowrap>10</td><td align="left" nowrap><b>LLMLingua-2</b></td><td align="left">ML semantic pruning via MobileBERT ONNX — code-safe, async</td></tr>
  <tr><td align="center" nowrap>11</td><td align="left" nowrap><b>Ultra</b></td><td align="left">Heuristic token pruning with an optional small-model (SLM) tier</td></tr>
  <tr><td align="center" nowrap>12</td><td align=
