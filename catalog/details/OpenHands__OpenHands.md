# OpenHands/OpenHands

🙌 OpenHands: AI-Driven Development

## installation

You can install OpenHands to run agents on any machine: on your laptop, on a dedicated computer like a Mac Mini,
or on a server in the cloud.

The most powerful way to run OpenHands is on a server in the cloud. This allows your agents to continue running
even when your laptop is shut, and makes it easier to trigger your agents through third-party services
like Slack, GitHub, and Datadog. See [SELF_HOSTING.md](docs/SELF_HOSTING.md) for details, especially with respect to security hardening.

Notably, you can run the backend in _multiple different environments_, and switch between
them from the same Agent Canvas frontend. E.g. you can share an Agent Server with your team for agents doing
code review and dependency updates, then have your personal agents running on your laptop.

### Option 1: Without a Sandbox

> [!WARNING]
> This runs the agent-server directly on the machine you're installing on — the agent will have full access to your filesystem!

**Prerequisites**: [Node.js](https://nodejs.org/) 24 or later, `uv`

```sh
npm install -g @openhands/agent-canvas
agent-canvas
```

The `agent-canvas` command starts the full local stack by default. You can also split it when you want to run pieces separately:

```sh
agent-canvas --frontend-only  # static frontend + ingress only
agent-canvas --backend-only   # agent server + automation backend + ingress only
```

### Option 2: With a Docker Sandbox

Install Docker Desktop on macOS/Windows, or Docker Engine/Docker Desktop on Linux.
Windows users can follow the [PowerShell quickstart](./README.windows.md).

The steps below are for macOS and Linux. A named Docker volume stores settings,
secrets, and conversations; projects are mounted at `/projects`.

**1. Prepare a workspace**

```sh
export PROJECTS_PATH="$HOME/projects"  # directory containing your project folders
mkdir -p "$PROJECTS_PATH"
```

On **Linux Docker Engine**, uid 10001 inside the container must be able to read
and write the workspace and its existing files. Grant that user access using
appropriate ownership or ACLs for your system. For a dedicated workspace you are
comfortable sharing with all local users, the following is another option:

```sh
find "$PROJECTS_PATH" -type d -exec chmod a+rwX {} +
find "$PROJECTS_PATH" -type f -exec chmod a+rw {} +
```

These commands grant all host users access to the workspace. Keep it separate
from `~/.openhands` and other sensitive data. Docker Desktop on macOS/Windows
handles bind-mount permissions, so those commands are normally unnecessary.

**2. Start Agent Canvas**

```sh
docker run -it --rm \
  -p 127.0.0.1:8000:8000 \
  -e AGENT_CANVAS_ALLOW_LAN_SESSION_KEY=true \
  -v openhands-state:/home/openhands/.openhands \
  -v "${PROJECTS_PATH}:/projects" \
  ghcr.io/openhands/agent-canvas:1.43.0 # x-release-please-version
```

Open [http://localhost:8000/canvas](http://localhost:8000/canvas). Reuse
`openhands-state` to retain state across container removals. A fresh volume does
not contain existing `~/.openhands` data; inspect or back it up with
`docker volume inspect openhands-state`.

<details>
<summary>Linux permission troubleshooting and existing state</summary>

If startup reports `Permission denied`, check access to the path named in the
error. On SELinux hosts, check whether the bind mount needs a `:z` or `:Z` label.
If you bind-mount existing `~/.openhands` state instead of the named volume,
uid 10001 needs access to its directories, existing key files and automation
database. Grant access using ownership or ACLs while keeping keys private.
Making state directories writable by all users can let another local user
replace the session key; do not use recursive world-writable permissions there.

Keep the default container user. An override can make the browser configuration
directory inaccessible. If you override the user, configure a writable
`XDG_CONFIG_HOME` and ensure state and workspace mounts are accessible.

</details>

> [!NOTE]
> The entrypoint stops the container with ex
