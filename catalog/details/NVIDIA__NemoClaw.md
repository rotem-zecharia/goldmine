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
