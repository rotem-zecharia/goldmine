# ifixai-ai/iFixAi

Independent Auditing of AI Agents. Run by human or the agent itself, to answer the most crucial question in the AI Agent Economy. Is the agent doing what is supposed to do? With iFixAi you can have th

## installation

Now try it yourself. Pick a path from the table above; full walkthrough: **[docs/get-started.md](docs/get-started.md)**.

## configuration

| Suite | Tests | Use when |
|---|---|---|
| `smoke` | 3 | just checking the pipeline works |
| `strategic` | 8 | quick read on the riskiest spots |
| `core` | 32 | the graded five-pillar scorecard |
| `extended` | 17 | frontier risk signal, scored outside the grade |
| `all` | 49 | everything (the default when you pass no `--suite`) |

Four themes (`security`, `reliability`, `compliance`, `frontier`) also work as `--suite` values; run `ifixai list suites` to browse them all.

```bash
ifixai run --provider http --endpoint <agent-url> --grounding sut  # your real deployed agent (recommended)
ifixai run --provider openai --suite strategic   # quick bare-model read (8 tests)
ifixai run --provider openai --suite core        # quick bare-model read, graded scorecard
```
