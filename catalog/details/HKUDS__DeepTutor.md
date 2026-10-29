# HKUDS/DeepTutor

DeepTutor: Lifelong Personalized Tutoring. https://deeptutor.info/.

## features

DeepTutor is an agent-native learning workspace that connects tutoring, problem solving, quiz generation, research, visualization, and mastery practice in one extensible system.

- **One runtime for every mode** — Chat, Ask Questions, Quiz, Research, Visualize, Solve, Mastery Path, Immersive Reading, and Audio Overview share one capability runtime and session context while keeping purpose-built loops and pipelines.
- **Task Board** — Track study tasks in To do, In progress, and Done, with notes, drag-and-drop or keyboard-accessible move buttons, and an archive you can restore from. Cards stay in the current workspace and follow the existing appearance and language settings; no model configuration is required.
- **Connected learning context** — Knowledge bases, books, Learning notebook pages, Favorites, question banks, personas, and Memory can be reused across the workflows that support them, subject to account grants and learning policies.
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
Help me install and configure the current dev version of DeepTutor from https://github.com/HKUDS/DeepTutor.
Clone the dev branch, or inspect and reuse my existing checkout. Start at
docs-for-dev/README.md, then read docs-for-dev/AGENT_SETUP.md and SKILL.md.
Follow the setup guide to prepare the environment,
configure my model provider, verify the setup, and start the Web app.
Ask me for any missing provider, model, or credential-source information;
do not print API keys. Preserve my existing files and settings, and finish
with the access URL and the results of your checks.
```

The [developer and agent handbook](docs-for-dev/README.md) is the documentation entry point for setup, architecture, extension development, testing, and troubleshooting. Its [Agent Setup guide](docs-for-dev/AGENT_SETUP.md) covers the full installation flow, including non-interactive CLI configuration. To install it yourself, choose one of the paths below.

DeepTutor ships four installation paths. They all share one runtime-home layout: private settings live in `data/user/settings/` under the directory you launch from (or under `DEEPTUTOR_HOME` / `deeptutor start --home` if you set one explicitly). See [Local Data Persistence](./docs-for-dev/DATA_STORAGE.md) for the complete storage layout, database support, and backup notes. For the full app, the recommended flow is **pick a runtime-home directory → install → `deeptutor init` → `deeptutor start`**.

### One-Command Docker Trial

If Docker is not installed 

## installation

python -m pip install -r requirements/full.txt
python -m pip install -e . --no-deps
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
python scripts/install_extras.py rag-lightrag    # Built-in LightRAG engine (exact supported SDK)
python scripts/install_extras.py graphrag        # Microsoft GraphRAG engine (Python 3.11–3.13)
python scripts/install_extras.py dev             # tests/lint tools
python scripts/install_extras.py partners        # Partner IM channel SDKs
python scripts/install_extras.py video-learning  # captions for reading/video-learning
python scripts/install_extras.py matrix          # Matrix channel without E2EE/libolm
python scripts/install_extras.py matrix-e2e      # Matrix E2EE; requires libolm
python scripts/install_extras.py math-animator   # Manim addon; requires LaTeX/ffmpeg/system libs
python scripts/install_extras.py edge-tts        # Optional free speech provider and video-lesson narration
```

**Video Lesson:** choose Video Lesson in chat or run `deeptutor run video_lesson "Explain a concept"`. The backend needs Node.js 22+ and npm. First use downloads pinned Remotion packages and a WebAssembly JavaScript interpreter; Docker is not required. Frame checks run inside the interpreter with no host filesystem, credentials, network or process APIs, under memory and execution limits. Cancellation stops the build process. Local and container deployments use the same execution path, with no unsandboxed fallback. The resulting lesson plays in the browser, with captions when optional narration is unavailable.

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

> See [CONTAINERIZATION.md](./docs-for-dev/CONTAINERIZATION.md) for podman/rootless/read-only-rootfs deployments and the full per-installation guide.

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
`./data/user/workspace`. Docker paths are selected at startup

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
