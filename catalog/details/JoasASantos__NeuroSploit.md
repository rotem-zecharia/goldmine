# JoasASantos/NeuroSploit

NeuroSploit is an advanced, AI-powered penetration testing framework designed to automate and augment various aspects of offensive security operations.

## installation

**Linux / macOS** (x64 & arm64):
```bash
curl -fsSL https://raw.githubusercontent.com/JoasASantos/NeuroSploit/main/setup.sh | bash
```

**Windows** (PowerShell, x64 & arm64):
```powershell
irm https://raw.githubusercontent.com/JoasASantos/NeuroSploit/main/install.ps1 | iex
```

## tools

neurosploit run http://testphp.vulnweb.com/ --subscription --model anthropic:claude-opus-4-8 -v

## configuration

| Flag | Meaning |
|------|---------|
| `--model provider:model` | Repeatable. First = primary; the rest fail over **and** form the voting jury. |
| `--subscription` | Use the local CLI login (Claude/Codex/Gemini/Grok) instead of an API key. |
| `--mcp` | Enable Playwright MCP (auto-provisioned via `npx`; backends without MCP use built-in tools). |
| `--vote-n N` | How many models must agree a finding is real (default 3 / 2 for whitebox). |
| `--max-agents N` | Cap agents run (`0` = all matching the recon). |
| `--offline` | Exercise the full pipeline without calling any model. |
| `-v, --verbose` | Log each agent as it launches, recon, and votes. |
