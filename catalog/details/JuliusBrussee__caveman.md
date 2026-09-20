# JuliusBrussee/caveman

🪨 why use many token when few token do trick. Viral skill + proxy for coding agents that cuts 65% of tokens by talking like a caveman.

## features

**Your AI coding agent bills by the word and writes like it knows that. Caveman make it stop.**

<a href="https://www.youtube.com/watch?v=L29q2LRiMRc">
  <img src="https://img.youtube.com/vi/L29q2LRiMRc/hqdefault.jpg" alt="ThePrimeagen reacts to Caveman: No way this actually works" width="360">
</a>

▶️ **[ThePrimeagen reacts: "No way this actually works"](https://www.youtube.com/watch?v=L29q2LRiMRc)**

<a href="https://github.com/JuliusBrussee/caveman/stargazers"><img src="https://img.shields.io/github/stars/JuliusBrussee/caveman?style=flat-square&color=F0A63C&label=stars" alt="GitHub stars"></a>
<a href="https://www.npmjs.com/package/@caveman-ai/cli"><img src="https://img.shields.io/npm/dm/@caveman-ai/cli?style=flat-square&color=F0A63C&label=cli%20downloads" alt="npm downloads"></a>
<a href="https://www.npmjs.com/package/@caveman-ai/middleware"><img src="https://img.shields.io/npm/v/@caveman-ai/middleware?style=flat-square&color=F0A63C&label=middleware%20npm" alt="middleware on npm"></a>
<a href="https://pypi.org/project/caveman-middleware/"><img src="https://img.shields.io/pypi/v/caveman-middleware?style=flat-square&color=F0A63C&label=middleware%20pypi" alt="middleware on PyPI"></a>
<a href="./INSTALL.md"><img src="https://img.shields.io/badge/works_with-30%2B_agents-orange?style=flat-square" alt="30+ agents"></a>
<a href="#wrap-any-agent"><img src="https://img.shields.io/badge/wraps-10_agents_natively-blue?style=flat-square" alt="10 native wrap profiles"></a>
<a href="#-license"><img src="https://img.shields.io/badge/license-MIT_%2B_BSL-green?style=flat-square" alt="License"></a>
<a href="https://skills.sh/JuliusBrussee/caveman"><img src="https://skills.sh/b/JuliusBrussee/caveman" alt="skills.sh"></a>

🏆 **#1 on GitHub Trending · July 2026** &nbsp;·&nbsp; 🥇 **#1 Repository of the Day on [Trendshift](https://trendshift.io/repositories/25391) · April 2026**

**[#1 on Hacker News](https://news.ycombinator.com/item?id=47647455)** · 904 points · 366 comments &nbsp;·&nbsp; **[#8 Product of the Day](https://www.producthunt.com/products/caveman)** on Product Hunt

📄 Cited in **[CAVEWOMAN](https://arxiv.org/abs/2606.24083)**, an Adobe Research paper that measured caveman-style output cutting cost **1.4 to 2.4×, up to 3×** &nbsp;·&nbsp; 🧪 Tested by **[JetBrains](https://blog.jetbrains.com/ai/2026/07/speak-to-ai-agents-like-cavemen-tosave-tokens/)** on 86 real coding tasks: *"costs you nothing measurable in quality"*

<a href="https://www.producthunt.com/products/caveman?embed=true&amp;utm_source=badge-featured&amp;utm_medium=badge&amp;utm_campaign=badge-caveman-2" target="_blank" rel="noopener noreferrer"><img src="https://api.producthunt.com/widgets/embed-image/v1/featured.svg?post_id=1220849&amp;theme=light&amp;t=1786634691828" alt="Caveman - why use many token when few do trick | Product Hunt" width="250" height="54"/></a>
<a href="https://trendshift.io/repositories/25391?utm_source=repository-badge&amp;utm_medium=badge&amp;utm_campaign=badge-repository-25391" target="_blank" rel="noopener noreferrer"><img src="https://trendshift.io/api/badge/repositories/25391" alt="JuliusBrussee%2Fcaveman | Trendshift" width="250" height="55"/></a>

⚡ **One command, no account, no API key.** `npx skills add JuliusBrussee/caveman -g` **[→ Quick Start](#-quick-start)**

</div>

---

<div align="center">

**[See it](#-see-it) · [Quick Start](#-quick-start) · [The Numbers](#-the-numbers) · [How it compares](#-how-it-compares) · [In the Wild](#-in-the-wild) · [The Skill](#-the-skill-unpacked) · [The Proxy](#-the-proxy-unpacked) · [Wrap](#wrap-any-agent) · [Your own app](#-caveman-in-your-own-app) · [When to Skip](#-when-to-use--when-to-skip) · [Docs](./docs/README.md)**

</div>

---

## 🪨 See it

<table>
<tr>
<th width="50%">🗣️ Normal agent · 69 tokens</th>
<th width="50%"><img src="docs/assets/dancing-rock.svg" width="18" height="18" alt=""> Caveman agent · 19 tokens</th>
</tr>
<tr>
<td valign="top">

> The reason your React component is re-renderi

## installation

Caveman come in two sizes. Start small.

### Small rock: the skill

A rule file that makes your agent answer in caveman. MIT, free forever, works in [30+ agents](./INSTALL.md) (Claude Code, Codex, Gemini, Cursor, Windsurf, Cline, Copilot, more). One command:

```bash
npx skills add JuliusBrussee/caveman -g
```

Type `/caveman` if your agent doesn't wake up on its own. That the whole install. One rock.

### Big rock: the proxy

Runs on your machine, between your agent and the AI provider, and shrinks what the agent *reads* before every call. MIT CLI, BSL-1.1 runtime:

```bash
npm install -g @caveman-ai/cli && caveman setup --install
caveman claude        # or codex · gemini · aider · kilo · qwen · opencode · hermes · openclaw · pi
```

### Your own app: the middleware

Building an agent in code instead of running one in a terminal? Same shrinking, one wrapper around the call you already make. MIT client, alpha today:

```bash
npm install @caveman-ai/middleware @caveman-ai/sdk        # TypeScript, plus your framework (ai, openai, …)
pip install 'caveman-middleware[langchain]' caveman-sdk   # Python 3.13+, swap the extra for your framework
```

Six lines of code and a local runtime. [Full walkthrough below](#-caveman-in-your-own-app).

They stack. Most people start with the small rock and graduate.

<details>
<summary><strong>More doors into the cave</strong> · full installer, Windows, single agents, uninstall</summary>

<br>

The full installer wires up Claude Code hooks and the statusline badge, finds every supported agent on your machine, and skips agents you no have. Safe to re-run. Needs Node.js 22.13+.

```bash
curl -fsSL https://raw.githubusercontent.com/JuliusBrussee/caveman/v2.7.0/install.sh | bash
```

Windows, PowerShell 5.1+:

```powershell
irm https://raw.githubusercontent.com/JuliusBrussee/caveman/v2.7.0/install.ps1 | iex
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
npx skills add JuliusBrussee/caveman --skill '*' -a codex --yes -g  # replace codex with your agent profile
```

**Install broke?** Open your agent in this repo and say: *"Read CLAUDE.md and INSTALL.md, install caveman for me."* Agent read repo, agent fix own brain. Snake eat tail.

Changed your mind: `npx -y github:JuliusBrussee/caveman -- --uninstall`

</details>

The full 30+ agent matrix, dry runs, flags, and verification live in [INSTALL.md](./INSTALL.md).

### 🕐 The first five minutes

**Small rock.** The skill, right after `npx skills add`:

1. **Ask it something.** Any coding question. Watch the preamble vanish and the answer stay.
2. **Turn the dial.** `/caveman lite` for tight-but-polite. `/caveman ultra` for grunts. `/caveman wenyan` for classical Chinese, because someone asked.
3. **Commit like a caveman.** `/caveman-commit` writes a Conventional Commit in one line.
4. **Review like a caveman.** `/caveman-review` gives one finding per line: `L42: 🔴 null deref. Guard it.`
5. **Shrink your memory files.** `/caveman-compress CLAUDE.md` cuts the prose, keeps every heading, path, and command, and backs up the original.
6. **Come home.** Say `stop caveman`. Normal prose returns. No hard feelings.

**Big rock.** The proxy, right after `npm install -g @caveman-ai/cli`:

1. **Find out where your tokens go.** `caveman learn` reads months of agent history already on your disk, locally, and ranks your token sinks worst-first with a one-line fix behind each. Do this before anything else. It is the most useful five minutes in this README.
2. **Let it fix them.** `caveman learn implement` hands each fix to Claude Code or Codex one diff at a time, applied only on your yes, and reverts anything that did not lower tokens per turn.
3. **W
