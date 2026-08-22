# modelcontextprotocol/python-sdk

The official Python SDK for Model Context Protocol servers and clients

## requirements

Python 3.10+.

## installation

```bash
uv add "mcp[cli]"      # or: pip install "mcp[cli]"
```

The `cli` extra adds the `mcp` command-line tool (`mcp dev`, `mcp run`, `mcp install`) on top of the SDK; install plain `mcp` if you don't need it. For one-off commands, `uv run --with "mcp[cli]" mcp ...` works without a project.
