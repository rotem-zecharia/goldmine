# zapier/zapier-mcp

Official plugin distribution for the hosted Zapier MCP server. Install it in your AI client and connect to thousands of apps.

## tools

[Zapier MCP](https://docs.zapier.com/mcp/home) gives any MCP-compatible AI client governed access to 9,000+ apps — send messages, pull data, trigger workflows, all in plain English. No code, no infrastructure, SOC 2 Type II certified. ⚡

This repo distributes the Zapier MCP plugin — the part that lives in your AI client. Install it from your client's marketplace and your assistant arrives knowing how to use Zapier well, with guided onboarding, a quick demo, and skills tailored to your role.

![AI connects to Zapier MCP, which connects to Gmail, Slack, Google Sheets, Notion, HubSpot, Salesforce, Linear, Asana, and 9,000 more apps](./assets/mcp-apps-diagram.png)

## What's in this repo

- **[`plugins/zapier/`](./plugins/zapier/)**: the plugin that onboards you to Zapier MCP and supercharges your experience

## installation

Connecting Zapier MCP to your AI client only takes a server URL — see [docs.zapier.com/mcp/clients](https://docs.zapier.com/mcp/clients) for step-by-step instructions for every supported client.

A few clients also install the plugin distributed from this repo, which layers guided onboarding, a first-use demo, and role-tailored skills on top of that base connection:

- **Claude Code**: add [`zapier/marketplace`](https://github.com/zapier/marketplace) or [`anthropics/claude-plugins-official`](https://github.com/anthropics/claude-plugins-official)
- **Cursor**: use the badge above, or add [`cursor/mcp-servers`](https://github.com/cursor/mcp-servers/tree/main/servers/zapier)
- **OpenAI Codex** and **GitHub Copilot CLI**: add [`zapier/marketplace`](https://github.com/zapier/marketplace)
- **Claude Cowork**: add [`anthropics/knowledge-work-plugins`](https://github.com/anthropics/knowledge-work-plugins)
- **Kiro**: via [kiro.dev/powers](https://kiro.dev/powers)
- **Gemini CLI**: `gemini extensions install https://github.com/zapier/zapier-mcp`, then `/mcp auth zapier` — see [`gemini-extension.json`](./gemini-extension.json)

VS Code connects directly to the hosted MCP server rather than through a plugin — use the badge above, or add `https://mcp.zapier.com/api/v1/connect` (`type: http`) manually.

## Third-party registries

Zapier MCP is also listed on:

- [Smithery](https://smithery.ai/servers/zapier)
- [PulseMCP](https://www.pulsemcp.com/servers/zapier)

## For contributors

- [AGENTS.md](./AGENTS.md): guide for AI agents working in this repo
- [CONTRIBUTING.md](./CONTRIBUTING.md): how to contribute
- [llms.txt](./llms.txt): LLM discovery index
