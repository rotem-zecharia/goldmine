# promptfoo/promptfoo

Test your prompts, agents, and RAGs. Red teaming/pentesting/vulnerability scanning for AI. Compare performance of GPT, Claude, Gemini, DeepSeek, and more. Simple declarative configs with command line 

## installation

Requires [Node.js](https://nodejs.org/en/download) `>=22.22.0` for npm and npx usage. Node.js 24 LTS
is recommended; see the [runtime support guide](https://www.promptfoo.dev/docs/installation/#nodejs-runtime-support).

```sh
npm install -g promptfoo
promptfoo init --example getting-started
```

Also available via `brew install promptfoo` and `pip install promptfoo`. You can also use `npx promptfoo@latest` to run any command without installing.

Most LLM providers require an API key. Set yours as an environment variable:

```sh
export OPENAI_API_KEY=sk-abc123
```

Once you're in the example directory, run an eval and view results:

```sh
cd getting-started
promptfoo eval
promptfoo view
```

See [Getting Started](https://www.promptfoo.dev/docs/getting-started/) (evals) or [Red Teaming](https://www.promptfoo.dev/docs/red-team/) (vulnerability scanning) for more.

## features

- **Developer-first**: Fast, with features like live reload and caching
- **Private**: LLM evals run 100% locally - your prompts never leave your machine
- **Flexible**: Works with any LLM API or programming language
- **Battle-tested**: Powers LLM apps serving 10M+ users in production
- **Data-driven**: Make decisions based on metrics, not gut feel
- **Open source**: MIT licensed, with an active community
