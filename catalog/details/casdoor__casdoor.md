# casdoor/casdoor

An open-source Agent-first Identity and Access Management (IAM) /LLM MCP & agent gateway and auth server with web UI supporting OpenClaw, MCP, OAuth, OIDC, SAML, CAS, LDAP, SCIM, WebAuthn, TOTP, MFA, 

## features

Casdoor is a **complete identity provider**, not an authentication proxy and not a library you embed. It stores your users, issues the tokens, and gives you an admin console to manage all of it — so your applications can delegate login entirely and never handle a password themselves.

- **One server, many protocols.** The same user directory is reachable over OAuth 2.0, OIDC, SAML 2.0, CAS, LDAP and SCIM, so a modern SPA and a legacy CAS-only app can share one set of accounts.
- **Everything is editable in the UI.** Organizations, applications, providers, sign-in methods, email and SMS templates, and login-page branding are configured in the web console instead of in files you have to redeploy.
- **Policy-based authorization built in.** Access rules are expressed with [Casbin](https://casbin.org/) — ACL, RBAC, ABAC and custom models — rather than a fixed permission scheme.
- **Straightforward to self-host.** A single Go binary plus a database. No JVM, no operator, no cluster required.

If all you need is a login screen in front of an existing reverse proxy, a smaller tool may suit you better. Casdoor is for when you want to own the user directory itself.

## installation

Four supported paths, fastest first. All of them end up at <http://localhost:8000>.

### Docker — all-in-one (evaluation)

```bash
docker run -p 8000:8000 casbin/casdoor-all-in-one
```

Bundles SQLite and demo data into a single container. Ideal for a first look, but **not intended for production**: the data lives inside the container and disappears with it.

Guide: [Try with Docker](https://casdoor.ai/docs/basic/try-with-docker)

### Docker Compose — Casdoor with MySQL

[`docker-compose.yml`](docker-compose.yml) starts Casdoor next to a MySQL 8 container.

> **Two things to know before running it:**
>
> 1. Compose **builds the image from source** (Go backend plus React frontend). The first `docker compose up` takes several minutes, so it is not the quick-trial path — use the all-in-one image above for that.
> 2. You have to point Casdoor at the bundled database first.

Set the MySQL settings in [`conf/app.conf`](conf/app.conf) to match the `db` service:

```ini
driverName = mysql
dataSourceName = root:123456@tcp(localhost:3306)/
dbName = casdoor
```

Use `localhost` here even though MySQL runs in a separate container: the compose file sets `RUNNING_IN_DOCKER=true`, and Casdoor rewrites `localhost` to the Docker host address at startup (see [`conf/conf.go`](conf/conf.go)). Then start everything:

```bash
docker compose up
```

The compose entrypoint already passes `--createDatabase=true`, so the `casdoor` database is created for you.

Guide: [Try with Docker](https://casdoor.ai/docs/basic/try-with-docker)

### Kubernetes — Helm

Requires Helm v3 and a running cluster:

```bash
helm install casdoor oci://registry-1.docker.io/casbin/casdoor-helm-charts
```

The chart does not expose Casdoor outside the cluster by default. To reach it, find the service and forward a port:

```bash
kubectl get svc
```

```bash
kubectl port-forward svc/<service-name-from-above> 8000:8000
```

For a real deployment, configure an Ingress and an external database through the chart's values. [`k8s.yaml`](k8s.yaml) in this repo is a minimal plain-manifest example if you would rather not use Helm.

Guide: [Try with Helm](https://casdoor.ai/docs/basic/try-with-helm)

### From source — for development

Use this if you intend to modify Casdoor. Prerequisites: **Go 1.25+** (see [`go.mod`](go.mod)), **Node.js 20 LTS**, **Yarn 1.x**, and a supported database (MySQL, PostgreSQL, SQLite, SQL Server and others).

```bash
git clone https://github.com/casdoor/casdoor.git
cd casdoor
```

Set `driverName`, `dataSourceName` and `dbName` in [`conf/app.conf`](conf/app.conf). For MySQL, create the `casdoor` database first, or start the server with `--createDatabase=true`. Then build the frontend and run the server:

```bash
cd web && yarn install && yarn build && cd .. && go run main.go
```

While working on the frontend, run `yarn start` in [`web/`](web) instead of `yarn build` to get hot reload on port 7001, with `go run main.go` serving the API from a second terminal.

Guide: [Server installation](https://casdoor.ai/docs/basic/server-installation)

## 👉 After you sign in

At this point you have a running identity provider with nothing connected to it yet. Next:

1. **Change the `admin` password.** `123` is a demo credential and must not survive contact with production.
2. **[Connect your first application](https://casdoor.ai/docs/how-to-connect/overview)** — create an Application in the console, copy its Client ID and Client Secret, and point your app's OAuth/OIDC client at Casdoor.
3. **[Add an identity provider](https://casdoor.ai/docs/provider/overview)** if you want Google, GitHub or Entra ID sign-in.
4. **[Pick an SDK](https://casdoor.ai/docs/category/integrations)** for your language, or call the [Public API](https://casdoor.ai/docs/basic/public-api) directly.
