# browser-use/browser-use

Open-source Python library for AI browser agents, plus Browser Use Cloud: stealth browsers and a hosted agent API.

## installation

## Path 1: Fully Hosted Cloud

Scale browser automation with our hosted agent, stealth browsers, and infrastructure for profiles, recordings, and data policies.

[Get started with the API ↗](https://docs.browser-use.com/cloud/agent/quickstart)

New Google, GitHub, or Microsoft signups get **$1 cloud credit**.

<br/>

## Path 2: CLI

Paste this prompt into Claude Code, Codex, Hermes, OpenClaw, or your favorite agent.

```text
Install browser-use with `uv tool install browser-use==1.0.8rc1`, run `browser-use skill install` to register the skill, and connect it to my browser. If setup or connection fails, run `browser-use --doctor` and follow its output and the error message.
```

<br/>

## Path 3: Python Library

> **browser-use 1.0.** The agent writes Python against raw CDP in a persistent REPL, on [Pydantic AI](https://ai.pydantic.dev). Coming from 0.x? Read [MIGRATING.md](https://github.com/browser-use/browser-use/blob/main/MIGRATING.md).

Python 3.11 or newer. Get an API key at [Browser Use Cloud](https://cloud.browser-use.com/new-api-key?utm_source=github&utm_medium=readme-quickstart-api-key), then install with uv, or pip in a venv:

```bash
uv init --python 3.12 my-agent && cd my-agent
uv add 'browser-use==1.0.8rc1'
uv run browser-use login             # sign in once; the key is saved (over SSH: --device-code)
```

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install 'browser-use==1.0.8rc1'
browser-use login
```

Or set `BROWSER_USE_API_KEY=bu_...` (a key from https://cloud.browser-use.com/new-api-key). In a notebook: `browser_use.login()`.

**Pin the exact version** (`==`, never `>=`). browser-use moves fast and releases can break things. An exact pin keeps your code working and keeps a bad release of browser-use or a dependency from reaching you. Upgrade on purpose, after reading the release notes.

```python
from browser_use import Agent

result = Agent('Find the number of stars of the browser-use repo').run_sync()
print(result.final_result())
```

Defaults: model `bu-4.0` (BU 4.0) on the Browser Use gateway, browser = a Browser Use Cloud browser (stopped when the run ends). One key pays for the model and the cloud browser (also `ChatBrowserUse(api_key=...)`'s), and also works for the CLI and MCP server. A `.env` file works too.

Without a key, an interactive desktop run opens Browser Use login and continues after approval.
Over SSH or on Linux without a desktop it prints a link and a code to approve on any device, then continues.
Login creates and saves the key automatically; no copying is needed. Ctrl-C stops it with the missing-key error.
Set `BROWSER_USE_AUTO_LOGIN=false` to disable automatic login (`=true` allows the device code in a container).
Servers, CI, notebooks, containers and piped input keep the missing-key error and the `browser-use login` instructions.

Cloud browsers print their interactive live-view link to stderr by default.
Use `Browser(live_view=True)` to open it automatically, or `Browser(live_view=False)` to hide it.
Anyone with the link can control the browser.

With telemetry enabled, anonymous `library_auth` events record missing keys, login outcomes, available keys, and browser starts.
These events use the existing installation ID and contain no API keys, login URLs, or account identifiers (fields: **Telemetry** below).
Key availability does not prove that the server accepts the key.
Cloud browser startup confirms that authentication worked.

**Local browser, your model:**

```python
from browser_use import Agent, Browser, ChatOpenAI

agent = Agent(
    'Find the number of stars of the browser-use repo',
    llm=ChatOpenAI('gpt-6-luna'),        # OPENAI_API_KEY; or ChatOpenAI(model, base_url=...) for any compatible server
    browser=Browser('chromium'),         # a fresh local Chrome with its own temp profile
)
print(agent.run_sync().final_result())  # in async code: result = await agent.run()
```

| Browser | What the agent drives |
|---|---|
| `Browser()` | a Browser Use C

## tools

Integrated Browser Use, or hit a bug? Tell us how it went: `browser-use feedback 'kind: integration_report ...'` (or `browser_use.feedback(...)`) sends it straight to the Browser Use team.

<br/>

# Browser Use for enterprises

Talk to us about:

- **Security and compliance:** SOC 2, HIPAA with a BAA, GDPR, zero data retention and EU data residency.
- **Network control:** domain allow and block lists, network policies, egress control, your own proxies, IP allowlists and private networking.
- **Agent controls:** tool and action restrictions, blocked downloads and uploads, and human approval for sensitive steps.
- **Identity and access:** SSO with SAML, SCIM provisioning and role-based access.
- **Secrets:** vault integrations and domain-scoped credentials, kept out of prompts and task text.
- **Audit logging:** a record of every navigation and action, exported to your SIEM.
- **Deployment:** a fully on-prem browser, in your VPC or self-hosted.
- **Support:** SLAs, dedicated support and onboarding.

[Reach out to us](https://browser-use.com/enterprise#talk-to-sales) to tell us what your team needs.

<br/>

# FAQ

<details>
<summary><b>Should I use the fully hosted cloud, CLI, or Python library?</b></summary>

- **[Fully Hosted Cloud](#path-1-fully-hosted-cloud):** Send tasks through the API and let Browser Use run the agent, browser, and infrastructure.
- **[CLI](#path-2-cli):** Give an existing agent (Claude Code, Codex, Hermes, OpenClaw, Pi, Cursor, etc.) browser access. You can use it interactively or in scripts.
- **[Python Library](#path-3-python-library):** Run the open source agent in your own application, with custom tools, structured output, and your choice of model.

The CLI and Python library can each connect to a local or cloud browser. A cloud browser hosts the browser; the fully hosted API runs the agent as well.
</details>

<details>
<summary><b>What's the best model to use?</b></summary>

The default is `bu-4.0` (BU 4.0) on the Browser Use gateway. `llm='bu-4.0-mini'` is the cost-efficient choice for simple tasks, and `llm='bu-4.0-pro'` is the most capable. The earlier models still work: `bu-fast` is `gpt-6-luna` at medium reasoning, `bu-ultrafast` the same model at low reasoning on the priority tier (fastest), and `bu-smart` a larger one. `ChatOpenAI('gpt-6-luna')` with your own OpenAI key runs that model directly. Models and prices: [docs](https://docs.browser-use.com/cloud/agent/models). See the [benchmark](https://github.com/browser-use/benchmark).
</details>

<details>
<summary><b>Can I use this for free?</b></summary>

The Python library is free and [MIT-licensed](https://github.com/browser-use/browser-use/blob/main/LICENSE). Model inference and hosted browsers are separate: API providers, including `ChatBrowserUse`, and Browser Use Cloud charge for usage. You can also use `Browser('chromium')` with a local model, e.g. Ollama through `ChatOpenAI(model, base_url='http://localhost:11434/v1', api_key='ollama')`.
</details>

<details>
<summary><b>Terms of Service</b></summary>

This open-source library is licensed under the MIT License. For Browser Use services & data policy, see our [Terms of Service](https://browser-use.com/legal/terms-of-service) and [Privacy Policy](https://browser-use.com/privacy/).
</details>

<details>
<summary><b>How do I handle authentication?</b></summary>

- **Local browser:** `Browser('chrome')` drives the Chrome you have open, with your logins; `Browser('chrome', profile='Work')` uses a copy of that profile; `Browser('chromium', user_data_dir='~/bu-profile')` keeps its own logins between runs.
- **Cloud browser:** `Browser(cloud_profile_id='work')` keeps logins in a cloud profile; see the [profile sync guide](https://github.com/browser-use/browser-harness/blob/main/interaction-skills/profile-sync.md).
- **Passwords:** pass them as `sensitive_data`; the model types them with `type_secret(name)` and their values are redacted from cell output, checkpoints, tool results, the task and t
