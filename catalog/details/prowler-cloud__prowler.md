# prowler-cloud/prowler

Prowler is the world’s most widely used open-source cloud security platform that automates security and compliance across any cloud environment.

## configuration

curl -sLO "https://raw.githubusercontent.com/prowler-cloud/prowler/refs/tags/${VERSION}/.env"
docker compose up -d
```

_Windows PowerShell:_

``` powershell
$VERSION = (Invoke-RestMethod -Uri "https://api.github.com/repos/prowler-cloud/prowler/releases/latest").tag_name
Invoke-WebRequest -Uri "https://raw.githubusercontent.com/prowler-cloud/prowler/refs/tags/$VERSION/docker-compose.yml" -OutFile "docker-compose.yml"

## installation

> [!Note]
  If you want to use AWS role assumption (e.g., with the "Connect assuming IAM Role" option), you may need to mount your local `.aws` directory into the container as a volume (e.g., `- "${HOME}/.aws:/home/prowler/.aws:ro"`). There are several ways to configure credentials for Docker containers. See the [Troubleshooting](./docs/troubleshooting.mdx) section for more details and examples.

You can find more information in the [Troubleshooting](./docs/troubleshooting.mdx) section.
