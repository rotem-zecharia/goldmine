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

### Run a request for each value

```http
### Create users
# @for-each ["david", "tom"] as name
# @assert response.statusCode == 201
POST {{base.url}}/users
Content-Type: application/json

{"name":"{{= name }}"}
```

### Run a request conditionally

```http
### Seed development
# @when env.mode == "development"
POST {{base.url}}/fixtures/seed
```

### Choose a workflow branch

```http
### Sign in
# @workflow sign-in
# @step Login using=Login
# @if last.statusCode == 200 run=GetProfile
# @elif last.statusCode == 401 run=RefreshToken
# @else fail="unexpected login response"
```

## configuration

```http
### Health check
# @compare dev stage prod base=stage
# @trace ttfb<=300ms total<=500ms
# @assert trace.withinBudget()
GET {{base.url}}/health
```

### Define a mock response

```http
### Declined payment
# @mock method=POST path=/payments
# @match json-rules={"amount":{"lte":0}}
HTTP/1.1 422 Unprocessable Entity
Content-Type: application/json

{"error":"amount must be positive"}
```

`@when` applies to an individual request. `@if`, `@elif` and `@else` choose which request to run inside a workflow. See the [RestermScript reference](docs/restermscript.md) for the expression language and the [full documentation](docs/resterm.md) for workflows, comparisons, tracing and mocks.

## CLI

`resterm run` executes `.http` / `.rest` files without opening the TUI, which is what CI runs.

```bash
resterm run --request CreateUser requests.http
```

The generated project talks to a local mock server. Start it in another terminal first:

```bash
resterm mock requests.http
```

In the TUI, press `g Shift+M` instead to start the same mock server from the workspace.

The [CLI documentation](docs/cli.md) covers selectors, output formats and more examples.

## Mock Servers

The same files that hold your requests can serve HTTP mocks.

- Match incoming requests by query, headers or JSON body, then pick a named or default response.
- Model polling and retry flows with response sequences, including independent cursors per resource or caller.
- Delay responses by a fixed amount, or give every request a different delay with `random`, `normal`, or `jitter`.
- Build responses from path, query, header and body values, with generators for dynamic data.
- Verify call counts with `@expect` or inspect received traffic from RestermScript.
- Hot reload source files and fixtures, with optional TLS.

Two scenarios on one route:

```http
### Payment accepted
# @mock method=POST path=/payments name=accepted default=true latency=150ms
HTTP/1.1 202 Accepted
Content-Type: application/json

{"id":"pay_123","status":"pending"}

### Payment declined
# @mock method=POST path=/payments name=declined
# @match query={"mode":"decline"} headers={"X-Tenant":"demo"} json={"amount":0}
HTTP/1.1 422 Unprocessable Entity
Content-Type: application/json

{"error":"amount must be positive"}
```

Serve one file or a whole directory:

```bash
resterm mock ./requests.http
resterm mock --recursive --addr 127.0.0.1:9090 ./requests
```

More in the [Mock Servers reference](docs/resterm.md#mock-servers), the [`resterm mock` CLI guide](docs/cli.md#resterm-mock) and the [working example](_examples/mocks.http).

## Headless

The [`headless`](./headless) package is the public Go API for the same engine that powers the TUI and CLI. Use it to run requests, workflows, assertions, compare runs and profiles from your own Go code or CI.

If you would rather not build a runner yourself, there is [resterm-runner](https://github.com/unkn0wn-root/resterm-runner).

## Keyboard cheat sheet

- Pane focus and layout
  - `Tab` / `Shift+Tab`: move between sidebar, editor and response.
  - `g+r`, `g+i`, `g+p`: jump to requests, editor or response.
  - `g+h` / `g+l`: resize horizontally. Changes sidebar width when the sidebar is focused, the editor/response split otherwise.
  - `g+j` / `g+k`: resize editor/response height when stacked, collapse or expand branches in the navigator.
  - `g+v` / `g+s`: toggle the response pane between inline and stacked layout.
  - `g+1`, `g+2`, `g+3`: minimize or restore sidebar, editor, response.
  - `g+z` / `g+Z`: zoom the focused pane, clear zoom.
- Environments and globals
  - `Ctrl+E`: switch environments.
  - `Ctrl+G`: inspect captured globals.
- Help and commands
  - `?`: open the searchable offline help index.
  - `K` (editor normal mode): open help for the directive, template or keyword under the cursor.
  - `:help <topic>` / `:man <topic>`: open an embedded topic; `:docs <topic>` opens the version-matched full manual.
  - `Ctrl+O`: open the file/workspace popup. Ty
