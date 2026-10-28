# HKUDS/DeepTutor

DeepTutor: Lifelong Personalized Tutoring. https://deeptutor.info/.

## features

DeepTutor is an agent-native learning workspace that connects tutoring, problem solving, quiz generation, research, visualization, and mastery practice in one extensible system.

- **One runtime for every mode** — Chat, Ask Questions, Quiz, Research, Visualize, Solve, Course Study, Mastery Path, Immersive Reading, and Audio Overview share one capability runtime and session context while keeping purpose-built loops and pipelines.
- **Task Board** — Track study tasks in To do, In progress, and Done, with notes, drag-and-drop or keyboard-accessible move buttons, and an archive you can restore from. Cards stay in the current workspace and follow the existing appearance and language settings; no model configuration is required.
- **Connected learning context** — Knowledge bases, books, Co-Writer drafts, notebooks, question banks, personas, and Memory can be reused across the workflows that support them, subject to account grants and learning policies.
- **Immersive video learning** — add YouTube or Bilibili links to Reading for native playback, transcript search, timestamp-grounded tutoring, saved notes, and resumable progress; YouTube captions and browsing can use an administrator-configured Invidious instance.
- **Subagents and Partners** — from Chat, consult a live agent harness (Claude Code, Codex, Grok CLI, Antigravity, Kimi, opencode, MiMo, Hermes, OpenClaw, or DeepSeek) or a Partner, import past conversations, and run persistent IM companions on the same brain.
- **Multi-engine knowledge** — versioned RAG libraries across LlamaIndex, PageIndex, GraphRAG, LightRAG, a remote LightRAG Server, a self-hosted WeKnora knowledge base, a Tencent IMA or MarginNote 4 library, a connected Kiwix ZIM archive, or a linked Obsidian vault, with pluggable document parsing. See [native LightRAG role models](deeptutor/services/rag/pipelines/lightrag/README.md) for independent extraction, query and vision settings, default-only creation and confirmed rebuilds.
- **Extensible tools and skills** — built-in tools, MCP servers, CLI apps, image / video / voice generation models, and installable community skills from EduHub.
- **Inspectable memory** — L1 traces, L2 surface summaries, and L3 synthesis make personalization visible and editable; the Memory Graph links L2 facts to L1 evidence and L3 synthesis to contributing surfaces.

---

## 🚀 Get Started

### Let Your Agent Set Up DeepTutor

Copy this prompt into your terminal-capable AI agent (such as Codex or Claude Code):

```text
Help me install and configure DeepTutor locally from https://github.com/HKUDS/DeepTutor.
Clone the repository, or reuse my existing checkout, and read SKILL.md and
docs-for-user/AGENT_SETUP.md first. Follow that guide to prepare the environment,
configure my model provider, verify the setup, and start the Web app.
Ask me for any missing provider, model, or credential-source information;
do not print API keys. Preserve my existing files and settings, and finish
with the access URL and the results of your checks.
```

The [Agent Setup guide](docs-for-user/AGENT_SETUP.md) covers the full flow, including non-interactive CLI configuration. To install it yourself, choose one of the paths below.

DeepTutor ships four installation paths. They all share one runtime-home layout: private settings live in `data/user/settings/` under the directory you launch from (or under `DEEPTUTOR_HOME` / `deeptutor start --home` if you set one explicitly). For the full app, the recommended flow is **pick a runtime-home directory → install → `deeptutor init` → `deeptutor start`**.

### One-Command Docker Trial

If Docker is not installed yet, [install Docker](https://docs.docker.com/get-docker/) first. Then try the full app without setting up Python or Node.js:

```bash
docker run --rm --name deeptutor \
  -p 127.0.0.1:3782:3782 \
  -v deeptutor-data:/app/data \
  ghcr.io/hkuds/deeptutor:latest
```

Open [http://127.0.0.1:3782](http://127.0.0.1:3782), configure model providers in **Settings → Provid

## installation

python -m pip install -e .
( cd web && npm ci --legacy-peer-deps )

deeptutor init
deeptutor start --dev
```

`deeptutor start` builds the local `web/` frontend for production once and reuses it; `--dev` runs Next.js with HMR. Config layout, ports, and `Ctrl+C` match Option 1.

<details>
<summary><b>Conda environment</b> (instead of <code>venv</code>)</summary>

```bash
conda create -n deeptutor python=3.11
conda activate deeptutor
python -m pip install --upgrade pip
```

</details>

<details>
<summary><b>Optional install extras</b> — RAG engines / dev / partners / matrix / math-animator</summary>

```bash
pip install -e ".[rag-lightrag]"    # Built-in LightRAG engine (exact supported SDK)
pip install -e ".[graphrag]"        # Microsoft GraphRAG engine (Python 3.11–3.13)
pip install -e ".[dev]"             # tests/lint tools
pip install -e ".[partners]"        # Partner IM channel SDKs
pip install -e ".[video-learning]"  # compatibility extra; captions ship in the full/CLI installs
pip install -e ".[matrix]"          # Matrix channel without E2EE/libolm
pip install -e ".[matrix-e2e]"      # Matrix E2EE; requires libolm
pip install -e ".[math-animator]"   # Manim addon; requires LaTeX/ffmpeg/system libs
```

</details>

<details>
<summary><b>Frontend dependency tweaks & dev-server troubleshooting</b></summary>

**Changing frontend dependencies:** run `npm install --legacy-peer-deps` to refresh `web/package-lock.json`, then commit both `web/package.json` and `web/package-lock.json`.

**Stuck dev server:** if `deeptutor start --dev` reports an existing frontend that isn't responding, stop the PID it prints. If no Next.js process is actually running, the lock files are stale — remove them and retry:

```bash
rm -f web/.next/dev/lock web/.next/lock
deeptutor start --dev
```

</details>

</details>

<details>
<summary><b>Option 3 — Docker</b> · one self-contained container</summary>

One container for the full Web app. Images on GitHub Container Registry:

- `ghcr.io/hkuds/deeptutor:latest` — latest stable release
- `ghcr.io/hkuds/deeptutor:<version>` — exact release without the leading `v` (for example `:1.6.3`); pre-releases receive only their version tag

> See [CONTAINERIZATION.md](./docs-for-user/CONTAINERIZATION.md) for podman/rootless/read-only-rootfs deployments and the full per-installation guide.

```bash
docker run --rm --name deeptutor \
  -p 127.0.0.1:3782:3782 \
  -v deeptutor-data:/app/data \
  ghcr.io/hkuds/deeptutor:latest
```

To choose a host content folder at container startup, mount it at the stable
container path and lock DeepTutor to that path:

```bash
mkdir -p "$PWD/deeptutor-workspace/outputs"
docker run --rm --name deeptutor \
  -p 127.0.0.1:3782:3782 \
  -v deeptutor-data:/app/data \
  -v "$PWD/deeptutor-workspace:/workspace" \
  -e DEEPTUTOR_WORKSPACE_ROOT=/workspace \
  -e DEEPTUTOR_WORKSPACE_ALLOWED_ROOTS=/workspace \
  ghcr.io/hkuds/deeptutor:latest
```

For Compose, set `DEEPTUTOR_WORKSPACE_HOST=/absolute/host/folder` before
running `python scripts/docker_compose.py up -d`. When omitted it uses
`./data/user/workspace`. Docker paths are selected at startup and therefore
appear locked in the Web settings page.

> **Only `3782` needs to be published.** The browser talks exclusively to the frontend origin; the Next.js middleware (`web/proxy.ts`) forwards `/api/*` and `/ws/*` to the FastAPI backend **inside the container**. Publishing `8001` (`-p 127.0.0.1:8001:8001`) is optional — handy only for hitting the API directly with curl or scripts.

Open [http://127.0.0.1:3782](http://127.0.0.1:3782). The container creates `/app/data/user/settings/*.json` on first boot; configure model providers from the Web Settings page. Config, API keys, logs, the default Content Workspace, memory, and knowledge bases persist in the `deeptutor-data` volume. A separately mounted Content Workspace persists at its host path instead. Optional extras belong on the deployment, not in a shell: set `DEEPTUTOR_EXTRAS` (and `DEEPTUTOR

## limitations

We want DeepTutor to keep iterating and improving — and ultimately to become a gift we give back to the open-source community. Our [**roadmap**](https://github.com/HKUDS/DeepTutor/issues/498) is updated continuously; vote on items there or propose new ones. If you'd like to contribute, see the [**Contributing Guide**](CONTRIBUTING.md) for branching strategy, coding standards, and how to get started.

<div align="center">

We hope DeepTutor becomes a gift for the community. 🎁

<a href="https://github.com/HKUDS/DeepTutor/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=HKUDS/DeepTutor&max=999" alt="Contributors" />
</a>

</div>

<p align="center">
 <a href="https://www.star-history.com/hkuds/deeptutor">
  <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/badge?repo=HKUDS/DeepTutor&theme=dark" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/badge?repo=HKUDS/DeepTutor" />
   <img alt="Star History Rank" src="https://api.star-history.com/badge?repo=HKUDS/DeepTutor" />
  </picture>
 </a>
</p>

<div align="center">

Licensed under the [Apache License 2.0](LICENSE).

<p>
  <img src="https://visitor-badge.laobi.icu/badge?page_id=HKUDS.DeepTutor&style=for-the-badge&color=00d4ff" alt="Views">
</p>

</div>

### Mastery turn grounding

Mastery turns read the active path's status before the first model request, using
the same status tool and mastery gates as an explicit tool call. This snapshot is
fresh for each turn, includes the active session mode, and is never cached across
turns. A failed read falls back to `mastery_status`; after changing the path, mode,
outline, or progress, the tutor can refresh through that tool. Card grading and
its existing handoff remain unchanged.

### Repeated image attachments

The agent loop sends identical inline user images once per request and replaces later
copies with references to the retained image. Stable request-only labels identify
the retained inline images across provider translations and appended turns. Unique
image blocks, remote URLs, differing
image options, assistant messages, and tool results remain complete. Saved history
keeps every original attachment; references are rebuilt after history is trimmed.
This reduces repeated image payloads, but provider-reported usage remains the
source of truth for billing and cache hits.
