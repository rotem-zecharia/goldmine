# sickn33/agentic-awesome-skills

AAS Core is the local, agent-first control plane for complete catalog discovery, agent-owned selection, stack validation, and planning, backed by 2,400+ agentic skills. Includes CLI, local MCP, catalo

## installation

### From selection to use

Start with AAS Core in Codex or Claude. Configure the local MCP using the [Codex](docs/users/codex-cli-skills.md) or [Claude](docs/users/claude-code-skills.md) guide. With the MCP available, ask the agent to inspect your project, compare relevant skills, and save the exact selection. Then validate its manifest and review the resulting plan before any installation. The first configuration command previews a change and returns an approval digest:

```bash
npm exec --yes --ignore-scripts --package=agentic-awesome-skills@18.15.0 -- aas mcp configure \
  --host codex \
  --scope user \
  --config /absolute/path/to/codex/config.toml \
  --cache-root /absolute/path/to/aas-cache
```

Use `--host claude` and its configuration path for Claude. The [Core setup guide](https://github.com/sickn33/agentic-awesome-skills/blob/v18.15.0/docs/users/aas-core.md#configure-the-local-mcp) explains approval, reconnection, validation, and planning. To hand the reviewed IDs to the direct installer, use `aas stack install-preview` as described in the [manifest handoff](docs/users/aas-core.md#use-the-reviewed-selection); that command only prepares a `--dry-run` preview and does not apply a Core plan.

### Install selected skills directly

If you already know the IDs, preview a focused install into your host's skill directory:

```bash
npm exec --yes --ignore-scripts --package=agentic-awesome-skills@18.15.0 -- \
  agentic-awesome-skills --release 18.15.0 --path .agents/skills \
  --skills brainstorming,systematic-debugging --dry-run
```

Review the preview, then repeat without `--dry-run` when ready. The direct installer does not consume or apply a Core plan. Antigravity's watched skill directory can overload its context, so its default target requires a selected set, a filter, or an explicit `--all` override. See the [installation guide](docs/users/getting-started.md) and [security guidance](docs/users/security-and-antivirus.md) for other targets, auditing, and failure modes.

## Choose Your Tool

Use the path for your agent. Core setup is available for Codex and Claude; the other rows show direct install targets or plugin options.

| Tool           | Install                                                                  | First Use                                              |
| -------------- | ------------------------------------------------------------------------ | ------------------------------------------------------ |
| Claude Code    | [AAS Core local MCP preview](docs/users/claude-code-skills.md), direct install, or Claude plugin marketplace | Ask Claude to choose and compose an AAS stack |
| Cursor         | `npx agentic-awesome-skills --cursor`                              | `@brainstorming help me plan a feature`              |
| Gemini CLI     | `npx agentic-awesome-skills --gemini`                              | `Use brainstorming to plan a feature`                |
| Codex CLI      | [AAS Core local MCP preview](docs/users/codex-cli-skills.md) or `npx agentic-awesome-skills --codex` | Ask Codex to choose and compose an AAS stack |
| Autohand Code  | `npx agentic-awesome-skills --path ~/.autohand/skills` or `--path .autohand/skills` | `Use brainstorming to plan a feature`                |
| Antigravity IDE | `npx agentic-awesome-skills --antigravity --skills <ids> --dry-run` | Ask an MCP-enabled agent to choose exact IDs first |
| Antigravity CLI (`agy`) | `npx agentic-awesome-skills --agy`                        | `/brainstorming help me plan a feature`              |
| Kiro CLI       | `npx agentic-awesome-skills --kiro`                                | `Use brainstorming to plan a feature`                |
| Kiro IDE       | `npx agentic-awesome-skills --path ~/.kiro/skills`                 | `Use @brainstorming to plan a feature`               |
| GitHub Copilot | `gh skill install sickn33/agentic-awesome-skills skills/brainstorming/SKILL.md --agent github-copilot --scope user --pin v14.2.0` (preview) | `A
