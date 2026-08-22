# yusufkaraaslan/Skill_Seekers

Convert documentation websites, GitHub repositories, and PDFs into Claude AI skills with automatic conflict detection

## installation

```bash
# 1. Install
pip install skill-seekers

# 2. Create a skill from any source
skill-seekers create https://docs.djangoproject.com/

# 3. Package it for your AI platform
skill-seekers package output/django --target claude
```

You now have `output/django-claude.zip`, ready to use.

```bash
# Pick a different AI agent for enhancement (default: claude)
skill-seekers create https://docs.djangoproject.com/ --agent kimi
skill-seekers create https://docs.djangoproject.com/ --agent-cmd "my-custom-agent run"
```

### 🛰️ AI-driven project scan

Point `scan` at a project and an AI agent reads its manifests, README, Dockerfile/CI and sampled source imports — then emits one config per detected framework, plus a `<project>-codebase.json` for your own code:

```bash
skill-seekers scan ./my-react-app --out ./configs/scanned/
# → react.json, vite.json, tailwind.json, jest.json, my-react-app-codebase.json

skill-seekers create ./configs/scanned/react.json
```

If a detection has no existing preset, the AI generates a fresh config; on exit you can optionally publish it back to the [community registry](https://github.com/yusufkaraaslan/skill-seekers-configs).

### All 18 source types

```bash
skill-seekers create facebook/react            # GitHub repository
skill-seekers create ./my-project              # Local codebase
skill-seekers create manual.pdf                # PDF
skill-seekers create report.docx               # Word
skill-seekers create book.epub                 # EPUB
skill-seekers create notebook.ipynb            # Jupyter
skill-seekers create openapi.yaml              # OpenAPI/Swagger
skill-seekers create presentation.pptx         # PowerPoint
skill-seekers create guide.adoc                # AsciiDoc
skill-seekers create page.html                 # Local HTML (or a whole dir)
skill-seekers create feed.rss                  # RSS/Atom
skill-seekers create curl.1                    # Man page

# Video (YouTube, Vimeo, or local — needs skill-seekers[video])
skill-seekers create --video-url https://www.youtube.com/watch?v=... --name mytutorial
skill-seekers create --setup                   # auto-install GPU-aware visual deps

skill-seekers create --space-key TEAM --name wiki               # Confluence
skill-seekers create --database-id ... --name docs              # Notion
skill-seekers create --chat-export-path ./slack-export --name team-chat  # Slack/Discord
```

See the [Scraping Guide](docs/user-guide/02-scraping.md) for every source type and its options.

---

## 📦 Installation

```bash
pip install skill-seekers              # Core: scraping, GitHub, PDF, packaging
pip install skill-seekers[all-llms]    # + every LLM platform
pip install skill-seekers[mcp]         # + MCP server
pip install skill-seekers[all]         # Everything
```

**Not sure what you need?** Run the wizard: `skill-seekers-setup`

<details>
<summary><b>All installation extras</b></summary>

| Install | Adds |
|---------|------|
| `skill-seekers[gemini]` | Google Gemini support |
| `skill-seekers[openai]` | OpenAI ChatGPT support |
| `skill-seekers[all-llms]` | All LLM platforms |
| `skill-seekers[mcp]` | MCP server for Claude Code, Cursor, etc. |
| `skill-seekers[video]` | YouTube/Vimeo transcript & metadata extraction |
| `skill-seekers[video-full]` | + Whisper transcription & visual frame extraction |
| `skill-seekers[jupyter]` | Jupyter Notebook support |
| `skill-seekers[pptx]` | PowerPoint support |
| `skill-seekers[confluence]` | Confluence wiki support |
| `skill-seekers[notion]` | Notion pages support |
| `skill-seekers[rss]` | RSS/Atom feed support |
| `skill-seekers[chat]` | Slack/Discord chat export support |
| `skill-seekers[asciidoc]` | AsciiDoc support |
| `skill-seekers[all]` | Everything |

> **Video visual deps (GPU-aware):** after installing `skill-seekers[video-full]`, run `skill-seekers create --setup` to auto-detect your GPU and install the matching PyTorch variant + easyocr.

</details>

**Prerequisites:** Python 3.10+, Git. New here?

## features

- ⚡ **99% faster** — days of manual data prep → 15–45 minutes
- 🎯 **Real skill quality** — 500+ line `SKILL.md` files with examples, patterns, and guides
- 📊 **RAG-ready chunks** — smart chunking preserves code blocks and context
- 🔄 **Multi-source** — combine docs + GitHub + PDFs + videos into one knowledge asset
- 🌐 **One prep, every target** — export to 22 targets without re-scraping
- ✅ **Battle-tested** — 3,900+ tests, 68 workflow presets, production-ready

---

## ✨ Key capabilities

<details>
<summary><b>Documentation scraping</b> — SPA discovery, llms.txt, smart categorization</summary>

Three-layer discovery for JavaScript SPA sites (`sitemap.xml` → `llms.txt` → headless browser rendering), automatic `llms.txt` detection (10× faster when present), smart topic categorization, and a lenient HTML parser fallback so broken markup still scrapes.

→ [Scraping Guide](docs/user-guide/02-scraping.md) · [llms.txt Support](docs/reference/LLMS_TXT_SUPPORT.md)
</details>

<details>
<summary><b>GitHub & codebase analysis (C3.x)</b> — AST parsing, pattern detection, how-to guides</summary>

Three-stream architecture: code analysis (AST, design patterns, tests), documentation (README, `docs/`, wiki), and community (issues, PRs, metadata). The C3.x pipeline adds 10 GoF pattern detectors across 9 languages, usage examples extracted from tests, AI-written how-to guides, config extraction, and architecture overviews.

```bash
skill-seekers create ./my-project --preset quick          # 1–2 min, surface level
skill-seekers create ./my-project --preset standard       # balanced (default)
skill-seekers create ./my-project --preset comprehensive  # deep, exhaustive
```

→ [Pattern Detection](docs/features/PATTERN_DETECTION.md) · [How-To Guides](docs/features/HOW_TO_GUIDES.md) · [Test Example Extraction](docs/features/TEST_EXAMPLE_EXTRACTION.md)
</details>

<details>
<summary><b>AI enhancement</b> — API or local agents, 68 workflow presets</summary>

Every AI call runs through one transport, in **API mode** (Anthropic, Google Gemini, OpenAI, Moonshot/Kimi, MiniMax) or **LOCAL mode** (Claude Code, Kimi Code, Codex, Copilot, OpenCode, custom agents — no API costs). Control depth with `--enhance-level 0-3` and pick an agent with `--agent`.

→ [Enhancement Guide](docs/user-guide/03-enhancement.md) · [Enhancement Modes](docs/features/ENHANCEMENT_MODES.md) · [Multi-Agent Setup](docs/guides/MULTI_AGENT_SETUP.md)
</details>

<details>
<summary><b>Unified multi-source scraping</b> — combine many sources into one skill</summary>

One config can pull documentation, GitHub, PDFs, videos, and more into a single knowledge asset, with conflict detection and pairwise synthesis across sources.

→ [Unified Scraping](docs/features/UNIFIED_SCRAPING.md)
</details>

<details>
<summary><b>Video extraction</b> — transcripts, frames, on-screen code</summary>

YouTube, Vimeo, and local files. Three-tier transcript fallback (subtitles → YouTube transcript API → local Whisper), plus optional visual extraction that OCRs on-screen code from sampled frames.

→ [Video Guide](docs/VIDEO_GUIDE.md)
</details>

<details>
<summary><b>Quality, sync & scale</b></summary>

Quality scoring with a gate (`skill-seekers quality output/react/ --threshold 7`), provisional English readability metrics (informational — they never affect the score), doc-change detection with scheduled re-scrapes and notifications, streaming ingestion for very large doc sets, and incremental updates.

→ [Large Documentation](docs/reference/LARGE_DOCUMENTATION.md) · [Code Quality](docs/reference/CODE_QUALITY.md)
</details>

---

## tools

Skill Seekers ships an MCP server for Claude Code, Cursor, Windsurf, VS Code + Cline, and IntelliJ IDEA.

```bash
# stdio mode (Claude Code, VS Code + Cline)
python -m skill_seekers.mcp.server_fastmcp

# HTTP mode (Cursor, Windsurf, IntelliJ)
python -m skill_seekers.mcp.server_fastmcp --transport http --port 8765
```

Then just ask your assistant: *"Package and upload the React skill."*

→ [MCP Setup](docs/guides/MCP_SETUP.md) · [MCP Reference](docs/reference/MCP_REFERENCE.md) · [HTTP Transport](docs/guides/HTTP_TRANSPORT.md)

---
