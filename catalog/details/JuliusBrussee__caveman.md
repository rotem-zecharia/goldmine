# JuliusBrussee/caveman

🪨 why use many token when few token do trick — Claude Code skill that cuts 65% of tokens by talking like caveman

## installation

Two products. Pick one or both.

**1 · Save input** — Caveman Proxy shrinks what your agent *reads* before every provider call, with byte-exact recovery. BSL-1.1 runtime, MIT CLI.

```bash
npm install -g @caveman-ai/cli && caveman setup --install
caveman claude        # or codex · gemini · aider · opencode · hermes · openclaw
```

**2 · Save output** — the skill, the original. Your agent *answers* in tight caveman-speak while code, commands, and errors stay exact. MIT, 30+ agents.

```bash
npx skills add JuliusBrussee/caveman
```

<details>
<summary><strong>Other ways in</strong> — full installer with hooks, Windows, one agent only</summary>

The full installer also wires the Claude Code hooks and statusline, finds every supported agent on your machine, and is safe to rerun (Node.js 18+):

```bash
curl -fsSL https://raw.githubusercontent.com/JuliusBrussee/caveman/v2.3.1/install.sh | bash
```

Windows (PowerShell 5.1+):

```powershell
irm https://raw.githubusercontent.com/JuliusBrussee/caveman/v2.3.1/install.ps1 | iex
```

One agent only:

```bash
# Claude Code
claude plugin marketplace add JuliusBrussee/caveman && claude plugin install caveman@caveman

# Gemini CLI
gemini extensions install https://github.com/JuliusBrussee/caveman

# Codex, Cursor, Windsurf, Cline, and other skills-compatible agents
npx skills add JuliusBrussee/caveman --skill '*' -a codex --yes  # replace codex with your agent profile
```

</details>

Full 30+ agent matrix, dry run, flags, verification, and uninstall: [INSTALL.md](./INSTALL.md).

## Where your tokens go

You have months of agent history on disk. `caveman learn` reads it and scores your setup. Local, read-only, no account.

```bash
caveman learn             # Claude Code + Codex + Gemini CLI + opencode; aider via CAVEMAN_AIDER_ROOT
```

<p align="center">
  <img src="docs/assets/learn-report.png" alt="Caveman Learn report: TLDR summary and savings cards on the left; ranked token sinks with an expanded fix and a session context depth histogram on the right" width="900">
</p>

The report shows your Cave Score, every token sink ranked by flow with a one-line fix behind each row, how deep each session ran into its context window, a replay of what the fixes would have cut from your past sessions, and a list-price illustration of what the ranked sinks cost over 30 days.

```bash
caveman learn implement   # hand the plan to Claude Code or Codex
```

`learn implement` opens your own agent with the plan and the `caveman-learn` skill, which instructs it to propose each fix as a diff, apply only on your yes, re-measure, and revert anything that did not lower tokens per turn. Caveman never makes your agent dumber to make it cheaper.

## Caveman Proxy

One command wraps your agent and routes provider traffic through a local proxy powered by Caveman Engine. In a pinned 54-run Claude Code benchmark it used **33.2% fewer provider-reported input tokens** than direct Claude Code while passing all 18 exact-answer checks. [Method, per-case results, and limits.](./docs/WRAP-BENCHMARK.md) `benchmark_counterfactual`

No code change, no Caveman backend: the proxy forwards each request to your chosen provider, and recovery copies stay on your disk. Claude Pro/Max OAuth credentials pass through to Anthropic as-is.

```bash
caveman claude             # Claude Code + Codex + Gemini CLI + opencode; aider via CAVEMAN_AIDER_ROOT
```

<p align="center">
  <img src="docs/assets/wrap-stack.svg" alt="coding agent talks to a local caveman proxy that forwards upstream to the provider with auth passed through byte-exact; a CCR store below the proxy keeps the original bytes and returns a recovery handle to the agent; an MCP toolkit side-channel gives the agent caveman_retrieve, toon encode/decode, and browse" width="820">
</p>

**What the engine does to a payload** — `detect()` types each payload, then routes it to a compressor that keeps what answers depend on:

| Detected type | Keeps | Target Savings|
|---|---|---|
| `json` | ke
