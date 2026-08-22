# arabcoders/ytptube

A self-hosted media download manager, automation interface, and media-library preparation layer for yt-dlp

## installation

Create `compose.yaml`:

```yaml
services:
  ytptube:
    image: ghcr.io/arabcoders/ytptube:latest
    container_name: ytptube
    restart: unless-stopped
    user: "${UID:-1000}:${UID:-1000}"
    environment:
      - YTP_TEMP_PATH=/downloads/tmp
      - YTP_DOWNLOAD_PATH=/downloads/files
    ports:
      - "8081:8081"
    volumes:
      - ./config:/config:rw
      - ./downloads:/downloads:rw
```

Create the directories and start the container:

```bash
mkdir -p ./{config,downloads/{files,tmp}}
docker compose up -d
```

Open `http://localhost:8081` and create the first local account.

The container runs as your user and group IDs so downloaded files remain accessible to the host account. Podman users 
can replace the `user` line with `userns_mode: keep-id` and run `podman-compose up -d`.

<details>
<summary>Docker command without Compose</summary>

```bash
mkdir -p ./{config,downloads/{files,tmp}} && docker run -itd --rm \
  --user "${UID}:${UID}" \
  --name ytptube \
  -e YTP_TEMP_PATH=/downloads/tmp \
  -e YTP_DOWNLOAD_PATH=/downloads/files \
  -p 8081:8081 \
  -v ./config:/config:rw \
  -v ./downloads:/downloads:rw \
  ghcr.io/arabcoders/ytptube:latest
```

</details>

<details>
<summary>Podman command without Compose</summary>

```bash
mkdir -p ./{config,downloads/{files,tmp}} && podman run -itd --rm \
  --userns=keep-id \
  --name ytptube \
  -e YTP_TEMP_PATH=/downloads/tmp \
  -e YTP_DOWNLOAD_PATH=/downloads/files \
  -p 8081:8081 \
  -v ./config:/config:rw \
  -v ./downloads:/downloads:rw \
  ghcr.io/arabcoders/ytptube:latest
```

</details>

## Other Installations

### Unraid

Install the **Community Applications** plugin, search for **ytptube**, and use the preconfigured template.

### Native Builds

ZIP archives for Windows, Linux, and macOS are published on the [GitHub Releases](https://github.com/arabcoders/ytptube/releases) page. Archive names follow this pattern:

```text
ytptube-{OS}-{arch}-{tag}.zip
```

Extract the archive and run `YTPTube`, or `YTPTube.exe` on Windows. Native builds disable application authentication 
by default. Set `YTP_DISABLE_AUTH=false` to require a local account.

Native builds do not support automatic yt-dlp or custom-package updates. The built-in player also requires 
`ffmpeg` on `PATH`. Some extractors require [Deno](https://deno.land/#installation). 
See [Manually update yt-dlp in a native executable](FAQ.md#manually-update-yt-dlp-in-native-executable).

## Security

> [!IMPORTANT]
> Do not expose YTPTube to an untrusted network without authentication. Authenticated users are instance administrators 
> and can pass yt-dlp options, including options that execute commands.

Server installations require local account setup. Only disable authentication when a trusted reverse proxy controls 
access or the instance is restricted to a private network. Read the [security recommendations](FAQ.md#security-recommendations)
before exposing an instance and use [security advisories](https://github.com/arabcoders/ytptube/security/advisories/new) 
to report vulnerabilities.

## Documentation

- [Features](FEATURES.md)
- [Configuration, usage, and troubleshooting](FAQ.md)
- [HTTP API](API.md)
- [Security policy](SECURITY.md)
- [Contribution process](CONTRIBUTING.md)

## Project Policy

YTPTube is a personal-first project. Contributions are welcome after prior discussion, but the maintainer may decline 
changes that do not fit the project's direction. Unsolicited pull requests may be closed. Read [CONTRIBUTING.md](CONTRIBUTING.md) 
before starting work. 

AI-assisted tools have been used in this project and will continue to be used where I find them useful. This project is
built for my own needs and use cases, and I maintain it according to my own preferences.

You are welcome to use it if it works for you, but I will not change the project's development approach to accommodate 
objections to the use of AI tools. I believe these tools can be genuinely useful when used appropriately. If the use of 
AI-
