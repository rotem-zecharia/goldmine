# wanshuiyin/Auto-claude-code-research-in-sleep

ARIS ⚔️ (Auto-Research-In-Sleep) — Lightweight Markdown-only skills for autonomous ML research: cross-model review loops, idea discovery, and experiment automation. No framework, no lock-in — works wi

## installation

```bash

## features

ARIS chains **82 composable skills** across the whole research lifecycle — literature & novelty → idea discovery → GPU experiments → autonomous review loop → paper writing → peer review — with **cross-model adversarial review** (Claude executes · GPT-5.6-Sol xhigh reviews · optional **GPT-5.5 Pro** via Oracle), anti-hallucination DBLP/CrossRef citations, a persistent **Research Wiki**, flexible model backends, human-in-the-loop checkpoints, and optional Feishu / Zotero / Obsidian / GPU integrations.

🔥 *And it scales to any agent's **ultracode-style deep mode** — the breadth/firepower pass adapts to the runtime (Claude Code ultracode + workflows on Opus 4.8, Codex `spawn_agent`, or plain sequential), feeding three roles: **breadth · cross-model review → accuracy · research wiki → memory**. However a loop is driven, it reports to the same cross-model jury + research wiki — **it can drive, never acquit**.*

<details>
<summary><b>Full feature list</b></summary>

- 📊 **82 composable skills** — mix and match, or chain into full pipelines (`/idea-discovery`, `/auto-review-loop`, `/paper-writing`, `/research-pipeline`). See [full catalog →](docs/SKILLS_CATALOG.md)
- 🔍 **Literature & novelty** — multi-source paper search (**[Zotero](docs/integrations/ZOTERO.md)** + **[Obsidian](docs/integrations/OBSIDIAN.md)** + **local PDFs** + arXiv/Scholar) + cross-model novelty verification
- 💡 **Idea discovery** — literature survey → brainstorm 8-12 ideas → novelty check → GPU pilot experiments → ranked report
- 🔄 **Auto review loop** — 4-round autonomous review, 5/10 → 7.5/10 overnight with 20+ GPU experiments
- 📝 **Paper writing** — narrative → outline → figures → LaTeX → PDF → auto-review (4/10 → 8.5/10), one command. Anti-hallucination citations via [DBLP](https://dblp.org)/[CrossRef](https://www.crossref.org)
- 🤖 **Cross-model collaboration** — Claude Code executes and GPT-5.6-Sol reviews; in Copilot CLI, `/auto-review-loop` uses the native complementary rubber-duck model and verifies the actual cross-family pair from host events. Optional: `— reviewer: oracle-pro` → **GPT-5.5 Pro** via [Oracle](https://github.com/steipete/oracle)
- 📝 **Peer review** — review others' papers as a conference reviewer, with structured scoring and meta-review
- 🖥️ **Review-driven experiments** — when GPT-5.6-Sol says "run an ablation", Claude auto-writes the script, rsyncs to GPU, runs in `screen`, collects results, folds back into the paper. Configure server in `CLAUDE.md` ([setup](#gpu-server-setup)), or rent from [Vast.ai](https://vast.ai) with `gpu: vast`
- 🔀 **Flexible models** — default Claude × GPT-5.6-Sol, also supports [GLM, MiniMax, Kimi, LongCat, DeepSeek, etc.](#alternative-model-combinations) — no Claude or OpenAI API required
- 🛑 **Human-in-the-loop** — configurable selection checkpoints. `AUTO_PROCEED=true` reports the choice and continues in the same turn; `false` asks for approval. Explicit Feishu interactive gates remain user-controlled
- 📱 **[Feishu/Lark notifications](docs/integrations/FEISHU.md)** — three modes: **off (default, recommended)**, push-only (webhook → mobile), interactive (approve/reject in Feishu). Zero impact when off

  <details>
  <summary>Preview: Push cards (group) &amp; Interactive chat (private)</summary>

  **Push Only** — group chat cards (experiment done, checkpoint, error, pipeline complete):

  <img src="assets/feishu_push.png" width="700" />

  **Interactive** — private chat with Claude Code (approve/reject, custom instructions):

  <img src="assets/feishu_interactive.jpg" width="700" />

  </details>

- 📚 **[Research Wiki](#-research-wiki--persistent-research-memory)** — persistent knowledge base across papers/ideas/experiments/claims. Failed ideas become anti-repetition memory — ARIS gets smarter every run. Inspired by [Karpathy's LLM Wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)
- 🧩 **Extensible** — domain-specific skills welcome! Add a `SKILL.md` and open a PR. See [community skills](

## requirements

1. [Claude Code](https://docs.anthropic.com/en/docs/claude-code) installed
2. (For review skills) [Codex CLI](https://github.com/openai/codex) installed and configured as MCP server:
   ```bash
   npm install -g @openai/codex
   claude mcp add codex -s user -- codex mcp-server
   ```
3. (For Workflow 3: paper writing) **LaTeX** environment with `latexmk` and `pdfinfo`:
   ```bash
   # macOS
   brew install --cask mactex    # or: brew install basictex
   brew install poppler          # provides pdfinfo

   # Ubuntu/Debian
   sudo apt install texlive-full latexmk poppler-utils

   # Verify
   latexmk --version && pdfinfo -v
   ```
   > **Windows (PowerShell):** Install a TeX distribution using the [MiKTeX Basic Installer](https://miktex.org/howto/install-miktex) or [TeX Live for Windows](https://tug.org/texlive/windows.html). Install [Poppler for Windows](https://github.com/oschwartz10612/poppler-windows/releases) separately, add the directory containing `pdfinfo.exe` to `PATH`, and open a new PowerShell window. Then verify:
   > ```powershell
   > latexmk --version
   > pdfinfo -v
   > ```
   > If either command is not found, refresh the TeX distribution's package/path settings and check that the Poppler directory containing `pdfinfo.exe` is on `PATH`.
   > If you only need Workflow 1 & 2 (idea discovery + auto review), LaTeX is not required.

<a id="install-skills"></a>

## tools

```

> Global install increases the risk of skill name collisions with other globally-installed packs. Use only if you don't mix ARIS with Superpowers / OpenHands / etc. — otherwise prefer the project-local install above.

</details>

> 💡 **New Claude Code versions** may not auto-create `~/.claude/skills/`. If using global install, create it first: `mkdir -p ~/.claude/skills/`. The symlink installer handles directory creation automatically.

<a id="optional-codex-plugin-for-code-review"></a>

<details>
<summary><b>Optional: Codex Plugin for Code Review</b></summary>

[codex-plugin-cc](https://github.com/openai/codex-plugin-cc) provides additional Codex capabilities that ARIS auto-detects when installed:

```bash
