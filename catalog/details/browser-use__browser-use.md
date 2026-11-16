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
Install browser-use with `uv tool install browser-use==1.0.6`, run `browser-use skill install` to register the skill, and connect it to my browser. If setup or connection fails, run `browser-use --doctor` and follow its output and the error message.
```

<br/>

## Path 3: Python Library

> **browser-use 1.0.** The agent writes Python against raw CDP in a persistent REPL, on [Pydantic AI](https://ai.pydantic.dev). Coming from 0.x? Read [MIGRATING.md](https://github.com/browser-use/browser-use/blob/main/MIGRATING.md).

Python 3.11 or newer. With uv, or pip in a venv:

```bash
uv init --python 3.12 my-agent && cd my-agent
uv add 'browser-use==1.0.6'
export BROWSER_USE_API_KEY=bu_...    # get one at https://cloud.browser-use.com/new-api-key
```

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install 'browser-use==1.0.6'
export BROWSER_USE_API_KEY=bu_...
```

**Pin the exact version** (`==`, never `>=`). browser-use moves fast and releases can break things. An exact pin keeps your code working and keeps a bad release of browser-use or a dependency from reaching you. Upgrade on purpose, after reading the release notes.

```python
from browser_use import Agent

result = Agent('Find the number of stars of the browser-use repo').run_sync()
print(result.final_result())
```

Defaults: model `bu-4.0` (BU 4.0) on the Browser Use gateway, browser = a Browser Use Cloud browser (stopped when the run ends). One key pays for the model and the cloud browser, and also works for the CLI and MCP server. A `.env` file works too.

Without a key, an interactive desktop run opens Browser Use login and continues after approval.
Login creates and saves the key automatically; no copying is needed.
Set `BROWSER_USE_AUTO_LOGIN=false` to disable automatic login.
Servers, CI, and piped input keep the missing-key error and the `browser-use login` instructions.

Cloud browsers print their interactive live-view link to stderr by default.
Use `Browser(live_view=True)` to open it automatically, or `Browser(live_view=False)` to hide it.
Anyone with the link can control the browser.

With telemetry enabled, anonymous `library_auth` events record missing keys, login outcomes, available keys, and browser starts.
These events use the existing installation ID and contain no API keys, login URLs, or account identifiers.
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
| `Browser()` | a Browser Use Cloud browser (default) |
| `Browser('chromium')` | a fresh local Chrome/Chromium/Edge with its own temp profile, deleted afterwards. Headless when there is no display (Docker, CI); `headless=`, `executable_path=`, `user_data_dir=` (a profile dir kept between runs) |
| `Browser('chrome')` | the Chrome you have open, with your logins (turn on chrome://inspect/#remote-debugging once) |
| `Browser('chrome', profile='Work')` | a new Chrome on a temporary copy of your Chrome profile `Work` (sync off); your Chrome can stay open, except on Windows |

Other models: `ChatAn

## tools

Something broken? `browser-use feedback 'what happened'` (or `browser_use.feedback(...)`) sends it straight to the Browser Use team.

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
- **Passwords:** pass them as `sensitive_data`; the model types them with `type_secret(name)` and their values are redacted from cell output, checkpoints, tool results, the task and the result. Not a sandbox: model-written Python can read them, and screenshots, page JavaScript and a cloud live view can reveal a typed value.
</details>

<details>
<summary><b>How do I solve CAPTCHAs?</b></summary>

[Browser Use Cloud](https://docs.browser-use.com/cloud/browser/quickstart) provides stealth browsers and proxies designed to reduce bot detection and CAPTCHA challenges. With the Python library, `Browser()` is a cloud browser by default.

Cloud browsers also solve CAPTCHAs automatically, and the agent waits for the solver with `solve_captcha()` instead of clicking the challenge. `Browser(captcha_solver=False)` turns the solver off.

Results depend on the site and challenge; no browser configuration guarantees that every CAPTCHA can be avoided or solved.
</details>

<details>
<summary><b>Can I limit which sites the agent visits?</b></summary>

`Browser(allowed_domains=['example.com', '*.example.org'])`, `Browser(prohibited_domains=['evil.com'])` or `Brows
