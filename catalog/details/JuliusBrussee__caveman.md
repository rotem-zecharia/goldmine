# JuliusBrussee/caveman

🪨 why use many token when few token do trick — Claude Code skill that cuts 65% of tokens by talking like caveman

## installation

Caveman come in two sizes.

**Small rock: the skill.** A rule file that makes your agent answer in caveman. MIT, free forever, works in [30+ agents](./INSTALL.md) (Claude Code, Codex, Gemini, Cursor, Windsurf, Cline, Copilot, more). One command:

```bash
npx skills add JuliusBrussee/caveman
```

Type `/caveman` if your agent doesn't wake up on its own. That the whole install. One rock.

**Big rock: the proxy.** Runs on your machine, between your agent and the AI provider, and shrinks what the agent *reads* before every call. Everything it squeezes gets a backup on your disk, so the agent can always pull the original back. MIT CLI, BSL-1.1 runtime:

```bash
npm install -g @caveman-ai/cli && caveman setup --install
caveman claude        # or codex · gemini · aider · kilo · qwen · opencode · hermes · openclaw · pi
```

They stack. Most people start with the small rock and graduate.

<details>
<summary><strong>More doors into the cave</strong> · full installer, Windows, single agents, uninstall</summary>

<br>

The full installer wires up Claude Code hooks and the statusline badge, finds every supported agent on your machine, and skips agents you no have. Safe to re-run. Needs Node.js 22.13+.

```bash
curl -fsSL https://raw.githubusercontent.com/JuliusBrussee/caveman/v2.6.0/install.sh | bash
```

Windows, PowerShell 5.1+:

```powershell
irm https://raw.githubusercontent.com/JuliusBrussee/caveman/v2.6.0/install.ps1 | iex
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

**Install broke?** Open your agent in this repo and say: *"Read CLAUDE.md and INSTALL.md, install caveman for me."* Agent read repo, agent fix own brain. Snake eat tail.

Changed your mind: `npx -y github:JuliusBrussee/caveman -- --uninstall`

</details>

The full 30+ agent matrix, dry runs, flags, and verification live in [INSTALL.md](./INSTALL.md).

## The numbers

A token is what AI billing counts, roughly three quarters of a word. Your agent pays for every token it writes and every token it reads. Reading is usually the bigger bill. The skill cuts the writing. The proxy cuts the reading.

### Skill: writing less

Ten ordinary coding prompts through the real Claude API, with the skill and without. Same model, same questions. Output tokens per reply:

| Task                               | Normal   | Caveman | Saved   |
| ---------------------------------- | -------: | ------: | ------: |
| Implement React error boundary     | 3454     | 456     | 87%     |
| Set up PostgreSQL connection pool  | 2347     | 380     | 84%     |
| Explain git rebase vs merge        | 702      | 292     | 58%     |
| Refactor callback to async/await   | 387      | 301     | 22%     |
| **Average across all ten prompts** | **1214** | **294** | **65%** |

Best row and worst row both up there on purpose. Caveman wins big when the agent would have written an essay, and barely at all when the answer was already mostly code.

<details>
<summary><strong>All ten prompts</strong> · regenerate with <code>uv run python benchmarks/run.py</code></summary>

<br>

<!-- BENCHMARK-TABLE-START -->
| Task                                    | Normal   | Caveman | Saved   |
| --------------------------------------- | -------- | ------- | ------- |
| Explain React re-render bug             | 1180     | 159     | 87%     |
| Fix auth middleware token expiry        | 704      | 121     | 83%     |
| Set up PostgreSQL connection pool       | 2347     | 380     | 84%     |
| Explain git rebase vs merge             | 702      | 292     | 58%     |
| Refactor callback to async/await    
