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
}
```

---

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

## Tools

- `search_cometchat_docs` — Search across SDK guides, UI Kit references, REST API documentation, and OpenAPI specs. Returns ranked snippets with titles + direct links. Optional `version` filter.
- `fetch_cometchat_doc_page` — Fetch the full content of any documentation page as markdown by URL or relative path.
- `get_cometchat_implementation_bundle` — Return a curated implementation bundle for a named scenario — prerequisites, install commands, configuration, working code.
- `list_cometchat_bundles` — List every available implementation bundle (identifier, title, framework, last-verified date) for discovery.

All four carry `readOnlyHint: true`, a `title` annotation, and a declared `outputSchema` with structured results. Names are ≤ 64 characters. Descriptions describe contracts only — no behavioral instructions to the agent, no cross-tool routing, no marketing language.

## Resources

| URI | Purpose |
|---|---|
| `cometchat://skills/overview` | Agent orientation skill — Product summary, decision guidance, workflow, common gotchas, verification checklist |
| `cometchat://bundles/react-uikit-quickstart` | React UI Kit install + init + login + chat surface |
| `cometchat://bundles/react-native-uikit-quickstart` | React Native UI Kit with navigation and chat screen |
| `cometchat://bundles/flutter-uikit-quickstart` | Flutter UI Kit install + init + basic chat |
| `cometchat://bundles/ios-uikit-quickstart` | iOS UI Kit (SwiftUI) install + chat view |
| `cometchat://bundles/android-uikit-quickstart` | Android UI Kit (Jetpack Compose) install + chat screen |
| `cometchat://bundles/js-sdk-messaging-basics` | Vanilla JS SDK — send/receive text and media messages |
| `cometchat://bundles/widget-embed` | No-code widget embed for HTML, Squarespace, Webflow, Wix, WordPress, Shopify |
| `cometchat://bundles/moderation-setup` | AI moderation rules, image moderation, webhooks |
| `cometchat://bundles/multi-tenant-chat` | Multi-tenant SaaS chat — tenant isolation, server-issued Auth Tokens |
| `cometchat://bundles/presence-and-typing` | Online presence, typing indicators, read receipts |

---

## How it works

1. **You prompt your agent** in natural language.
2. **The agent reads the orientation skill** (`cometchat://skills/overview`) to understand which tool/bundle fits your request.
3. **For top scenarios**, the agent pulls a curated implementation bundle — ready-to-run code with prerequisites, install commands, configuration, and working examples.
4. **For long-tail questions**, the agent searches CometChat's docs and reads specific reference pages.
5. **The agent writes the code** into your project, using the bundle as the source of truth and your project structure as the constraint.

---

## CometChat in 30 seconds

CometChat is a real-time communications platform for adding chat, voice, and video calling to web and mobile apps. Used in production across SaaS, marketplaces, gaming, healthcare, education, and creator platforms.

- **Free tier:** first 100 monthly active users, no credit card required.
- **SDKs:** JavaScript, React Native, iOS, Android, Flutter.
- **UI Kits:** React, React Native, iOS, Android, Flutter, Angular, Vue.
- **No-code:** chat widget for any HTML site.
- **Sign up:** [`app.cometchat.com`](https://app.cometchat.com) — you'll need an App ID, Auth Key, 
