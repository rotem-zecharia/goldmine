# mrpulor-gh/nuphus-mcp

Desktop automation MCP server — computer use for any AI agent: control screen, windows, mouse/keyboard, and Chrome via Model Context Protocol (stdio)

## features

- **38 MCP tools** (15 desktop + 23 browser) — screenshots, window control,
  mouse/keyboard, Chrome CDP automation, and more — see [TOOLS.md](TOOLS.md) /
  [TOOLS.zh-CN.md](TOOLS.zh-CN.md) for the full reference.
- **Desktop automation**: screen size, screenshot (PNG/base64), window list,
  window activate/screenshot/move/resize/info, mouse click/drag/scroll/position,
  keyboard input/hotkey, clipboard write/clean — implemented on the
  `desktop-api` crate (xcap + Win32, no Tauri dependency).
- **Computer vision pair**: `desktop_vision` (BYOK — send a screenshot to your
  own vision model via an OpenAI-compatible or Anthropic native API) +
  `desktop_perceive` (local OCR with PaddleOCR, models auto-downloaded on first
  run; optional YOLO icon detection). Used together they give AI agents **both
  semantic understanding
  and pixel-precise coordinates** — the battle-tested vision→perceive flow from
  the Nuphus desktop app. See [TOOLS.md](TOOLS.md) for BYOK env vars, model
  setup, and the recommended flow.
- **Browser automation**: navigate, snapshot (accessibility tree with `@N`
  refs), click, type, exec, scroll, extract, screenshot, evaluate,
  back/forward, wait_for, cookies get/set/import, upload, tabs, downloads —
  implemented on `nuphus-browser` (chromiumoxide CDP).
- **Zero-cost stdio**: no HTTP server, no daemon. The process reads
  single-line JSON from stdin and writes responses to stdout.
- **Safety-first**: destructive tools are annotated per the MCP spec; optional
  strict-confirm mode; path validation for screenshots, uploads, and file drags.

## requirements

- **Rust toolchain** (stable) — build from source with Cargo.
- **Chrome or Edge** — required for browser tools. The server auto-detects an
  installed browser; if none is found, `browser_*` tools return a clear error.
- **Windows recommended** for full desktop control — see Platform Support below.

## installation

**Install via npm (recommended — all platforms, prebuilt binaries):**

```sh
npm install -g @nuphus/nuphus-mcp
```

The `nuphus-mcp` meta package installs the prebuilt binary for your platform
automatically (Windows x64/arm64, macOS arm64, Linux x64/arm64) and puts the
`nuphus-mcp` command on your PATH. No Rust toolchain needed:

```sh
nuphus-mcp   # stdio MCP server
```

**Build from source** (requires the Rust toolchain):

```sh
cargo build --release -p nuphus-mcp

## configuration

export NUPHUS_MCP_CONFIRM_WRITE=1      # macOS / Linux
setx NUPHUS_MCP_CONFIRM_WRITE 1        # Windows (persistent for new shells)
