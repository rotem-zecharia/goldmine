# microsoft/agent-lightning

The absolute trainer to light up AI agents.

## features

- 🪶 **~3,500 lines of code:** We treat simplicity as the first principle.
- 🧩 **Train with real agent harnesses:** Agents interact with the model through the Agent Lightning v1.0 proxy with **ZERO changes**, while keeping tools, context, control flow, and environments in the loop.
- ☸️ **Native Kubernetes support:** Run agents directly as Kubernetes Jobs without relying on external sandbox services.
- 💻 **Full coding agent training example:** Using only **6K training samples**, an end-to-end Qwen3.5-9B workflow improves SWE-bench Verified from **41.8% to 56.4%**, a gain of **14.6 percentage points**. We release the full pipeline, including data cleaning, reward-hacking prevention, and training scripts.

## installation

The following is an example installation on a CUDA 13.0 machine:

```bash
cd <this-repo>
uv sync
bash scripts/setup_verl.sh 0.8.0 cu130
```

See the [Installation Guide](https://microsoft.github.io/agent-lightning/stable/00-installation/) for details.

## tools

| Example | Description |
|---|---|
| [Calc-X](https://microsoft.github.io/agent-lightning/stable/50-example-calc-x/) | POC math reasoning example with AutoGen and MCP calculator tools, requiring only one GPU. |
| [GSM8K](https://microsoft.github.io/agent-lightning/stable/55-example-gsm8k/) | POC grade-school math reasoning example. |
| [ScienceWorld](https://microsoft.github.io/agent-lightning/stable/60-example-science-world/) | Interactive science tasks in a text-based environment. |
| [Search-R1](https://microsoft.github.io/agent-lightning/stable/65-example-search-r1/) | Multi-turn retrieval and reasoning agent. |
| [LLM-in-Sandbox](https://microsoft.github.io/agent-lightning/stable/70-example-llm-in-sandbox/) | General agent with computer and code execution tools. |
| [Coding Agent](https://microsoft.github.io/agent-lightning/stable/75-example-coding-agent/) | Coding agent trained with repository tests. |
