# langchain-ai/open-swe

An Open-Source Asynchronous Coding Agent

## configuration

Every task runs in its own **isolated cloud sandbox** — a remote Linux environment with full shell access. The repo is cloned in, the agent gets full permissions, and the blast radius of any mistake is fully contained. No production access, no confirmation prompts.

Open SWE supports multiple sandbox providers out of the box — [Modal](https://modal.com/), [Daytona](https://www.daytona.io/), [Runloop](https://www.runloop.ai/), [E2B](https://e2b.dev/), and [LangSmith](https://smith.langchain.com/) — and you can plug in your own. See the [Customization Guide](docs/CUSTOMIZATION.md#1-sandbox) for details.

This follows the principle all three companies converge on: **isolate first, then give full permissions inside the boundary.**

- Each thread gets a persistent sandbox (reused across follow-up messages)
- Sandboxes auto-recreate if they become unreachable
- Multiple tasks run in parallel — each in its own sandbox, no queuing

## tools

Stripe's key insight: *tool curation matters more than tool quantity.* Open SWE follows this principle with a small, focused toolset:

| Tool | Purpose |
|---|---|
| `execute` | Shell commands in the sandbox |
| `fetch_url` | Fetch web pages as markdown |
| `http_request` | API calls (GET, POST, etc.) |
| `list_threads` / `get_thread` | Discover and inspect readable Open SWE threads |
| `manage_thread` | Perform authorization-checked dashboard thread actions |
| `linear_comment` | Post updates to Linear tickets |
| `linear_search_issues` | Search Linear issues by free text |
| `output_iframe` | Render sandboxed HTML visualizations in the dashboard |
| `slack_add_reaction` | React to Slack messages |
| `slack_thread_reply` | Reply in Slack threads |

GitHub operations are performed with `gh` inside the sandbox, backed by the LangSmith proxy. Plus the built-in Deep Agents tools: `read_file`, `write_file`, `edit_file`, `delete`, `ls`, `glob`, `grep`, `execute`, and `task` (subagent spawning). Thread discovery and management tools run only on the parent agent, derive the actor from trusted run configuration plus application-generated follow-up attribution, recheck allowed-organization membership, and preserve the dashboard's owner, participant, and admin authorization checks.

**Optional observability tools (server-side):** Admins can connect Datadog and LangSmith from team settings (Admin → Observability credentials). When connected, the agent gains Datadog tools (via Datadog's hosted MCP server, default `toolsets=core`) and read-only LangSmith tools (`langsmith_get_trace`, `langsmith_list_runs`). These run in the LangGraph server process using credentials encrypted at rest — the sandbox never holds Datadog or LangSmith keys. They are loaded **only for runs triggered by an authorized user** (admins plus any emails in `OBSERVABILITY_AUTHORIZED_EMAILS`; active members of `ALLOWED_GITHUB_ORGS` also receive LangSmith tools), so a prompt-injected run from an untrusted contributor cannot reach team observability data. Use scoped, read-oriented keys regardless: observability data (logs, traces) is attacker-influenced content that can carry prompt injection, and the agent has network egress — the same residual-risk class as `web_search` / `fetch_url`.

**Optional Corridor guardrails (server-side MCP):** Set `CORRIDOR_API_TOKEN` (or `CORRIDOR_MCP_TOKEN` / `CORRIDOR_TOKEN`) to load Corridor's hosted MCP server for each agent run. Open SWE exposes only Corridor's `analyzePlan` tool. `CORRIDOR_MCP_URL` defaults to `https://app.corridor.dev/api/mcp`; if set explicitly, Open SWE only accepts the same HTTPS host and `/api/mcp` path. Tokens are sent via `Authorization: Bearer ...` from the LangGraph server process and are never placed in the sandbox. A legacy `?token=...` URL is accepted and normalized into the header form.

### 4. Context Engineering — AGENTS.md + Source Context

Open SWE gathers context from two sources:

- **`AGENTS.md`** — If the repo contains an `AGENTS.md` file at the root, it's read from the sandbox and injected into the system prompt. This is your repo-level equivalent of Stripe's rule files: encoding conventions, testing requirements, and architectural decisions that every agent run should follow.
- **Source context** — The full Linear issue (title, description, comments) or Slack thread history is assembled and passed to the agent, so it starts with rich context rather than discovering everything through tool calls.

### 5. Orchestration — Subagents + Middleware

Open SWE's orchestration has two layers:

**Subagents:** The Deep Agents framework natively supports spawning child agents via the `task` tool. The main agent can fan out independent subtasks to isolated subagents — each with its own middleware stack and file operations. This is similar to Ramp's child sessions for parallel work.

**Middleware:** Deterministic middleware hooks run around the agent loop:

- **`check_message_queue_before_model`** — Injects follo

## features

- **Trigger from Linear, Slack, or GitHub** — mention `@openswe` in a comment to kick off a task
- **Instant acknowledgement** — reacts with 👀 the moment it picks up your message
- **Message it while it's running** — send follow-up messages mid-task and it'll pick them up before its next step
- **Run multiple tasks in parallel** — each task runs in its own isolated cloud sandbox
- **GitHub OAuth built-in** — authenticates with your GitHub account automatically
- **Opens PRs automatically** — commits changes and opens a draft PR when done, linked back to your ticket
- **Subagent support** — the agent can spawn child agents for parallel subtasks
- **Web dashboard** — a companion app (in `ui/`) for GitHub login, per-user model/profile settings, team defaults, enabled-repo and review-style management, user mappings, and an Agents chat UI
- **Desktop app (experimental)** — an Electron wrapper (in `desktop/`) around the same dashboard; the web UI remains the recommended way to use Open SWE

---

## installation

- **[Installation Guide](docs/INSTALLATION.md)** — local dev (backend + dashboard), GitHub App creation, LangSmith, Linear/Slack/GitHub triggers, and production deployment
- **macOS Desktop beta** — clone this repository and run `make install-desktop` from the root to install or update the app
- **[Customization Guide](docs/CUSTOMIZATION.md)** — swap the sandbox, model, tools, triggers, system prompt, and middleware for your org

## License

MIT
