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
