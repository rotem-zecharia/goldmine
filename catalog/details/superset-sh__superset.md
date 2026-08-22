# superset-sh/superset

Superset is an agentic IDE to orchestrate 100+ coding agents in parallel. Run any agent with your own subscription.

## features

<table>
<tr>
<td width="50%" valign="middle">

### Parallel Workspaces

Run 100+ coding agents at once, each in its own git worktree with its own branch, terminal, and environment. Compare the results and merge the winner.

[Docs →](https://docs.superset.sh/workspaces)

</td>
<td width="50%">
  <a href="https://docs.superset.sh/workspaces"><img src="apps/marketing/public/images/readme/agents-working.gif" alt="Claude streaming a billing migration while other agents run in parallel workspaces" width="100%" /></a>
</td>
</tr>
<tr>
<td width="50%" valign="middle">

### Agent Monitoring

Track every agent from the sidebar, with working indicators, completion chimes, and dock badges when one needs your attention.

[Docs →](https://docs.superset.sh/agent-integration)

</td>
<td width="50%">
  <a href="https://docs.superset.sh/agent-integration"><img src="apps/marketing/public/images/readme/agent-monitoring.gif" alt="An agent finishing its task and the sidebar status flipping from working to done" width="100%" /></a>
</td>
</tr>
<tr>
<td width="50%" valign="middle">

### Built-in Terminal

Tabs, infinite splits, presets, and persistent sessions that survive restarts. Press ⌘I for a rich prompt editor with multiline editing and @-file mentions.

[Docs →](https://docs.superset.sh/terminal-integration)

</td>
<td width="50%">
  <a href="https://docs.superset.sh/terminal-integration"><img src="apps/marketing/public/images/readme/terminal.gif" alt="Typing a follow-up with an @-file mention in the rich prompt editor next to a split terminal" width="100%" /></a>
</td>
</tr>
<tr>
<td width="50%" valign="middle">

### Built-in Diff Viewer

Inspect, comment on, and edit agent changes without leaving the app, then commit and push when it's ready.

[Docs →](https://docs.superset.sh/diff-viewer)

</td>
<td width="50%">
  <a href="https://docs.superset.sh/diff-viewer"><img src="apps/marketing/public/images/readme/diff-viewer.png" alt="Reviewing an agent's changes in the diff viewer" width="100%" /></a>
</td>
</tr>
<tr>
<td width="50%" valign="middle">

### In-App Browser & Ports

Preview running dev servers in a browser pane. Ports are detected per workspace, so every worktree gets its own preview.

[Docs →](https://docs.superset.sh/browser)

</td>
<td width="50%">
  <a href="https://docs.superset.sh/browser"><img src="apps/marketing/public/images/readme/browser-ports.png" alt="In-app browser previewing a dev server with detected ports" width="100%" /></a>
</td>
</tr>
<tr>
<td width="50%" valign="middle">

### Automations

Run agent sessions on a schedule: triage issues overnight, draft the weekly changelog, keep dependencies fresh.

[Docs →](https://docs.superset.sh/automations)

</td>
<td width="50%">
  <a href="https://docs.superset.sh/automations"><img src="apps/marketing/public/images/readme/automations.png" alt="Scheduled agent automations" width="100%" /></a>
</td>
</tr>
<tr>
<td width="50%" valign="middle">

### Remote Workspaces

Connect another machine and reach its workspaces from anywhere: the desktop app, the CLI, or your phone. Wake offline hosts with a custom command.

[Docs →](https://docs.superset.sh/remote-workspaces)

</td>
<td width="50%">
  <a href="https://docs.superset.sh/remote-workspaces"><img src="apps/docs/public/images/remote-workspaces-hosts-members.png" alt="Hosts and members in organization settings" width="100%" /></a>
</td>
</tr>
<tr>
<td width="50%" valign="middle">

### Superset CLI

Script it from any shell: create workspaces, launch agents, read their terminals, and manage automations with a single binary. If an agent can run a command, it can drive Superset.

[Docs →](https://docs.superset.sh/cli/getting-started)

</td>
<td width="50%">
  <a href="https://docs.superset.sh/cli/getting-started"><img src="apps/marketing/public/images/readme/cli-demo.gif" alt="Creating a workspace and launching an agent from the Superset CLI" width="100%" /></a>
</td>
</tr>
<tr>
<td width="50%" valign="middle">

### Command Palette

## installation

Download the desktop app:

- **macOS**: [Apple Silicon (.dmg)](https://github.com/superset-sh/superset/releases/latest/download/Superset-arm64.dmg) · [Intel (.dmg)](https://github.com/superset-sh/superset/releases/latest/download/Superset-x64.dmg)
- **Linux**: [x64 AppImage](https://github.com/superset-sh/superset/releases/latest/download/Superset-x86_64.AppImage) (experimental; macOS is the primary target)
- **Windows**: not yet available
- [All builds](https://github.com/superset-sh/superset/releases/latest)

All you need installed is [Git](https://git-scm.com/). [gh](https://cli.github.com/) is optional and unlocks the PR workflows; Superset offers to install it for you.

## Development

Want to hack on Superset or contribute a PR? Clone the repository, add it to the
installed Superset app, and create a workspace for your change:

```bash
git clone https://github.com/superset-sh/superset.git
```

Then run the development setup from that workspace terminal:

```bash
./.superset/setup.local.sh
bun run dev
```

Run `setup.local.sh` once in every new worktree. It configures workspace-specific
app identity and ports so the development desktop app can run alongside the
installed Superset app and other development worktrees.

No Neon account or third-party credentials are needed. `setup.local.sh` brings
up a local Postgres + Electric stack via Docker and seeds a dev account. Sign in
with the **"Sign in as dev"** button (or `admin@local.test` / `supersetdev`).

Prereqs: [Bun](https://bun.sh/) v1.3.14+ (pinned in `.bun-version`), `docker`, `jq`, and `caddy`, which `bun dev` runs as the local HTTPS proxy (`brew install jq caddy && caddy trust`).

See [**DEVELOPMENT.md**](./DEVELOPMENT.md) for the full guide: what the setup script does, manual setup against real services, common commands, troubleshooting, and how to build the desktop app. Contribution process lives in [**CONTRIBUTING.md**](./CONTRIBUTING.md).

## configuration

Configure workspace setup, teardown, and run scripts in `.superset/config.json`. See [full documentation](https://docs.superset.sh/setup-teardown-scripts).

```json
{
  "setup": ["./.superset/setup.sh"],
  "teardown": ["./.superset/teardown.sh"],
  "run": ["./.superset/run.sh"]
}
```

Keyboard shortcuts are customizable via **Settings → Keyboard Shortcuts** (⌘/); see the [full shortcut list](https://docs.superset.sh/keyboard-shortcuts).

## Tech Stack

<p>
  <a href="https://www.electronjs.org/"><img src="https://img.shields.io/badge/Electron-191970?logo=Electron&logoColor=white" alt="Electron" /></a>
  <a href="https://reactjs.org/"><img src="https://img.shields.io/badge/React-%2320232a.svg?logo=react&logoColor=%2361DAFB" alt="React" /></a>
  <a href="https://tailwindcss.com/"><img src="https://img.shields.io/badge/Tailwindcss-%2338B2AC.svg?logo=tailwind-css&logoColor=white" alt="TailwindCSS" /></a>
  <a href="https://bun.sh/"><img src="https://img.shields.io/badge/Bun-000000?logo=bun&logoColor=white" alt="Bun" /></a>
  <a href="https://turbo.build/"><img src="https://img.shields.io/badge/Turborepo-EF4444?logo=turborepo&logoColor=white" alt="Turborepo" /></a>
  <a href="https://vitejs.dev/"><img src="https://img.shields.io/badge/Vite-%23646CFF.svg?logo=vite&logoColor=white" alt="Vite" /></a>
  <a href="https://biomejs.dev/"><img src="https://img.shields.io/badge/Biome-339AF0?logo=biome&logoColor=white" alt="Biome" /></a>
  <a href="https://orm.drizzle.team/"><img src="https://img.shields.io/badge/Drizzle%20ORM-FFE873?logo=drizzle&logoColor=black" alt="Drizzle ORM" /></a>
  <a href="https://neon.tech/"><img src="https://img.shields.io/badge/Neon-00E9CA?logo=neon&logoColor=white" alt="Neon" /></a>
  <a href="https://trpc.io/"><img src="https://img.shields.io/badge/tRPC-2596BE?logo=trpc&logoColor=white" alt="tRPC" /></a>
</p>

## Private by Default

- **Source Available**: full source is on GitHub under Elastic License 2.0 (ELv2).
- **Explicit Connections**: you choose which agents, providers, and integrations to connect.

## Contributing

We welcome contributions! See [CONTRIBUTING.md](CONTRIBUTING.md) for how to get set up and open a PR. Bugs and feature requests go in [issues](https://github.com/superset-sh/superset/issues).

<a href="https://github.com/superset-sh/superset/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=superset-sh/superset" />
</a>

## Community

Join the Superset community to get help, share feedback, and connect with other users:

- **[Discord](https://discord.gg/cZeD9WYcV7)**: chat with the team and community
- **[Twitter](https://x.com/superset_sh)**: follow for updates and announcements
- **[GitHub Issues](https://github.com/superset-sh/superset/issues)**: report bugs and request features
- **[GitHub Discussions](https://github.com/superset-sh/superset/discussions)**: ask questions and share ideas

### Team

[![Avi Twitter](https://img.shields.io/badge/Avi-@avimakesrobots-555?logo=x)](https://x.com/avimakesrobots)
[![Kiet Twitter](https://img.shields.io/badge/Kiet-@flyakiet-555?logo=x)](https://x.com/flyakiet)
[![Satya Twitter](https://img.shields.io/badge/Satya-@saddle__paddle-555?logo=x)](https://x.com/saddle_paddle)

## License & what's free forever

**The desktop app is free forever.** Running agents in parallel on your own machine will never require payment. Anything we charge for will be an optional service on top.

The whole app is in this repo under the [Elastic License 2.0](LICENSE.md): use it, fork it, modify it, self-host it for your team. The only thing off the table is repackaging Superset itself as a service you sell to others.
