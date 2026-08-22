# rsmdt/the-startup

The Agentic Startup - A collection of Claude Code commands, skills, and agents.

## installation

**Requirements:** Claude Code v2.0+ with marketplace support

```bash
curl -fsSL https://raw.githubusercontent.com/rsmdt/the-startup/main/install.sh | sh
```

This installs the core plugins, configures the default output style, and sets up the [statusline](#-statusline) with a customizable config file.

<details>
<summary><strong>Manual Installation</strong></summary>

Start `claude` and run the following:

```bash

## configuration

The statusline reads from `~/.config/the-agentic-startup/statusline.toml`:

```toml

## tools

plan = "auto"
fallback_plan = "pro"

[thresholds.context]
warn = 70    # percentage
danger = 90

[thresholds.cost]

## features

Real workflow features that solve real problems — not just another AI wrapper.
