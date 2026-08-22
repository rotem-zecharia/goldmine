# arc53/DocsGPT

Private AI platform for agents, assistants and enterprise search. Built-in Agent Builder, Deep research, Document analysis, Multi-model support, and API connectivity for agents.

## limitations

- [x] Agent Workflow Builder with conditional nodes ( February 2026 )
- [x] Research mode ( March 2026 )
- [x] SharePoint & Confluence connectors ( March – April 2026 )
- [x] Postgres migration for user data ( April 2026 )
- [x] OpenTelemetry observability ( April 2026 )
- [x] Bring Your Own Model (BYOM) ( April 2026 )
- [x] Agent scheduling (RedBeat-backed) ( April 2026 )
- [x] Notifications & conversation search ( May 2026 )
- [x] Analytics & logs revamp with per-agent attribution ( June 2026 )
- [x] OIDC / SSO login with SCIM provisioning & groups ( June 2026 )
- [x] Admin dashboard & role-based access control (RBAC) ( June 2026 )
- [x] Agent import / export ( June 2026 )
- [x] Teams with team-scoped sharing & roles ( June 2026 )

You can find our full roadmap [here](https://github.com/orgs/arc53/projects/2). Please don't hesitate to contribute or create issues, it helps us improve DocsGPT!

## installation

> [!Note]
> Make sure you have [Docker](https://docs.docker.com/engine/install/) installed

A more detailed [Quickstart](https://docs.docsgpt.cloud/quickstart) is available in our documentation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/arc53/DocsGPT.git
   cd DocsGPT
   ```

**For macOS and Linux:**

2. **Run the setup script:**

   ```bash
   ./setup.sh
   ```

**For Windows:**

2. **Run the PowerShell setup script:**

   ```powershell
   PowerShell -ExecutionPolicy Bypass -File .\setup.ps1
   ```

Either script will guide you through setting up DocsGPT. Five options are available: using the public API, running locally, connecting to a local inference engine, using a cloud API provider, or building the docker image locally. The scripts will automatically configure your `.env` file and handle necessary downloads and installations based on your chosen option.

**Navigate to http://localhost:5173/**

To stop DocsGPT, open a terminal in the `DocsGPT` directory and run:

```bash
docker compose -f deployment/docker-compose.yaml down
```

(or use the specific `docker compose down` command shown after running the setup script).

> [!Note]
> For development environment setup instructions, please refer to the [Development Environment Guide](https://docs.docsgpt.cloud/Deploying/Development-Environment).
