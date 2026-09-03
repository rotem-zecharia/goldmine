# JuliusBrussee/caveman

🪨 why use many token when few token do trick — Claude Code skill that cuts 65% of tokens by talking like caveman

## installation

Caveman comes in two sizes.

**The small one is the skill**: a rule file that makes your agent answer in caveman. Free forever, MIT, runs in [30+ agents](./INSTALL.md) (Claude Code, Codex, Gemini, Cursor, Windsurf, Cline, Copilot, more), installs in one command:

```bash
npx skills add JuliusBrussee/caveman
```

Type `/caveman` in your agent if it doesn't wake up on its own. That the whole install. One rock.

**The big one is the proxy.** It sits between your agent and the AI provider, on your machine, and shrinks what the agent *reads* before every call; a copy of anything it compressed stays on your disk in case the agent needs the original back. MIT CLI, BSL-1.1 runtime:

```bash
npm install -g @caveman-ai/cli && caveman setup --install
caveman claude        # or codex · gemini · aider · kilo · qwen · opencode · hermes · openclaw · pi
```

They stack. Most people start with the skill and graduate.

<details>
<summary><strong>More doors into the cave</strong> — full installer, Windows, single agents, uninstall</summary>

The full installer wires up Claude Code hooks and the statusline badge, detects every supported agent on your machine, and reruns safely (Node.js 22.13+):

```bash
curl -fsSL https://raw.githubusercontent.com/JuliusBrussee/caveman/v2.5.0/install.sh | bash
```

On Windows (PowerShell 5.1+):

```powershell
irm https://raw.githubusercontent.com/JuliusBrussee/caveman/v2.5.0/install.ps1 | iex
```

Just one agent:

```bash
# Claude Code
claude plugin marketplace add JuliusBrussee/caveman && claude plugin install caveman@caveman

# Gemini CLI
gemini extensions install https://github.com/JuliusBrussee/caveman

# Qwen Code CLI, then its Caveman wrapper
npm i -g @qwen-code/qwen-code
caveman qwen

# Codex, Cursor, Windsurf, Cline, and other skills-compatible agents
npx skills add JuliusBrussee/caveman --skill '*' -a codex --yes  # replace codex with your agent profile
```

Changed your mind: `npx -y github:JuliusBrussee/caveman -- --uninstall`.

</details>

The full 30+ agent matrix, dry runs, flags, and verification live in [INSTALL.md](./INSTALL.md).

## What you save

Quick vocabulary, since tokens are the whole point: a token is the unit AI billing runs on, roughly three-quarters of a word. Your agent spends them twice, once on everything it writes and again on everything it reads, and the reading is usually the bigger half of the bill. Caveman goes after both.

### Writing less

Ten ordinary coding prompts through the real Claude API, with the skill and without. Same model, same questions; the only change is caveman telling it to keep it short:

![Bar chart of output tokens per task: a normal agent averages 1,214 tokens per reply, caveman averages 294, a 65% reduction. Best case 87% (React error boundary), worst case 22% (callback refactor).](docs/assets/chart-skill-output.svg)

<details>
<summary><strong>The numbers behind the chart</strong> — regenerate with <code>uv run python benchmarks/run.py</code></summary>

<!-- BENCHMARK-TABLE-START -->
| Task                                    | Normal   | Caveman | Saved   |
| --------------------------------------- | -------- | ------- | ------- |
| Explain React re-render bug             | 1180     | 159     | 87%     |
| Fix auth middleware token expiry        | 704      | 121     | 83%     |
| Set up PostgreSQL connection pool       | 2347     | 380     | 84%     |
| Explain git rebase vs merge             | 702      | 292     | 58%     |
| Refactor callback to async/await        | 387      | 301     | 22%     |
| Architecture: microservices vs monolith | 446      | 310     | 30%     |
| Review PR for security issues           | 678      | 398     | 41%     |
| Docker multi-stage build                | 1042     | 290     | 72%     |
| Debug PostgreSQL race condition         | 1200     | 232     | 81%     |
| Implement React error boundary          | 3454     | 456     | 87%     |
| **Average**                             | **1214** | **294** | **65%** |
<!-- BENCHMA
