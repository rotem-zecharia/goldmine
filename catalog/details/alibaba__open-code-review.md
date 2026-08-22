# alibaba/open-code-review

Fast, efficient, battle-tested at Alibaba's scale. Hybrid architecture code review tool: deterministic pipelines + LLM Agent, precise line-level comments, built-in multi-language ruleset (NPE, thread-

## features

### The Problem with General-Purpose Agents

If you've used general-purpose agents like Claude Code with Skills for code review, you've likely encountered these pain points:

- **Incomplete coverage** — On larger changesets, agents tend to "cut corners," selectively reviewing only some files and missing others.
- **Position drift** — Reported issues frequently don't match the actual code location, with line numbers or file references drifting off target.
- **Unstable quality** — Natural-language-driven Skills are hard to debug, and review quality fluctuates significantly with minor prompt variations.

The root cause: a purely language-driven architecture lacks hard constraints on the review process.

### Core Design: Deterministic Engineering × Agent Hybrid

Open Code Review's core philosophy is to combine deterministic engineering with an agent, each handling what it does best.

**Deterministic Engineering — Hard Constraints**

For review steps that *must not go wrong*, engineering logic — not the language model — guarantees correctness:

- **Precise file selection** — Determines exactly which files need review and which should be filtered, ensuring no important change is missed.
- **Smart file bundling** — Groups related files into a single review unit (e.g., `message_en.properties` and `message_zh.properties` are bundled together). Each bundle runs as a sub-agent with isolated context — a divide-and-conquer strategy that stays stable on very large changesets and naturally supports concurrent review.
- **Fine-grained rule matching** — Matches review rules to each file's characteristics, keeping the model's attention sharply focused and eliminating information noise at the source. Compared to purely language-driven rule guidance, template-engine-based rule matching is more stable and predictable.
- **External positioning and reflection modules** — Independent comment-positioning and comment-reflection modules systematically improve both the location accuracy and content accuracy of AI feedback.

**Agent — Dynamic Decision-Making**

The agent's strengths are concentrated where they matter most — dynamic decisions and dynamic context retrieval:

- **Scenario-tuned prompts** — Prompt templates deeply optimized for code review, improving effectiveness while reducing token consumption.
- **Scenario-tuned toolset** — Distilled from deep analysis of tool-call traces in large-scale production data — including call frequency distributions, per-tool repetition rates, and the impact of new tools on the overall call chain — resulting in a purpose-built toolset that is more stable and predictable for code review than a generic agent toolkit.

## How to Use

## requirements

- **Git >= 2.41** — Open Code Review relies on Git for diff generation, code search, and repository operations.

### CLI

#### Install

```bash
npm install -g @alibaba-group/open-code-review
```

After installation, the `ocr` command is available globally.

For other installation methods (install script, GitHub Release binary, from source), see [Installation](https://open-codereview.ai/docs/installation).

#### Quick Start

**1. Configure LLM**

You must configure an LLM before reviewing code, unless you use [Delegation Mode](https://open-codereview.ai/docs/delegate).

```bash
ocr config provider          # Select a built-in provider or add a custom one
ocr config model             # Pick a model for the active provider
```

![Provider setup](imgs/providers.jpg)

The interactive UI guides you through provider selection, API key entry, and model configuration, then automatically tests connectivity.

For CLI setup, environment variables, custom providers, and other advanced configuration, see [Configuration](https://open-codereview.ai/docs/configuration).

**2. Review**

```bash
cd your-project

# Workspace mode — review all staged, unstaged, and untracked changes
ocr review

## configuration

ocr delegate preview
ocr delegate rule src/main.go src/handler.go
```

## Documentation

Full documentation lives at **[open-codereview.ai/docs](https://open-codereview.ai/docs)**:

- [Quickstart](https://open-codereview.ai/docs/quickstart) — install and run your first review
- [Installation](https://open-codereview.ai/docs/installation) — all platforms and package managers
- [CLI Reference](https://open-codereview.ai/docs/cli-reference) — every command and flag
- [Review Rules](https://open-codereview.ai/docs/review-rules) — customize review rules with path filtering and targeting
- [Configuration](https://open-codereview.ai/docs/configuration) — config keys and environment variables
- [MCP Server](https://open-codereview.ai/docs/mcp) — extend the review agent with external tools
- Coding Agent Integrations — choose the platform you use
  - [Claude Code](plugins/open-code-review/README.md#claude-code) — install a plugin with review slash commands
  - [Codex](plugins/open-code-review/README.md#codex) — install a plugin with callable review skills
  - [Cursor](plugins/open-code-review/README.md#cursor) — install a plugin with portable review skills
  - [OpenCode](plugins/open-code-review/opencode/README.md) — install native review tools and slash commands
  - [QCA Forward](plugins/open-code-review/qca/README.md) — run delegation mode with the QCA host model and a ready-to-publish template
  - [Skill-compatible agents](https://open-codereview.ai/docs/agent-skill) — install the portable agent skill
- Review Execution Modes — after integration, choose which LLM performs the review
  - [Default (OCR-managed)](https://open-codereview.ai/docs/configuration) — OCR runs the review using its configured LLM
  - [Delegation Mode](https://open-codereview.ai/docs/delegate) — your coding agent runs the review using its own LLM; no OCR API key required
- [CI/CD Integration](https://open-codereview.ai/docs/cicd) — GitHub Actions, GitLab CI, GitFlic CI, and Gerrit integration
- [Session Viewer](https://open-codereview.ai/docs/viewer) — browse and replay review sessions in browser
- [Telemetry](https://open-codereview.ai/docs/telemetry) — OpenTelemetry integration for observability
- [FAQ](https://open-codereview.ai/docs/faq) — common questions and troubleshooting

## Contributing

This project exists thanks to all the people who contribute. See [CONTRIBUTING.md](CONTRIBUTING.md) for development setup, coding guidelines, and how to submit pull requests.

<a href="https://github.com/alibaba/open-code-review/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=alibaba/open-code-review" />
</a>

## License

[Apache-2.0](LICENSE) — Copyright 2026 Alibaba
