# prowler-cloud/prowler

Prowler is the world’s most widely used open-source cloud security platform that automates security and compliance across any cloud environment.

## installation

## Prowler Local Server

Prowler Local Server offers flexible installation methods tailored to various environments:

> For detailed instructions on using Prowler Local Server, refer to the [usage guide](https://docs.prowler.com/user-guide/tutorials/prowler-app).

### Docker Compose

#### Requirements

- `Docker Compose` installed: https://docs.docker.com/compose/install/.

#### Commands

_macOS/Linux:_

``` console
VERSION=$(curl -s https://api.github.com/repos/prowler-cloud/prowler/releases/latest | jq -r .tag_name)
curl -sLO "https://raw.githubusercontent.com/prowler-cloud/prowler/refs/tags/${VERSION}/docker-compose.yml"

## configuration

curl -sLO "https://raw.githubusercontent.com/prowler-cloud/prowler/refs/tags/${VERSION}/.env"
docker compose up -d
```

_Windows PowerShell:_

``` powershell
$VERSION = (Invoke-RestMethod -Uri "https://api.github.com/repos/prowler-cloud/prowler/releases/latest").tag_name
Invoke-WebRequest -Uri "https://raw.githubusercontent.com/prowler-cloud/prowler/refs/tags/$VERSION/docker-compose.yml" -OutFile "docker-compose.yml"
# Environment variables can be customized in the .env file. Using default values in production environments is not recommended.
Invoke-WebRequest -Uri "https://raw.githubusercontent.com/prowler-cloud/prowler/refs/tags/$VERSION/.env" -OutFile ".env"
docker compose up -d
```

> [!WARNING]
> 🔒 For a secure setup, the API auto-generates a unique key pair, `DJANGO_TOKEN_SIGNING_KEY` and `DJANGO_TOKEN_VERIFYING_KEY`, and stores it in `~/.config/prowler-api` (non-container) or the bound Docker volume in `_data/api` (container). Never commit or reuse static/default keys. To rotate keys, delete the stored key files and restart the API.

Once configured, access Prowler Local Server at http://localhost:3000. Sign up using your email and password to get started.
