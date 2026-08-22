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

## features

Thanks to tools like Claude Code and Cursor, your team ships code non-stop. But your penetration test? That happens once a year. This creates a massive security gap. For the other 364 days, you could be unknowingly shipping vulnerabilities to production.

Shannon closes that gap by providing on-demand, automated penetration testing that can run against every build or release.

## requirements

- **Docker**: required for the worker container.
- **Node.js 18+**: required for the recommended `npx` workflow.
- **AI provider credentials**: Shannon runs on Anthropic, OpenAI, xAI, AWS Bedrock, [any other provider](docs/ai-providers.md#any-other-provider) in the harness catalogue, and any endpoint that speaks the Anthropic Messages API or the OpenAI Chat Completions or Responses API through a [custom base URL](docs/ai-providers.md#custom-base-url). You bring your own key, and Keygraph never proxies your model traffic. Shannon is provider-agnostic. See [AI providers](docs/ai-providers.md#suggested-models) for suggested model IDs.
- **Cyber safeguards cleared with your provider**: Anthropic and OpenAI apply real-time safeguards to cyber-security workloads, which can interrupt a scan mid-run. Complete their guidance for legitimate security testers before your first run - see [AI providers](docs/ai-providers.md#cyber-safeguards-do-this-before-your-first-scan).

## configuration

npx @keygraph/shannon setup

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
