# KeygraphHQ/shannon

Shannon is an AI pentester for web applications and APIs. It analyzes your source code, identifies attack vectors, and executes real exploits to prove vulnerabilities before they reach production.

## tools

It analyzes your source code, identifies attack paths, and executes real exploits to prove vulnerabilities before they reach production.

**This repository is Shannon Open Source: the full agent, run locally from your command line.**

---

<a href="https://discord.gg/9ZqQPuhJB7"><picture><source media="(prefers-color-scheme: dark)" srcset="./assets/discord_button_dark.png"><source media="(prefers-color-scheme: light)" srcset="./assets/discord_button_light.png"><img src="./assets/discord_button_light.png" height="40" alt="Join Discord"></picture></a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="https://keygraph.io/"><picture><source media="(prefers-color-scheme: dark)" srcset="./assets/keygraph_button_dark.png"><source media="(prefers-color-scheme: light)" srcset="./assets/keygraph_button_light.png"><img src="./assets/keygraph_button_light.png" height="40" alt="Visit Keygraph.io"></picture></a>

---

</div>

> [!TIP]
> **AI agents and LLMs:** start with [llms.txt](llms.txt) for a concise map of this repository, or use [llms-full.txt](llms-full.txt) for the README and docs combined into one file.

## Table of Contents

- [What is Shannon?](#what-is-shannon)
- [Shannon in Action](#shannon-in-action)
- [Quick Start](#quick-start)
- [Key Capabilities](#key-capabilities)
- [Editions](#editions)
- [Architecture](#architecture)
- [Documentation](#documentation)
- [Safety, Scope, and Limitations](#safety-scope-and-limitations)
- [License](#license)
- [About Keygraph](#about-keygraph)
- [Community and Support](#community-and-support)
- [Common Questions](#common-questions)

## What is Shannon?

Shannon is an autonomous AI pentester developed by [Keygraph](https://keygraph.io). It performs security testing of web applications and their underlying APIs by combining source-code analysis with live exploitation.

Shannon analyzes your web application's source code to identify potential attack vectors, then uses browser automation and command-line tools to execute real exploits against the running application and its APIs. Only vulnerabilities with a working proof-of-concept are included in the final report.

Shannon is the agent. This repository is Shannon Open Source, the standalone pentester you run yourself. The same Shannon also powers the [Keygraph platform](https://keygraph.io), Keygraph's commercial pentesting product. See [Editions](#editions) for how the two compare.

## features

Thanks to tools like Claude Code and Cursor, your team ships code non-stop. But your penetration test? That happens once a year. This creates a massive security gap. For the other 364 days, you could be unknowingly shipping vulnerabilities to production.

Shannon closes that gap by providing on-demand, automated penetration testing that can run against every build or release.

## Shannon in Action

<p align="center">
  <img src="assets/shannon-action.gif" alt="Shannon running an autonomous pentest" width="100%">
</p>

Sample penetration test reports from intentionally vulnerable applications, produced by Shannon Open Source:

| Target | Summary | Report |
| --- | --- | --- |
| OWASP Juice Shop | 20+ vulnerabilities, including authentication bypass, SQL injection, IDOR, and SSRF. | [View report](sample-reports/shannon-report-juice-shop.md) |
| c{api}tal API | Approximately 15 critical and high-severity API findings, including command injection, auth bypass, and mass assignment. | [View report](sample-reports/shannon-report-capital-api.md) |
| OWASP crAPI | 15+ critical and high-severity findings across JWT, injection, SSRF, and API authorization paths. | [View report](sample-reports/shannon-report-crapi.md) |

## requirements

- **Docker**: required for the worker container.
- **Node.js 18+**: required for the recommended `npx` workflow.
- **AI provider credentials**: Shannon runs on Anthropic, OpenAI, xAI, AWS Bedrock, [any other provider](docs/ai-providers.md#any-other-provider) in the harness catalogue, and any endpoint that speaks the Anthropic Messages API or the OpenAI Chat Completions or Responses API through a [custom base URL](docs/ai-providers.md#custom-base-url). You bring your own key, and Keygraph never proxies your model traffic. Shannon is provider-agnostic. See [AI providers](docs/ai-providers.md#suggested-models) for suggested model IDs.
- **Cyber safeguards cleared with your provider**: Anthropic and OpenAI apply real-time safeguards to cyber-security workloads, which can interrupt a scan mid-run. Complete their guidance for legitimate security testers before your first run - see [AI providers](docs/ai-providers.md#cyber-safeguards-do-this-before-your-first-scan).

### Run Shannon

> [!WARNING]
> Shannon actively executes exploits. Run it only against applications and environments you own or have explicit written authorization to test. Do not run Shannon against production systems.

```bash

## configuration

npx @keygraph/shannon setup

# Run a pentest against a source-available target.
npx @keygraph/shannon start -u https://your-app.com -r /path/to/your-repo
```

Shannon pulls the worker image from Docker Hub, starts the required local infrastructure, mounts the target repository read-only inside an ephemeral worker container, and writes results to a local workspace.

For source builds, authenticated scans, provider-specific setup, and platform notes, see [Documentation](#documentation).

> [!TIP]
> **Prefer to use a subscription instead of API credits?**
>
> - **OpenAI Codex:** The latest version of Shannon supports ChatGPT Plus and Pro subscriptions. Follow the [OpenAI Codex subscription setup guide](docs/ai-providers.md#openai-codex-chatgpt-pluspro-subscription) to get started.
> - **Claude Code:** The latest version of Shannon does not support Claude Code subscriptions. Follow the [Claude Code subscription setup guide](docs/ai-providers.md#claude-code-subscription) to use version `1.9.0`, which is the final release built on the Claude Agent SDK.

## limitations

Shannon is not a passive scanner. Its exploitation agents can create users, submit forms, mutate application state, trigger outbound requests, and otherwise affect the target system. Use sandboxed, staging, or local development environments with disposable data.

You are responsible for using Shannon legally and ethically. Do not point Shannon at systems, repositories, or applications you do not own or do not have explicit authorization to test.

Important limitations:

- Shannon Open Source focuses on actively exploitable issues such as Injection, XSS, SSRF, Broken Authentication, and Broken Authorization. Broader static-analysis coverage, including vulnerable dependencies and insecure configurations, is delivered through the Keygraph platform.
- Findings still require human review. LLM-generated reports can contain weakly supported or incorrect details.
- Anthropic, OpenAI, xAI, and AWS Bedrock are built-in providers, and any Anthropic Messages API or OpenAI Chat Completions or Responses API endpoint works through a custom base URL. Model capability varies, and a model that does not follow Shannon's instructions or tool-use constraints reliably will produce weaker results.
- A full run can take roughly 1 to 1.5 hours and may incur LLM API costs depending on model pricing and application complexity.
- Do not scan untrusted or adversarial codebases. AI-powered tools that read source code can be exposed to prompt injection.

Read the full [Safety and limitations](docs/safety.md) guide before running Shannon in a new environment.

## License

Shannon Open Source is licensed under the [GNU Affero General Public License v3.0](LICENSE).

Commercial and enterprise licensing is available for organizations that need different license terms, commercial support, private redistribution, managed-service use, or broader deployment options, including the Keygraph platform.

For commercial licensing, contact [shannon@keygraph.io](mailto:shannon@keygraph.io).

## About Keygraph

**Keygraph** is the company behind Shannon. It also builds the **Keygraph platform**, the commercial agentic pentesting product that closes the full AppSec lifecycle and runs an enhanced build of Shannon as its pentesting engine.

## Community and Support

**Community office hours** are available for hands-on help with bugs, deployments, and configuration questions.

- US/EU: Thursday, 10:00 AM PT
- Asia: Thursday, 2:00 PM IST
- [Book a slot](https://cal.com/george-flores-keygraph/shannon-community-office-hours)

[Join Discord](https://discord.gg/cmctpMBXwE) to ask questions, share feedback, and connect with other Shannon users.

At this time, Keygraph is not accepting external code contributions. Issues are welcome for bug reports and feature requests:

- [Report bugs](https://github.com/KeygraphHQ/shannon/issues)
- [Suggest features](https://github.com/KeygraphHQ/shannon/discussions)

Stay connected:

- [Keygraph website](https://keygraph.io)
- [Twitter/X: @KeygraphHQ](https://twitter.com/KeygraphHQ)
- [LinkedIn: Keygraph](https://linkedin.com/company/keygraph)

## Common Questions

### Can I self-host Shannon?

Yes. Shannon Open Source runs entirely on your own infrastructure in an ephemeral Docker container. Your source code is mounted read-only and never leaves your environment.

### Does Shannon support bring your own key (BYOK)?

Yes, always. You provide the LLM credentials Shannon uses to run a pentest, in every deployment, open source and commercial. Keygraph never proxies your model traffic.

### Does Shannon output SARIF?

Yes. Shannon emits SARIF 2.1.0, the OASIS standard format for static analysis results, alongside structured JSON. Any SARIF consumer reads it: code scanning services, vulnerability management platforms, security dashboards, and CI/CD pipelines. Set `report.sarif` to `"true"` in your configuration file to enable the SARIF log.

### Which AI providers does Shannon support?

Anthropic, OpenAI, xAI, and AWS Bedrock are built in and configured
