# Skyvern-AI/skyvern

Automate browser based workflows with AI

## installation

## Skyvern Cloud
[Skyvern Cloud](https://app.skyvern.com) is a managed cloud version of Skyvern that allows you to run Skyvern without worrying about the infrastructure. It allows you to run multiple Skyvern instances in parallel and comes bundled with anti-bot detection mechanisms, proxy network, and CAPTCHA solvers.

If you'd like to try it out, navigate to [app.skyvern.com](https://app.skyvern.com) and create an account.

## Run Locally (UI + Server)

Choose your preferred setup method:

> **Database default**: `skyvern quickstart` and `skyvern run server` default to a SQLite database at `~/.skyvern/data.db` so the pip path works without Postgres or Docker. To use Postgres instead, pass `--database-string` for an existing database (or omit `--no-postgres` so `quickstart` starts its own Postgres container). Docker Compose always uses the bundled Postgres service.

### Option A: pip install (Recommended for Python-managed local setup)

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

### Option B: Docker Compose

Use this option if you want everything containerized (Postgres, API, UI) and don't want to install Python/Node locally.

1. Install [Docker Desktop](https://www.docker.com/products/docker-desktop/)
2. Clone the repository:
   ```bash
   git clone https://github.com/skyvern-ai/skyvern.git && cd skyvern
   ```
3. Configure your LLM provider in `.env` (the `quickstart --docker-compose` command below will create it from `.env.example` if missing):
   ```bash
   cp .env.example .env  # if not already created
   # edit .env to add your LLM API key
   ```
4. Start everything:
   ```bash
   docker compose up -d
   ```
5. Open http://localhost:8080

### Troubleshooting

**`(sqlite3.OperationalError) table organizations already exists`** — You hit a known bug in `pip install skyvern==1.0.31`. Fix:

```bash
rm ~/.skyvern/data.db   # remove the leftover SQLite file
pip install --upgrade skyvern   # 1.0.32+ contains the fix
skyvern quickstart
```

If you are still on 1.0.31 and cannot upgrade, install via uv instead:

```bash
uv pip install skyvern
```

**`pip install skyvern` fails with ResolutionImpossible (litellm / fastmcp)** — You hit a dependency-resolution conflict in 1.0.31. Either upgrade to 1.0.32+ or use uv: `uv pip install skyvern`.

## SDK

**Skyvern is a Playwright extension that adds AI-powered browser automation.** It gives you the full power of Playwright with additional AI capabilities—use natural language prompts to interact with elements, extract data, and automate complex multi-step workflows.

**Installation:**
- Python SDK / cloud API: `pip install skyvern`
- Local server + packaged UI: `pip install "skyvern[all]"` then run `skyvern quickstart`
- Local server + packaged UI with Postgres: `pip install "skyvern[all]"` then run `skyvern quickstart --database-string=postgresql+psycopg://user:pass@host:5432/dbname`
- Packaged UI for an existing API: `pip install "skyvern[ui]"` then set `VITE_API_BASE_URL` (and `VITE_SKYVERN_API_KEY` if your API requires a key) and run `skyvern run ui`
- TypeScript: `npm install @skyvern/client`

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

### AI-Augmented Playwright Actions

All standard Playwright actions support an optional `prompt` parameter for AI-powered element location:

| Action | Playwright | AI-Augmented |
|--------|------------|--------------|
| Click | `page.click("#btn")` | `page.click(prompt="Click login button")` |
| Fill | `page.fill("#email", "a@b.com")` | `page.fill(prompt="Email field", value="a@b.com")` |
| Select | `page.select_option("#country", "US")` | `page.select_option(prompt="Country dropdown", value="US")` |
| Upload | `page.upload_file("#file", "doc.pdf")` | `page.upload_file(prompt="Upload area", files="doc.pdf")` |

**Three interaction modes:**
```python
# 1. Traditional Playwright - CSS/XPath selectors
await page.click("#submit-button")

# 2. AI-powered - natural language
await page.click(prompt="Click the green Submit button")

# 3. AI fallback - tries selector first, falls back to AI if it fails
await page.click("#submit-btn", prompt="Click the Submit button")
```

### Core AI Commands - Examples

```python
# act - Perform actions using natural language
await page.act("Click the login button and wait for the dashboard to load")

# extract - Extract structured data with optional JSON schema
result = await page.extract("Get the product name and price")
result = await page.extract(
    prompt="Extract order details",
    schema={"order_id": "string", "total": "number", "items": "array"}
)

# validate - Check page state (returns bool)
is_logged_in = await page.validate("Check if the user is logged in")

# prompt - Send arbitrary prompts to the LLM
summary = await page.prompt("Summarize what's on this page")
```

## features

## Skyvern Tasks
Tasks are the fundamental building block inside Skyvern. Each task is a single request to Skyvern, instructing it to navigate through a website and accomplish a specific goal.

Tasks require you to specify a `url`, `prompt`, and can optionally include a `data schema` (if you want the output to conform to a specific schema) and `error codes` (if you want Skyvern to stop running in specific situations).

<p align="center">
  <img src="fern/images/skyvern_2_0_screenshot.png"/>
</p>


## Skyvern Workflows
Workflows are a way to chain multiple tasks together to form a cohesive unit of work.

For example, if you wanted to download all invoices newer than January 1st, you could create a workflow that first navigated to the invoices page, then filtered down to only show invoices newer than January 1st, extracted a list of all eligible invoices, and iterated through each invoice to download it.

Another example is if you wanted to automate purchasing products from an e-commerce store, you could create a workflow that first navigated to the desired product, then added it to a cart. Second, it would navigate to the cart and validate the cart state. Finally, it would go through the checkout process to purchase the items.

Supported workflow features include:
1. Browser Task
1. Browser Action
1. Data Extraction
1. Validation
1. For Loops
1. File parsing
1. Sending emails
1. Text Prompts
1. HTTP Request Block
1. Custom Code Block
1. Uploading files to block storage
1. (Coming soon) Conditionals

<p align="center">
  <img src="fern/images/block_example_v2.png"/>
</p>

## Livestreaming
Skyvern allows you to livestream the viewport of the browser to your local machine so that you can see exactly what Skyvern is doing on the web. This is useful for debugging and understanding how Skyvern is interacting with a website, and intervening when necessary

## Form Filling
Skyvern is natively capable of filling out form inputs on websites. Passing in information via the `navigation_goal` will allow Skyvern to comprehend the information and fill out the form accordingly.

## Data Extraction
Skyvern is also capable of extracting data from a website.

You can also specify a `data_extraction_schema` directly within the main prompt to tell Skyvern exactly what data you'd like to extract from the website, in jsonc format. Skyvern's output will be structured in accordance to the supplied schema.

## File Downloading
Skyvern is also capable of downloading files from a website. All downloaded files are automatically uploaded to block storage (if configured), and you can access them via the UI.

## Authentication
Skyvern supports a number of different authentication methods to make it easier to automate tasks behind a login. If you'd like to try it out, please reach out to us [via email](mailto:founders@skyvern.com) or [discord](https://discord.gg/fG2XXEuQX3).

<p align="center">
  <img src="fern/images/secure_password_task_example.png"/>
</p>


### 🔐 2FA Support (TOTP)
Skyvern supports a number of different 2FA methods to allow you to automate workflows that require 2FA.

Examples include:
1. QR-based 2FA (e.g. Google Authenticator, Authy)
1. Email based 2FA
1. SMS based 2FA

🔐 Learn more about 2FA support [here](https://www.skyvern.com/docs/credentials/totp).

### Password Manager Integrations
Skyvern currently supports the following password manager integrations:
- [x] Bitwarden
- [x] Custom Credential Service (HTTP API)
- [ ] 1Password
- [ ] LastPass


## Model Context Protocol (MCP)

Skyvern supports the Model Context Protocol (MCP) to allow you to use any LLM that supports MCP.

See the MCP documentation [here](https://www.skyvern.com/docs/integrations/mcp#mcp-server)
