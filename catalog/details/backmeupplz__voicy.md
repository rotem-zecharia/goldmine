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
