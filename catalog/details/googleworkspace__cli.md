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

## Quick Start

```bash
gws auth setup     # walks you through Google Cloud project config
gws auth login     # subsequent OAuth login
gws drive files list --params '{"pageSize": 5}'
```

## features

**For humans** — stop writing `curl` calls against REST docs. `gws` gives you `--help` on every resource, `--dry-run` to preview requests, and auto‑pagination.

**For AI agents** — every response is structured JSON. Pair it with the included agent skills and your LLM can manage Workspace without custom tooling.

```bash
# List the 10 most recent files
gws drive files list --params '{"pageSize": 10}'

# Create a spreadsheet
gws sheets spreadsheets create --json '{"properties": {"title": "Q1 Budget"}}'

# Send a Chat message
gws chat spaces messages create \
  --params '{"parent": "spaces/xyz"}' \
  --json '{"text": "Deploy complete."}' \
  --dry-run

# Introspect any method's request/response schema
gws schema drive.files.list

# Stream paginated results as NDJSON
gws drive files list --params '{"pageSize": 100}' --page-all | jq -r '.files[].name'
```

## Authentication

The CLI supports multiple auth workflows so it works on your laptop, in CI, and on a server.

## tools

### Multipart Uploads

```bash
gws drive files create --json '{"name": "report.pdf"}' --upload ./report.pdf
```

### Pagination

| Flag                | Description                                    | Default |
| ------------------- | ---------------------------------------------- | ------- |
| `--page-all`        | Auto-paginate, one JSON line per page (NDJSON) | off     |
| `--page-limit <N>`  | Max pages to fetch                             | 10      |
| `--page-delay <MS>` | Delay between pages                            | 100 ms  |

### Google Sheets — Shell Escaping

Sheets ranges use `!` which bash interprets as history expansion. Always wrap values in **single quotes**:

```bash
# Read cells A1:C10 from "Sheet1"
gws sheets spreadsheets values get \
  --params '{"spreadsheetId": "SPREADSHEET_ID", "range": "Sheet1!A1:C10"}'

# Append rows
gws sheets spreadsheets values append \
  --params '{"spreadsheetId": "ID", "range": "Sheet1!A1", "valueInputOption": "USER_ENTERED"}' \
  --json '{"values": [["Name", "Score"], ["Alice", 95]]}'
```

### Helper Commands

Some services ship hand-crafted helper commands alongside the auto-generated Discovery surface. Helper commands are prefixed with `+` so they are visually distinct and never collide with Discovery-generated method names.

Time-aware helpers (`+agenda`, `+standup-report`, `+weekly-digest`, `+meeting-prep`) automatically use your **Google account timezone** (fetched from Calendar Settings API and cached for 24 hours). Override with `--timezone`/`--tz` on `+agenda`, or set the `--timezone` flag for explicit control.

Run `gws <service> --help` to see both Discovery methods and helper commands together.

```bash
gws gmail --help      # shows +send, +reply, +reply-all, +forward, +triage, +watch …
gws calendar --help   # shows +insert, +agenda …
gws drive --help      # shows +upload …
```

**Full helper reference:**

| Service | Command | Description |
|---------|---------|-------------|
| `gmail` | `+send` | Send an email |
| `gmail` | `+reply` | Reply to a message (handles threading automatically) |
| `gmail` | `+reply-all` | Reply-all to a message |
| `gmail` | `+forward` | Forward a message to new recipients |
| `gmail` | `+triage` | Show unread inbox summary (sender, subject, date) |
| `gmail` | `+watch` | Watch for new emails and stream them as NDJSON |
| `sheets` | `+append` | Append a row to a spreadsheet |
| `sheets` | `+read` | Read values from a spreadsheet |
| `docs` | `+write` | Append text to a document |
| `chat` | `+send` | Send a message to a space |
| `drive` | `+upload` | Upload a file with automatic metadata |
| `calendar` | `+insert` | Create a new event |
| `calendar` | `+agenda` | Show upcoming events (uses Google account timezone; override with `--timezone`) |
| `script` | `+push` | Replace all files in an Apps Script project with local files |
| `workflow` | `+standup-report` | Today's meetings + open tasks as a standup summary |
| `workflow` | `+meeting-prep` | Prepare for your next meeting: agenda, attendees, and linked docs |
| `workflow` | `+email-to-task` | Convert a Gmail message into a Google Tasks entry |
| `workflow` | `+weekly-digest` | Weekly summary: this week's meetings + unread email count |
| `workflow` | `+file-announce` | Announce a Drive file in a Chat space |
| `events` | `+subscribe` | Subscribe to Workspace events and stream them as NDJSON |
| `events` | `+renew` | Renew/reactivate Workspace Events subscriptions |
| `modelarmor` | `+sanitize-prompt` | Sanitize a user prompt through a Model Armor template |
| `modelarmor` | `+sanitize-response` | Sanitize a model response through a Model Armor template |
| `modelarmor` | `+create-template` | Create a new Model Armor template |

**Examples:**

```bash
# Send an email
gws gmail +send --to alice@example.com --subject "Hello" --body "Hi there"

# Reply to a message
gws gmail +reply --message-id MESSAGE_ID --body "Thanks!"

# Append a row to a spreadsheet
gws sheets +append --spreadshe

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

## Exit Codes

`gws` uses structured exit codes so scripts can branch on the failure type without parsing error output.

| Code | Meaning | Example cause |
|------|---------|---------------|
| `0` | Success | Command completed normally |
| `1` | API error | Google returned a 4xx/5xx response |
| `2` | Auth error | Credentials missing, expired, or invalid |
| `3` | Validation error | Bad arguments, unknown service, invalid flag |
| `4` | Discovery error | Could not fetch the API schema document |
| `5` | Internal error | Unexpected failure |

```bash
gws drive files list --params '{"fileId": "bad"}'
echo $?   # 1 — API error

gws unknown-service files list
echo $?   # 3 — validation error (unknown service)
```

## Architecture

`gws` uses a **two-phase parsing** strategy:

1. Read `argv[1]` to identify the service (e.g. `drive`)
2. Fetch the service's Discovery Document (cached 24 h)
3. Build a `clap::Command` tree from the document's resources and methods
4. Re-parse the remaining arguments
5. Authenticate, build the HTTP request, execute

All output — success, errors, download metadata — is structured JSON.

## Troubleshooting

### "Access blocked" or 403 during login

Your OAuth app is in **testing mode** and your account is not listed as a test user.

**Fix:** Open the [OAuth consent screen](https://console.cloud.google.com/apis/credentials/consent) in your GCP project → **Test users** → **Add users** → enter your Google account email. Then retry `gws auth login`.

### "Google hasn't verified this app"

Expected when your app is in testing mode. Click **Advanced** → **Go to \<app name\> (unsafe)** to proceed. This is safe for personal use; verification is only required to publish the app to other users.

### Too many scopes / consent screen error

Unverified (testing mode) apps are limited to ~25 OAuth scopes. The `recommended` scope preset includes many scopes and will exceed this limit.

**Fix:** Select only the scopes you need:

```bash
gws auth login --scopes drive,gmail,calendar
```

### `gcloud` CLI not found

`gws auth setup` requires the `gcloud` CLI to automate project creation. You have three options:

1. [Install gcloud](https://cloud.google.com/sdk/docs/install) and use `gcloud` directly.
2. Re-run `gws auth setup` which wraps `gcloud` calls.
3. Skip `gcloud` entirely — set up OAuth credentials manually in the [Cloud Console](#manual-oauth-setup-google-cloud-console)

### `redirect_uri_mismatch`

The OAuth client was not created as a **Desktop app** type. In the [Credentials](https://console.cloud.google.com/apis/credentials) page, delete the existing client, create a new one with type **Desktop app**, and download the new JSON.
