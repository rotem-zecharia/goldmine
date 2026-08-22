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


## ⚡ Architecture

<p align="center">
  <img src="docs/images/architecture.jpg" alt="Agent Lightning v1.0 architecture" width="800">
</p>

Agent Lightning v1.0 keeps the training architecture simple with three lightweight components:

- **Trainer:** Runs `verl` and vLLM, builds training samples, and updates the policy.
- **API Gateway:** Proxies model requests and captures training data.
- **Rollout Controller:** Runs agents locally or as Kubernetes Jobs.

The Trainer creates rollouts, the Controller launches agents, and the Gateway turns interactions into training data, while agents continue to run with their real harnesses.

## ⚡ Results

We evaluate Agent Lightning v1.0 across several practical training domains, including Search R1, LLM-in-Sandbox, and Coding Agent. Pure RL delivers substantial improvements across all three domains, as shown below.

<p align="center">
  <img src="docs/images/benchmark-comparison.jpg" alt="Agent Lightning v1.0 benchmark comparison" width="600">
</p>

## ⚡ Documentation

| Section | Content |
|---------|---------|
| [Installation](https://microsoft.github.io/agent-lightning/stable/00-installation/) | Base environment and `verl` GPU stack |
| [Quick Start](https://microsoft.github.io/agent-lightning/stable/01-quick-start/) | Local first run and end-to-end flow |
| [Basics](https://microsoft.github.io/agent-lightning/stable/05-basics/) | Components, rollouts, events, and trajectories |
| [Trainer Configuration](https://microsoft.github.io/agent-lightning/stable/20-trainer-configuration/) | `verl` integration and trace aggregation |
| [API Gateway Configuration](https://microsoft.github.io/agent-lightning/stable/25-api-gateway-configuration/) | Gateway and model proxy settings |
| [Controller Configuration](https://microsoft.github.io/agent-lightning/stable/30-controller-configuration/) | Local and Kubernetes runners |
| [Asynchronous Training](https://microsoft.github.io/agent-lightning/stable/35-asynchronous-training/) | Collocated async collection and pause/drain |

## tools

| Example | Description |
|---|---|
| [Calc-X](https://microsoft.github.io/agent-lightning/stable/50-example-calc-x/) | POC math reasoning example with AutoGen and MCP calculator tools, requiring only one GPU. |
| [GSM8K](https://microsoft.github.io/agent-lightning/stable/55-example-gsm8k/) | POC grade-school math reasoning example. |
| [ScienceWorld](https://microsoft.github.io/agent-lightning/stable/60-example-science-world/) | Interactive science tasks in a text-based environment. |
| [Search-R1](https://microsoft.github.io/agent-lightning/stable/65-example-search-r1/) | Multi-turn retrieval and reasoning agent. |
| [LLM-in-Sandbox](https://microsoft.github.io/agent-lightning/stable/70-example-llm-in-sandbox/) | General agent with computer and code execution tools. |
| [Coding Agent](https://microsoft.github.io/agent-lightning/stable/75-example-coding-agent/) | Coding agent trained with repository tests. |

## ⚡ Articles

- 8/19/2026 [Agent Lightning v1.0: Towards Harnessed Agentic RL](https://arxiv.org/abs/2608.17528) technical report.
- 12/17/2025 [Adopting the Trajectory Level Aggregation for Faster Training](https://agent-lightning.github.io/posts/trajectory_level_aggregation/) Agent-lightning blog.
- 11/4/2025 [Tuning ANY AI agent with Tinker ✕ Agent-lightning](https://medium.com/@yugez/tuning-any-ai-agent-with-tinker-agent-lightning-part-1-1d8c9a397f0e) Medium. See also [Part 2](https://medium.com/@yugez/tuning-any-ai-agent-with-tinker-agent-lightning-part-2-332c5437f0dc).
- 10/22/2025 [No More Retokenization Drift: Returning Token IDs via the OpenAI Compatible API Matters in Agent RL](https://blog.vllm.ai/2025/10/22/agent-lightning.html) vLLM blog. See also [Zhihu writeup](https://zhuanlan.zhihu.com/p/1965067274642785725).
- 8/11/2025 [Training AI Agents to Write and Self-correct SQL with Reinforcement Learning](https://medium.com/@yugez/training-ai-agents-to-write-and-self-correct-sql-with-reinforcement-learning-571ed31281ad) Medium.
- 8/5/2025 [Agent Lightning: Train ANY AI Agents with Reinforcement Learning](https://arxiv.org/abs/2508.03680) arXiv paper.
- 7/26/2025 [We discovered an approach to train any AI agent with RL, with (almost) zero code changes.](https://www.reddit.com/r/LocalLLaMA/comments/1m9m670/we_discovered_an_approach_to_train_any_ai_agent/) Reddit.
- 6/6/2025 [Agent Lightning - Microsoft Research](https://www.microsoft.com/en-us/research/project/agent-lightning/) Project page.

## ⚡ Community Projects

- [DeepWerewolf](https://github.com/af-74413592/DeepWerewolf) — A case study of agent RL training for the Chinese Werewolf game built with AgentScope and Agent Lightning.
- [AgentFlow](https://agentflow.stanford.edu/) — A modular multi-agent framework that combines planner, executor, verifier, and generator agents with the Flow-GRPO algorithm to tackle long-horizon, sparse-reward tasks.
- [Youtu-Agent](https://github.com/TencentCloudADP/Youtu-agent) — Youtu-Agent lets you build and train your agent with ease. Built with [a modified branch](https://github.com/microsoft/agent-lightning/tree/contrib/youtu-agent-lightning) of Agent Lightning, Youtu-Agent has verified up to 128 GPUs RL training on maths/code and search capabilities with steady convergence. Also check [the recipe](https://github.com/TencentCloudADP/youtu-agent/tree/rl/agl) and their blog [*Stop Wrestling with Your Agent RL: How Youtu-Agent Achieved Stable, 128-GPU Scaling Without Breaking a Sweat*](https://spotted-coconut-df8.notion.site/Stop-Wrestling-with-Your-Agent-RL-How-Youtu-Agent-Achieved-Stable-128-GPU-Scaling-Without-Breaking-2ca5e8f089ba80539a98c582b65e0233).

## ⚡ Citation

If you use Agent Lightning v1.0 in your research or projects, please cite the technical report:

```bibtex
@misc{he2026agentlightningv10harnessed,
  title={Agent Lightning v1.0: Towards Harnessed Agentic RL},
  author={Zhiyuan He and Siwei Zhang and Zhiwen Zhou and Yuqing Yang and Yu Kang and Yuge Zhang and Luna K. Qiu and Tin Yan Tsui and Jiahang Xu and Cho
