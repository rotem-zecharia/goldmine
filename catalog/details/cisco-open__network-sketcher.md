# cisco-open/network-sketcher

Network Sketcher is an AI-ready network design tool with Local MCP, Online, and Offline editions for creating network designs and exporting PowerPoint diagrams and Excel-based configuration data.

## installation

<img  alt="ns_demo_mcp" src="https://github.com/user-attachments/assets/1b9a85f9-0785-4dbb-b980-68ec0c1f31c9" />



The quickest way to try Network Sketcher with an AI agent is the Local MCP edition.

### 1. Install

```bash
git clone https://github.com/cisco-open/network-sketcher/
cd network-sketcher/network-sketcher_local_mcp
python -m pip install -r requirements_mcp.txt
```

### 2. Add it to your MCP client

For Cursor, add this to your MCP configuration:

```json
{
  "mcpServers": {
    "network-sketcher": {
      "command": "python",
      "args": [
        "/path/to/network-sketcher/network-sketcher_local_mcp/ns_mcp_server.py"
      ]
    }
  }
}
```

For Claude Code:

```bash
claude mcp add network-sketcher -- python "/path/to/network-sketcher/network-sketcher_local_mcp/ns_mcp_server.py"
```

Replace `/path/to/network-sketcher/` with your local clone path.

### 3. Ask your agent to build a network

Example prompt:

```text
Using Network Sketcher Local MCP, create a small 5-site WAN design with HQ, two data centers, two branches, Internet and WAN waypoints, edge routers, simple L2 segments, and representative IP addressing. Then build the default L1/L2/L3 diagrams and device table.
```

The generated files will be saved in your Network Sketcher workspace.

<img  alt="image" src="https://github.com/user-attachments/assets/26068524-6293-4f7f-ab0c-f6b7e2c8b842" />

<img  alt="image" src="https://github.com/user-attachments/assets/b3501923-195e-45bc-9120-f6b78396e300" />



## Ecosystem & Integrations

Network Sketcher Local MCP is listed on the official MCP Registry and major MCP platforms:

- **Registries:** [MCP Registry](https://registry.modelcontextprotocol.io/?q=network-sketcher) · [Glama](https://glama.ai/mcp/servers/cisco-open/network-sketcher) · [PulseMCP](https://www.pulsemcp.com/servers/network-sketcher)
- **Hubs:** [LobeHub](https://lobehub.com/mcp/cisco-open-network-sketcher)

Network Sketcher provides three editions:

- [**Network Sketcher Local MCP**](#network-sketcher-local-mcp) — **AI-native MCP server for LLM clients (Cursor, Claude Code, etc.)**. The most direct AI integration: the LLM calls Network Sketcher tools without a browser or copy-paste.
- [**Network Sketcher Online**](#network-sketcher-online) — Browser-based web service.
- [**Network Sketcher Offline**](#network-sketcher-offline) — Desktop GUI + CLI. Runs independently with the `network-sketcher_offline/` folder alone.

You can use any combination.

| | **Local MCP (AI-native)** | Online (Web Service) | Offline (GUI + CLI) |
| --- | --- | --- | --- |
| Interface | **LLM client (Cursor, Claude Code, etc.)** | Web browser | Desktop GUI / Command-line |
| Key dependencies | **Python + MCP SDK** | Python + Flask | Python + tkinter |
| Multi-user | Single user | Multiple users via browser | Single user |
| Client requires | **Python + MCP client** | Web browser only | Python runtime environment |
| AI-native design | **Yes (most direct)** | Yes | No |
| Master format | **`.nsm` only** | `.xlsx` / `.nsm` both | `.xlsx` only |
| Internal data storage | No | No | No |
| External communication | stdio to LLM client (local) | [HTTPS](https://github.com/cisco-open/network-sketcher/wiki/User_Guide(Online_Edition)%5BEN%5D#external-communication) | No |
| Tested platforms | Windows (Mac OS, Linux compatible by design) | Windows (Mac OS, Linux untested) | Windows, Mac OS, Linux |
| Folder | **`network-sketcher_local_mcp/`** | `network-sketcher_online/` | `network-sketcher_offline/` |

```
network-sketcher/
├── network-sketcher_local_mcp/  # Local MCP edition — MCP server for LLM clients (AI-native)
├── network-sketcher_online/     # Online edition — Web service (browser-based)
├── network-sketcher_offline/    # Offline edition — GUI + CLI (standalone desktop app)
├── README.md
├── LICENSE
└── ...
```

## Extensions: Cisco & Third-Party Converters

The [Network Sketcher Cisco Extension](https://github.com/CiscoDevNet/network-sketcher-cisco-extension) repository

## features

- **No browser, no copy-paste.** The LLM calls `add device ...` and similar commands as Tool invocations
- Reuses `network-sketcher_online/ns_engine/` **as a library** (no code duplication)
- **No changes** are made to the existing `_online` / `_offline` folders
- stdio transport (designed for local operation)
- **Platform import workflow:** See [Extensions: Cisco & Third-Party Converters](#extensions-cisco--third-party-converters) above (`run_commands` + `build_default_outputs`)

## limitations

- Single-user edition designed to run on a local PC
- Only stdio transport is supported (HTTP/SSE not supported)
- Diagram generation for large networks may take some time
- LLM clients cannot directly view binary output (PPTX / SVG); if visual feedback is needed, the user should open the generated SVG directly
- **Verification status:** End-to-end verified in both Cursor and Claude Code. The server follows the standard MCP specification, so any MCP-compatible AI agent/client is expected to work, not just these two.

## requirements

- Python 3.10 or later (required by the MCP SDK; the engine itself supports 3.9+)
- The full Network Sketcher repository (the `network-sketcher_online/` folder must be present)
- **Recommended LLM: Claude Opus 4.7 or later.** The Local MCP edition relies heavily on multi-step tool calling, schema interpretation, and adherence to the layout / workflow rules embedded in the server instructions and AI Context (e.g., RULE 0 / 0.5 layout, RULE 3.5 multi-transport WAN waypoint design, mandatory `get_workspace_info` to `get_ai_context` bootstrap). Weaker or older models may struggle with these workflows.

## tools

Cursor and Claude Code use different configuration mechanisms, so the setup steps are split below. Pick the one that matches your client.

### For Cursor

Add the following to the Cursor MCP configuration file (`File > Preferences > Cursor Settings > MCP` → `mcp.json`):

```json
{
  "mcpServers": {
    "network-sketcher": {
      "command": "python",
      "args": [
        "/path/to/network-sketcher/network-sketcher_local_mcp/ns_mcp_server.py"
      ]
    }
  }
}
```

Replace `/path/to/network-sketcher/` with the actual path where you cloned the repository.
On Windows, you can use either forward slashes (`/`) or escaped backslashes (`\\`).

### For Claude Code

Register the MCP server with the `claude` CLI. The `--` (double dash) separator is required so that the script path is passed to `python` rather than parsed as a flag of `claude mcp add`:

```bash
# Local scope (default; current project only, stored in ~/.claude.json)
claude mcp add network-sketcher -- python "/path/to/network-sketcher/network-sketcher_local_mcp/ns_mcp_server.py"

# User scope (available across all your projects)
claude mcp add --scope user network-sketcher -- python "/path/to/network-sketcher/network-sketcher_local_mcp/ns_mcp_server.py"

# Project scope (shared with team via .mcp.json in project root)
claude mcp add --scope project network-sketcher -- python "/path/to/network-sketcher/network-sketcher_local_mcp/ns_mcp_server.py"
```

Replace `/path/to/network-sketcher/` with the actual path where you cloned the repository. See the [Claude Code MCP installation scopes documentation](https://docs.claude.com/en/docs/claude-code/mcp#mcp-installation-scopes) for details on each scope and when to use which.

## User Guide (Local MCP)
| Language  | Link |
| ------------- | ------------- |
| English  | [Link](https://github.com/cisco-open/network-sketcher/wiki/User_Guide(Local_MCP_Edition)%5BEN%5D) |
| Japanese  | [Link](https://github.com/cisco-open/network-sketcher/wiki/User_Guide(Local_MCP_Edition)%5BJP%5D) |

<br>
<br>

<p align="center">━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━</p>

<br>

# Network Sketcher Online

> **AI-native software:** Network Sketcher Online is designed around AI (LLM) interaction — generate AI context, send it to an LLM, and paste the resulting commands back to update your network design, all within the browser.


<img  alt="image" src="https://github.com/user-attachments/assets/cd645a8b-9661-4f74-8bf3-cd12b3395c82" />


### Demo Video (Ver 3.0.1b)

A demo video of approximately 4 minutes, starting with the installation of Network Sketcher. This demo video demonstrates creating a network configuration using LLM from URL information and performing additional editing. No sound, no captions.


https://github.com/user-attachments/assets/2acaea3b-32f2-4ff0-90ad-a3dc810293d2



## What is Network Sketcher Online?

Network Sketcher Online is a browser-based web service. It wraps the Network Sketcher CLI and provides an intuitive web UI for diagram generation and AI-driven network design — no python on PCs required.
