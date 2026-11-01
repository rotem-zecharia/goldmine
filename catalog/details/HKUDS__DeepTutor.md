# HKUDS/DeepTutor

DeepTutor: Lifelong Personalized Tutoring. https://deeptutor.info/.

## features

DeepTutor is an agent-native learning workspace that connects tutoring, research, creation, and practice in one extensible system.

- **One runtime, many learning modes** — Chat, Quiz, Research, Visualize, Solve, Mastery Path, Reading, and more share session context while retaining purpose-built workflows.
- **A connected learning workspace** — Home, Learning, and Resources connect Chat, Books, Reading, Practice, Task Board, Calendar, and Learning notebook with shared materials, progress, and learning context.
- **Grounded knowledge and reading** — Build versioned libraries with LlamaIndex, PageIndex, GraphRAG, or LightRAG, connect external knowledge sources, and learn beside documents, video, and audio with source-linked citations.
- **Partners and subagents** — Consult live agents such as Claude Code, Codex, and Grok CLI, import past conversations, or run persistent Partners with their own memory, resources, and IM channels.
- **Inspectable memory** — L1 traces, L2 facts, and L3 synthesis make personalization visible and editable, with evidence links you can audit in the Memory Graph.
- **Extensible by design** — Add personas, built-in or community skills, MCP services, CLI apps, and generation models through one agent-native runtime.

---

## 🚀 Get Started

Choose the installation path that fits how you want to use DeepTutor. Terminal-based installs share one runtime home: private settings live in `data/user/settings/` under the launch directory, or under `DEEPTUTOR_HOME` / `deeptutor start --home` when set explicitly. After starting the app, configure a provider and model in **Settings → Providers** and **Language models**.

<details>
<summary><b>Desktop — macOS and Windows (Preview)</b></summary>

**Open DeepTutor** bundles Python, Node.js, and the full learning workspace, so no terminal or separate runtime installation is needed. Desktop previews are available on `dev`; the **v1.7.0 Release does not include desktop installers**.

Open a successful [Desktop Release workflow run](https://github.com/HKUDS/DeepTutor/actions/workflows/desktop-release.yml?query=branch%3Adev), scroll to **Artifacts**, and download the matching target. GitHub sign-in is required, and artifacts expire after seven days.

| Your computer | Download target | Installer |
| --- | --- | --- |
| **Mac with Apple Silicon** | `macos-arm64` | Open the DMG and drag **Open DeepTutor** into **Applications**. |
| **Mac with Intel** | `macos-x64` | Open the DMG and drag **Open DeepTutor** into **Applications**. |
| **Windows x64** | `windows-x64` | Run the Setup `.exe`, or extract the portable ZIP and launch `Open DeepTutor.exe`. |

Windows preview builds are unsigned and may show a SmartScreen warning. See the [desktop guide](apps/desktop/README.md) for signing, local data, and source builds.

</details>

<details>
<summary><b>Docker — Fastest Full-App Trial</b></summary>

Run the full Web app without installing Python or Node.js:

```bash
docker run --rm --name deeptutor \
  -p 127.0.0.1:3782:3782 \
  -v deeptutor-data:/app/data \
  ghcr.io/hkuds/deeptutor:latest
```

Open [http://127.0.0.1:3782](http://127.0.0.1:3782). The named volume preserves settings and local data; only port `3782` is required for the Web app. See the [Docker guide](https://docs.deeptutor.info/get-started/docker/) for host workspaces, local model services, reverse proxies, and production deployment.

</details>

<details>
<summary><b>PyPI — Full Web App and CLI</b></summary>

Use **Python 3.11–3.14** and **Node.js 20.9+**. In the modular 1.7.0 release, `deeptutor[full]` installs the Web app and CLI; bare `deeptutor` installs core chat and the SDK.

```bash
mkdir -p my-deeptutor && cd my-deeptutor
python -m pip install -U "deeptutor[full]"
deeptutor init     # ports + LLM provider + optional embedding/search
deeptutor start    # starts backend + frontend
```

Open the URL printed in the terminal, by default [http://127.0.0.1:3782](http://127.0.0.1:3782). Press `Ctrl+C` to stop both servi

## installation

deeptutor module install solve              # install the matching module and dependencies
deeptutor module uninstall solve --dry-run  # inspect the plan and dependency blockers
deeptutor module uninstall solve            # remove only this module's distribution
deeptutor chat                              # restart the CLI; use start for an installed Web app
```

Examples: `solve`, `research`, `questions`, `knowledge`, `parsing`, `reading`, `mastery`, `books`, `memory`, `notebook`, and `partners`. Dependents block removal; core cannot be removed through the module command. Disabling or uninstalling preserves settings, conversations, knowledge bases, and generated files. Shared third-party dependencies are retained.

**In the browser:** **Settings → Runtime status → Modules** shows module status and the corresponding terminal commands. Package changes require a stopped environment and are performed in the CLI. **Chat → Customize page** and **Learning → New learning activity → Customize page** change personal page choices immediately; hiding an entry does not uninstall its module or revoke access.

The 1.7.0 package family uses matching versions across core and feature wheels. For local wheel installation, pass `--wheelhouse /path/to/wheels` to `module install`. See [module installation and source development](docs-for-dev/MODULES.md) for building the wheels and deployment details.

</details>

## 🧩 Ecosystem — EduHub & the Skills Community

DeepTutor skills use the open **Agent-Skills** format — a folder with a `SKILL.md` playbook (YAML frontmatter + Markdown) and optional reference files. Nothing about it is DeepTutor-specific, so any registry that speaks the format becomes a source for your library. DeepTutor ships with **[EduHub](https://eduhub.deeptutor.info/)** — our own education-focused skill registry — wired in as the default hub.

<details>
<summary><b>EduHub — DeepTutor's skill ecosystem</b></summary>

[**EduHub**](https://eduhub.deeptutor.info/) is the community hub DeepTutor launched for sharing teaching-oriented agent skills — Socratic tutors, flashcard builders, essay feedback, exam blueprints, concept explainers, and more. It is built into DeepTutor, so there's nothing to configure: a bare slug or an `eduhub:` prefix resolves to it.

**Find and install** — in the browser, open **Personalization → Skills → Import from EduHub** to browse the catalog and download a skill straight into your library. From the terminal:

```bash
deeptutor skill search "socratic tutor"               # search EduHub (the default hub)
deeptutor skill install socratic-tutor                # fetch → verify → register
deeptutor skill install eduhub:socratic-tutor@1.2.0   # pin a hub and a version
deeptutor skill list                                  # local skills with their hub provenance
```

**Publish your own** — package a `SKILL.md` and share it back to the community:

```bash
deeptutor skill login                                 # browser sign-in to EduHub
deeptutor skill publish ./my-skill                    # interactive: pick a track + tags, then upload
deeptutor skill update                                # roll back or release a new version
```

EduHub is also a standalone, ClawHub-compatible registry, so agents that aren't DeepTutor (Claude Code, Codex, …) can use it directly through the `eduhub` CLI — `npx eduhub install socratic-tutor`.

</details>

<details>
<summary><b>The import safety gate</b></summary>

Whatever the source, every import passes the **same safety gate** before anything touches your workspace:

- the registry's **security verdict** is checked first — flagged packages are refused unless you pass `--allow-unverified`;
- archives are extracted defensively with path-traversal, entry-count, size, compression-ratio, suffix, and symlink checks; executable bits are stripped, while extensionless files remain allowed;
- frontmatter is normalized to DeepTutor's schema and `always:` is **stripped**, so a downloaded skill

## limitations

We want DeepTutor to keep iterating and improving — and ultimately to become a gift we give back to the open-source community. Our [**roadmap**](https://github.com/HKUDS/DeepTutor/issues/498) is updated continuously; vote on items there or propose new ones. If you'd like to contribute, see the [**Contributing Guide**](CONTRIBUTING.md) for branching strategy, coding standards, and how to get started.

<div align="center">

We hope DeepTutor becomes a gift for the community. 🎁

See the [development-branch contributor list](CONTRIBUTORS.md) for recently integrated contributions.

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
