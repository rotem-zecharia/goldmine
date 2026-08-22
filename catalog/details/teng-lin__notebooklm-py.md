# teng-lin/notebooklm-py

Unofficial Python API and agentic skill for Google Gemini Notebook. Full programmatic access to NotebookLM's features—including capabilities the web UI doesn't expose—via Python, CLI, and AI agents li

## features

### Complete NotebookLM Coverage

| Category | Capabilities |
|----------|--------------|
| **Notebooks** | Create, list, rename, delete |
| **Sources** | URLs, YouTube, files (PDF, text, Markdown, Word, EPUB, audio, video, images), Google Drive, pasted text; refresh, get guide/fulltext |
| **Chat** | Questions, conversation history, custom personas, suggested starter prompts |
| **Notes** | Create, list, rename, delete, save chat answers, save conversation history |
| **Source Labels** | AI-generated or manual topic labels; add/remove source membership; filter sources by label |
| **Research** | Web and Drive research agents (fast/deep modes) with auto-import |
| **Sharing** | Public/private links, user permissions (viewer/editor), view level control |

### Content Generation (All Artifact Types)

| Type | Options | Download Format |
|------|---------|-----------------|
| **Audio Overview** | 4 formats (deep-dive, brief, critique, debate), 3 lengths, 50+ languages | MP3 |
| **Video Overview** | 4 formats (explainer, brief, cinematic, short), 8 visual styles (+ auto/custom), plus a dedicated `cinematic-video` CLI alias | MP4 |
| **Slide Deck** | Detailed or presenter format, adjustable length; individual slide revision | PDF, PPTX |
| **Infographic** | 3 orientations, 3 detail levels | PNG |
| **Quiz** | Configurable quantity and difficulty | JSON, Markdown, HTML |
| **Flashcards** | Configurable quantity and difficulty | JSON, Markdown, HTML |
| **Report** | Briefing doc, study guide, blog post, or custom prompt | Markdown |
| **Data Table** | Custom structure via natural language | CSV |
| **Mind Map** | Hierarchical node tree — **two kinds**: note-backed JSON or the newer interactive studio map (`--kind` / `MindMapKind`) | JSON |

### Beyond the Web UI

Programmatic, batch, and local-file capabilities the API/CLI make easy — several in richer formats, or at a scale, than clicking through the web app:

- **Batch downloads** - Download all artifacts of a type at once
- **Quiz/Flashcard export** - Get structured JSON, Markdown, or HTML files
- **Mind map data extraction** - Export hierarchical JSON for visualization tools
- **Data table CSV export** - Download structured tables as spreadsheets
- **Slide deck as PPTX or PDF** - Download editable PowerPoint or PDF files
- **Slide revision** - Modify individual slides with natural-language prompts
- **Report template customization** - Append extra instructions to built-in format templates
- **Save chat history to notes** - Persist a whole Q&A conversation (not just a single answer) as a notebook note
- **Source fulltext access** - Retrieve the indexed text content of any source
- **Programmatic sharing** - Manage permissions without the UI

## installation

The full install guide — six personas (agent, end-user, library, headless, contributor, power-user), optional extras matrix, platform notes — lives in **[docs/installation.md](docs/installation.md)**.

**Quickest start** (CLI users and AI agents) — install the CLI with `uv tool` (recommended) or `pipx`:

```bash
uv tool install "notebooklm-py[browser]"   # or: pipx install "notebooklm-py[browser]"
notebooklm login                           # first run auto-downloads Chromium (~170 MB), then Google sign-in
notebooklm auth check --test --json        # verify: expect "status": "ok"
```

**Why `uv tool` / `pipx`?** They install the CLI into its own isolated environment and put `notebooklm` on your `PATH` — no dependency clashes with other tools, a one-line upgrade (`uv tool upgrade notebooklm-py`) or uninstall, and, crucially, they work on modern macOS (Homebrew Python) and Debian/Ubuntu where a system-wide `pip install` is blocked with `error: externally-managed-environment` ([PEP 668](https://peps.python.org/pep-0668/)). No `uv` yet? `curl -LsSf https://astral.sh/uv/install.sh | sh` (or `brew install uv` / `winget install astral-sh.uv`).

**Prefer plain `pip`?** It works the same **inside a virtualenv** (and directly on Windows, where Python isn't externally-managed):

```bash
python3 -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install "notebooklm-py[browser]"
```

**As a library** (embedded in your app — no Playwright, no Chromium):

```bash
uv add notebooklm-py                    # or, inside a virtualenv: pip install notebooklm-py
```

If `playwright install chromium` fails on Linux with `TypeError: onExit is not a function`, see the [Linux workaround](docs/troubleshooting.md#linux). **Contributors:** see [CONTRIBUTING.md](CONTRIBUTING.md).


### Authentication & Access

Flexible auth for local dev, headless servers, and multi-tenant setups:

- **Three ways to get cookies** - Interactive Playwright login (default), import from an already-signed-in browser (`login --browser-cookies chrome`, no Playwright), or a durable **master token**.
- **Master-token auth** - Mints fresh web cookies **on demand** with no per-session browser (`login --master-token --account you@example.com`), so it self-heals expired sessions unattended — the auth model for servers, CI, and the remote MCP connector (claude.ai / ChatGPT).
- **Multi-account profiles** - Switch between Google accounts without re-authenticating.

### Agent Setup

**Option 1 — CLI install**:

```bash
notebooklm skill install
```

Installs the skill into `~/.claude/skills/notebooklm` and `~/.agents/skills/notebooklm`.

**Option 2 — `npx` install** (via the open skills ecosystem):

```bash
npx skills add teng-lin/notebooklm-py
```

Fetches the canonical [SKILL.md](SKILL.md) directly from GitHub.

## Quick Start

<p align="center">
  <a href="https://asciinema.org/a/767284" target="_blank"><img src="https://asciinema.org/a/767284.svg" width="600" /></a>
  <br>
  <em>16-minute session compressed to 30 seconds</em>
</p>

### CLI

```bash
# 1. Authenticate (opens browser)
notebooklm login
# Or use Microsoft Edge (for orgs that require Edge for SSO)
# notebooklm login --browser msedge
# Or reuse cookies from an already-logged-in browser session
# notebooklm login --browser-cookies chrome
# notebooklm login --browser-cookies 'chrome::Profile 1'  # one Chromium profile
# (combine with --profile to populate a specific profile;
#  use --account / --all-accounts after auth inspect when several
#  Google accounts are signed in)

# 2. Create a notebook and add sources
notebooklm create "My Research"
notebooklm use <notebook_id>
notebooklm source add "https://en.wikipedia.org/wiki/Artificial_intelligence"
notebooklm source add "./paper.pdf"

# 3. Chat with your sources
notebooklm ask "What are the key themes?"
notebooklm ask --prompt-file ./long_question.txt  # Read question from file

# 4. Generate content (use --prompt-file for long prompts)
notebooklm g

## tools

```python
import asyncio
from notebooklm import NotebookLMClient, MindMapKind


async def main():
    async with NotebookLMClient.from_storage() as client:
        # Create notebook and add sources
        nb = await client.notebooks.create("Research")
        await client.sources.add_url(nb.id, "https://example.com", wait=True)

        # Chat with your sources
        result = await client.chat.ask(nb.id, "Summarize this")
        print(result.answer)

        # Generate content (podcast, video, quiz, etc.)
        status = await client.artifacts.generate_audio(nb.id, instructions="make it fun")
        await client.artifacts.wait_for_completion(nb.id, status.task_id)
        await client.artifacts.download_audio(nb.id, "podcast.m4a")

        # Generate quiz and download as JSON
        status = await client.artifacts.generate_quiz(nb.id)
        await client.artifacts.wait_for_completion(nb.id, status.task_id)
        await client.artifacts.download_quiz(nb.id, "quiz.json", output_format="json")

        # Generate a mind map via the unified client.mind_maps API (issue #1256) —
        # two kinds: the newer MindMapKind.INTERACTIVE studio map (shown; polled to
        # completion by default) or MindMapKind.NOTE_BACKED JSON. Both export via:
        mm = await client.mind_maps.generate(nb.id, kind=MindMapKind.INTERACTIVE)
        await client.artifacts.download_mind_map(nb.id, "mindmap.json", mm.id)


asyncio.run(main())
```

## Documentation

- **[CLI Reference](docs/cli-reference.md)** - Complete command documentation
- **[Python API](docs/python-api.md)** - Full API reference
- **[MCP Guide](docs/mcp-guide.md)** - MCP server setup, transports, and tool reference
- **[REST API Server](docs/installation.md#rest-api-server)** - Experimental localhost FastAPI server
- **[Configuration](docs/configuration.md)** - Storage and settings
- **[Quota & Tier Limits](docs/quota-limits.md)** - Per-tier notebook/source/studio limits and how they map to `AccountLimits.tier`
- **[Release Guide](docs/releasing.md)** - Release checklist and packaging verification
- **[Troubleshooting](docs/troubleshooting.md)** - Common issues and solutions
- **[API Stability](docs/stability.md)** - Versioning policy and stability guarantees
- **[Upgrading to v0.8.0](docs/upgrading-to-0.8.0.md)** - Breaking-change migration guide for the v0.8.0 error-and-return contract

### For Contributors

- **[Architecture](docs/architecture.md)** - Architectural overview and design principles
- **[Development Guide](docs/development.md)** - Architecture, testing, and releasing
- **[RPC Development](docs/rpc-development.md)** - Protocol capture and debugging
- **[RPC Reference](docs/rpc-reference.md)** - Payload structures
- **[Changelog](CHANGELOG.md)** - Version history and release notes
- **[Security](SECURITY.md)** - Security policy and credential handling

## License

MIT License. See [LICENSE](LICENSE) for details.
