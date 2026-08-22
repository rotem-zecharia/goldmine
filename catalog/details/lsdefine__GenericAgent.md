# lsdefine/GenericAgent

Self-evolving agent: grows skill tree from 3.3K-line seed, achieving full system control with 6x less token consumption

## features

**GenericAgent** is a minimal, self-evolving autonomous agent framework. Its core is just **~3K lines of code**. Through **9 atomic tools + a ~100-line Agent Loop**, it grants any LLM system-level control over a local computer — covering browser, terminal, filesystem, keyboard/mouse input, screen vision, and mobile devices (ADB).

> Design philosophy — **don't preload skills, evolve them.**

Every time GenericAgent solves a new task, it automatically crystallizes the execution path into a reusable **Skill**. The longer you use it, the more skills accumulate — forming a personal skill tree grown entirely from 3K lines of seed code.

> 🤖 **Self-Bootstrap Proof** — Everything in this repository, from installing Git and running `git init` to every commit message, was completed autonomously by GenericAgent. The author never opened a terminal once.

### 📑 Table of Contents

- [Key Features](#-key-features)
- [Demo Showcase](#-demo-showcase)
- [Quick Start](#-quick-start)
- [Usage](#-usage)
- [Unlocking Advanced Capabilities](#-unlocking-advanced-capabilities)
- [Architecture](#-architecture)
- [Self-Evolution Mechanism](#-self-evolution-mechanism)
- [Comparison](#-comparison)
- [Evaluation](#-evaluation)
- [Roadmap & News](#-roadmap--news)
- [Community & Support](#-community--support)
- [License](#-license)

---

## 📋 Key Features

| Feature | Description |
| :--- | :--- |
| 🧬 **Self-Evolving** | Automatically crystallizes each task into a Skill. Capabilities grow with every use, forming your personal skill tree. |
| 🪶 **Minimal Architecture** | ~3K lines of core code. Agent Loop is ~100 lines. No complex dependencies, zero deployment overhead. |
| ⚡ **Strong Execution** | **TMWebdriver** injects into a real browser (preserving login sessions). 9 atomic tools take direct control of the system. |
| 🔌 **High Compatibility** | Supports Claude / Gemini / Kimi / MiniMax and other major models. Cross-platform. |
| 💰 **Token Efficient** | <30K context window — a fraction of the 200K–1M other agents consume. Less noise, fewer hallucinations, higher success rate, lower cost. |

---

## 🎯 Demo Showcase

<table>
  <tr>
    <td align="center" width="50%"><b>🛡️ Real-Browser CAPTCHA Survival</b></td>
    <td align="center" width="50%"><b>🌐 Autonomous Web Exploration</b></td>
  </tr>
  <tr>
    <td><img src="assets/demo/discord_hcaptcha_real_browser.gif" width="100%" alt="Discord hCaptcha passed in real browser"></td>
    <td><img src="assets/demo/autonomous_explore.png" width="100%" alt="Web Exploration"></td>
  </tr>
  <tr>
    <td><sub>While configuring a Discord bot, an hCaptcha <i>"Are you human?"</i> challenge pops up mid-task — GA's real browser session passes it and the task continues. See <a href="#browser-realness-of-ga-web-tools">Browser Realness</a>.</sub></td>
    <td><sub>Autonomously browses and periodically summarizes web content.</sub></td>
  </tr>
  <tr>
    <td align="center"><b>🧋 Food Delivery Order</b></td>
    <td align="center"><b>📈 Quantitative Stock Screening</b></td>
  </tr>
  <tr>
    <td><img src="assets/demo/order_tea.gif" width="100%" alt="Order Tea"></td>
    <td><img src="assets/demo/selectstock.gif" width="100%" alt="Stock Selection"></td>
  </tr>
  <tr>
    <td><sub><i>"Order me a milk tea"</i> — navigates the delivery app, selects items, completes checkout.</sub></td>
    <td><sub><i>"Find GEM stocks with EXPMA golden cross, turnover &gt; 5%"</i> — quantitative screening.</sub></td>
  </tr>
  <tr>
    <td align="center"><b>💰 Expense Tracking</b></td>
    <td align="center"><b>💬 Batch Messaging</b></td>
  </tr>
  <tr>
    <td><img src="assets/demo/alipay_expense.png" width="100%" alt="Alipay Expense"></td>
    <td align="center"><img src="assets/demo/wechat_batch.png" width="65%" alt="WeChat Batch"></td>
  </tr>
  <tr>
    <td><sub><i>"Find expenses over ¥2K in the last 3 months"</i> — drives Alipay via ADB.</sub></td>
    <td><sub>Sends bulk WeChat messages, fully driving the WeChat client.</sub></td>
  </tr>
</t

## installation

> ⚠️ **Python version**: use **Python 3.11 or 3.12**. **Do not** use Python 3.14 — it is incompatible with `pywebview` and a few other GA dependencies.
>
> 📖 Detailed installation guide: **[installation.md](docs/installation.md)** · **[installation_zh.md（中文）](docs/installation_zh.md)**

### For LLM Agents

Fetch the installation guide and follow it:

```bash
curl -fsSL https://raw.githubusercontent.com/lsdefine/GenericAgent/refs/heads/main/docs/installation.md
```

### For Humans

#### Method 1 — Clone & install *(recommended)*

```bash
git clone https://github.com/lsdefine/GenericAgent.git && cd GenericAgent
uv venv && uv pip install -e ".[ui]"
cp mykey_template_en.py mykey.py   # fill in your LLM API key
```

Dependencies are deliberately tiered: the agent core needs only `requests`, plus four lightweight packages (`beautifulsoup4`, `bottle`, `simple-websocket-server`, `aiohttp`) for TMWebdriver's local server. The `[ui]` extra pulls in frontend libraries (Streamlit, `prompt_toolkit`/`rich` for the TUI, …) — install it for the bundled UIs, or skip it entirely and drive the agent headless. No Playwright, no LangChain, no browser binaries to download.

Then launch:

```bash
python frontends/tui_v3.py   # Terminal UI (recommended)
python launch.pyw            # Streamlit web UI
```

#### Method 2 — One-line installer *(convenience)*

Sets up a self-contained directory with an isolated Python environment, Git, and a ready-to-run package. The script is in [`assets/`](assets/) if you'd like to read it first.

**Windows PowerShell**

```powershell
powershell -ExecutionPolicy Bypass -c "$env:GLOBAL=1; irm https://raw.githubusercontent.com/lsdefine/GenericAgent/main/assets/ga_install.ps1 | iex"
```

**Linux / macOS**

```bash
GLOBAL=1 bash -c "$(curl -fsSL https://raw.githubusercontent.com/lsdefine/GenericAgent/main/assets/ga_install.sh)"
```

> 💡 GenericAgent grows its environment **through the Agent itself** — don't pre-install everything. See [Unlocking Advanced Capabilities](#-unlocking-advanced-capabilities) below.

---

## tools

### Frontends

#### Terminal UI *(recommended)*

A lightweight, scrollback-first terminal interface built on `prompt_toolkit` + `rich`. Supports multiple concurrent sessions and real-time streaming.

```bash
python frontends/tui_v3.py
```

<details>
<summary><b>⚠️ Windows TUI Troubleshooting</b></summary>

TUI rendering on Windows can be flaky depending on terminal + font. Common causes:

1. `prompt_toolkit` / `rich` are not on the latest version — `pip install -U prompt_toolkit rich` first.
2. PowerShell / cmd ship with terminals that have rough Unicode + key-binding support. **Prefer Git Bash on Windows**, which is much better behaved.
3. If it still looks broken, ask GA itself to fix it:
   > *"My experience using `frontends/tui_v3.py` in PowerShell / cmd / Git Bash on Windows is very poor — lots of incompatibility. Please refer to Claude Code's best practices for the Windows terminal and fix all font and rendering incompatibilities."*

</details>

#### Streamlit UI

```bash
python launch.pyw
```

### Bot Interface (IM)

GenericAgent also supports IM frontends such as Telegram, Discord, and Lark.

| Platform | Command |
| :--- | :--- |
| Telegram | `python frontends/tgapp.py` |
| Discord | `python frontends/dcapp.py` |
| Lark / Feishu | `python frontends/fsapp.py` |

> WeChat, QQ, WeCom and DingTalk are also supported — see the Chinese section below.
> For detailed setup, ask GenericAgent itself.

---

## limitations

- **2026-05-23** — 🆕 **TUI v3 released** (`frontends/tui_v3.py`). Block-based scrollback with proper resize reflow, per-terminal color profile for cross-terminal parity, and feature parity with v2.
- **2026-05-18** — 🆕 **Morphling mode**. Project-level skill absorption — extract goal + tests from any external repo, then decide per component: call, rewrite, or discard. See `memory/morphling_sop.md`.
- **2026-05-17** — 🆕 **Goal Hive mode**. Multi-worker cooperative Goal mode — BBS-coordinated master/workers running long-horizon objectives in parallel. See `memory/goal_hive_sop.md`.
- **2026-05-15** — 🖥️ **Desktop GUI released**. One-line installs ship a ready-to-run desktop app (`frontends/GenericAgent.exe`). Developers launch via `python launch.pyw`.
- **2026-05-14** — 🆕 **Conductor sub-agent orchestration**. Spawn, supervise, and auto-clean parallel sub-agents; first-class delegation primitives complementing `/btw` side-questions.
- **2026-05-12** — 🆕 **TUI v2 released** (`frontends/tuiapp_v2.py`). Refined Textual frontend with image-paste folding, file paste, block-delete, Ctrl+C copy, history navigation, and `/llm` / `/export` / `/continue` pickers.
- **2026-05-08** — 🆕 **Goal mode** (`reflect/goal_mode.py`). Time-budget-driven self-driven loop — "keep optimizing X for N hours" with no premature delivery.
- **2026-04-21** — 📄 [**Technical Report on arXiv**](https://arxiv.org/abs/2604.17091) — *GenericAgent: A Token-Efficient Self-Evolving LLM Agent via Contextual Information Density Maximization*.
- **2026-04-11** — Introduced **L4 session archive memory** and scheduler cron integration.
- **2026-03-23** — Personal WeChat supported as a bot frontend.
- **2026-03-10** — [Released million-scale Skill Library](https://mp.weixin.qq.com/s/q2gQ7YvWoiAcwxzaiwpuiQ?scene=1&click_id=7) *(Chinese)*.
- **2026-03-08** — [Released "Dintal Claw" — a GenericAgent-powered government-affairs bot](https://mp.weixin.qq.com/s/eiEhwo-j6S-WpLxgBnNxBg) *(Chinese)*.
- **2026-03-01** — [Featured by Jiqizhixin (机器之心)](https://mp.weixin.qq.com/s/uVWpTTF5I1yzAENV_qm7yg) *(Chinese)*.
- **2026-01-16** — GenericAgent **V1.0** public release.

---

## ⭐ Community & Support

If this project helped you, please consider leaving a **Star!** 🙏

### 🚩 Friendly Links

Thanks to the **LinuxDo** community for the support!

[![LinuxDo](https://img.shields.io/badge/Community-LinuxDo-blue?style=for-the-badge)](https://linux.do/)

**Community GUIs** *(independent open-source projects)*:

- [chilishark27/ga-manager](https://github.com/chilishark27/ga-manager)
- [wangjc683/galley](https://github.com/wangjc683/galley) — Out-of-the-box local agent workbench with a bundled GA runtime (CPython 3.11 + deps), native GUI/CLI, multi-session + Project orchestration, local-first.
- [FroStorM/A3Agent](https://github.com/FroStorM/A3Agent/tree/workbench)
- [Fwind43/GenericAgent-Admin](https://github.com/Fwind43/GenericAgent-Admin) — Go + React desktop admin panel: service lifecycle management, native chat, Goal mode, BBS team board, file editor, model config wizard, TMWebDriver monitor, self-update, and Windows tray/desktop-pet integration.

---

## 📄 License

Distributed under the **MIT License**. See [`LICENSE`](LICENSE) for full text.

> *Disclaimer: The official GenericAgent channels are this GitHub repository and https://gaagent.ai. DintalClaw is currently the only officially authorized commercial partner; any other third-party website, organization, or individual using the GenericAgent name is not official unless explicitly listed here.*

---

<a id="-中文"></a>

## 🌟 项目简介

**GenericAgent** 是一个极简、可自我进化的自主 Agent 框架。核心仅 **~3K 行代码**，通过 **9 个原子工具 + ~100 行 Agent Loop**，赋予任意 LLM 对本地计算机的系统级控制能力，覆盖浏览器、终端、文件系统、键鼠输入、屏幕视觉及移动设备（ADB）。

> 设计哲学 —— **不预设技能，靠进化获得能力。**

每解决一个新任务，GenericAgent 就将执行路径自动固化为 Skill，供后续直接调用。使用时间越长，沉淀的技能越多，形成一棵完全属于你、从 3K 行种子代码生长出来的专属技能树。

> 🤖 **自举实证** — 本仓库的一切，从安装 Git、`git init` 到每一条 commit message，均由 GenericAgent 自主完成。作者全程未打开过一次终端。

### 📑 目录

- [核心特性](#-核心特性)
- [实例展示](#-实
