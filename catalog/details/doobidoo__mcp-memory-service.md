# doobidoo/mcp-memory-service

Open-source persistent memory for AI agent pipelines (LangGraph, CrewAI, AutoGen) and Claude. REST API + knowledge graph + autonomous consolidation.

## installation

cloudflared tunnel --url http://localhost:8765
# → Outputs: https://random-name.trycloudflare.com

# 3. In claude.ai: Settings → Connectors → Add Connector
# Paste the URL: https://random-name.trycloudflare.com/mcp
# OAuth flow will handle authentication automatically
```

**Production Setup:** See [Remote MCP Setup Guide](docs/remote-mcp-setup.md) for Let's Encrypt, nginx, and firewall configuration.
**Step-by-Step Tutorial:** [Blog: 5-Minute claude.ai Setup](https://doobidoo.github.io/mcp-memory-service/blog/remote-mcp-tutorial.html) | [Wiki Guide](https://github.com/doobidoo/mcp-memory-service/wiki/Claude-AI-Remote-MCP-Integration)

---

## features

| Without mcp-memory-service | With mcp-memory-service |
|---|---|
| Each agent run starts from zero | Agents retrieve prior decisions in 5ms |
| Memory is local to one graph/run | Memory is shared across all agents and runs |
| You manage Redis + Pinecone + glue code | One self-hosted service, zero cloud cost |
| No causal relationships between facts | Knowledge graph with typed edges (causes, fixes, contradicts) |
| Context window limits create amnesia | Autonomous consolidation compresses old memories |

**Key capabilities for agent pipelines:**
- **Framework-agnostic REST API** — 76 endpoints, no MCP client library needed
- **Knowledge graph** — agents share causal chains, not just facts
- **`X-Agent-ID` header** — auto-tag memories by agent identity for scoped retrieval
- **`conversation_id`** — bypass deduplication for incremental conversation storage
- **SSE events** — real-time notifications when any agent stores or deletes a memory
- **Embeddings run locally via ONNX** — memory never leaves your infrastructure

## tools

```

```python
import httpx

BASE_URL = "http://localhost:8000"

# Store — auto-tag with X-Agent-ID header
async with httpx.AsyncClient() as client:
    await client.post(f"{BASE_URL}/api/memories", json={
        "content": "API rate limit is 100 req/min",
        "tags": ["api", "limits"],
    }, headers={"X-Agent-ID": "researcher"})
    # Stored with tags: ["api", "limits", "agent:researcher"]

# Search — scope to a specific agent
    results = await client.post(f"{BASE_URL}/api/memories/search", json={
        "query": "API rate limits",
        "tags": ["agent:researcher"],
    })
    print(results.json()["memories"])
```

**Framework-specific guides:** [docs/agents/](docs/agents/)

### Real-World: Multi-Agent Cluster with Shared Memory

> *"After I work with one of the cluster agents on something I want my local agent to know about, the cluster agent adds a special tag to the memory entry that my local agent recognizes as a message from a cluster agent. So they end up using it as a comms bridge — and it's pretty delightful."*
> — [@jeremykoerber](https://github.com/jeremykoerber), [issue #591](https://github.com/doobidoo/mcp-memory-service/issues/591)

A 5-agent openclaw cluster uses mcp-memory-service as shared state **and** as an inter-agent messaging bus — without any custom protocol. Cluster agents tag memories with a sentinel like `msg:cluster`, and the local agent filters on that tag to receive cross-cluster signals. The memory service becomes the coordination layer with zero additional infrastructure.

```python
# Cluster agent stores a learning and flags it for the local agent
await client.post(f"{BASE_URL}/api/memories", json={
    "content": "Rate limit on provider X is 50 RPM — switch to provider Y after 40",
    "tags": ["api", "limits", "msg:cluster"],       # sentinel tag
}, headers={"X-Agent-ID": "cluster-agent-3"})

# Local agent polls for cluster messages
results = await client.post(f"{BASE_URL}/api/memories/search", json={
    "query": "messages from cluster",
    "tags": ["msg:cluster"],
})
```

This pattern — **tags as inter-agent signals** — emerges naturally from the tagging system and requires no additional infrastructure.

### Real-World: Self-Hosted Docker Stack with Cloudflare Tunnel

> *"The quality of life that session-independent memory adds to AI workflows is immense. File-based memory demands constant discipline. Semantic recall from a live database doesn't. Storing data on my own hardware while making it remotely accessible across platforms turned out to be a feature I didn't know I needed."*
> — [@PL-Peter](https://github.com/PL-Peter), [discussion #602](https://github.com/doobidoo/mcp-memory-service/discussions/602)

A production-tested self-hosted deployment using Docker containers behind a Cloudflare tunnel, with [AuthMCP Gateway](https://github.com/loglux/authmcp-gateway) handling authentication:

| Layer | Role |
|-------|------|
| **Cloudflare Tunnel** | Name-based routing, subnet-based access control, authentication before hitting self-hosted resources |
| **AuthMCP Gateway** | Auth/aggregation with locally managed users, admin UI, per-user MCP server access control, bearer token auth |
| **mcp-memory-service** | Two Docker containers sharing one SQLite backend — one for MCP, one for the web UI (document ingestion) |

**Security best practices for this setup:**
- Use Cloudflare ZeroTrust with subnet-based access control (e.g., allow Anthropic subnets + your own IPs)
- Add **Client IP Address Filtering** to all Cloudflare API tokens (Dashboard → My Profile → API Tokens → Edit → Client IP Address Filtering) to limit abuse if a token leaks
- If using IPv6, include your IPv6 /64 network in the allowlist (Python prefers IPv6 by default)
- For long-running browser sessions, request the `offline_access` scope during authorization to receive a rotating `refresh_token` (lifetime via `MCP_OAUTH_REFRESH_TOKEN_EXPIRE_DAYS`, default 30 days). Without this scope, access tokens are the only crede
