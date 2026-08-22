# openai/codex-security

OpenAI's Codex Security CLI and TypeScript SDK for finding, validating, and fixing security vulnerabilities. npm: https://www.npmjs.com/package/@openai/codex-security

## installation

Requires Node.js 22.13.0 or later in the 22.x release line, Node.js 24.x, or
Node.js 26.x; Python 3.10 or later; and access to Codex Security.

```bash
npm install @openai/codex-security
npx @openai/codex-security login
npx @openai/codex-security scan .
npx @openai/codex-security scan . --patch
npx @openai/codex-security scan . --patch --patch-severity high --json
npx @openai/codex-security scan . --patch --patch-severity high --create-pr
npx @openai/codex-security scan . --model gpt-5.6-terra --effort high
npx @openai/codex-security scan . --scan-prompt-file scan.md --post-scan-prompt-file follow-up.md
npx @openai/codex-security scan . --validation-prompt-file validation.md
npx @openai/codex-security scan . --mode deep --workers 2 --subagents 0 --stop-after-no-new 3 --max-discovery-runs 10 --max-time-hours 1.5
```

For CI, set `OPENAI_API_KEY` or `CODEX_API_KEY` instead of signing in.

Use `--validation-prompt-file` to replace final validation with your own setup,
testing, and cleanup instructions. This works for standard and diff scans;
Deep scans do not support it. See [custom validation](sdk/typescript/README.md#custom-validation).
For a runnable local example, see the [custom validation demo](examples/custom-validation/README.md).
Environment API keys are passed directly to the current scan and are never
stored in Codex's credential home or system keyring.

After showing the findings summary, interactive scans with findings ask whether
to open a finding browser where you can inspect full details, choose a severity
threshold, select individual findings, and add patch instructions for each one.
Each selected finding runs in its own saved Codex desktop task.
Use `--patch --patch-severity high` to fix high and critical findings. Add
`--create-pr`, or enable the pull request option during review, to commit the
verified files and open a draft GitHub pull request. Ordinary scans do not
change repository files.

Deep-scan discovery stops after 96 hours by default. Set `--max-time-hours` to
any positive number of hours, including fractional hours, up to 96. Completed
findings are preserved and returned when the limit is reached.

To use another inference provider, set its API key and select a model:

```bash
export OPENROUTER_API_KEY="<your-openrouter-api-key>"
npx @openai/codex-security scan . --provider openrouter --model anthropic/claude-sonnet-4.5

export FIREWORKS_API_KEY="<your-fireworks-api-key>"
npx @openai/codex-security scan . --provider fireworks --model accounts/fireworks/models/qwen3-235b-a22b

export AWS_BEARER_TOKEN_BEDROCK="<your-bedrock-api-key>"
export AWS_REGION="us-east-2"
npx @openai/codex-security scan . --provider amazon-bedrock --model openai.gpt-5.6-luna
```

Amazon Bedrock also supports standard AWS access keys, profiles, web identity,
container credentials, and the default AWS credential chain.

Local sign-in honors Codex's configured credential backend, including a system
keyring required by a managed device. Codex Security keeps login and scan
credentials in the same private, persistent state directory.

If both a ChatGPT sign-in and an API key are available, interactive scans ask
which credential to use. CI and other noninteractive scans keep the existing
API-key precedence. Select a credential explicitly when needed:

```bash
npx @openai/codex-security scan . --auth chatgpt
npx @openai/codex-security scan . --auth api-key
```

To make your ChatGPT sign-in the automatic default, unset any configured API
keys:

```bash
unset OPENAI_API_KEY CODEX_API_KEY
```

Scan history is stored in the Codex Security workbench state directory. If that
directory cannot be written, set `CODEX_SECURITY_STATE_DIR` to a writable
directory outside the repository.

`findings list [repository]` shows open findings across a repository's scans
and identifies findings not confirmed in its latest scan.

Use `patch OCCURRENCE_ID` to fix one saved finding, or
`patch --scan SCAN_ID --severity high` to fix selected findings from a s
