# samber/cc-skills-golang

🧑‍🎨 A collection of Golang agentic skills that works

## installation

#### `golang-cli`

Go CLI application development. Project layout, exit codes, signal handling, I/O patterns, argument parsing, and terminal UX.

#### `golang-continuous-integration`

CI/CD pipeline configuration for Go projects using GitHub Actions. Build, test, lint, and release workflows.

#### `golang-dependency-management`

Go module dependency strategies. go.mod conventions, versioning, replace directives, tool dependencies, and multi-module workspaces.

#### `golang-gopls`

Semantic code intelligence for your local build via `gopls`, the official Go language server. Go-to-definition, find references, call/implementation hierarchy, workspace symbol search, diagnostics, safe rename, and refactors (extract/inline/fill/rewrite). Reachable via gopls's own MCP server, Claude Code's native `LSP` tool, or the `gopls` CLI.

#### `golang-pkg-go-dev`

Go package and module exploration via `godig`, a pkg.go.dev API client (CLI + MCP server). Package docs, API references, symbols, code examples, versions, importers, licenses, and known vulnerabilities. Prefer over Context7 for Go packages.

#### `golang-popular-libraries`

Curated recommendations for production-ready Go libraries and frameworks. When the stdlib is enough vs when to reach for a package.

#### `golang-project-layout`

Go project structure and workspace setup. cmd/internal/pkg conventions, monorepo layout, CLI project structure, and when to keep things flat.

#### `golang-stay-updated`

Resources to stay current with Go. Official channels, community hubs, key people to follow, and learning resources.

## tools

#### `golang-graphql`

GraphQL API development in Go using gqlgen/graphql-go. Schema definition, resolvers, subscriptions, dataloader, and federation.

#### `golang-grpc`

gRPC in Go. Protobuf organization, service definitions, streaming, interceptors, error codes, and code generation workflow.

#### `golang-swagger`

OpenAPI/Swagger docs with swaggo/swag. Annotation comments, code generation, framework integrations (gin, echo, fiber, chi), security definitions.

### Dependency Injection

#### `golang-google-wire`

Compile-time dependency injection with google/wire. Provider sets, injector generation, wire.Build, and structured DI patterns.

#### `golang-uber-dig`

Reflection-based DI with uber-go/dig. Provide/Invoke, dig.In/dig.Out, named values, value groups, optional dependencies, and Decorate.

#### `golang-uber-fx`

Application framework with uber-go/fx. fx.New, fx.Provide/Invoke, fx.Module, lifecycle hooks, fx.Annotate, fx.Decorate, signal-aware Run.

### Frameworks

#### `golang-spf13-cobra`

CLI command trees with spf13/cobra. Command hierarchy, RunE hooks, flag management, shell completion, usage templates, and testing with SetArgs.

#### `golang-spf13-viper`

Layered configuration with spf13/viper. Flag > env > file > KV > default precedence, BindPFlag, hot reload, test isolation, and remote KV integration.

### samber/\*

#### `golang-samber-do`

Dependency injection with samber/do. Type-safe service containers, lifecycle management, scopes, health checks, and graceful shutdown.

#### `golang-samber-hot`

In-memory caching with samber/hot. 9 eviction algorithms (LRU, LFU, TinyLFU, W-TinyLFU, S3FIFO, ARC, SIEVE...), TTL, loaders, sharding, stale-while-revalidate, Prometheus metrics.

#### `golang-samber-lo`

Functional programming helpers with samber/lo. 500+ type-safe generic functions for slices, maps, channels, strings. Immutable (lo), parallel (lop), mutable (lom), iterators (loi), SIMD.

#### `golang-samber-mo`

Monadic types with samber/mo. Option, Result, Either, Future, IO, Task, State for type-safe nullable values, error handling, and functional composition.

#### `golang-samber-oops`

Structured error handling with samber/oops. Error builders, stack traces, error codes, context attributes, public vs developer messages, panic recovery, and APM integration.

#### `golang-samber-ro`

Reactive streams with samber/ro. 150+ type-safe operators, cold/hot observables, 5 subject types, 40+ plugins, automatic backpressure, and Go context integration.

#### `golang-samber-slog`

Structured logging pipeline with samber/slog-\*\*\*\* packages. Multi-handler routing (slog-multi), sampling, formatting, HTTP middleware, and 20+ backend sinks.

### Testing

#### `golang-stretchr-testify`

Testing with stretchr/testify. assert, require, mock, and suite packages. Assertions, mock expectations, argument matchers, suite lifecycle, and custom matchers.

## 🕵 Use in CI for AI-driven reviews

Add AI agents as PR reviewers alongside traditional static analysis. When configured with this skill plugin, the agent applies the relevant Go skills per review area — catching architectural drift, logic bugs, and concurrency hazards that linters cannot detect.

See [GOLANG-AI-DRIVEN-REVIEW.md](./GOLANG-AI-DRIVEN-REVIEW.md) for full setup instructions (Claude Code Action and GitHub Copilot).

## 🎯 Tuning Skill Triggers

If a skill triggers too often or not often enough, please [open an issue](https://github.com/samber/cc-skills-golang/issues) suggesting a description change. The `description` field in SKILL.md frontmatter is the primary triggering mechanism — small wording adjustments can significantly improve trigger accuracy. Some `SKILL.md` files might have a `When to use` section which is another level of exclusion. Finally, `SKILL.md` files are an entrypoint for lazy loading references with deep knowledge located in `references/`.

## 🔄 Overlap

Claude reports very little overlap between skills in this repo, thanks to cross-reference. I 
