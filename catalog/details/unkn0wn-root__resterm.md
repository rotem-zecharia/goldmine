# unkn0wn-root/resterm

Terminal API client for HTTP, GraphQL and gRPC. Plain .http files you can diff and version, with workflows, mocks, profiling, tracing, OpenAPI import, SSH tunnels, Kubernetes port-forwards, WebSocket,

## features

- **HTTP, GraphQL, gRPC, WebSocket and SSE** out of the box.
- **Automation lives in the request files:** conditions (`@when`, `@if`/`@elif`/`@else`, `@for-each`), multi-step workflows (`@workflow` / `@step`), captures, variables and assertions (`@capture`, `@var`, `@assert`).
- **RestermScript**, a small expression language built for Resterm, with JavaScript hooks when you want them.
- **Vim-style controls** with contextual bottom bar hints, searchable offline help, `K` help under the cursor, `/` search and commands like `:w`, `:q`, `:help` and `:docs`.
- **Built-in auth and tunneling:** OAuth 2.0 (client credentials, password, auth code with PKCE), auth backed by your existing CLIs, SSH tunnels and Kubernetes port-forwards. No extra tools needed.
- **CLI runner:** `resterm run` for scripted runs and CI, with JSON and JUnit output.
- **Mock servers** declared next to the requests they mimic, with matching rules, sequences, call verification and hot reload.
- **Timeline tracing, profiling and compare runs** across environments.
- **Streaming transcripts** and an interactive console for WebSocket and SSE.
- **No AI integration**, ever.

## installation

1. Install Resterm (see [Installation](#installation) for scripts, Windows and manual installs).

   ```bash
   brew install resterm
   ```

2. Bootstrap a workspace.

   ```bash
   mkdir my-api && cd my-api
   resterm init
   ```

   `resterm init` gives you a small project that works without an internet connection. The generated `requests.http` includes local mock scenarios and a few requests that build on each other. They cover assertions, bearer auth, JSON matching, `json-rules`, and `@for-each`.

3. Start it and send your first request.

   ```bash
   resterm
   ```

   Press `Ctrl+Enter` in the editor to send the highlighted request.

No files yet? Just run `resterm`, type a URL and press `Ctrl+Enter`. A pasted curl command works too.

## tools

These examples show some of the directives you can use in `.http` files. Requests and workflows can be run in the TUI or with `resterm run`. Mock responses can be served in the TUI or with `resterm mock`.

## configuration

```http
