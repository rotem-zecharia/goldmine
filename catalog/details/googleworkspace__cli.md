# googleworkspace/cli

Google Workspace CLI — one command-line tool for Drive, Gmail, Calendar, Sheets, Docs, Chat, Admin, and more. Dynamically built from Google Discovery Service. Includes AI agent skills.

## requirements

- **Node.js 18+** — for `npm install` (or download a pre-built binary from [GitHub Releases](https://github.com/googleworkspace/cli/releases))
- **A Google Cloud project** — required for OAuth credentials. You can create one via the [Google Cloud Console](https://console.cloud.google.com/) or with the [`gcloud` CLI](https://cloud.google.com/sdk/docs/install) or with the `gws auth setup` command.
- **A Google account** with access to Google Workspace

## installation

The recommended way to install `gws` is to download the pre-built binary for your OS and architecture from the **[GitHub Releases](https://github.com/googleworkspace/cli/releases)** page. Extract the archive and place the `gws` binary in your `$PATH`.

For convenience, you can also use `npm` to automate downloading the appropriate binary from GitHub Releases:

```bash
npm install -g @googleworkspace/cli
```

Or build from source:

```bash
cargo install --git https://github.com/googleworkspace/cli --locked
```

A Nix flake is also available at `github:googleworkspace/cli`

```bash
nix run github:googleworkspace/cli
```

On macOS and Linux, you can also install via [Homebrew](https://brew.sh/):

```bash
brew install googleworkspace-cli
```

## features

**For humans** — stop writing `curl` calls against REST docs. `gws` gives you `--help` on every resource, `--dry-run` to preview requests, and auto‑pagination.

**For AI agents** — every response is structured JSON. Pair it with the included agent skills and your LLM can manage Workspace without custom tooling.

```bash

## tools

Sheets ranges use `!` which bash interprets as history expansion. Always wrap values in **single quotes**:

```bash

## configuration

All variables are optional. See [`.env.example`](.env.example) for a copy-paste template.

| Variable | Description |
|---|---|
| `GOOGLE_WORKSPACE_CLI_TOKEN` | Pre-obtained OAuth2 access token (highest priority) |
| `GOOGLE_WORKSPACE_CLI_CREDENTIALS_FILE` | Path to OAuth credentials JSON (user or service account) |
| `GOOGLE_WORKSPACE_CLI_CLIENT_ID` | OAuth client ID (alternative to `client_secret.json`) |
| `GOOGLE_WORKSPACE_CLI_CLIENT_SECRET` | OAuth client secret (paired with `CLIENT_ID`) |
| `GOOGLE_WORKSPACE_CLI_CONFIG_DIR` | Override config directory (default: `~/.config/gws`) |
| `GOOGLE_WORKSPACE_CLI_SANITIZE_TEMPLATE` | Default Model Armor template |
| `GOOGLE_WORKSPACE_CLI_SANITIZE_MODE` | `warn` (default) or `block` |
| `GOOGLE_WORKSPACE_CLI_LOG` | Log level for stderr (e.g., `gws=debug`). Off by default. |
| `GOOGLE_WORKSPACE_CLI_LOG_FILE` | Directory for JSON log files with daily rotation. Off by default. |
| `GOOGLE_WORKSPACE_PROJECT_ID` | GCP project ID override for quota/billing and fallback for helper commands |

Environment variables can also be set in a `.env` file (loaded via [dotenvy](https://crates.io/crates/dotenvy)).
