# wshobson/agents

Multi-harness agentic plugin marketplace for Claude Code, Codex, Cursor, OpenCode, GitHub Copilot, Google Antigravity, and Pi

## tools

<a id="agentic-plugin-marketplace"></a>
<a id="claude-code-plugins-agents-and-skills"></a>

Use one collection of plugins, agents, skills, and commands across Claude Code, OpenAI Codex CLI, Cursor, OpenCode, Antigravity CLI, GitHub Copilot, and Pi. A harness is the coding tool that loads and runs the components. Plugins cover Python and JavaScript development, code review, testing, infrastructure, security, and other work.

The catalog contains 94 plugins, including 92 local plugins and 2 external entries. The local source contains 202 agents, 184 skills, and 105 commands. The components share a Markdown source, with installation and capabilities adapted to each harness.

## Multi-harness support

Choose the harness you use and follow its setup route. Available components depend on the installation route and the harness's capabilities.

| Tool | Installation | Components and limits |
|---|---|---|
| [Claude Code](#claude-code) | Plugin marketplace | Source agents, skills, and commands; plugin-specific hooks and MCP configuration |
| [OpenAI Codex CLI](#codex-cli) | Native marketplace or generated artifacts | Native source skills; generated TOML agents and commands as skills use a separate route |
| [Cursor](#cursor) | Plugin marketplace | Source agents, skills, and commands, with curated project rules |
| [OpenCode](#install-from-a-clone) | `make install-opencode` | Generated agents, skills, and commands, with translated tool permissions |
| [Antigravity CLI](#install-from-a-clone) | `make install-antigravity` | Generated plugins containing agents, skills, and commands |
| [GitHub Copilot](#install-from-a-clone) | `make install-copilot` | Generated agent profiles and skills; commands also become invocable skills |
| [Pi](#install-from-a-clone) | `make install-pi` | Generated skills and prompt templates; agents require a subagent extension |

See the [capability matrix](docs/harnesses.md) for model mappings, tool permissions, hooks, and installation differences.

For individual skills, use a [skills-only installer](#skills-only) and select your coding tool.

## installation

Choose a plugin for the work you do:

| Plugin | Use it for |
|---|---|
| [python-development](plugins/python-development/) | Python, Django, FastAPI, testing, and packaging |
| [javascript-typescript](plugins/javascript-typescript/) | JavaScript and TypeScript development and project setup |
| [developer-essentials](plugins/developer-essentials/) | Code review, debugging, Git, and testing patterns |
| [security-scanning](plugins/security-scanning/) | Security review, dependency checks, and code scanning |

See the [plugin catalog](docs/plugins.md) for all 94 plugins and the [usage guide](docs/usage.md) for commands and examples.

### Claude Code

Run these commands inside Claude Code to register the marketplace and install the Python development plugin:

```text
/plugin marketplace add wshobson/agents
/plugin install python-development@claude-code-workflows
```

Then ask Claude to use the Python agents for your task, or run the plugin's scaffolding command:

```text
/python-development:python-scaffold Create a FastAPI service with tests
```

### Codex CLI

Run these commands in a terminal with a current Codex CLI:

```bash
codex plugin marketplace add wshobson/agents
codex plugin add python-development@claude-code-workflows
```

The native Codex manifests expose source skills. The generated TOML agents and command-derived skills use a separate adapter path. Native installation also reads the original skill bodies, while generated copies split oversized bodies into reference files for the 8 KB budget. See the [Codex setup details](docs/harnesses.md#native-install) before choosing an installation route.

### Cursor

Cursor uses the committed [plugin marketplace registry](.cursor-plugin/marketplace.json). Follow the [Cursor setup instructions](docs/harnesses.md#native-install) to add the marketplace and install a plugin.

<a id="skills-only-gh-skill-npx-skills"></a>
<a id="skills-only-gh-skill--npx-skills"></a>

### Skills only

Install an individual skill with GitHub CLI's `gh skill` command or the `npx skills` installer. Select your coding tool when prompted. Both installers read skills from GitHub without cloning the repository and install them without the plugin's agents, commands, or hooks.

```bash
gh skill install wshobson/agents python-testing-patterns
npx skills add wshobson/agents --skill python-testing-patterns
```

`gh skill` requires GitHub CLI 2.90 or later. The `npx` command requires Node.js and npm. See [skills-only installation](docs/harnesses.md#skills-only-installers) for other agents, install scopes, and version pinning.

<a id="codex-cli--cursor--opencode--antigravity-cli--copilot--pi"></a>
<a id="opencode-antigravity-cli-copilot-and-pi"></a>

### Install from a clone

For OpenCode, Antigravity CLI, GitHub Copilot, and Pi, clone the repository and use the installer for your harness. Install [uv](https://docs.astral.sh/uv/getting-started/installation/), Python 3.12 or later, and the coding tool you want to use. The following clone command uses GitHub CLI:

```bash
gh repo clone wshobson/agents ~/agents
cd ~/agents
```

Run the command for your tool. Each target generates the artifacts and links all local plugins into that tool's user configuration:

```bash
make install-opencode
make install-antigravity
make install-copilot
make install-pi
```

Pi's agents require its reference `subagent` extension or a compatible extension. See the [global install guide](docs/harnesses.md#global-install) for configuration paths and uninstall commands.

## What's inside

| Component | Count | Purpose |
|---|---:|---|
| Plugins | 94 | Installable groups of components, including 92 local plugins and 2 external entries |
| Agents | 202 | Instructions for specialist subagents that handle delegated work |
| Skills | 184 | Guidance and reference material that an agent loads when relevant |
| Commands | 105 | Named workflows you invoke, such as project scaffolding or a security scan |

The agent, skill, and command counts cover loca
