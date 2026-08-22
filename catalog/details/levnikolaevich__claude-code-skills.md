# levnikolaevich/claude-code-skills

Standalone engineering skills for Claude Code and Codex: review, audit, optimization, testing, product discovery, architecture, and safe publishing.

## installation

Add the marketplace and install only the suites you need:

```text
/plugin marketplace add levnikolaevich/claude-code-skills
/plugin install review-suite@levnikolaevich-skills-marketplace
/plugin install codebase-audit-suite@levnikolaevich-skills-marketplace
/plugin install optimization-suite@levnikolaevich-skills-marketplace
/plugin install testing-suite@levnikolaevich-skills-marketplace
/plugin install product-discovery-suite@levnikolaevich-skills-marketplace
/plugin install maintainer-suite@levnikolaevich-skills-marketplace
/plugin install architecture-suite@levnikolaevich-skills-marketplace
/reload-plugins
```

Invoke a skill by its namespaced name, for example `/review-suite:ln-12-delivery-reviewer`.

For local development, load one plugin directly:

```bash
claude --plugin-dir ./plugins/review-suite
```

## Install in Codex

```bash
codex plugin marketplace add levnikolaevich/claude-code-skills
codex plugin add review-suite@levnikolaevich-skills-marketplace
codex plugin add codebase-audit-suite@levnikolaevich-skills-marketplace
codex plugin add optimization-suite@levnikolaevich-skills-marketplace
codex plugin add testing-suite@levnikolaevich-skills-marketplace
codex plugin add product-discovery-suite@levnikolaevich-skills-marketplace
codex plugin add maintainer-suite@levnikolaevich-skills-marketplace
codex plugin add architecture-suite@levnikolaevich-skills-marketplace
```

## Repository layout

```text
.
├── .agents/plugins/marketplace.json       # Codex catalog
├── .claude-plugin/marketplace.json        # Claude Code catalog
└── plugins/
    ├── review-suite/
    ├── codebase-audit-suite/
    ├── optimization-suite/
    ├── testing-suite/
    ├── product-discovery-suite/
    ├── maintainer-suite/
    └── architecture-suite/
```

Each plugin contains a portable Agent Plugins v1 `plugin.json`, the current `.codex-plugin/plugin.json` OpenAI host adapter, and one shared `skills/<skill>/SKILL.md` tree.

This is the smallest practical shared layout for distributed plugins:

- Both hosts use `skills/<name>/SKILL.md`, so each skill has one canonical copy.
- Agent Plugins clients discover the portable package through root `plugin.json`; its minimal manifest owns only the schema target and stable name.
- Current ChatGPT and Codex packaging still requires `.codex-plugin/plugin.json`, which remains the single owner of mutable version, description, publisher, and interface metadata.
- Claude Code scans each marketplace source's standard `skills/` directory, so a duplicate Claude-specific plugin manifest is unnecessary.
- `agents/openai.yaml`, references, scripts, assets, hooks, agents, and MCP configuration are optional and omitted until a concrete need appears.

The structure follows the [Agent Plugins v1 specification](https://agent-plugins.org/specification), current [OpenAI plugin guide](https://developers.openai.com/plugins/build/plugins), [Agent Skills specification](https://agentskills.io/specification), [Claude Code skill guide](https://code.claude.com/docs/en/skills), and [Claude Code plugin reference](https://code.claude.com/docs/en/plugins-reference).

## Indexing

The first digit identifies the plugin and the second identifies the skill within it: `1x` review, `2x` audit, `3x` optimization, `4x` testing, `5x` product discovery, `6x` repository maintenance, and `7x` architecture artifact creation. See the canonical allocation and overflow rules in [AGENTS.md](AGENTS.md#index-system).

## License

[MIT](LICENSE)
