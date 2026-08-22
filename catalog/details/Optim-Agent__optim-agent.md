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
# Stable release from PyPI
python -m pip install optim-agent

# Latest source from GitHub
python -m pip install "optim-agent @ git+https://github.com/Optim-Agent/optim-agent.git"
```

Requires one authenticated agent CLI on `PATH`:
[claude](https://docs.anthropic.com/en/docs/claude-code),
[codex](https://github.com/openai/codex), or
[opencode](https://github.com/sst/opencode).

## Quickstart

```python
import optim_agent as oa

def objective(trial):
    threshold = trial.suggest_float(
        "threshold", 0.05, 0.95,
        context="decision threshold; higher values trade recall for precision",
    )
    budget = trial.suggest_int(
        "budget", 10, 200, log=True,
        context="compute or operating budget; larger values may improve quality",
    )
    return evaluate_system(threshold=threshold, budget=budget)  # domain code

study = oa.create_study(
    direction="maximize",
    sampler=oa.AgentSampler(
        backend="claude",  # or "codex" / "opencode"
        effort="high",
        context="maximize system quality under a strict operating-cost budget",
        history=5,
        explicit_reasoning=True,
        qualitative_notes=True,
    ),
    storage="study.json",  # optional: persist and resume
    summarize=True,  # optional: agent-written result summary after the last trial
)
study.optimize(objective, n_trials=20)
print(study.best_value, study.best_params)
print(study.summary)  # the summary agent's narration of the finished study
```

Optional `context` gives domain meaning to the study and parameters. Provide it
study-wide on `AgentSampler(context=...)`, per parameter on
`suggest_*(..., context=...)`, or both.

## Where It Applies

| Area | Parameters optim-agent can tune | Example objective |
|---|---|---|
| **Model training** | learning rates, architectures, augmentation, regularization | validation quality, compute, robustness |
| **Inference and serving** | quantization, batching, decoding, caching, routing | quality, latency, throughput, cost |
| **Quantitative research** | signal windows, thresholds, rebalance rules, risk controls | walk-forward return, drawdown, turnover |
| **Reinforcement learning and decisions** | objective weights, exploration schedules, environment settings, policy thresholds | return, safety, sample efficiency |
| **Scientific workflows** | simulation inputs, solver settings, experimental controls | fit, error, runtime, resource use |
| **Black-box systems** | any bounded categorical, integer, or continuous configuration | scalar objective score |

For reinforcement learning, optim-agent tunes the system around the learning
loop; it does not replace the policy-learning algorithm.

## Optimization Trajectory

![Agent optimization trajectory compared with TPE](docs/assets/optimization_trajectory.gif)

This seed-0 Branin trace compares TPE and GPT-5.5 under the same 10-trial
budget, with incumbent objective values after each trial. It is a trajectory
illustration; aggregate benchmark results and reproduction commands follow.

### Optimizing Math Functions without Context: Branin-2D and Ackley-5D

Hard-function agents receive **no supplied task context**: only generic
`x1...x5` parameter names, numeric bounds, and trial history. Runs use 10 trials
over five seeds; Random and TPE are unchanged baselines.

#### Top-tier Agents

![No-context top-tier hard-function benchmark](docs/assets/hard_benchmarks_tier.png)

| method        | mean best Branin ↓ | mean best Ackley-5D ↓ |
| ------------- | -----------------: | --------------------: |
| Random        |              5.008 |                19.639 |
| TPE           |             11.395 |                18.843 |
| GPT-5.5       |              1.326

## tools

### Sampler Prompt Controls

`effort` is forwarded to the backend CLI's reasoning-effort flag. The harness
prompt is controlled separately:

```python
oa.AgentSampler(
    backend="codex",
    effort="medium",
    history=5,
    explicit_reasoning=True,
    qualitative_notes=True,
)
```

Set `history=None` to show all completed/pruned trials. Use
`explicit_reasoning=False` or `qualitative_notes=False` for shorter agent
replies.

### Trial Logging

`study.optimize(..., verbose=...)` controls per-trial output:

- `verbose=True` (default) renders a table on an interactive terminal: one row
  per trial with columns `trial`, `value`, `best`, `state`, plus one column per
  search-space parameter in first-seen order. Long rows are truncated with an
  ellipsis to fit the terminal width; missing values (e.g. failed trials)
  render as `-`.
- When stdout is not a TTY (piped output, CI logs), `verbose=True` / `"table"`
  automatically falls back to the greppable one-line format
  (`[optim-agent] trial 3: value=0.91 state=complete best=0.91`).
- `verbose="line"` always uses the one-line format, even on a TTY.
- `verbose="table"` uses the table on a TTY and the line format when piped.
- `verbose=False` silences per-trial output.

With define-by-run spaces, a trial that introduces a new parameter key reprints
the header with the superset of columns.

### Summary Agent

Pass `summarize=True` to `create_study` to have the agent narrate the finished
study once, after the last trial completes:

```python
study = oa.create_study(
    sampler=oa.AgentSampler(backend="claude"),
    storage="study.json",
    summarize=True,
)
study.optimize(objective, n_trials=20)
print(study.summary)  # also persisted in JSON / SQLite storage
```

The summary is structured into four sections — best configuration, search-space
insights, trajectory highlights, and suggested next steps. It is printed to the
terminal and persisted on `study.summary` (additive key in JSON storage and the
SQLite `meta` table; old stored studies load with `summary=None`).

Backend resolution: an explicit `summary_backend=` wins; otherwise the
sampler's backend is reused when the sampler is an `AgentSampler`. With any
other sampler, pass `summary_backend=` or `create_study` raises a `ValueError`
naming the fix. `summary_model=` / `summary_effort=` override the sampler's
model/effort for the summary. Agent replies that cannot be parsed into all four
sections fall back to printing the raw text — a summary never fails the study,
and studies with zero complete trials skip it with a one-line notice.
`backend="mock"` works for the summarizer too, so demos and tests run without a
real agent CLI.

### Pruning

```python
study = oa.create_study(
    sampler=oa.AgentSampler(backend="codex"),
    pruner=oa.AgentPruner(
        backend="codex", level="medium", effort="medium",
    ),  # level: loose | medium | tight
)

def objective(trial):
    lr = trial.suggest_float("lr", 1e-5, 1e-1, log=True,
                             context="learning rate for training an image classifier")
    for epoch in range(20):
        loss = train_one_epoch(lr)
        trial.report(loss, epoch)
        if trial.should_prune():
            raise oa.TrialPruned()
    return loss
```

The pruner agent compares the current learning curve against completed trials
and answers prune/keep; `loose` prunes only clearly underperforming runs,
while `tight` prunes aggressively. Agent errors never prune a trial.

### Concurrency & Distributed Studies

Set `max_concurrency` (default `1`) to evaluate several trials at once, and use
a SQLite `storage` file (`.db` / `.sqlite`) as the concurrency-safe shared
history:

```python
study = oa.create_study(
    sampler=oa.AgentSampler(backend="claude"),
    storage="study.db",        # SQLite → safe for many workers; .json stays single-writer
    max_concurrency=8,         # up to 8 objectives run at once
)
study.optimize(objective, n_trials=100)
```

- **Within a process**, `max_concurrency
