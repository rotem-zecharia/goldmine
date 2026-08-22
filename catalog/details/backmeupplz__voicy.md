# backmeupplz/voicy

@voicybot Telegram bot main repository

## installation

1. Clone this repo: `git clone https://github.com/backmeupplz/voicy`
2. Launch a [mongo database](https://www.mongodb.com/) locally
3. Create `.env` file with the environment variables listed below
4. Install `ffmpeg` on machines that run local transcription workers
5. Run `yarn` in the root folder
6. Run `yarn start`

## configuration

| Variable      | Description                                                     |
| ------------- | --------------------------------------------------------------- |
| `MONGO`       | URI for the mongo database used                                 |
| `TOKEN`       | Telegram bot token                                              |
| `SALT`        | Random salt to generate various encrypted stuff                 |
| `ADMIN_ID`    | Chat id of the person who shall receive valuable logs           |
| `ENVIRONMENT` | App environment, can be `development`, defaults to `production` |

See examples in `.env.sample` file.

Optional live activity stream:

| Variable                                     | Description                                                                           |
| -------------------------------------------- | ------------------------------------------------------------------------------------- |
| `VOICY_ACTIVITY_STREAM_URL`                  | Symphony activity stream base URL or full `/activity/v1/events` URL                   |
| `VOICY_ACTIVITY_STREAM_TOKEN`                | Submit token sent as `Authorization: Bearer ...`                                      |
| `VOICY_ACTIVITY_STREAM_ANONYMIZATION_SECRET` | Optional HMAC secret for deterministic chat/user labels; defaults to the submit token |
| `VOICY_ACTIVITY_STREAM_TIMEOUT_MS`           | Optional submit timeout, default `750`                                                |

When the stream URL or token is missing, activity emitters are no-ops. Events
are fire-and-forget and contain only anonymized chat labels, command names,
media source kinds, and runtime/job milestones; Telegram message text, raw chat
IDs, raw user IDs, file IDs, tokens, emails, and phone numbers must not be sent.

## Continuous integration

Any commit pushed to `main` gets deployed to [@voicybot](https://t.me/voicybot) via [CI Ninja](https://github.com/backmeupplz/ci-ninja).

## Windows GPU transcription worker

Voicy queues incoming Telegram audio in Mongo and expects one or more
authenticated worker clients to process those jobs. The Windows GPU worker is
the supported local setup for Nikita's RTX 4070 Ti machine: it polls the backend
worker API, downloads the queued audio source, runs a local transcription command
on CUDA, and uploads the final transcript back to Voicy.

The worker API is mounted at `/worker/v1` and requires
`Authorization: Bearer <VOICY_WORKER_TOKEN>` on every request. Create a worker
token from a trusted backend shell after building the TypeScript output:

```sh
yarn build-ts
MONGO='mongodb://...' yarn worker:create-client windows-4070-ti
```

Store the printed token only in the Windows worker environment as
`VOICY_WORKER_TOKEN`; the backend stores only its SHA-256 hash. If a token is
lost or exposed, create a replacement token and disable the old `WorkerClient`
record in Mongo by setting `enabled` to `false`.

On the Windows machine, build this repo, install FFmpeg, Node.js 20+, Python
3.11, current NVIDIA drivers, and a CUDA-capable transcription stack such as
`faster-whisper`. Configure the worker with:

```powershell
$env:VOICY_WORKER_API_URL = "https://<voicy-host>/worker/v1"
$env:VOICY_WORKER_TOKEN = "voicy_worker_..."
$env:VOICY_WORKER_WORK_DIR = "C:\voicy-worker\jobs"
$env:VOICY_WORKER_ENGINE = "faster-whisper"
$env:VOICY_WORKER_MODEL = "large-v3"
$env:VOICY_WORKER_RESTART_DELAY_MS = "10000"
$env:VOICY_WORKER_TELEGRAM_BOT_TOKEN = "<telegram-bot-token>"
$env:VOICY_WORKER_TELEGRAM_API_URL = "http://127.0.0.1:8081"
$env:VOICY_WORKER_DOWNLOAD_CONCURRENCY = "2"
$env:VOICY_WORKER_TRANSCRIPTION_CONCURRENCY = "1"
$env:VOICY_WORKER_TRANSCRIBE_EXECUTABLE = "C:\voicy-worker\.venv\Scripts\python.exe"
$env:VOICY_WORKER_TRANSCRIBE_ARGS_JSON = '["C:\\voicy-worker\\transcribe.py","{input}","{output}","{language}","{model}"]'
yarn worker:run
```

For production on Windows, install the checked-in scheduled-task supervisor with
`scripts/install-windows-worker.ps1`
