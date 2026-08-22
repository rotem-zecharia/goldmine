# alibaba/open-code-review

Fast, efficient, battle-tested at Alibaba's scale. Hybrid architecture code review tool: deterministic pipelines + LLM Agent, precise line-level comments, built-in multi-language ruleset (NPE, thread-

## requirements

- **Git >= 2.41** — Open Code Review relies on Git for diff generation, code search, and repository operations.

## features

ocr review --from main --to feature-branch

## configuration

ocr delegate preview
ocr delegate rule src/main.go src/handler.go
```
