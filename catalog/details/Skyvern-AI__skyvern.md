# Skyvern-AI/skyvern

Automate browser based workflows with AI

## installation

Dependencies needed:
- [Python 3.11, 3.12, or 3.13](https://www.python.org/downloads/)

Additionally, for Windows:
- [Rust](https://rustup.rs/)
- VS Code with C++ dev tools and Windows SDK

#### 1. Install Skyvern

```bash
pip install "skyvern[all]"
```

#### 2. Run Skyvern

```bash
skyvern quickstart
```

The pip quickstart uses SQLite by default. To use a local Postgres container instead, run `skyvern quickstart` (Postgres container is started unless you pass `--no-postgres`), or connect to an existing database with `--database-string=postgresql+psycopg://user:pass@host:5432/dbname`.

## tools

Skyvern adds four core AI commands directly on the page object:

| Command | Description |
|---------|-------------|
| `page.act(prompt)` | Perform actions using natural language (e.g., "Click the login button") |
| `page.extract(prompt, schema)` | Extract structured data from the page with optional JSON schema |
| `page.validate(prompt)` | Validate page state, returns `bool` (e.g., "Check if user is logged in") |
| `page.prompt(prompt, schema)` | Send arbitrary prompts to the LLM with optional response schema |

Additionally, `page.agent` provides higher-level workflow commands:

| Command | Description |
|---------|-------------|
| `page.agent.run_task(prompt)` | Execute complex multi-step tasks |
| `page.agent.login(credential_type, credential_id)` | Authenticate with stored credentials (Skyvern, Bitwarden, 1Password) |
| `page.agent.download_files(prompt)` | Navigate and download files |
| `page.agent.run_workflow(workflow_id)` | Execute pre-built workflows |
