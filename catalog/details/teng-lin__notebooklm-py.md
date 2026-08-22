# teng-lin/notebooklm-py

Unofficial Python API and agentic skill for Google Gemini Notebook. Full programmatic access to NotebookLM's features—including capabilities the web UI doesn't expose—via Python, CLI, and AI agents li

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
