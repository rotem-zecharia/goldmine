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
