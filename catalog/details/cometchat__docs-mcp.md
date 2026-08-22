# cometchat/docs-mcp

CometChat docs search + implementation bundles: add chat, voice, video & moderation to your app through your AI coding agent.

## installation

| Agent | How to add |
|---|---|
| **Claude.ai / Claude Desktop** | Settings → Connectors → Add custom connector → URL: `https://mcp.cometchat.com/mcp` |
| **Cursor** | `Cmd+Shift+P` → Open MCP settings → Add custom MCP → paste config below |
| **Windsurf** | Plugins (hammer icon) → Manage plugins → View raw config → paste config below |
| **VS Code (Copilot Agent)** | `Cmd+Shift+P` → MCP: Add MCP Server → URL: `https://mcp.cometchat.com/mcp`, Transport: HTTP |
| **Claude Code (CLI)** | `claude mcp add --transport http cometchat https://mcp.cometchat.com/mcp` |
| **Smithery** | `npx -y smithery mcp add cometchat/docs-mcp` |
| **Codex CLI** | `codex plugin marketplace add cometchat/docs-mcp` |

## configuration

```json
{
  "mcpServers": {
    "cometchat": {
      "url": "https://mcp.cometchat.com/mcp"
    }
  }

## tools

After connecting, prompt your agent with any of these:

- *"How do I install the React UI Kit in my Vite project?"*
- *"Walk me through multi-tenant chat for a Next.js SaaS where workspaces are isolated."*
- *"Show me how to add presence indicators and typing dots to my iOS conversation list."*
- *"Set up content moderation so banned words are blocked before delivery."*
- *"Build a no-code chat widget for my Webflow site."*
- *"What's the rate limit for sending messages, and what error code do I get when I hit it?"*

The agent reads CometChat's documentation, pulls the relevant implementation bundle, and writes the integration code into your project.

---
