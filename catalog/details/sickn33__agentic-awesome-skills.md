# sickn33/agentic-awesome-skills

AAS Core is the local, agent-first control plane for complete catalog discovery, agent-owned selection, stack validation, and planning, backed by 2,115+ agentic skills. Includes CLI, local MCP, catalo

## features

- **Agent-first, locally controlled**: Codex or Claude inspects the project and chooses from the complete local catalog without uploading your repository to AAS.
- **Complete and inspectable**: every catalog skill is searchable, readable, and available for agent selection; Core does not certify suitability, compatibility, or operational safety, and metadata is informational rather than an eligibility gate.
- **Approval before writes**: the durable artifacts are an approved stack and immutable plan, not an opaque one-shot install.
- **Installable, not just inspirational**: use the compatible legacy installer or plugin distributions when direct delivery is the right path.
- **Built for major agent workflows**: Claude Code, Cursor, Codex CLI, Autohand Code, Gemini CLI, Antigravity, Kiro, OpenCode, Copilot, and more.
- **Broad coverage with real utility**: 2,121+ skills across development, testing, security, infrastructure, product, and marketing.
- **Inspect before installing**: the hosted [Skill Workbench](https://sickn33.github.io/agentic-awesome-skills/workbench) reviews agent-produced stack manifests and immutable plans without browser-side installation.
- **Focused delivery remains available**: specialized plugins package curated sets for web, security, data, docs, DevOps, QA, OSS, or agent/MCP workflows.
- **Useful whether you want breadth or curation**: install the full catalog, choose a specialized plugin, start with bundles, or compare alternatives before installing.

### Why not just search the skills directory?

Direct file search can find candidate prose, but it leaves the result in the conversation. AAS Core adds verified catalog identity, explicit target binding, durable desired state, optional selection evidence, deterministic validation, immutable planning, and dedicated review surfaces. Its value is not choosing better than the coding agent; it is turning the agent's choice into reproducible, inspectable state.

## Table of Contents

- [Support the Project](#support-the-project)
- [AAS Core: Agent-First Preview](#aas-core-agent-first-preview)
- [Why This Repo](#why-this-repo)
- [Installation](#installation)
- [Recommended Specialized Plugins](#recommended-specialized-plugins)
- [Choose Your Tool](#choose-your-tool)
- [Quick FAQ](#quick-faq)
- [Bundles & Workflows](#bundles--workflows)
- [Browse 2,121+ Skills](#browse-2121-skills)
- [Troubleshooting](#troubleshooting)
- [Stable Skills Manifest v1](#stable-skills-manifest-v1)
- [Contributing](#contributing)
- [Community](#community)
- [Credits & Sources](#credits--sources)
- [Repo Contributors](#repo-contributors)
- [Star History](#star-history)
- [License](#license)

## installation

For Codex and Claude, start with the [AAS Core guide](https://github.com/sickn33/agentic-awesome-skills/blob/v17.1.0/docs/users/aas-core.md): configure the local MCP, ask the agent to inspect the project and choose exact IDs from the full catalog, review the proposed `aas-stack.json`, then run CLI validation and planning. The MCP and validation are read-only. Planning writes only the requested plan artifact; it does not materialize skill payloads or AAS managed state in the target.

Use direct installation when your host does not yet have a native AAS Core adapter, when you already know the exact skill IDs, or when you deliberately prefer manual selection:

- **Specialized plugins** when the job has a clear domain.
- **Full library install** when you want every skill available in a local skills directory.
- **Bundles and workflows** when you want role-based recommendations or ordered execution playbooks.

### From selection to use

On unreleased `main`, `aas stack install-preview --manifest <file> --destination <skill-directory>` prepares a direct-installer dry run from the agent-selected IDs. It does not execute installation or choose skills; destination names must satisfy the installer's filename restrictions. See [the manifest handoff](docs/users/aas-core.md#use-the-reviewed-selection).

1. Describe the project outcome to Codex or Claude with the local AAS MCP configured.
2. Have the agent compare candidates and read the selected instructions and support files. Preserve the exact IDs in `aas-stack.json` and review their prerequisites.
3. Validate the manifest and review a CLI plan when you need an artifact-based check. Workbench can help inspect the artifacts.
4. For actual use, preview the supported direct installer with those same IDs, an exact release and the intended host directory. Review its own changes, then repeat without `--dry-run` when installation is authorized. Invoke the skill in a real task and keep the resulting check or artifact for reuse.

For example, after reviewing `brainstorming` and `systematic-debugging` for a Codex project, run from that project directory:

```bash
npm exec --yes --ignore-scripts --package=agentic-awesome-skills@16.8.0 -- \
  agentic-awesome-skills --release 16.8.0 --path .agents/skills \
  --skills brainstorming,systematic-debugging --dry-run
```

Replace the example IDs with the reviewed selection. The direct installer has its own preview and ownership format; it does not consume or apply a Core plan. Core apply/recovery remain experimental. [Worked cases](docs/users/workflows.md#recorded-worked-cases) show observed inputs and outputs without claiming guaranteed model performance.

### Direct skill install

```bash
# Antigravity: preview an exact, agent-selected set before writing.
npx agentic-awesome-skills --antigravity --skills brainstorming,systematic-debugging --dry-run

## tools

npx agentic-awesome-skills --agy
```

On `main`, the npm installer uses a shallow partial clone and checks out the canonical `skills/` tree after verifying the cloned commit against the immutable `gitHead` recorded for that exact npm package version. Git 2.25+ is required. Plugin mirrors, documentation and app assets are excluded from that temporary checkout; every canonical skill and support file remains available. See the [measured distribution comparison](docs/maintainers/distribution-efficiency.md). If the GitHub tag moved or npm identity metadata is unavailable, installation stops before copying content. Use `--tag main` only when you intentionally accept a mutable, explicitly unverified repository ref.

Antigravity watches `~/.agents/skills` and may load enough installed instructions
to exhaust its context, slow startup, trigger truncation errors, or enter a crash
loop. For that target, the installer stops before cloning or writing unless you
provide `--skills`, a metadata filter, or the explicit `--all` override. The bare
`npx agentic-awesome-skills` command uses the same protected Antigravity target.

The recommended flow is to ask Codex or Claude with the read-only AAS Core MCP
configured to inspect the project, search the complete catalog, and choose exact
skill IDs. The agent selects the IDs; AAS MCP validates them without installing; the agent
or user then previews the direct installation with the command above and repeats
it without `--dry-run` after review.

Other direct-install targets retain the legacy-compatible full-catalog behavior
when no selectors are supplied. The CLI prints the catalog's risk summary first:
a full install includes `critical` and authorized-use-only `offensive`
instructions. Installation copies files; it does not execute their commands,
but an agent may act on an installed skill later. Prefer an exact reviewed set:

```bash
npx agentic-awesome-skills audit --skills brainstorming,backend-dev-guidelines
npx agentic-awesome-skills --skills brainstorming,backend-dev-guidelines --dry-run
```

If you deliberately accept the context and crash-loop risk, the complete
Antigravity catalog remains available through explicit consent:

```bash
npx agentic-awesome-skills --antigravity --all
```

The audit reads the selected skill directories without executing them and
reports command, network, credential, filesystem, privileged, destructive,
symlink, and binary signals. It is a review aid, not a safety certificate. See
[Security, trust, and antivirus alerts](docs/users/security-and-antivirus.md).
