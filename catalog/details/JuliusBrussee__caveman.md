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
curl -fsSL https://raw.githubusercontent.com/JuliusBrussee/caveman/v2.2.0/install.sh | bash
```

Windows (PowerShell 5.1+):

```powershell
irm https://raw.githubusercontent.com/JuliusBrussee/caveman/v2.2.0/install.ps1 | iex
```

One agent only:

```bash
