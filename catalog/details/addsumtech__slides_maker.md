# addsumtech/slides_maker

Turn papers, code, and docs into presentation-ready, natively editable PPTX in Codex / Claude Code. Native charts and equations, speaker notes, click-build animations, and an independent critic review

## installation

<p align="center">
  <img src="https://slides.addsum.top/docs/assets/quickstart_en.png" alt="Quick start: install once, start /slide-maker, it reads or researches, confirm the plan, build + critic review, get the pptx then tune">
</p>

### Step 1: Install

> **⚡ Don't want to install anything? Use the [slide-maker (addsum studio)](https://chatgpt.com/g/g-6a5b41f0a33881918be69e8b10f8b4ff-slide-maker-gpt) in ChatGPT** — it inherits this skill's
> ability, so you can make slides right in ChatGPT: open the link or find it in the **GPT Store**.
> Zero setup; the local install below stays the full-power path.
>
> **Prefer a marketplace? slide-maker is also published on
> [Tencent SkillHub](https://skillhub.cloud.tencent.com/skills/slides-maker),
> [Coze](https://xiaping.coze.com/skill/c0136d99-50d0-4f05-909a-f78fa4be7104), and
> [ClawHub](https://clawhub.ai/dong845/skills/slide-maker) — the last one installs straight into
> [OpenClaw](https://openclaw.ai), so OpenClaw users get slide-maker too** —
> grab it there by following each page's install instructions, then come back for the runtime
> dependencies below (they apply however you install).

slide-maker relies on three system tools: **Python 3.9+**, **LibreOffice** (renders slide previews for the automatic layout checks), and **one SVG rasterizer** for icons (librsvg, cairosvg, or any Chrome-family browser). Install them for your OS:

| OS | LibreOffice | Icon rasterizer |
| --- | --- | --- |
| macOS | `brew install --cask libreoffice` | `brew install librsvg` |
| Linux | `sudo apt install libreoffice` | `sudo apt install librsvg2-bin` |
| Windows | `winget install TheDocumentFoundation.LibreOffice` | Chrome or Edge installed (used headless) |

(Windows works too; we just test it less, so if you hit an environment quirk, run `check_env.py` below to self-diagnose or open an issue with the error.)

**With those system tools in place, install slide-maker itself.** The four lines below clone the repo, install its Python packages, and register it as a skill:

```bash
git clone --depth 1 https://github.com/addsumtech/slides_maker.git
cd slides_maker
python3 -m pip install -r skills/slide-maker/requirements.txt
python3 skills/slide-maker/scripts/install_skill.py --target both
```

If you only use one tool, replace `both` with `codex` or `claude`. Not sure what's missing? The [check command](#troubleshooting) prints the exact fix.

**Prefer a one-liner? Install just the skill with [`npx skills`](https://github.com/vercel-labs/skills)** (no clone, about 1.1 MB):

```bash
npx skills add addsumtech/slides_maker
```

It prompts for the agent and scope. The skill lives under `skills/slide-maker/` and the repo carries no heavy assets (the gallery and demo site live in [slides_maker-site](https://github.com/addsumtech/slides_maker-site)), so the install stays small and fast. Add `-g` to install globally (all projects), `-a claude-code` (or `-a codex`) to skip the agent prompt, and `-y` for a fully non-interactive run. You still need the runtime dependencies above: LibreOffice, an SVG rasterizer, and `python3 -m pip install -r skills/slide-maker/requirements.txt`.

**On Claude Code, you can also add it as a plugin** so it stays updated with a normal plugin command:

```text
/plugin marketplace add addsumtech/slides_maker
/plugin install slide-maker@slides-maker
```

This is the same skill, just managed by Claude Code's plugin system instead of copied into your skills folder. The runtime dependencies above still apply.

### Keeping it up to date

slide-maker checks before it asks you anything, and **stays completely silent when you are current**. When a newer version exists it does not update itself and does not just mention it — it asks, once, at the top:

- **yes** — it updates for you, then builds the whole deck on the new version. You don't need to know how you installed it: it works that out and runs the right command itself.
- **no** — don't update; build on the version you already have ins
