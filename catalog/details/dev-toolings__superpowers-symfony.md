# dev-toolings/superpowers-symfony

Claude Code plugin for Symfony 7.4 LTS & 8.x — 44 skills, 7 AI subagents & 13 commands for API Platform v4, Doctrine ORM 3, TDD (Pest/PHPUnit), Messenger, security & DDD.

## features

- **Specialized Agents** - 7 subagents with skill preloading and project memory
- **TDD Workflows** - RED-GREEN-REFACTOR with Pest PHP or PHPUnit
- **Doctrine Mastery** - Relations, migrations, transactions, Foundry fixtures
- **API Platform** - Resources, filters, serialization, versioning, DTOs
- **Symfony Messenger** - Async processing, handlers, retry strategies
- **Security** - Voters, rate limiting, form validation
- **Architecture** - Hexagonal/Ports & Adapters, CQRS, DI patterns
- **Quality** - PHP-CS-Fixer, PHPStan integration
- **Docker Support** - Docker Compose, Symfony Docker (FrankenPHP), DDEV
- **Auto-detection** - Detects Symfony version, API Platform, Docker setup, and test framework at session start

## installation

/plugin install superpowers-symfony@superpowers-symfony
```

## tools

Once installed, skills and commands are available automatically. Claude can invoke them based on task context, or you can call them explicitly.

## configuration

| Skill | Description |
|-------|-------------|
| `using-symfony-superpowers` | Entry point and overview |
| `runner-selection` | Docker vs Host environment detection |
| `bootstrap-check` | Project verification and setup |
| `daily-workflow` | Daily development workflow |
| `effective-context` | Context management best practices |
