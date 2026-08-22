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

### Production Support / Help for Companies:

We're eager to provide personalized assistance when deploying your DocsGPT to a live environment.

[Get a Demo :wave:](https://www.docsgpt.cloud/contact)⁠

[Send Email :email:](mailto:support@docsgpt.cloud?subject=DocsGPT%20support%2Fsolutions)

## Join the Lighthouse Program 🌟

Calling all developers and GenAI innovators! The **DocsGPT Lighthouse Program** connects technical leaders actively deploying or extending DocsGPT in real-world scenarios. Collaborate directly with our team to shape the roadmap, access priority support, and build enterprise-ready solutions with exclusive community insights.

[Learn More & Apply →](https://docs.google.com/forms/d/1KAADiJinUJ8EMQyfTXUIGyFbqINNClNR3jBNWq7DgTE)

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

## Contributing

Please refer to the [CONTRIBUTING.md](CONTRIBUTING.md) file for information about how to get involved. We welcome issues, questions, and pull requests.

## Architecture

![Architecture chart](https://github.com/user-attachments/assets/fc6a7841-ddfc-45e6-b5a0-d05fe648cbe2)

## Project Structure

- **Application** - Backend Flask application.

- **Extensions** - Integrations and widgets (e.g., Chatwoot, React widget).

- **Frontend** - Web UI built with [Vite](https://vitejs.dev/) and [React](https://react.dev/).

- **Scripts** - Miscellaneous utility scripts.

## Code Of Conduct

We as members, contributors, and leaders, pledge to make participation in our community a harassment-free experience for everyone, regardless of age, body size, visible or invisible disability, ethnicity, sex characteristics, gender identity and expression, level of experience, education, socio-economic status, nationality, personal appearance, race, religion, or sexual identity and orientation. Please refer to the [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) file for more information about contributing.

## Many Thanks To Our Contributors⚡

<a href="https://github.com/arc53/DocsGPT/graphs/contributors" alt="View Contributors">
  <img src="https://contrib.rocks/image?repo=arc53/DocsGPT" alt="Contributors" />
</a>

## License

The source code license is [MIT](https://opensource.org/license/mit/), as described in the [LICENSE](LICENSE) file.

## This project is supported by:

<p>
  <a href="https://www.digitalocean.com/?utm_medium=opensource&utm_source=DocsGPT">
    <img src="https://opensource.nyc3.cdn.digitaloceanspaces.com/attribution/assets/SVG/DO_Logo_horizontal_blue.svg" width="201px">
  </a>
</p>
<p>
  <a href="https://get.neon.com/docsgpt">
    <img width="201" alt="color" src="https://github.com/user-attachments/assets/7d9813b7-0e6d-403f-b5af-68af066b326f" />
  </a>
  
</p>
