# siyuan-note/siyuan

An open-source, privacy-first, self-hosted knowledge workspace where humans and AI agents work together 开源、隐私优先、自托管的知识工作空间，让人与智能体在此协作

## features

Most features are free, even for commercial use.

- Content block
  - Block-level reference and two-way links
  - Custom attributes
  - SQL query embed
  - Protocol `siyuan://`
- Editor
  - Block-style
  - Markdown WYSIWYG
  - List outline
  - Block zoom-in
  - Million-word large document editing
  - Mathematical formulas, charts, flowcharts, Gantt charts, timing charts, staves, etc.
  - Web clipping
  - PDF Annotation link
- Export
  - Block ref and embed
  - Standard Markdown with assets
  - PDF, Word and HTML
  - Copy to WeChat MP, Zhihu and Yuque
- Database
  - Table view
- Flashcard spaced repetition
- AI writing and Q/A chat via OpenAI API
- Tesseract OCR 
- Multi-tab, drag and drop to split screen
- Template snippet
- JavaScript/CSS snippet
- Android/iOS/HarmonyOS App
- Docker deployment
- [API](https://github.com/siyuan-note/siyuan/blob/master/docs/API.md)
- Community marketplace

Some features are only available to paid members, for more details please refer to [Pricing](https://b3log.org/siyuan/en/pricing.html).

## 🏗️ Architecture and Ecosystem

![SiYuan Arch](screenshots/SiYuan_Arch.png "SiYuan Arch")

| Project                                                  | Description           | Forks                                                                           | Stars                                                                                | 
|----------------------------------------------------------|-----------------------|---------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
| [lute](https://github.com/88250/lute)                    | Editor engine         | ![GitHub forks](https://img.shields.io/github/forks/88250/lute)                 | ![GitHub Repo stars](https://img.shields.io/github/stars/88250/lute)                 |
| [chrome](https://github.com/siyuan-note/siyuan-chrome)   | Chrome/Edge extension | ![GitHub forks](https://img.shields.io/github/forks/siyuan-note/siyuan-chrome)  | ![GitHub Repo stars](https://img.shields.io/github/stars/siyuan-note/siyuan-chrome)  |
| [bazaar](https://github.com/siyuan-note/bazaar)          | Community marketplace | ![GitHub forks](https://img.shields.io/github/forks/siyuan-note/bazaar)         | ![GitHub Repo stars](https://img.shields.io/github/stars/siyuan-note/bazaar)         |
| [dejavu](https://github.com/siyuan-note/dejavu)          | Data repo             | ![GitHub forks](https://img.shields.io/github/forks/siyuan-note/dejavu)         | ![GitHub Repo stars](https://img.shields.io/github/stars/siyuan-note/dejavu)         |
| [petal](https://github.com/siyuan-note/petal)            | Plugin API            | ![GitHub forks](https://img.shields.io/github/forks/siyuan-note/petal)          | ![GitHub Repo stars](https://img.shields.io/github/stars/siyuan-note/petal)          |
| [android](https://github.com/siyuan-note/siyuan-android) | Android App           | ![GitHub forks](https://img.shields.io/github/forks/siyuan-note/siyuan-android) | ![GitHub Repo stars](https://img.shields.io/github/stars/siyuan-note/siyuan-android) |
| [ios](https://github.com/siyuan-note/siyuan-ios)         | iOS App               | ![GitHub forks](https://img.shields.io/github/forks/siyuan-note/siyuan-ios)     | ![GitHub Repo stars](https://img.shields.io/github/stars/siyuan-note/siyuan-ios)     |
| [harmony](https://github.com/siyuan-note/siyuan-harmony) | HarmonyOS App         | ![GitHub forks](https://img.shields.io/github/forks/siyuan-note/siyuan-harmony) | ![GitHub Repo stars](https://img.shields.io/github/stars/siyuan-note/siyuan-harmony) |
| [riff](https://github.com/siyuan-note/riff)              | Spaced repetition     | ![GitHub forks](https://img.shields.io/github/forks/siyuan-note/riff)           | ![GitHub Repo stars](https://img.shields.io/github/stars/siyuan-note/riff)           |

## limitations

- [SiYuan development plan and progress](https://github.com/orgs/siyuan-note/projects/1)
- [SiYuan changelog](CHANGELOG.md)

## installation

It is recommended to give priority to installing through the application market on desktop and mobile, so that you can upgrade the version with one click in the future.

### App Market

Mobile:

- [App Store](https://apps.apple.com/us/app/siyuan/id1583226508)
- [Google Play](https://play.google.com/store/apps/details?id=org.b3log.siyuan)
- [F-Droid](https://f-droid.org/packages/org.b3log.siyuan)

Desktop:

- [Microsoft Store](https://apps.microsoft.com/detail/9p7hpmxp73k4)

### Installation Package

- [B3log](https://b3log.org/siyuan/en/download.html)
- [GitHub](https://github.com/siyuan-note/siyuan/releases)

### Package Manager

#### `siyuan`

[![Packaging status](https://repology.org/badge/vertical-allrepos/siyuan.svg)](https://repology.org/project/siyuan/versions)

#### `siyuan-note`

[![Packaging status](https://repology.org/badge/vertical-allrepos/siyuan-note.svg)](https://repology.org/project/siyuan-note/versions)

### Docker Hosting

<details>
<summary>Docker Deployment</summary>

#### Overview

The easiest way to serve SiYuan on a server is to deploy it through Docker.

- Image name `b3log/siyuan`
- [Image URL](https://hub.docker.com/r/b3log/siyuan)

#### File structure

The overall program is located under `/opt/siyuan/`, which is basically the structure under the resources folder of the Electron installation package:

- appearance: icon, theme, languages
- guide: user guide document
- stage: interface and static resources
- kernel: kernel program

#### Entrypoint

The entry point is set when building the Docker image: `ENTRYPOINT ["/opt/siyuan/entrypoint.sh"]`. This script allows changing the `PUID` and `PGID` of the user that will run inside the container. This is especially relevant to solve permission issues when mounting directories from the host. The `PUID` (User ID) and `PGID` (Group ID) can be passed as environment variables, making it easier to ensure correct permissions when accessing host-mounted directories.

Use the following parameters when running the container with `docker run b3log/siyuan`:

> **Note:** Since v3.7.0, the `serve` subcommand must be passed explicitly (e.g. `docker run b3log/siyuan serve --workspace=...`). Run `docker run --rm b3log/siyuan serve --help` to see all serving options.

- `--workspace`: Specifies the workspace folder path, mounted to the container via `-v` on the host
- `--accessAuthCode`: Specifies the lock screen password

More parameters can be found using `--help`. Here’s an example of a startup command with the new environment variables:

```bash
docker run -d \
  -v workspace_dir_host:workspace_dir_container \
  -p 6806:6806 \
  -e PUID=1001 -e PGID=1002 \
  b3log/siyuan \
  serve \
  --workspace=workspace_dir_container \
  --accessAuthCode=xxx
```

- `PUID`: Custom user ID (optional, defaults to `1000` if not provided)
- `PGID`: Custom group ID (optional, defaults to `1000` if not provided)
- `workspace_dir_host`: The workspace folder path on the host
- `workspace_dir_container`: The path of the workspace folder in the container, as specified in `--workspace`
  - Alternatively, it's possible to set the path via the `SIYUAN_WORKSPACE_PATH` env variable. The commandline will always have the priority, if both are set
- `accessAuthCode`: Lock screen password (please **be sure to modify**, otherwise anyone can access your data)
  - Alternatively, it's possible to set the lock screen password via the `SIYUAN_ACCESS_AUTH_CODE` env variable. The commandline will always have the priority, if both are set
  - To disable the lock screen password set the env variable `SIYUAN_ACCESS_AUTH_CODE_BYPASS=true`
- OIDC can replace the lock screen password as the required Docker access authentication. Set `SIYUAN_OIDC_ENABLED=true`, `SIYUAN_OIDC_PROVIDER` (`custom`, `google`, `microsoft`, or `github`), `SIYUAN_OIDC_CLIENT_ID`, and the provider-specific values below. GitHub uses its OAuth 2.0 user API adapter; the other providers use OpenID Connect discovery and ID Token validation. An inv

## tools

| Category | Commands |
|----------|----------|
| Notebooks & Documents | `notebook`, `document`, `dailynote` — CRUD and daily notes |
| Content | `block`, `attr`, `outline` — block read/write, attributes, outline |
| Metadata | `tag`, `bookmark`, `template` — tags, bookmarks, template snippets |
| Queries | `search`, `sql` — full-text, semantic, asset-content, and SQL queries |
| References | `ref` — backlinks and mentions |
| Import/Export | `export`, `import`, `inbox` — Markdown, HTML, preview, Word, .sy.zip, Data, cloud inbox |
| Data Management | `repo`, `history`, `sync` — snapshots, versions, cloud sync |
| Utilities | `asset`, `file` — resources and file system |
| Database | `database` — attribute view management |
| Server | `serve` — start the kernel HTTP server |
| Workspace & System | `workspace`, `system` — list, inspect, system info |

Run `siyuan --help` for the full command tree. Use `-f json` (default is `-f table`) for script-friendly output. Most mutating commands also support `--dry-run` to preview changes without applying them.
