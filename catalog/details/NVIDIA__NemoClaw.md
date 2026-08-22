# NVIDIA/NemoClaw

Run agents like Hermes, LangChain Deep Agents, and OpenClaw more securely inside NVIDIA OpenShell with managed inference

## installation

Review [Prerequisites](https://docs.nvidia.com/nemoclaw/latest/get-started/prerequisites.html) before installing.
On a supported DGX or Windows Subsystem for Linux (WSL) host, press Enter at the `Run express install with these settings? [Y/n]:` prompt to use the recommended preset settings for that platform.
Express install mode installs OpenClaw by default.
If you accept, refer to [NemoClaw Quickstart with OpenClaw](https://docs.nvidia.com/nemoclaw/latest/get-started/quickstart.html).
Enter `n` if you want to choose Hermes or LangChain Deep Agents Code, a sandbox name, an inference provider, and a model interactively.
When connecting to a Hermes sandbox from a light terminal, NemoClaw may install a managed `nemoclaw-light` Hermes skin for readable assistant text; it removes that managed skin state again when the terminal no longer needs it and preserves any user-selected Hermes skin.

| Agent | Guide |
|-------|-------|
| OpenClaw (default) | [Quickstart with OpenClaw](https://docs.nvidia.com/nemoclaw/latest/get-started/quickstart.html) |
| Hermes | [Quickstart with Hermes](https://docs.nvidia.com/nemoclaw/latest/get-started/quickstart-hermes.html) |
| LangChain Deep Agents Code | [Quickstart with LangChain Deep Agents Code](https://docs.nvidia.com/nemoclaw/latest/user-guide/deepagents/get-started/quickstart.html) |

## Documentation

Refer to the following pages on the official documentation website for more information on NemoClaw.

| Page | Description |
|------|-------------|
| [Overview](https://docs.nvidia.com/nemoclaw/latest/about/overview.html) | What NemoClaw does and how it fits together. |
| [Architecture Overview](https://docs.nvidia.com/nemoclaw/latest/about/how-it-works.html) | High-level overview of the host CLI, agent integration layer, blueprint, sandbox lifecycle, and protection layers. |
| [Ecosystem](https://docs.nvidia.com/nemoclaw/latest/about/ecosystem.html) | How OpenClaw, OpenShell, and NemoClaw form a stack and when to use NemoClaw versus OpenShell alone. |
| [Architecture Details](https://docs.nvidia.com/nemoclaw/latest/reference/architecture.html) | Detailed description of agent integration structure, blueprint lifecycle, sandbox environment, and host-side state. |
| [Prerequisites](https://docs.nvidia.com/nemoclaw/latest/get-started/prerequisites.html) | Hardware, software, and supported platforms, with any platform-specific pre-setup. |
| [Choose an Inference Provider](https://docs.nvidia.com/nemoclaw/latest/user-guide/openclaw/inference/learn-and-choose/choose-inference-provider) | Supported providers, validation, and routed inference configuration. |
| [Network Policies](https://docs.nvidia.com/nemoclaw/latest/reference/network-policies.html) | Baseline rules, operator approval flow, and egress control. |
| [Customize Network Policy](https://docs.nvidia.com/nemoclaw/latest/network-policy/customize-network-policy.html) | Static and dynamic policy changes, presets. |
| [Security Best Practices](https://docs.nvidia.com/nemoclaw/latest/security/best-practices.html) | Controls reference, risk framework, and posture profiles for sandbox security. |
| [Sandbox Hardening](https://docs.nvidia.com/nemoclaw/latest/user-guide/openclaw/manage-sandboxes/configure-sandboxes/review-sandbox-hardening) | Container security measures, capability drops, process limits. |
| [CLI Commands](https://docs.nvidia.com/nemoclaw/latest/reference/commands.html) | Full NemoClaw CLI command reference. |
| [Troubleshooting](https://docs.nvidia.com/nemoclaw/latest/reference/troubleshooting.html) | Common issues and resolution steps. |

## Community

Join the NemoClaw community to ask questions, share feedback, and report issues.
NemoClaw is an alpha project, so maintainers review issues, discussions, and pull requests on a best effort basis without guaranteed response timelines.

| Need | Channel |
|------|---------|
| Setup or usage questions | [GitHub Discussions](https://github.com/NVIDIA/NemoClaw/discussions) or [Discord](ht
