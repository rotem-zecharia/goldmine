# Kuberwastaken/claurst

Agentic Coding for Builders who Ship

## installation

**Linux / macOS:**

```bash
curl -fsSL https://github.com/kuberwastaken/claurst/releases/latest/download/install.sh | bash
```

**Windows (PowerShell):**

```powershell
irm https://github.com/kuberwastaken/claurst/releases/latest/download/install.ps1 | iex
```

This drops `claurst` into `~/.local/bin` (or `%LOCALAPPDATA%\Programs\claurst` on Windows; Git Bash uses the same Windows path) and adds it to your `PATH` automatically. Open a new terminal and run `claurst`.

## tools

export ANTHROPIC_API_KEY=sk-ant-...

## features

- Base image: `rust:1-bullseye`.
- Preinstalled build dependencies: `gnupg2`, `libasound2-dev`, `libxdo-dev`, and `pkg-config`.
- Devcontainer features enabled: `common-utils` (with `vscode` user `uid/gid 1000` and Zsh install disabled), `git`, and `docker-outside-of-docker` (`moby: false`).
- Runs as `vscode` user by default.
- Persistent Cargo caches via named volumes for `/usr/local/cargo/registry` and `/usr/local/cargo/git`.
- Binds local `.claurst` into `/home/vscode/.claurst` for local settings/session history access.
- Sets `GNUPGHOME=/home/vscode/.gnupg` and prepends `src-rust/target/debug` and `src-rust/target/release` to `PATH`.
- Post-create setup creates and permissions `.gnupg`, and fixes ownership for `/usr/local/cargo`.
- VS Code setting `terminal.integrated.inheritEnv` is enabled.
