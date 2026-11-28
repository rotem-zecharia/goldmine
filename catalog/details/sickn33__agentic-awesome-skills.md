# sickn33/agentic-awesome-skills

3,000+ reusable AI agent skills for Claude Code, Codex, Cursor and Gemini CLI. AAS Core adds local catalog discovery, agent-owned selection and plan preview. CLI, MCP and plugins.

## installation

### From selection to use

With AAS Core already configured, use the [Core guide](docs/users/aas-core.md) to review the exact skill IDs your agent selects. The npm-based bootstrap for the current Core release is paused. You can install the skills themselves directly from GitHub.

### Install selected skills directly

With [GitHub CLI](https://cli.github.com/) and `gh skill` available, preview and install one skill from the current release. This example uses Codex at user scope:

```sh
gh skill preview sickn33/agentic-awesome-skills skills/brainstorming/SKILL.md@v21.5.0
gh skill install sickn33/agentic-awesome-skills skills/brainstorming/SKILL.md --agent codex --scope user --pin v21.5.0
```

To update a pinned skill, preview it at the newer release tag and repeat the install with that tag. See the [installation and update guide](docs/users/getting-started.md#install-and-update-without-npm) for other agents, switching from an npm install, downloading a ZIP, and updating a Git clone.

## Choose Your Tool

| Tool | GitHub CLI `--agent` value |
| --- | --- |
| Claude Code | `claude-code` |
| Cursor | `cursor` |
| Gemini CLI | `gemini-cli` |
| Codex | `codex` |
| Antigravity 2.0 | `antigravity2.0` |
| Antigravity CLI | `antigravity-cli` |
| GitHub Copilot | `github-copilot` |
| Kiro CLI | `kiro-cli` |
| OpenCode | `opencode` |
| AdaL | `adal` |

For a custom skill directory, use `--dir <directory>` in place of `--agent` and `--scope`. For Claude Code and Codex plugin installation, see the [plugin guide](docs/users/plugins.md).

## Recommended Specialized Plugins

Choose a focused plugin for the domain you are working in. These packages are available for Claude Code and Codex; compatible bundles also have a standard Agent Plugins manifest. See the [plugin guide](docs/users/plugins.md) for installation and host support.

| Plugin | Skills | Best for |
| --- | ---: | --- |
| AAS Web App Builder | 10 | Frontend and full-stack developers shipping modern web apps. |
| AAS Product Design Studio | 10 | Product UI, brand, portfolio, accessibility, and richer visual work. |
| AAS Security Engineer | 10 | Authorized security testing, audit, and hardening. |
| AAS Secure App Builder | 9 | Developers who want security embedded while building features. |
| AAS Documents & Presentations | 9 | Office files, document conversion, decks, and slide workflows. |
| AAS Data Analytics | 10 | Product analytics, SQL, dashboards, and experiments. |
| AAS Agent & MCP Builder | 10 | Agentic apps, MCP tools, RAG systems, and evaluation loops. |
| AAS QA & Test Automation | 10 | Test suites, browser automation, and QA stabilization. |
| AAS DevOps & Cloud | 10 | Infrastructure, deployments, and operational workflows. |
| AAS Accessibility & Inclusive UX | 8 | WCAG audits, automated scans, screen-reader checks, and accessible QA. |
| AAS API Platform Builder | 10 | API design, OpenAPI contracts, auth, security, load tests, and observability. |
| AAS SaaS Launch & Revenue | 10 | SaaS MVPs, pricing, payments, analytics, lifecycle, referrals, and SEO. |
| AAS AI Product & Evaluation Ops | 10 | AI product metrics, evals, tracing, experiments, and model-quality loops. |

Browse the [plugin roadmap](docs/users/specialized-plugin-roadmap.md), [live plugin catalog](https://aaskills.tech/plugins), or generated [`plugins/`](plugins/) tree for the full set.

## Bundles & Workflows

Bundles suggest related skills; workflows describe the order to use them. They are guidance for selecting and running skills, not additional packages to install.

- [Bundles](docs/users/bundles.md) group skills by role or goal, such as `Web Wizard`, `Security Engineer`, and `OSS Maintainer`.
- [Workflows](docs/users/workflows.md) give ordered playbooks for planning, shipping, testing, and auditing; [workflow metadata](data/workflows.json) is available for integrations.
- If too many installed skills overload Antigravity, follow the [selective activation guide](docs/users/agent-overload-recovery.m
