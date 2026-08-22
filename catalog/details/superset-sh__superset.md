# superset-sh/superset

Superset is an agentic IDE to orchestrate 100+ coding agents in parallel. Run any agent with your own subscription.

## features

<table>
<tr>
<td width="50%" valign="middle">

## installation

Download the desktop app:

- **macOS**: [Apple Silicon (.dmg)](https://github.com/superset-sh/superset/releases/latest/download/Superset-arm64.dmg) · [Intel (.dmg)](https://github.com/superset-sh/superset/releases/latest/download/Superset-x64.dmg)
- **Linux**: [x64 AppImage](https://github.com/superset-sh/superset/releases/latest/download/Superset-x86_64.AppImage) (experimental; macOS is the primary target)
- **Windows**: not yet available
- [All builds](https://github.com/superset-sh/superset/releases/latest)

All you need installed is [Git](https://git-scm.com/). [gh](https://cli.github.com/) is optional and unlocks the PR workflows; Superset offers to install it for you.

## configuration

Configure workspace setup, teardown, and run scripts in `.superset/config.json`. See [full documentation](https://docs.superset.sh/setup-teardown-scripts).

```json
{
  "setup": ["./.superset/setup.sh"],
  "teardown": ["./.superset/teardown.sh"],
  "run": ["./.superset/run.sh"]
