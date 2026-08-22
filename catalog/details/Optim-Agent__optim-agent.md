# Optim-Agent/optim-agent

LLM agents as your hyperparameter optimizer.

## features

- **Semantic proposals** - coding agents reason over parameter meanings, study
  context, and observed outcomes instead of treating every dimension as an
  anonymous coordinate.
- **Small-budget leverage** - useful when evaluations are expensive and classical
  surrogates are still data-starved.
- **Agent CLI upside** - proposal quality can improve as the underlying coding
  agents improve, such as moving from GPT-5.5 to GPT-5.6, without changing your
  optimization code.
- **Auditable decisions** - JSON/SQLite studies retain configurations,
  outcomes, states, context, and optional agent rationale.
- **Bounded execution** - the agent only proposes values; optim-agent validates
  them against the declared space, and invalid output falls back to safe
  sampling.

## installation

Install the Codex skill:

```text
$skill-installer install https://github.com/Optim-Agent/optim-agent
```

Install the Claude Code plugin:

```bash
claude plugin marketplace add Optim-Agent/optim-agent && claude plugin install optim-agent@optim-agent
```

Install the Python package:

```bash
