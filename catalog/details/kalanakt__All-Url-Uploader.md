# kalanakt/All-Url-Uploader

A simple telegram Bot, Upload Media File/ video To telegram using the direct download link. (youtube, Mediafire, google drive, mega drive, etc)

## tools

- `/start` - welcome message, shortcuts, and usage guidance
- `/help` - supported link formats and flow overview
- `/about` - runtime details, repo link, and project notes
- `/thumb` - show the currently saved custom thumbnail
- `/delthumb` - remove the saved custom thumbnail

## installation

1. Clone the repository and move into it:

```bash
git clone https://github.com/kalanakt/All-Url-Uploader.git
cd All-Url-Uploader
```

2. Create a `.env` file in the project root:

```dotenv
BOT_TOKEN=
OWNER_ID=
AUTH_USERS=
DOWNLOAD_LOCATION=./DOWNLOADS
CHUNK_SIZE=128
HTTP_PROXY=
PROCESS_MAX_TIMEOUT=3700
```

3. Install dependencies:

```bash
uv sync --group dev
```

4. Start the bot:

```bash
uv run python bot.py
```

## configuration

- `BOT_TOKEN` - required Telegram bot token
- `OWNER_ID` - required Telegram user ID for the bot owner
- `AUTH_USERS` - optional comma-separated list of user IDs that bypass the cooldown
- `DOWNLOAD_LOCATION` - optional base directory for temporary downloads and uploads
- `CHUNK_SIZE` - optional direct-download chunk size; values below `1024` are treated as kilobytes for backward compatibility
- `HTTP_PROXY` - optional proxy URL passed to network requests and `yt-dlp`
- `PROCESS_MAX_TIMEOUT` - optional process timeout in seconds for external tools

## Project Layout

- root runtime entrypoints: `bot.py`, `app.py`, `config.py`
- routers: `routers/`
- services: `services/`
- shared helpers and models: `utils/`
- tests: `tests/`
- external documentation site: `docs/`

## Docker

Build and run the container with your existing `.env` file:

```bash
docker build -t all-url-uploader .
docker run --env-file .env all-url-uploader
```

## Checks

Run the same core checks used in GitHub Actions:

```bash
uv run pytest
uv run pylint $(git ls-files '*.py')
cd docs && npm run build
```

## Deploy

| Deploy on Railway | Deploy on Koyeb | Deploy on Heroku |
|------------------|-----------------|------------------|
| [![Deploy on Railway](https://railway.com/button.svg)](https://railway.com/deploy/all-url-uploader?referralCode=monthfree&utm_medium=integration&utm_source=template&utm_campaign=generic) | [![Deploy to Koyeb](https://www.koyeb.com/static/images/deploy/button.svg)](https://app.koyeb.com/deploy?type=git&repository=github.com/kalanakt/All-Url-Uploader&branch=main&name=all-url-uploader) | [![Deploy to Heroku](https://www.herokucdn.com/deploy/button.svg)](https://www.heroku.com/deploy?template=https://github.com/kalanakt/All-Url-Uploader) |

## Contributors

<!-- readme: contributors -start -->
<table>
	<tbody>
		<tr>
            <td align="center">
                <a href="https://github.com/kalanakt">
                    <img src="https://avatars.githubusercontent.com/u/86665964?v=4" width="100;" alt="kalanakt"/>
                    <br />
                    <sub><b>kalana kt</b></sub>
                </a>
            </td>
            <td align="center">
                <a href="https://github.com/tromcho">
                    <img src="https://avatars.githubusercontent.com/u/113139586?v=4" width="100;" alt="tromcho"/>
                    <br />
                    <sub><b>tromcho</b></sub>
                </a>
            </td>
            <td align="center">
                <a href="https://github.com/fzsouser">
                    <img src="https://avatars.githubusercontent.com/u/108298343?v=4" width="100;" alt="fzsouser"/>
                    <br />
                    <sub><b>Fzso</b></sub>
                </a>
            </td>
            <td align="center">
                <a href="https://github.com/hybridvamp">
                    <img src="https://avatars.githubusercontent.com/u/48980248?v=4" width="100;" alt="hybridvamp"/>
                    <br />
                    <sub><b>HYBRID</b></sub>
                </a>
            </td>
            <td align="center">
                <a href="https://github.com/Divarion-D">
                    <img src="https://avatars.githubusercontent.com/u/42798043?v=4" width="100;" alt="Divarion-D"/>
                    <br />
                    <sub><b>Danil</b></sub>
                </a>
            </td>
            <td align="center">
                <a href="https://github.com/AvikaTrivedi">
                    <img src="https://avatars.githubusercontent.com/u/84050503?v=4" width="100;" alt="AvikaTrivedi"/>
                    <br />
                    <sub><b>Avika Trivedi</b></sub>
                </a>
            </td>
		</tr>
		<tr>
            <td align="center">
                <a href="https://github.com/libresoul">
                    <img src="https://avatars.githubusercontent.com/u/69932259?v=4" width="100;" alt="libresoul"/>
                    <br />
                  
