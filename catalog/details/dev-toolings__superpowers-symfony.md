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

### From the marketplace (recommended)

```bash
# Add the marketplace
/plugin marketplace add dev-toolings/superpowers-symfony

# Install the plugin
/plugin install superpowers-symfony@superpowers-symfony
```

### For your team (project-scoped)

Add to your project's `.claude/settings.json`:

```json
{
  "extraKnownMarketplaces": {
    "superpowers-symfony": {
      "source": {
        "source": "github",
        "repo": "dev-toolings/superpowers-symfony"
      }
    }
  },
  "enabledPlugins": {
    "superpowers-symfony@superpowers-symfony": true
  }
}
```

## tools

Once installed, skills and commands are available automatically. Claude can invoke them based on task context, or you can call them explicitly.

### Skills (invoke with `/skill-name`)

```
/symfony:tdd-with-pest
/symfony:doctrine-relations
/symfony:api-platform-dto-resources
```

### Slash commands

```
/brainstorm
/write-plan
/execute-plan
/symfony-check
```

## Available Skills

## configuration

| Skill | Description |
|-------|-------------|
| `using-symfony-superpowers` | Entry point and overview |
| `runner-selection` | Docker vs Host environment detection |
| `bootstrap-check` | Project verification and setup |
| `daily-workflow` | Daily development workflow |
| `effective-context` | Context management best practices |

### Testing

| Skill | Description |
|-------|-------------|
| `tdd-with-pest` | TDD workflow with Pest PHP |
| `tdd-with-phpunit` | TDD workflow with PHPUnit |
| `functional-tests` | WebTestCase for HTTP testing |
| `api-platform-tests` | API Platform test utilities |
| `test-doubles-mocking` | Mocks, stubs, and fakes |
| `e2e-panther-playwright` | End-to-end browser testing |

### Doctrine ORM

| Skill | Description |
|-------|-------------|
| `doctrine-relations` | Entity relationships (1:1, 1:N, N:N) |
| `doctrine-migrations` | Schema versioning |
| `doctrine-fixtures-foundry` | Test data factories with Foundry |
| `doctrine-transactions` | Transaction handling |
| `doctrine-batch-processing` | Bulk operations |
| `doctrine-fetch-modes` | Performance optimization |
