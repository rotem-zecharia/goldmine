# aerovato/container

Safely run OpenCode, Codex, Claude Code with full permissions.

## requirements

- Windows, macOS, or Linux
- Docker or Podman

## installation

macOS and Linux:

```bash
curl -fsSL https://container.aerovato.com/install.sh | sh
```

Windows PowerShell:

```powershell
irm https://container.aerovato.com/install.ps1 | iex
```

Alternatively, install through npm:

```bash
npm install -g @aerovato/container
```

## configuration

Run the guided onboarding flow:

```bash
container init
```

Choose your coding harnesses, development tools, runtime, and mounts, then accept the initial image build.

## tools

```bash
container                           # Open the current project's workspace
container run /path/to/project      # Open a specific project
container run /path -- -p 8080:80   # Pass runtime flags
container list                      # List managed containers
container stop                      # Stop the current workspace
container remove                    # Remove the current workspace
container settings                  # Change common settings
container init                      # Re-run onboarding
```

Rebuild the shared image when updating tools or customizations:

```bash
container build
container build tools
container build harness
container build user
```
