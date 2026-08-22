# K-Dense-AI/scientific-agent-skills

Turn any AI agent into an AI Scientist. The #1 Agent Skills library for science, used by 175,000+ scientists worldwide. 163 ready-to-use validated skills plus 100+ scientific databases covering biolog

## installation

gh skill install K-Dense-AI/scientific-agent-skills

## requirements

- **Python**: 3.13+ for repository tooling; individual skill dependencies may support broader Python ranges
- **uv**: Python package manager (required for installing skill dependencies)
- **Client**: Any agent that supports the [Agent Skills](https://agentskills.io/) standard (Cursor, Claude Code, Gemini CLI, Codex, Google Antigravity, etc.)
- **System**: macOS, Linux, or Windows with WSL2
- **Dependencies**: Automatically handled by individual skills (check `SKILL.md` files for specific requirements)

## tools

Once you've installed the skills, you can ask your AI agent to execute complex multi-step scientific workflows. Here are some example prompts:

## features

- **[The Model Is No Longer the Bottleneck](https://www.k-dense.ai/blog/the-model-is-no-longer-the-bottleneck)** — The case for why a repository like this one exists: frontier models now match specialized scientific software on raw capability (±0.079 ppm on NMR hydrogen shift prediction), so the limiting factor has moved to the workflow around the model — data access, code execution, verification, and auditable output.
- **[The AI Co-Scientist Is Here. The Bottleneck Is Verification.](https://www.k-dense.ai/blog/ai-co-scientist-verification-bottleneck)** — A 10-point checklist for evaluating a research agent, built around exposing sources, code, data provenance, and intermediate work rather than a polished final answer — the same reasoning behind the provenance and retrieval-contract requirements in skills like [database-lookup](skills/database-lookup/) and [scientific-writing](skills/scientific-writing/).
- **[Reproduction, Not Generation, Is AI's Killer App for Science](https://www.k-dense.ai/blog/reproduction-not-generation-ai-for-science)** — Why re-running published analyses is the highest-value use of an agent: 78% of papers and 93% of individual analysis tasks reproduced across a 221-study benchmark, because a reproduction can be checked against known numbers while a generated claim cannot.
- **[Introducing K-Bench 01: Nine Frontier Models, 178 Real Scientific Tasks, and a Lot of Confident Wrong Answers](https://www.k-dense.ai/blog/introducing-k-bench-01-internal-benchmark)** — Nine frontier models on 178 real user tasks, with overclaiming in 40% of runs. Useful calibration for what to check when an agent reports success, and context for the verification boundaries written into the clinical, regulatory, and research-methodology skills above.

## configuration

uv run python tests/run_all.py --isolated
```

The [Skill Tests](https://github.com/K-Dense-AI/scientific-agent-skills/actions/workflows/skill-tests.yml) workflow runs the contract plus the standard-library-only suites on every pull request; the full `--isolated` sweep builds ~100 environments and is run locally or on a schedule.
