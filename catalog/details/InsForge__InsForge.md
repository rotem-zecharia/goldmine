# InsForge/InsForge

The all-in-one, open-source backend platform for agentic coding. InsForge gives your coding agent database, auth, storage, compute, hosting, and AI gateway to ship full-stack apps end-to-end.

## installation

### Cloud-hosted: [insforge.dev](https://insforge.dev)

<a href="https://insforge.dev" target="_blank" rel="noopener noreferrer"><img src="https://img.shields.io/badge/insforge.dev-181818?logo=data:image/svg%2bxml;base64,PHN2ZyB3aWR0aD0iMjQwIiBoZWlnaHQ9IjI0MCIgdmlld0JveD0iMCAwIDI0MCAyNDAiIGZpbGw9Im5vbmUiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PHBhdGggZD0iTTI2LjExODQgMTAxLjZDMjMuMjkzOSA5OC43ODMzIDIzLjI5MzkgOTQuMjE2NiAyNi4xMTg0IDkxLjRMOTcuNzE2NyAyMEwyMDAgMjBMNzcuMjYgMTQyLjRDNzQuNDM1NSAxNDUuMjE3IDY5Ljg1NjIgMTQ1LjIxNyA2Ny4wMzE3IDE0Mi40TDI2LjExODQgMTAxLjZaIiBmaWxsPSJ3aGl0ZSIvPjxwYXRoIGQ9Ik0xNTUuMjUxIDc3LjM3NUwyMDAgMTIyVjIyNEwxMDQuMTA5IDEyOC4zNzVMMTU1LjI1MSA3Ny4zNzVaIiBmaWxsPSJ3aGl0ZSIvPjwvc3ZnPgo=&logoColor=white" alt="InsForge.dev"></a>

### Self-hosted: Docker Compose

Prerequisites: [Docker](https://www.docker.com/) with Compose v2.

#### 1. Setup

```bash
curl -fsSL https://raw.githubusercontent.com/InsForge/InsForge/main/deploy/setup.sh | sh -s ~/insforge
```

Fetches the files the stack reads and generates `JWT_SECRET`, `ENCRYPTION_KEY`,
`POSTGRES_PASSWORD`, `ROOT_ADMIN_PASSWORD`, and the two access keys into
`~/insforge/.env` (mode 600). Nothing is started. Re-running refreshes the files
and keeps every value you have set — it only ever adds `COMPOSE_FILE`, or points
it at this checkout's compose file if it still names the development one.

```bash
cd ~/insforge
$EDITOR .env          # API_BASE_URL, VITE_API_BASE_URL — the URL browsers will use
docker compose up -d
```

`.env` sets `COMPOSE_FILE`, so plain `docker compose` commands work from that
directory — no `-f` flags to remember.

[![Deploy on Docker][docker-btn]][docker-deploy]

<details>
<summary>Building from source instead</summary>

For working on InsForge itself. `docker-compose.prod.yml` reads the same
variables but generates nothing, so set the secrets in `.env` yourself before
starting anything you expose.

```bash
git clone https://github.com/InsForge/InsForge.git
cd InsForge
cp .env.example .env
$EDITOR .env
docker compose -f docker-compose.prod.yml up
```

Set `JWT_SECRET`, `ENCRYPTION_KEY`, `POSTGRES_PASSWORD`, and
`ROOT_ADMIN_PASSWORD` — `.env.example` ships placeholders for them, and the
compose file falls back to published defaults for any you leave unset. Set
`ACCESS_API_KEY` and `ACCESS_ANON_KEY` too if you want to know your own keys;
left empty, the backend generates a pair only it knows.

This path passes `-f` explicitly, which overrides `COMPOSE_FILE`. Add overlays as
further `-f` flags rather than editing that variable.

</details>

#### 2. Connect InsForge MCP

Open [http://localhost:7130](http://localhost:7130)

Follow the steps to connect InsForge MCP Server

<div align="center">
<img src="assets/connect.png" alt="Connect InsForge MCP" width="600">
</div>

#### 3. Verify installation

To verify the connection, send the following prompt to your agent:
```
I'm using InsForge as my backend platform, call InsForge MCP's fetch-docs tool to learn about InsForge instructions.
```

#### 4. Running Multiple Projects

Give each project its own directory:

```bash
curl -fsSL https://raw.githubusercontent.com/InsForge/InsForge/main/deploy/setup.sh | sh -s ~/project1
curl -fsSL https://raw.githubusercontent.com/InsForge/InsForge/main/deploy/setup.sh | sh -s ~/project2
```

Then give each a project name and its own ports. Both `.env` files start with
`COMPOSE_PROJECT_NAME=insforge`, and **two directories sharing that name share
containers** — the second `up -d` adopts the first's, rebuilt with the second's
config. Set it before starting anything.

`~/project1/.env` keeps the default ports — which collide with the `~/insforge`
instance from the quickstart above if it is still running. Stop that one, or give
`project1` its own ports the way `project2` has:

```env
COMPOSE_PROJECT_NAME=project1
```

`~/project2/.env`:

```env
COMPOSE_PROJECT_NAME=project2
POSTGRES_PORT=5442
POSTGREST_PORT=5440
APP_PORT=7230
AUTH_PORT=7231
DENO_PORT=7233
```

Now each dir
