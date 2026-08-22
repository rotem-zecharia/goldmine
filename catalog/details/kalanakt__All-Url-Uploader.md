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
