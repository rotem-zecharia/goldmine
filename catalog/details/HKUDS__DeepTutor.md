# HKUDS/DeepTutor

DeepTutor: Lifelong Personalized Tutoring. https://deeptutor.info/.

## features

DeepTutor is an agent-native learning workspace that connects tutoring, problem solving, quiz generation, research, visualization, and mastery practice in one extensible system.

- **One runtime for every mode** — Chat, Quiz, Research, Visualize, Solve, Mastery Path, and Immersive Reading run on the same agent loop, so you switch the objective, not the engine, and context moves with the learner.
- **Connected learning context** — Knowledge bases, books, Co-Writer drafts, notebooks, question banks, personas, and Memory stay available across every workflow instead of living in isolated tools.
- **Subagents and Partners** — consult a live coding CLI (Claude Code, Codex, Gemini, Kimi, opencode, or MiMo) or a Partner from any turn (or import their past conversations), and run persistent IM companions on the same brain.
- **Multi-engine knowledge** — versioned RAG libraries across LlamaIndex, PageIndex, GraphRAG, LightRAG, a remote LightRAG Server, a Tencent IMA or MarginNote 4 library, or a linked Obsidian vault, with pluggable document parsing.
- **Extensible tools and skills** — built-in tools, MCP servers, CLI apps, image / video / voice generation models, and installable community skills from EduHub.
- **Inspectable memory** — L1 traces, L2 surface summaries, and L3 synthesis make personalization visible and editable, with a Memory Graph that traces every claim back to its evidence.

---

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
<summary><b>Optional install extras</b> — dev / partners / matrix / math-animator</summary>

```bash
pip install -e ".[dev]"             # tests/lint tools
pip install -e ".[partners]"        # Partner IM channel SDKs + MCP client
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

- `ghcr.io/hkuds/deeptutor:latest` — stable release
- `ghcr.io/hkuds/deeptutor:pre` — pre-release, when available

> See [CONTAINERIZATION.md](./CONTAINERIZATION.md) for podman/rootless/read-only-rootfs deployments and the full per-installation guide.

```bash
docker run --rm --name deeptutor \
  -p 127.0.0.1:3782:3782 \
  -v deeptutor-data:/app/data \
  ghcr.io/hkuds/deeptutor:latest
```

> **Only `3782` needs to be published.** The browser talks exclusively to the frontend origin; the Next.js middleware (`web/proxy.ts`) forwards `/api/*` and `/ws/*` to the FastAPI backend **inside the container**. Publishing `8001` (`-p 127.0.0.1:8001:8001`) is optional — handy only for hitting the API directly with curl or scripts.

Open [http://127.0.0.1:3782](http://127.0.0.1:3782). The container creates `/app/data/user/settings/*.json` on first boot; configure model providers from the Web Settings page. Config, API keys, logs, workspace files, memory, and knowledge bases persist in the `deeptutor-data` volume.

- **Different host ports:** change the left side of each `-p host:container` mapping (e.g. `-p 127.0.0.1:8088:3782`). If you change container-side ports in `/app/data/user/settings/system.json`, restart and update the right side of each mapping to match.
- **Detached:** add `-d`, then `docker logs -f deeptutor` to follow, `docker stop deeptutor` to stop, `docker rm deeptutor` before reusing the name. The `deeptutor-data` volume keeps your settings and workspace across restarts.

**Remote Docker / reverse proxy:** the browser only talks to the frontend
origin (`:3782`); the in-container Next.js middleware forwards `/api/*` and
`/ws/*` to the backend server-side. For the common single-container case you
don't configure an API base at all — just point your reverse proxy / TLS
terminator at `:3782`. You only need an API base for a **split deployment**
(backend in a separate container/host): set `next_public_api_base` in
`data/user/settings/system.json` to the in-network address the frontend server
uses to reach the backend (it's read server-side, never sent to the browser).

```json
{
  "next_public_api_base": "http://backend:8001"

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
