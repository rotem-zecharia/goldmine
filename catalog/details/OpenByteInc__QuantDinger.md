# OpenByteInc/QuantDinger

AI quantitative trading platform for crypto, stocks, and forex with backtesting, live trading, market data, and multi-agent research.vibe-trading ,trading-agents,ai-trader,ai-trading

## installation

### Option A: prebuilt images

Prerequisites: Docker with Compose v2. Node.js and a local Python environment are
not required.

Linux or macOS:

```bash
curl -fsSL https://raw.githubusercontent.com/OpenByteInc/QuantDinger/main/install.sh | bash
```

Windows PowerShell:

```powershell
irm https://raw.githubusercontent.com/OpenByteInc/QuantDinger/main/install.ps1 | iex
```

The installer asks for the initial administrator credentials, generates the
required secrets, downloads the GHCR Compose stack, and starts it.

Open:

- Web: <http://127.0.0.1:8888>
- Mobile H5: <http://127.0.0.1:8889>
- API health: <http://127.0.0.1:5000/api/health>

### Docker administrator and settings notes

Detailed guides: [English](docs/deployment/ADMIN_AND_SETTINGS_TROUBLESHOOTING_EN.md) |
[中文](docs/deployment/ADMIN_AND_SETTINGS_TROUBLESHOOTING_CN.md)

On a fresh database, the backend creates the initial administrator from
`ADMIN_USER`, `ADMIN_PASSWORD`, and optional `ADMIN_EMAIL`. Passwords are stored
as hashes, never as plaintext. An existing PostgreSQL volume is not overwritten:
the backend only replaces the untouched legacy `quantdinger` / `123456`
administrator when a non-default administrator is explicitly configured. It
never overwrites an account whose password was already changed, and it refuses
to promote an existing account that already uses the requested username.

Manual Docker deployments retain `quantdinger` / `123456` only for backward
compatibility when the administrator variables are left at their defaults. This
credential is not suitable for an internet-facing deployment; change it before
first start or immediately after the first login. The one-command installer does
not accept `123456` as the chosen password.

The Settings UI writes runtime configuration to `/app/.env`. In the GHCR stack
this is the host `backend.env`; in a source deployment it is
`backend_api_python/.env`. Current backend images automatically give runtime UID
`10001` ownership and keep mode `600`. Do not use `chmod 755` or recursive `777`:
these files contain passwords and API keys, and `755` still does not grant write
access to UID `10001` when root owns the file.

Verify write access with:

```bash
docker compose exec -u 10001:10001 -T backend \
  sh -c 'test -w /app/.env && echo writable=yes || echo writable=no'
```

The hardened production override intentionally mounts `/app/.env` read-only.
When using `docker-compose.production.yml`, manage configuration on the host and
recreate the services instead of saving it from the Settings UI. See the
[English guide](docs/deployment/ADMIN_AND_SETTINGS_TROUBLESHOOTING_EN.md) or
[中文指南](docs/deployment/ADMIN_AND_SETTINGS_TROUBLESHOOTING_CN.md) for
legacy-image recovery and rootless/NFS notes.

### Option B: source checkout

```bash
git clone https://github.com/OpenByteInc/QuantDinger.git
cd QuantDinger
cp backend_api_python/env.example backend_api_python/.env
cp .env.example .env
```

Before the first start, replace the example values in both environment files:

| File | Required production values |
| --- | --- |
| `backend_api_python/.env` | `SECRET_KEY`, `CREDENTIAL_ENCRYPTION_KEY`, `ADMIN_USER`, `ADMIN_PASSWORD` |
| `.env` | `POSTGRES_PASSWORD`, `REDIS_PASSWORD`, `CELERY_REDIS_PASSWORD`, `GRAFANA_ADMIN_PASSWORD` |

Generate independent secrets with:

```bash
python -c "import secrets; print(secrets.token_hex(32))"
```

Start the core stack from local backend source:

```bash
docker compose up -d --build
docker compose ps
```

The base stack does not start Prometheus, Grafana, or Alertmanager. This keeps
the default open-source installation smaller.

For detailed installation paths, Windows notes, China mirror settings, and
PostgreSQL migration guidance, see
[Installation troubleshooting](docs/deployment/INSTALL_TROUBLESHOOTING.md) and the
[cloud deployment guide](docs/deployment/CLOUD_DEPLOYMENT_EN.md).

## Production deployment

Validate secrets before starting a production stack:

```bash
python backend_api_python/s
