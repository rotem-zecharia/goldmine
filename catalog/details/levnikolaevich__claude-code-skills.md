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
