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

**Prerequisites**:

- Docker: Docker Desktop on macOS/Windows, or Docker Engine/Docker Desktop on Linux.
- A host directory for `PROJECTS_PATH` containing the project folders you want the agent to access. Create it before starting the container.

**macOS / Linux:**

```sh
export PROJECTS_PATH="$HOME/projects"  # directory containing your project folders
mkdir -p "$PROJECTS_PATH" "$HOME/.openhands"

docker run -it --rm \
  -p 127.0.0.1:8000:8000 \
  -e AGENT_CANVAS_ALLOW_LAN_SESSION_KEY=true \
  -v "$HOME/.openhands:/home/openhands/.openhands" \
  -v "${PROJECTS_PATH}:/projects" \
  ghcr.io/openhands/agent-canvas:1.26.0 # x-release-please-version
```

**Windows (PowerShell / Windows Terminal):** See [README.windows.md](./README.windows.md) for the equivalent commands.

The agent will be able to access any project under `PROJECTS_PATH`.

### Option 3: With Multiple Docker Sandboxes

Run each new conversation in its own Docker container, with its own Agent Server and tools. This is useful for running several agents concurrently. Canvas and the outer Agent Server run on your host and route conversation requests to the containers.

**Prerequisites**: Node.js 24 or later, `uv`, and a running Docker Desktop (macOS) or Docker Engine/Desktop (Linux). The user starting Canvas must be able to run `docker` commands.

**macOS / Linux:**

```sh
npm install -g @openhands/agent-canvas
OH_CONVERSATION_RUNTIME=docker agent-canvas
```

Open [http://localhost:8000](http://localhost:8000) and start a new conversation. Existing local conversations are not converted. Each container mounts its conversation's workspace and persisted state, so workspace files and conversation history survive container replacement. Conversations using the same host workspace still share those files; choose separate directories or worktrees to avoid conflicting edits.

This setting isolates conversation execution; it does not move the entire Canvas or automation service into a sandbox. For Windows, see [README.windows.md](./README.windows.md#option-3-with-multiple-docker-sandboxes-wsl-2).

### Option 4: From Source

> [!WARNING]
> This runs the agent-server directly on the machine you're installing on — the agent will have full access to your filesystem!

**Prerequisites**: [Node.js](https://nodejs.org/) 24 or later, `npm`, `uv` (for running the agent server via `uvx`)

```sh
git clone https://github.com/OpenHands/OpenHands.git
cd OpenHands
npm install
npm run dev
```

---

Access the UI at [http://localhost:8000](http://localhost:8000) for the npm/source launchers, or [http://local
