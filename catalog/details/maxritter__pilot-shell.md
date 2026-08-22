# maxritter/pilot-shell

How real engineers run Claude Code and Codex: spec-driven planning, enforced TDD, persistent memory, and quality enforcement on all levels. Make your agents production-ready.

## features

**Claude Code and Codex CLI write code fast** — but without structure, they skip tests, lose context, and produce inconsistent results. Other frameworks add complexity (dozens of agents, thousands of lines of config) without meaningfully better output.

**Pilot Shell is different.** Every component solves a real problem with an engineered solution:

- **`/prd`** — brainstorm ideas into clear requirements with optional deep research
- **`/spec`** — plans, implements, and verifies features end-to-end with TDD
- **`/build`** — names a goal, then runs autonomously: judge loops until criterion passes
- **`/fix`** — bugfix workflow with TDD; bails out when complexity exceeds the standard fix lane
- **Spec collaboration** — share specs with teammates, annotations flow back grouped by author
- **Quality hooks** — enforce linting, formatting, type checking, and tests as quality gates
- **Context engineering** — preserves decisions and knowledge across sessions
- **Memory sharing** — share captured memories with your team through the project repo
- **Code intelligence** — semantic search (Semble) + code knowledge graph (CodeGraph)
- **Token optimization** — 60–90% cost reduction via RTK compression and Semble code search
- **Pilot Bot** — persistent automation agent with scheduled tasks and background jobs
- **Extensions** — reusable rules, skills, and MCP servers with team sharing and customization
- **Console** — local web dashboard with real-time notifications and session management

---

<h2 id="install">Getting Started</h2>

## requirements

**At least one AI agent:** Pilot Shell supports **Claude Code** (primary — full feature coverage) and **Codex** through Codex CLI or the ChatGPT desktop app (all workflows, fewer platform features). Install at least one before running the Pilot installer:

- **Claude Code:** Install via the [native installer](https://code.claude.com/docs/en/quickstart). If you have the `npm` or `brew` version, uninstall it first. Requires a Claude subscription — [Max 5x or 20x](https://claude.com/pricing) for solo, [Team Premium](https://claude.com/pricing) for teams, [Enterprise](https://claude.com/pricing) for organizations.
- **Codex:** Install [Codex CLI](https://developers.openai.com/codex/cli) or the ChatGPT desktop app. Pilot detects the CLI and the Codex binary bundled with ChatGPT on macOS. Requires an OpenAI subscription — [Plus or Pro](https://developers.openai.com/codex/pricing) for solo, [Business or Enterprise](https://developers.openai.com/codex/pricing) for teams.

**Terminal (Recommended):** [cmux](https://cmux.com) works great with Pilot Shell — its vertical tab layout lets you run multiple sessions side by side. Any modern terminal works: [Ghostty](https://ghostty.org/), [iTerm2](https://iterm2.com/), or the built-in macOS/Linux terminal.

## installation

**Works with any existing project.** Pilot Shell integrates with **Claude Code** and **Codex CLI or ChatGPT desktop**, using their built-in concepts (rules, hooks, skills, subagents, MCP) to improve your experience:

```bash
curl -fsSL https://raw.githubusercontent.com/maxritter/pilot-shell/main/install.sh | bash
```

Installs globally on macOS, Linux, and Windows (WSL2). After installation, run `claude` or `codex` directly. On macOS, you can instead restart ChatGPT desktop and open the project there. Pilot Shell loads automatically in either Codex client. Run `pilot update` to check for updates.

<details>
<summary><b>Downgrade</b></summary>

If you encounter an issue or unfixed bug in the latest version, you can always go back to a previous version (see [releases](https://github.com/maxritter/pilot-shell/releases)):

```bash
export VERSION=10.5.1
curl -fsSL https://raw.githubusercontent.com/maxritter/pilot-shell/main/install.sh | bash
```
</details>

<details>
<summary><b>Uninstalling</b></summary>

Removes the Pilot binary, plugin files, managed commands/rules, settings and shell aliases:

```bash
curl -fsSL https://raw.githubusercontent.com/maxritter/pilot-shell/main/uninstall.sh | bash
```
</details>

<details>
<summary><b>Reset & Refresh</b></summary>

Over time, accumulated session logs and Pilot Shell's caches can slow things down. A periodic reset gives you a clean baseline:

```bash
# 1. If using Claude Code, log out first
/logout

## configuration

# Using CLAUDE_CONFIG_DIR? Substitute it for ~/.claude, and back up
# "$CLAUDE_CONFIG_DIR/.claude.json" instead of ~/.claude.json.
mv ~/.claude.json ~/.claude.json.bak
mv ~/.claude       ~/.claude.bak
mv ~/.codex        ~/.codex.bak
mv ~/.pilot        ~/.pilot.bak

## tools

Daily token costs, model routing breakdown, and usage trends across sessions for both Claude Code and Codex sessions. Correlates costs to commits and show savings via CLI proxy integration.

### Settings

Configure spec workflow toggles, reviewer settings, and Console preferences. Toggle labels show which review agents run on Claude Code + Codex, and which Codex Companion Reviewers require the Claude Code Codex plugin.

### Documentation

Documentation, guides, and quick-start resources to explain the concepts in detail.

---

## Documentation

For full details on every component, see the **[Documentation](https://pilot-shell.com/docs/)**.

---

## Changelog

See the full changelog at [GitHub Releases](https://github.com/maxritter/pilot-shell/releases).

---

## Contributing

Found a bug or missing a feature? [Open an issue](https://github.com/maxritter/pilot-shell/issues) on GitHub.

---

## License

See [LICENSE](LICENSE).

---

<div align="center">

**How real engineers run Claude Code and Codex**

</div>

[osai-verify: 8d67182dee08d42091c5]: #
