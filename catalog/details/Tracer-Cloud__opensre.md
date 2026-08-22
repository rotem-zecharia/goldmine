# Tracer-Cloud/opensre

Build your own AI SRE agents. The open source toolkit for the AI era.

## features

When something breaks in production, the evidence is scattered across logs, metrics, traces, runbooks, and Slack threads. OpenSRE is an open-source framework for AI SRE agents that resolve production incidents, built to run on your own infrastructure.

We do that because SWE-bench<sup>1</sup> gave coding agents scalable training data and clear feedback. Production incident response still lacks an equivalent.

Distributed failures are slower, noisier, and harder to simulate and evaluate than local code tasks, which is why AI SRE, and AI for production debugging more broadly, remains unsolved.

OpenSRE is building _that_ missing layer:

> an open reinforcement learning environment for agentic infrastructure incident response, with end-to-end tests and synthetic incident simulations for realistic production failures

We do that by:

- building easy-to-deploy, customizable AI SRE agents for production incident investigation and response
- running scored synthetic RCA suites that check root-cause accuracy, required evidence, and adversarial red herrings [(tests/synthetic)](tests/synthetic/rds_postgres)
- running real-world end-to-end tests across cloud-backed scenarios including Kubernetes, EC2, CloudWatch, Lambda, ECS Fargate, and Flink [(tests/e2e)](tests/e2e)
- keeping semantic test-catalog naming so e2e vs synthetic and local vs cloud boundaries stay obvious [(tests/README.md)](tests/README.md)

Our mission is to build AI SRE agents on top of this, scale it to thousands of realistic infrastructure failure scenarios, and establish OpenSRE as the benchmark and training ground for AI SRE.

<sup>1</sup> https://arxiv.org/abs/2310.06770

---

## installation

The root installer URL auto-detects Unix shell vs PowerShell and installs the latest build from `main`. OpenSRE moves quickly, so `main` is the latest stable version for normal installs.

macOS / Linux:

```bash
curl -fsSL https://install.opensre.com | bash
```

The macOS/Linux installer does not require sudo. If no writable bin directory is already on `PATH`, it installs to `~/.local/bin` and prints the shell command to apply the PATH update.

Equivalent explicit main-channel form:

```bash
curl -fsSL https://install.opensre.com | bash -s -- --main
```

Homebrew:

```bash
brew tap tracer-cloud/tap
brew install tracer-cloud/tap/opensre
```

Windows (PowerShell):

```powershell
irm https://install.opensre.com | iex
```

<!--
```bash
pipx install opensre
``` -->

---

## Quick Start

Contributors: start at [`main.py`](main.py) for the process entrypoint map.

Configure once, then pick how you want to run investigations:

```bash
opensre onboard
```

**Interactive shell** — with no subcommand, `opensre` starts a REPL (TTY required). Describe incidents in plain language, stream investigations, and use slash commands for session control (`/help`, `/status`, `/cost`, `/sessions`, `/resume`, `/compact`, `/new`, `/exit`), integrations (`/integrations list`, `/integrations verify`), local agent fleet monitoring (`/agents`), and reasoning depth (`/effort` for **OpenAI** and **Codex** — `low` through `max`). Ctrl+C cancels an in-flight investigation without losing session state. See **[interactive shell commands](https://www.opensre.com/docs/interactive-shell-commands)** for the full reference.

```bash
opensre
```

**Headless CLI** — run one agent turn non-interactively from a terminal, script, or CI job:

```bash
opensre ask "why is checkout-api slow?"
```

See **[Headless CLI](https://www.opensre.com/docs/headless-cli)** for stdin prompts, JSON output, and tool approvals.

**One-shot investigation** — run the agent once against an alert file:

```bash
opensre investigate -i tests/e2e/kubernetes/fixtures/datadog_k8s_alert.json
```

**Remote runtime investigation** — investigate a deployed service by name (live health, logs, and deployment status):

```bash
opensre investigate --service api-backend
```

**Hermes log watch** — tail a Hermes `errors.log`, classify incidents, and optionally alert on Telegram:

```bash
opensre hermes watch
```

**From Python** — drive the agent in-process from your own code (source checkout required):

```python
from core.agent_harness import AgentSession

session = AgentSession.start()
result = session.chat("why is checkout-api slow?")
if result.answered:
    print(result.primary_response_text)
```

See **[Python API](https://www.opensre.com/docs/python-api)** for sessions, conversations, and custom output sinks.

**For your team's daily loop:** embed OpenSRE in the Python services and automations your teammates already use.
Start with the in-repo [Python API guide](docs/python-api.mdx), then use it every day to make incident response repeatable.

Other useful commands:

```bash
opensre integrations setup
opensre agents scan
opensre update
opensre uninstall   # remove opensre and all local data
```

---

## Deployment

Two primary AWS EC2 paths and a general hosted option:

- **Gateway (AMI + systemd):** `make build-gateway-image` then `make deploy-gateway` — Telegram gateway only, no Docker; the gateway is installed into a server image that new servers start from.
- **Hosted (Railway / ECS / Vercel):** deploy with the repo `Dockerfile`; set `LLM_PROVIDER` and the matching API key (see [`.env.example`](.env.example)), plus `DATABASE_URI` and `REDIS_URI` if persistence is needed.

**[Full deployment steps and prerequisites → DEPLOYMENT.md](DEPLOYMENT.md)**

---

## How OpenSRE Works

<img
  src="https://github.com/user-attachments/assets/936ab1f2-9bda-438d-9897-e8e9cd98e335"
  width="1064"
  height="568"
  alt="opensre-how-it-works-github"
/>

When an alert fires, OpenSRE automatically:

1. **Fetches** the 
