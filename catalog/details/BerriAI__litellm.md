# BerriAI/litellm

The fastest, litest AI Gateway. Rust core with Python SDK. Call 100+ LLM APIs in OpenAI (or native) format with cost tracking, guardrails, load balancing, and logging [Bedrock, Azure, OpenAI, Anthropi

## features

Managing LLM calls across providers gets complicated fast — different SDKs, auth patterns, request formats, and error types for every model. LiteLLM removes that friction:

- **Unified API** — one interface for 100+ LLMs, no provider-specific SDK juggling
- **Drop-in OpenAI compatibility** — swap providers without rewriting your code
- **Production-ready gateway** — virtual keys, spend tracking, guardrails, load balancing, and an admin dashboard out of the box
- **8ms P95 latency** at 1k RPS ([benchmarks](https://docs.litellm.ai/docs/benchmarks))

## installation

This requires uv to be installed.

```bash
git clone https://github.com/BerriAI/litellm.git
cd litellm
make install-dev    # Install development dependencies
make format         # Format your code
make lint           # Run all linting checks
make test-unit      # Run unit tests
make format-check   # Check formatting only
```

For detailed contributing guidelines, see [CONTRIBUTING.md](CONTRIBUTING.md).

> **📖 Contributing to documentation?** The LiteLLM docs have moved to a separate repository: [BerriAI/litellm-docs](https://github.com/BerriAI/litellm-docs). Please open doc PRs there. Docs are served at [docs.litellm.ai](https://docs.litellm.ai).
