# googleapis/mcp-toolbox

MCP Toolbox for Databases is an open source MCP server for databases.

## features

- **Out-of-the-Box Database Access:** Prebuilt generic tools for instant data exploration (e.g., `list_tables`, `execute_sql`) directly from your IDE or CLI.
- **Custom Tools Framework:** Build production-ready tools with your own predefined logic, ensuring safety through Restricted Access, Structured Queries, and Semantic Search.
- **Simplified Development:** Integrate tools into your Agent Development Kit (ADK), LangChain, LlamaIndex, or custom agents in less than 10 lines of code.
- **Better Performance:** Handles connection pooling, integrated auth (IAM), and end-to-end observability (OpenTelemetry) out of the box.
- **Enhanced Security**: Integrated authentication for more secure access to your data.
- **End-to-end Observability**: Out of the box metrics and tracing with built-in support for OpenTelemetry.

---

## installation

Stop context-switching and let your AI assistant become a true co-developer. By connecting your IDE to your databases with MCP Toolbox, you can query your data in plain English, automate schema discovery and management, and generate database-aware code.

You can use the Toolbox in any MCP-compatible IDE or client (e.g., Gemini CLI, Google Antigravity, Claude Code, Codex, etc.) by configuring the MCP server.

**Prebuilt tools are also conveniently available via the [Google Antigravity MCP Store](https://antigravity.google/docs/mcp) with a simple click-to-install experience.**

1. Add the following to your client's MCP configuration file (usually `mcp.json` or `claude_desktop_config.json`):

    ```json
    {
      "mcpServers": {
        "toolbox-postgres": {
          "command": "npx",
          "args": [
            "-y",
            "@toolbox-sdk/server",
            "--prebuilt=postgres",
            "--stdio"
          ]
        }
      }
    }
    ```

2. Set the appropriate environment variables to connect, see the [Prebuilt Tools Reference](https://mcp-toolbox.dev/documentation/configuration/prebuilt-configs/).

When you run Toolbox with a `--prebuilt=<database>` flag, you instantly get access to standard tools to interact with that database. You can also specify a specific toolset using the `--prebuilt=<database>/<toolset>` syntax (e.g., `--prebuilt=postgres/data` to only load SQL tools). 

Supported databases currently include:
- **Google Cloud:** AlloyDB, BigQuery, Cloud SQL (PostgreSQL, MySQL, SQL Server), Spanner, Firestore, Knowledge Catalog (formerly known as Dataplex).
- **Other Databases:** PostgreSQL, MySQL, [MariaDB](https://mcp-toolbox.dev/integrations/mariadb/source/), SQL Server, Oracle, MongoDB, Redis, Elasticsearch, CockroachDB, ClickHouse, Couchbase, Neo4j, Snowflake, Trino, and more.

For a full list of available tools and their capabilities across all supported databases, see the [Prebuilt Tools Reference](https://mcp-toolbox.dev/documentation/configuration/prebuilt-configs/).

*See the [Install & Run the Toolbox server](#install--run-the-toolbox-server) section for different execution methods like Docker or binaries.*


> [!TIP]
> For users looking for a managed solution, [Google Cloud MCP Servers](https://cloud.google.com/blog/products/databases/managed-mcp-servers-for-google-cloud-databases) 
> provide a managed MCP experience with prebuilt tools; you can [learn more about the differences here](https://mcp-toolbox.dev/dev/reference/faq/).

---

## tools

The `tools` section of a `tools.yaml` define the actions an agent can take: what
type of tool it is, which source(s) it affects, what parameters it uses, etc.

```yaml
kind: tool
name: search-hotels-by-name
type: postgres-sql
source: my-pg-source
description: Search for hotels based on name.
parameters:
  - name: name
    type: string
    description: The name of the hotel.
statement: SELECT * FROM hotels WHERE name ILIKE '%' || $1 || '%';
```

For more details on configuring different types of tools, see the
[Tools](https://mcp-toolbox.dev/documentation/configuration/tools/).
