# lsdefine/GenericAgent

Self-evolving agent: grows skill tree from 3.3K-line seed, achieving full system control with 6x less token consumption

## features

**GenericAgent** is a minimal, self-evolving autonomous agent framework. Its core is just **~3K lines of code**. Through **9 atomic tools + a ~100-line Agent Loop**, it grants any LLM system-level control over a local computer — covering browser, terminal, filesystem, keyboard/mouse input, screen vision, and mobile devices (ADB).

> Design philosophy — **don't preload skills, evolve them.**

Every time GenericAgent solves a new task, it automatically crystallizes the execution path into a reusable **Skill**. The longer you use it, the more skills accumulate — forming a personal skill tree grown entirely from 3K lines of seed code.

> 🤖 **Self-Bootstrap Proof** — Everything in this repository, from installing Git and running `git init` to every commit message, was completed autonomously by GenericAgent. The author never opened a terminal once.

## installation

> ⚠️ **Python version**: use **Python 3.11 or 3.12**. **Do not** use Python 3.14 — it is incompatible with `pywebview` and a few other GA dependencies.
>
> 📖 Detailed installation guide: **[installation.md](docs/installation.md)** · **[installation_zh.md（中文）](docs/installation_zh.md)**

## tools

> *GenericAgent provides only **9 atomic tools**, forming the foundational capabilities for interacting with the outside world.*

| Tool | Function |
| :--- | :--- |
| `code_run` | Execute arbitrary code (Python / PowerShell) |
| `file_read` | Read files |
| `file_write` | Write / create / overwrite files |
| `file_patch` | Patch / modify files |
| `web_scan` | Perceive web content |
| `web_execute_js` | Control browser behavior |
| `ask_user` | Human-in-the-loop confirmation |
| `update_working_checkpoint` | *(memory)* Short-term working notepad |
| `start_long_term_update` | *(memory)* Distill long-term memory |

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
