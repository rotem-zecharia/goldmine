# oOo0oOo/lean-lsp-mcp

Lean Theorem Prover MCP

## features

* **Rich Lean Interaction**: Access diagnostics, goal states, term information, hover documentation and more.
* **External Search Tools**: Use `LeanSearch`, `Loogle`, `Lean Finder`, `Lean Hammer` and `Lean State Search` to find relevant theorems and definitions.
* **Easy Setup**: Simple configuration for various clients, including VSCode, Cursor and Claude Code.

## installation

[Install uv](https://docs.astral.sh/uv/getting-started/installation/) for your system. On Linux/MacOS: `curl -LsSf https://astral.sh/uv/install.sh | sh`

### 1b. Alternative: Install with Nix

If you use Nix, you can install the package directly from GitHub:

```bash
nix profile install github:oOo0oOo/lean-lsp-mcp
```

Or run it without installing: `nix run github:oOo0oOo/lean-lsp-mcp`.

This provides the MCP server only. You still need a Lean toolchain (`elan`/`lake`) for your project, same as the `uv` setup below.

### 2. Run `lake build`

`lean-lsp-mcp` will run `lake serve` in the project root to use the language server (for most tools). Some clients (e.g. Cursor) might timeout during this process. Therefore, it is recommended to run `lake build` manually before starting the MCP. This ensures a faster build time and avoids timeouts.

### 3. Configure your IDE/Setup

<details>
<summary><b>VSCode (Click to expand)</b></summary>
One-click config setup:

[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_Server-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=lean-lsp&config=%7B%22command%22%3A%22uvx%22%2C%22args%22%3A%5B%22lean-lsp-mcp%22%5D%7D)

[![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Server-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=lean-lsp&config=%7B%22command%22%3A%22uvx%22%2C%22args%22%3A%5B%22lean-lsp-mcp%22%5D%7D&quality=insiders)

OR using the setup wizard:

Ctrl+Shift+P > "MCP: Add Server..." > "Command (stdio)" > "uvx lean-lsp-mcp" > "lean-lsp" (or any name you like) > Global or Workspace

OR manually adding config by opening `mcp.json` with: 

Ctrl+Shift+P > "MCP: Open User Configuration"

and adding the following

```jsonc
{
    "servers": {
        "lean-lsp": {
            "type": "stdio",
            "command": "uvx",
            "args": [
                "lean-lsp-mcp"
            ]
        }
    }
}
```

If you installed VSCode on Windows and are using WSL2 as your development environment, you may need to use this config instead:

```jsonc
{
    "servers": {
        "lean-lsp": {
            "type": "stdio",
            "command": "wsl.exe",
            "args": [
                "uvx",
                "lean-lsp-mcp"
            ]
        }
    }
}
```
If that doesn't work, you can try cloning this repository and replace `"lean-lsp-mcp"` with `"/path/to/cloned/lean-lsp-mcp"`.

</details>

<details>
<summary><b>Cursor (Click to expand)</b></summary>
1. Open MCP Settings (File > Preferences > Cursor Settings > MCP)

2. "+ Add a new global MCP Server" > ("Create File")

3. Paste the server config into `mcp.json` file:

```jsonc
{
    "mcpServers": {
        "lean-lsp": {
            "command": "uvx",
            "args": ["lean-lsp-mcp"]
        }
    }
}
```
</details>

<details>
<summary><b>Claude Code (Click to expand)</b></summary>
Run one of these commands in the root directory of your Lean project (where `lakefile.toml` is located):

```bash
# Local-scoped MCP server
claude mcp add lean-lsp uvx lean-lsp-mcp

# OR project-scoped MCP server
# (creates or updates a .mcp.json file in the current directory)
claude mcp add lean-lsp -s project uvx lean-lsp-mcp
```

You can find more details about MCP server configuration for Claude Code [here](https://docs.anthropic.com/en/docs/agents-and-tools/claude-code/tutorials#configure-mcp-servers).
</details>

<details>
<summary><b>Mistral Vibe (Click to expand)</b></summary>
(These instructions cover Mac/Linux.)

1. Edit `~/.vibe/config.toml`.

2. Paste the following into the file (e.g. at the end):
```toml
[[mcp_servers]]
name = "lean-lsp"
transport = "stdio"
command = "uvx"
args = ["lean-lsp-mcp"]
tool_timeout_sec = 600
```
If there are no existing MCP servers, you may have to remove `mcp_servers = []`.
</details>

### 4. Install ripgrep (optional but recommended)


## tools

### List of available tools

See [Tools documentation](docs/tools.md) for the full list of available tools.

### Disabling Tools

Many clients allow the user to disable specific tools manually (e.g. lean_build).

**VSCode**: Click on the Wrench/Screwdriver icon in the chat.

**Cursor**: In "Cursor Settings" > "MCP" click on the name of a tool to disable it (strikethrough).

You can also disable tools at server startup:

- `LEAN_MCP_DISABLED_TOOLS`: Comma-separated tool names (for example `lean_run_code,lean_build`).
- `LEAN_MCP_INSTRUCTIONS`: Replacement server instructions string.
- `LEAN_MCP_TOOL_DESCRIPTIONS`: JSON object to override tool descriptions.

Example:

```bash
export LEAN_MCP_DISABLED_TOOLS="lean_run_code,lean_build"
export LEAN_MCP_INSTRUCTIONS="Prefer lean_local_search before remote search tools."
export LEAN_MCP_TOOL_DESCRIPTIONS='{"lean_goal":"Primary proof-state inspection tool."}'
```

## configuration

This MCP server works out-of-the-box without any configuration. However, a few optional settings are available.

### Environment Variables

- `LEAN_LOG_LEVEL`: Log level for the server. Options are "INFO", "WARNING", "ERROR", "NONE". Defaults to "INFO".
- `LEAN_LOG_FILE_CONFIG`: Config file path for logging, with priority over `LEAN_LOG_LEVEL`. If not set, logs are printed to stdout.
- `LEAN_PROJECT_PATH`: Path to your Lean project root. A valid Lean project root must contain `lean-toolchain` and either `lakefile.lean` or `lakefile.toml`. Relative `file_path` arguments resolve against this root. This variable is required for `streamable-http` and `sse`.
- `LEAN_MCP_DISABLED_TOOLS`: Comma-separated list of tool names to remove from MCP tool listing.
- `LEAN_MCP_INSTRUCTIONS`: Replacement server instructions string.
- `LEAN_MCP_TOOL_DESCRIPTIONS`: JSON object mapping tool names to replacement descriptions.
- `LEAN_MCP_SCRATCH_SLOTS`: Number of parallel scratch documents used for snippet
  trials. Defaults to `1`; increase it only when parallel attempts are worth the
  additional Lean process memory.
- `LEAN_REPL`: Set to `true`, `1`, or `yes` to enable fast REPL-based `lean_run_code` and line-based `lean_multi_attempt` (see [REPL Setup](#repl-setup)).
- `LEAN_REPL_PATH`: Path to the `repl` binary. Auto-detected from `.lake/packages/repl/` or `.lake/packages/REPL/` if not set.
- `LEAN_REPL_TIMEOUT`: Per-command timeout in seconds (default: 60).
- `LEAN_REPL_MEM_MB`: Max memory per REPL in MB (default: 16384). Only enforced on Linux/macOS.
- `LEAN_LSP_MCP_TOKEN`: Secret token for bearer authentication when using `streamable-http` or `sse` transport. If set, bearer auth is required for every request.
- `LEAN_BUILD_CONCURRENCY`: Build concurrency mode for `lean_build`. Options: `allow` (default), `cancel`, `share`.
- `LEAN_STATE_SEARCH_URL`: URL for a self-hosted [premise-search.com](https://premise-search.com) instance. Rate limits are skipped when set to a custom backend.
- `LEAN_HAMMER_URL`: URL for a self-hosted [Lean Hammer Premise Search](https://github.com/hanwenzhu/lean-premise-server) instance. Rate limits are skipped when set to a custom backend.
- `LEAN_LOOGLE_LOCAL`: Set to `true`, `1`, or `yes` to enable local loogle (see [Local Loogle](#local-loogle) section).
- `LEAN_LOOGLE_CACHE_DIR`: Override the cache directory for local loogle (default: `~/.cache/lean-lsp-mcp/loogle`).
- `LOOGLE_URL`: URL for a self-hosted Loogle instance (default: `https://loogle.lean-lang.org`). Rate limits are skipped when set to a custom backend.
- `LOOGLE_HEADERS`: JSON object of extra HTTP headers for Loogle requests (e.g. `'{"X-API-Key": "..."}'`).

You can also often set these environment variables in your MCP client configuration:
<details>
<summary><b>VSCode mcp.json Example</b></summary>

```jsonc
{
    "servers": {
        "lean-lsp": {
            "type": "stdio",
            "command": "uvx",
            "args": [
                "lean-lsp-mcp"
            ],
            "env": {
                "LEAN_PROJECT_PATH": "/path/to/your/lean/project",
                "LEAN_LOG_LEVEL": "NONE"
            }
        }
    }
}
```
</details>

### Transport Methods

The Lean LSP MCP server supports the following transport methods:

- `stdio`: Standard input/output (default)
- `streamable-http`: HTTP streaming
- `sse`: Server-sent events (MCP legacy, use `streamable-http` if possible)

`stdio` supports project inference and switching as you move between Lean projects. `streamable-http` and `sse` are single-project deployments: they require `LEAN_PROJECT_PATH` at startup and reject tool-driven project switching.

You can specify the transport method using the `--transport` argument when running the server. For `sse` and `streamable-http` you can also optionally specify the host and port:

```bash
uvx lean-lsp-mcp --transport stdio # Default transport
uvx lean-lsp-mcp --transport streamable-http # Available at http://127.0.0.1:8000/mcp
uvx lean-ls
