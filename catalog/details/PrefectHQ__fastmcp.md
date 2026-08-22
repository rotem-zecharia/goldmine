# PrefectHQ/fastmcp

🚀 The fast, Pythonic way to build MCP servers and clients.

## features

Building an effective MCP application is harder than it looks. FastMCP handles all of it. Declare a tool with a Python function, and the schema, validation, and documentation are generated automatically. Connect to a server with a URL, and transport negotiation, authentication, and protocol lifecycle are managed for you. You focus on your logic, and the MCP part just works: **with FastMCP, best practices are built in.**

**That's why FastMCP is the standard framework for working with MCP.** FastMCP 1.0 was incorporated into the official MCP Python SDK in 2024. Today, the actively maintained standalone project is downloaded a million times a day, and some version of FastMCP powers 70% of MCP servers across all languages.

FastMCP has three pillars:

<table>
<tr>
<td align="center" valign="top" width="33%">
<a href="https://gofastmcp.com/servers/server">
<img src="https://raw.githubusercontent.com/PrefectHQ/fastmcp/main/docs/assets/images/servers-card.png" alt="Servers" />
<br /><strong>Servers</strong>
</a>
<br />Expose tools, resources, and prompts to LLMs.
</td>
<td align="center" valign="top" width="33%">
<a href="https://gofastmcp.com/apps/overview">
<img src="https://raw.githubusercontent.com/PrefectHQ/fastmcp/main/docs/assets/images/apps-card.png" alt="Apps" />
<br /><strong>Apps</strong>
</a>
<br />Give your tools interactive UIs rendered directly in the conversation.
</td>
<td align="center" valign="top" width="33%">
<a href="https://gofastmcp.com/clients/client">
<img src="https://raw.githubusercontent.com/PrefectHQ/fastmcp/main/docs/assets/images/clients-card.png" alt="Clients" />
<br /><strong>Clients</strong>
</a>
<br />Connect to any MCP server — local or remote, programmatic or CLI.
</td>
</tr>
</table>

**[Servers](https://gofastmcp.com/servers/server)** wrap your Python functions into MCP-compliant tools, resources, and prompts. **[Clients](https://gofastmcp.com/clients/client)** connect to any server with full protocol support. And **[Apps](https://gofastmcp.com/apps/overview)** give your tools interactive UIs rendered directly in the conversation.

**Building in TypeScript?** [FastMCP for TypeScript](https://github.com/PrefectHQ/fastmcp-ts) is the official counterpart, built and maintained by the same team. Same pillars, same ideas, `npm install @prefecthq/fastmcp-ts`.

Ready to build? Start with the [installation guide](https://gofastmcp.com/getting-started/installation) or jump straight to the [quickstart](https://gofastmcp.com/getting-started/quickstart).

## installation

We recommend adding FastMCP to your project with [uv](https://docs.astral.sh/uv/):

```bash
uv add fastmcp
```

For full installation instructions, including verification and upgrading, see the [**Installation Guide**](https://gofastmcp.com/getting-started/installation).

**Upgrading?** We have guides for:
- [Upgrading from FastMCP 3](https://gofastmcp.com/getting-started/upgrading/from-fastmcp-3)
- [Upgrading from FastMCP 2](https://gofastmcp.com/getting-started/upgrading/from-fastmcp-2)
- [Upgrading from MCP SDK v1](https://gofastmcp.com/getting-started/upgrading/from-mcp-sdk-v1) or [v2](https://gofastmcp.com/getting-started/upgrading/from-mcp-sdk-v2)
- [Upgrading from the low-level SDK v1](https://gofastmcp.com/getting-started/upgrading/from-low-level-sdk-v1) or [v2](https://gofastmcp.com/getting-started/upgrading/from-low-level-sdk-v2)
