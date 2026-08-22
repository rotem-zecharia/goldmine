# mrexodia/ida-pro-mcp

AI-powered reverse engineering assistant that bridges IDA Pro with language models through MCP.

## requirements

- [Python](https://www.python.org/downloads/) (**3.11 or higher**)
  - Use `idapyswitch` to switch to the newest Python version
- [IDA Pro](https://hex-rays.com/ida-pro) (8.3 or higher, 9 recommended), **IDA Free is not supported**
- Supported MCP Client (pick one you like)
  - [Amazon Q Developer CLI](https://aws.amazon.com/q/developer/)
  - [Augment Code](https://www.augmentcode.com/)
  - [Claude](https://claude.ai/download)
  - [Claude Code](https://www.anthropic.com/code)
  - [Cline](https://cline.bot)
  - [Codex](https://github.com/openai/codex)
  - [Copilot CLI](https://docs.github.com/en/copilot)
  - [Crush](https://github.com/charmbracelet/crush)
  - [Cursor](https://cursor.com)
  - [Gemini CLI](https://google-gemini.github.io/gemini-cli/)
  - [Kilo Code](https://kilo.ai/)
  - [Kiro](https://kiro.dev/)
  - [LM Studio](https://lmstudio.ai/)
  - [Opencode](https://opencode.ai/)
  - [Qodo Gen](https://www.qodo.ai/)
  - [Qwen Coder](https://qwenlm.github.io/qwen-code-docs/)
  - [Roo Code](https://roocode.com)
  - [Trae](https://trae.ai/)
  - [VS Code](https://code.visualstudio.com/)
  - [VS Code Insiders](https://code.visualstudio.com/insiders)
  - [Warp](https://www.warp.dev/)
  - [Windsurf](https://windsurf.com)
  - [Zed](https://zed.dev/)
  - [Kimi Code](https://moonshotai.github.io/kimi-code/en/)
  - [Other MCP Clients](https://modelcontextprotocol.io/clients#example-clients): Run `ida-pro-mcp --config` to get the JSON config for your client.

**Note**: This requires having idalib activated globally and [uv](https://astral.sh/uv) installed:

```bash
# windows
uv run "C:\Program Files\IDA Professional 9.3\idalib\python\py-activate-idalib.py"
# macos
uv run "/Applications/IDA Professional 9.3.app/Contents/MacOS/idalib/python/py-activate-idalib.py"
# linux
uv run "/path/to/idapro-9.3/idalib/python/py-activate-idalib.py"
```

## installation

To install the latest IDA Pro MCP in Claude Code:

```bash
claude plugin marketplace add mrexodia/claude-marketplace
claude plugin uninstall ida-pro-mcp@mrexodia
claude plugin install ida-pro-mcp@mrexodia
```

## Installation (Codex)

To install the latest IDA Pro MCP in Codex:

```bash
codex plugin marketplace add mrexodia/codex-marketplace
codex plugin remove ida-pro-mcp@mrexodia
codex plugin add ida-pro-mcp@mrexodia
```

## Installation (Kimi Code)

To install the latest IDA Pro MCP in Kimi Code, run this slash command in the chat:

```
/plugins install https://github.com/mrexodia/ida-pro-mcp/tree/main
/reload
```

This installs the `idalib` MCP server and the `idapython` skill. Plugins are copied to
`$KIMI_CODE_HOME/plugins/managed/`, so `uv` must be on your `PATH`. The first session after
installing is slower, because `uv` resolves the dependencies before the server responds.

## Installation (GUI)

**Note**: the MCP plugin is no longer recommended and will eventually be deprecated. Use `idalib-mcp` instead.

If you want to configure the MCP server manually from the IDA GUI:

```sh
pip uninstall ida-pro-mcp
pip install https://github.com/mrexodia/ida-pro-mcp/archive/refs/heads/main.zip
```

Configure the MCP servers and install the IDA Plugin:

```
ida-pro-mcp --install
```

**Important**: Make sure you completely restart IDA and your MCP client for the installation to take effect. Some clients (like Claude) run in the background and need to be quit from the tray icon.

## Prompt Engineering

LLMs are prone to hallucinations and you need to be specific with your prompting. For reverse engineering the conversion between integers and bytes are especially problematic. Below is a minimal example prompt, feel free to start a discussion or open an issue if you have good results with a different prompt:

```md
Your task is to analyze a crackme in IDA Pro. You can use the MCP tools to retrieve information. In general use the following strategy:

- Inspect the decompilation and add comments with your findings
- Rename variables to more sensible names
- Change the variable and argument types if necessary (especially pointer and array types)
- Change function names to be more descriptive
- If more details are necessary, disassemble the function and add comments with your findings
- NEVER convert number bases yourself. Use the `int_convert` MCP tool if needed!
- Do not attempt brute forcing, derive any solutions purely from the disassembly and simple python scripts
- Create a report.md with your findings and steps taken at the end
- When you find a solution, prompt to user for feedback with the password you found
```

This prompt was just the first experiment, please share if you found ways to improve the output!

Another prompt by [@can1357](https://github.com/can1357):

```md
Your task is to create a complete and comprehensive reverse engineering analysis. Reference AGENTS.md to understand the project goals and ensure the analysis serves our purposes.

Use the following systematic methodology:

1. **Decompilation Analysis**
   - Thoroughly inspect the decompiler output
   - Add detailed comments documenting your findings
   - Focus on understanding the actual functionality and purpose of each component (do not rely on old, incorrect comments)

2. **Improve Readability in the Database**
   - Rename variables to sensible, descriptive names
   - Correct variable and argument types where necessary (especially pointers and array types)
   - Update function names to be descriptive of their actual purpose

3. **Deep Dive When Needed**
   - If more details are necessary, examine the disassembly and add comments with findings
   - Document any low-level behaviors that aren't clear from the decompilation alone
   - Use sub-agents to perform detailed analysis

4. **Important Constraints**
   - NEVER convert number bases yourself - use the int_convert MCP tool if needed
   - Use MCP tools to retrieve information as necessary
   - Derive all co

## tools

- `idb_open(input_path, mode="prefer_headless", run_auto_analysis=True, build_caches=True, init_hexrays=True, preferred_session_id="")`: Open a binary, warm up subsystems (strings cache, Hex-Rays), and return its session ID. If a worker or GUI for this path is already running on the host, that instance is adopted and `preferred_session_id` is ignored.
- `idb_list()`: List open sessions and running GUI IDA instances. Each entry has `adopted` (True if this supervisor manages it, False for GUIs/workers discovered but not yet opened via `idb_open`), `backend` (`worker` or `gui`), `is_active`, and process IDs.
- `idb_close(database, save=True)`: Save (optionally), unregister the session, and terminate its owned worker, freeing a slot toward `--max-workers`. Adopted GUI/worker instances are detached, not killed.
- `idb_save(session_id, path="")`: Save a session's IDB to disk. Forwarded as a regular worker tool (`database=<id>` injected) — same signature in both backends.
- Per-database health: call `server_health(database=<id>)` (forwarded). `idb_list()` reports `is_active` from the supervisor's TCP/RPC probe.

Worker controls:

- `--max-workers N`: maximum simultaneous database workers (`0` = unlimited, default `4`).
- `IDA_MCP_MAX_WORKERS`: environment default for `--max-workers`.


## MCP Resources

**Resources** represent browsable state (read-only data) following MCP's philosophy.

**Core IDB State:**
- `ida://idb/metadata` - IDB file info (path, arch, base, size, hashes)
- `ida://idb/segments` - Memory segments with permissions
- `ida://idb/entrypoints` - Entry points (main, TLS callbacks, etc.)

**UI State:**
- `ida://cursor` - Current cursor position and function
- `ida://selection` - Current selection range

**Type Information:**
- `ida://types` - All local types
- `ida://structs` - All structures/unions
- `ida://struct/{name}` - Structure definition with fields

**Lookups:**
- `ida://import/{name}` - Import details by name
- `ida://export/{name}` - Export details by name
- `ida://xrefs/from/{addr}` - Cross-references from address

## Core Functions

- `lookup_funcs(queries)`: Get function(s) by address or name (auto-detects, accepts list or comma-separated string).
- `int_convert(inputs)`: Convert numbers to different formats (decimal, hex, bytes, ASCII, binary).
- `list_funcs(queries)`: List functions (paginated, filtered).
- `list_globals(queries)`: List global variables (paginated, filtered).
- `imports(offset, count)`: List all imported symbols with module names (paginated).
- `decompile(addr)`: Decompile function at the given address.
- `disasm(addr)`: Disassemble function with full details (arguments, stack frame, etc).
- `xrefs_to(addrs)`: Get all cross-references to address(es).
- `xrefs_to_field(queries)`: Get cross-references to specific struct field(s).
- `callees(addrs)`: Get functions called by function(s) at address(es).

## Modification Operations

- `add_bookmark(addr, name, prefix)`: Add or replace the IDA bookmark at an address; set `prefix=""` for no prefix.
- `set_comments(items)`: Set comments at address(es) in both disassembly and decompiler views.
- `patch_asm(items)`: Patch assembly instructions at address(es).
- `declare_type(decls)`: Declare C type(s) in the local type library.
- `define_func(items)`: Define function(s) at address(es). Optionally specify `end` for explicit bounds.
- `define_code(items)`: Convert bytes to code instruction(s) at address(es).
- `undefine(items)`: Undefine item(s) at address(es), converting back to raw bytes. Optionally specify `end` or `size`.

## Memory Reading Operations

- `get_bytes(addrs)`: Read raw bytes at address(es).
- `get_int(queries)`: Read integer values using ty (i8/u64/i16le/i16be/etc).
- `get_string(addrs)`: Read null-terminated string(s).
- `get_global_value(queries)`: Read global variable value(s) by address or name (auto-detects, compile-time values).

## Stack Frame Operations

- `stack_frame(addrs)`: Get stack frame variables for function(s).
- `
