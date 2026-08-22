# nyldn/claude-octopus

Surface AI blindspots before you ship. Put up to 8 AI models on every research, design or coding task.

## installation

```bash

## configuration

```

```json
{
  "mcpServers": {
    "claude-octopus": {
      "command": "npx",
      "args": ["tsx", "${userHome}/.cursor/claude-octopus/mcp-server/src/index.ts"],
      "env": {
        "OCTO_CLAW_ENABLED": "true",
        "OPENAI_API_KEY": "${env:OPENAI_API_KEY}"
      }
    }
  }

## tools

~/.claude-octopus/plugin/scripts/orchestrate.sh update-plugin
