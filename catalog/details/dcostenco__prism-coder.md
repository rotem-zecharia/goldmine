# dcostenco/prism-coder

Persistent session memory for AI coding agents — local-first, with on-device inference, associative recall, and drift detection. Works with Claude Code, Cursor, and Codex.

## installation

Prism also ships as a plugin, which registers the MCP server and the startup
skill for you.

**Claude Code** — from the community marketplace:

```bash
/plugin marketplace add anthropics/claude-plugins-community
/plugin install synalux-prism@claude-community
```

**Codex** — this repository is itself a plugin marketplace:

```bash
codex plugin marketplace add dcostenco/prism-coder
codex plugin add synalux-prism@prism
```

The plugin registers `prism-mcp` via `npx -y prism-mcp-server`. If you already
configured Prism by hand — `prism connect` writes an `mcp_servers.prism-mcp`
entry — you have that server twice under one key. Install the plugin **or**
run `prism connect`, not both.

## configuration

`prism connect` now reads Claude, Cursor, Gemini, and Codex configuration
through a single verified file snapshot, preventing another process from
swapping a file between Prism's safety check and its read. Supported symlinked
dotfiles still work, while dangling or planted symlinks fail loudly instead of
being followed or overwritten. This release also carries the patched
dependencies and cross-platform release checks introduced in v20.2.5.

Cloud fallback is now documented consistently as Gemini 3.6 Flash. Plan
ceilings govern automatic `prism_infer` routing; direct use of any downloaded
model through local Ollama remains free on every tier.

---

## requirements

External contributions now require signing the [Individual CLA](./CLA.md). The CLA check is merge-blocking on the `main` branch.

---

</details>

## features

Your AI agent forgets everything between sessions. Prism fixes that — and adds verification, drift detection, and multi-agent coordination on top.

## tools

| Feature | Prism Coder | Ollama | LM Studio | Mem0 | Zep |
|---|:---:|:---:|:---:|:---:|:---:|
| Local inference cascade | ✅ | ✅ runtime | ✅ app | — | — |
| Cloud fallback | ✅ optional | — | ◐ provider-dependent | ◐ | ◐ |
| Persistent memory | ✅ | — | ◐ project context | ✅ | ✅ |
| Knowledge/tool integration | ✅ MCP + ingestion | ◐ APIs | ◐ integrations | ✅ SDK/API | ✅ SDK/API |
| MCP server | ✅ native | — | ◐ client integration | ◐ client integration | ◐ client integration |
