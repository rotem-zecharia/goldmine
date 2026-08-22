# ArchiveBox/ArchiveBox

🗃 Open source self-hosted web archiving. Takes URLs/browser history/bookmarks/Pocket/Pinboard/etc., saves HTML, JS, PDFs, media, and more...

## installation

uv tool install --python 3.13 --prerelease explicit --upgrade 'archivebox>=0.9.0rc0,<0.10'
mkdir -p ~/archivebox/data && cd ~/archivebox/data
archivebox init
archivebox install

## features

- [**Free & open source**](https://github.com/ArchiveBox/ArchiveBox/blob/dev/LICENSE), own your own data & maintain your privacy by self-hosting
- [**Powerful CLI**](https://github.com/ArchiveBox/ArchiveBox/wiki/Usage#CLI-Usage) with [modular dependencies](#dependencies) and [support for Google Drive/NFS/SMB/S3/B2/etc.](https://github.com/ArchiveBox/ArchiveBox/wiki/Setting-Up-Storage)
- [**Comprehensive documentation**](https://github.com/ArchiveBox/ArchiveBox/wiki), [active development](https://github.com/ArchiveBox/ArchiveBox/wiki/Roadmap), and [rich community](https://github.com/ArchiveBox/ArchiveBox/wiki/Web-Archiving-Community)
- [**Extracts a wide variety of content out-of-the-box**](https://github.com/ArchiveBox/ArchiveBox/issues/51): [media (yt-dlp), articles (readability), code (git), etc.](#output-formats)
- [**Supports scheduled/realtime importing**](https://github.com/ArchiveBox/ArchiveBox/wiki/Scheduled-Archiving) from [many types of sources](#input-formats)
- [**Uses standard, durable, long-term formats**](#output-formats) like HTML, JSON, PDF, PNG, MP4, TXT, and WARC
- [**Powerful CLI**](https://github.com/ArchiveBox/ArchiveBox/wiki/Usage#CLI-Usage), [**self-hosted web UI**](https://github.com/ArchiveBox/ArchiveBox/wiki/Usage#UI-Usage), [Python API](https://docs.archivebox.io/en/dev/apidocs/archivebox/archivebox.html) (BETA), [REST API](https://github.com/ArchiveBox/ArchiveBox/issues/496) (ALPHA), or [desktop app](https://github.com/ArchiveBox/electron-archivebox)
- [**Saves all pages to archive.org as well**](https://github.com/ArchiveBox/ArchiveBox/wiki/Configuration#save_archive_dot_org) by default for redundancy (can be [disabled](https://github.com/ArchiveBox/ArchiveBox/wiki/Security-Overview#stealth-mode) for local-only mode)
- Advanced users: support for archiving [content requiring login/paywall/cookies](https://github.com/ArchiveBox/ArchiveBox/wiki/Configuration#chrome_user_data_dir) (see wiki security caveats!)
- Planned: support for running [JS during archiving](https://github.com/ArchiveBox/ArchiveBox/issues/51) to adblock, [autoscroll](https://github.com/ArchiveBox/ArchiveBox/issues/80), [modal-hide](https://github.com/ArchiveBox/ArchiveBox/issues/175), [thread-expand](https://github.com/ArchiveBox/ArchiveBox/issues/345)

<br/>

## tools

docker compose exec archivebox archivebox add 'https://example.com'
docker compose exec archivebox archivebox help
</code></pre>
<i>For more info, see <a href="https://github.com/ArchiveBox/ArchiveBox/wiki/Install#option-a-docker--docker-compose-setup-%EF%B8%8F">Install: Docker Compose</a> in the Wiki. ➡️</i>
</li>
</ol>

See <a href="#%EF%B8%8F-cli-usage">below</a> for more usage examples using the CLI, Web UI, or <a href="https://github.com/ArchiveBox/ArchiveBox/wiki/Usage#sql-shell-usage">filesystem/SQL/Python</a> to manage your archive.
<br/><br/>
</details>

<details>
<summary><b><img src="https://user-images.githubusercontent.com/511499/117447182-29758200-af0b-11eb-97bd-58723fee62ab.png" alt="Docker" height="28px" align="top"/> <code>docker run</code></b>  (macOS/Linux)</summary>
<br/>
<ol>
<li>Install <a href="https://docs.docker.com/get-docker/">Docker</a> on your system (if not already installed).</li>
<li>Create a new empty directory and initialize your collection (can be anywhere).
<pre lang="bash"><code style="white-space: pre-line">mkdir -p ~/archivebox/data && cd ~/archivebox/data
docker run --rm -v $PWD:/data -it archivebox/archivebox:dev init
docker run --rm -v $PWD:/data -it archivebox/archivebox:dev install
</code></pre>
</li>
<li>Optional: Start the server, then open <code>/admin/</code> on the hostname or IP used to reach ArchiveBox (local example: <a href="http://admin.archivebox.localhost:8000/admin/">http://admin.archivebox.localhost:8000/admin/</a>) to create the first admin. If <code>BASE_URL</code> is not configured yet, continue through the web setup wizard.
<pre lang="bash"><code style="white-space: pre-line">docker run -v $PWD:/data -p 8000:8000 archivebox/archivebox:dev

## configuration

</code></pre>
</details>

<br/>
<br/>

> [!TIP]
> Whether in Docker or not, ArchiveBox commands work the same way, and can be used to access the same data on-disk.
> For example, you could run the Web UI in Docker Compose, and run one-off commands with `uv`-installed ArchiveBox.

<details>
<summary><i>Expand to show comparison...</i></summary><br/>

<pre lang="bash"><code style="white-space: pre-line">
archivebox add --depth=1 'https://example.com'                     # add a URL with uv-installed archivebox on the host
docker compose run --rm archivebox add --depth=1 'https://example.com'                  # or w/ Docker Compose
docker run -it -v $PWD:/data archivebox/archivebox:dev add --depth=1 'https://example.com'  # or w/ Docker, all equivalent
</code></pre>

<i>For more info, see our <a href="https://github.com/ArchiveBox/ArchiveBox/wiki/Docker">Docker</a> wiki. ➡️</i>

</details>


<br/>
<div align="center" style="text-align: center">
<img src="https://github.com/ArchiveBox/ArchiveBox/assets/511499/65f82532-18dd-49c5-86f1-02b1f3100e1e" width="49%" alt="grass"/><img src="https://github.com/ArchiveBox/ArchiveBox/assets/511499/65f82532-18dd-49c5-86f1-02b1f3100e1e" width="49%" alt="grass"/>
</div>
<br/>

<div align="center" style="text-align: center">
<sub>. . . . . . . . . . . . . . . . . . . . . . . . . . . .</sub>
<br/><br/>
<a href="https://demo.archivebox.io">DEMO: <code>https://demo.archivebox.io</code></a><br/>
<a href="https://github.com/ArchiveBox/ArchiveBox/wiki/Usage">Usage</a> | <a href="https://github.com/ArchiveBox/ArchiveBox/wiki/Configuration">Configuration</a> | <a href="#Caveats">Caveats</a>
<br/>
</div>

<br/>

---

<div align="center" style="text-align: center">
<img src="https://github.com/ArchiveBox/ArchiveBox/assets/511499/ac1f897a-8baa-4f8b-8ee8-7443611f258b" width="96%" alt="lego"/>
</div>

<br/>

## requirements

To achieve high-fidelity archives in as many situations as possible, ArchiveBox depends on a variety of 3rd-party libraries and tools that specialize in extracting different types of content.

> Under-the-hood, ArchiveBox uses [Django](https://www.djangoproject.com/start/overview/) to power its [Web UI](https://github.com/ArchiveBox/ArchiveBox/wiki/Usage#ui-usage), [Django Ninja](https://django-ninja.dev/) for the REST API, and [SQlite](https://www.sqlite.org/locrsf.html) + the filesystem to provide [fast & durable metadata storage](https://www.sqlite.org/locrsf.html) w/ [deterministic upgrades](https://stackoverflow.com/a/39976321/2156113).

ArchiveBox bundles industry-standard tools like [Google Chrome](https://github.com/ArchiveBox/ArchiveBox/wiki/Chromium-Install), [`wget`, `yt-dlp`, `readability`, etc.](#dependencies) internally, and its operation can be [tuned, secured, and extended](https://github.com/ArchiveBox/ArchiveBox/wiki/Configuration) as-needed for many different applications.

<br/>
<details>
<summary><i>Expand to learn more about ArchiveBox's internals & dependencies...</i></summary><br/>

<blockquote>
<p><em>TIP: For better security while running ArchiveBox, and to avoid polluting your host system with a bunch of sub-dependencies that you need to keep up-to-date,<strong>it is strongly recommended to use the <a href="https://github.com/ArchiveBox/ArchiveBox/wiki/Docker">⭐️ official Docker image</a></strong> which provides everything in an easy container with simple one-liner upgrades.</em></p>
</blockquote>

<ul>
<li>Language: Python <code>&gt;=3.13</code></li>
<li>Backend: <a href="https://www.djangoproject.com/">Django</a> + <a href="https://django-ninja.dev/">Django-Ninja</a> for REST API</li>
<li>Frontend: <a href="https://docs.djangoproject.com/en/6.0/ref/contrib/admin/">Django Admin</a> + Vanilla HTML, CSS, JS</li>
<li>Web Server: <a href="https://www.djangoproject.com/">Django</a> + <a href="https://github.com/django/daphne/"><code>daphne</code></a> (ASGI)</li>
<li>Database: <a href="https://docs.djangoproject.com/en/6.0/ref/databases/#sqlite-notes">Django ORM</a> saving to <a href="https://www.sqlite.org/mostdeployed.html">SQLite3</a> <code>./data/index.sqlite3</code></li>
<li>Job Queue: Custom orchestrator using <code>supervisord</code> for worker management</li>
<li>Build/test/lint: <a href="https://github.com/astral-sh/uv"><code>uv</code></a> / <code>pyright</code>+<code>ty</code>+<code>pytest</code> / <code>ruff</code></li>
<li>Subdependencies: <a href="https://github.com/ArchiveBox/abxpkg"><code>abxpkg</code></a> installs apt/brew/pip/npm pkgs at runtime (e.g. <code>yt-dlp</code>, <code>singlefile</code>, <code>readability</code>, <code>git</code>)</li>
</ul>


These optional subdependencies used for archiving sites include:

<img src="https://github.com/ArchiveBox/ArchiveBox/assets/511499/62a02155-05d7-4f3e-8de5-75a50a145c4f" alt="archivebox --version CLI output screenshot showing dependencies installed" width="330px" align="right" style="max-width: 100%;">

<ul>
<li><code>chromium</code> / <code>chrome</code> (for screenshots, PDF, DOM HTML, and headless JS scripts)</li>
<li><code>node</code> &amp; <code>npm</code> (for readability, mercury, and singlefile)</li>
<li><code>wget</code> (for plain HTML, static files, and WARC saving)</li>
<li><code>curl</code> (for fetching headers, favicon, and posting to Archive.org)</li>
<li><code>yt-dlp</code> or <code>youtube-dl</code> (for audio, video, and subtitles)</li>
<li><code>git</code> (for cloning git repos)</li>
<li><code>singlefile</code> (for saving into a self-contained html file)</li>
<li><code>postlight/parser</code> (for discussion threads, forums, and articles)</li>
<li><code>readability</code> (for articles and long text content)</li>
<li>and more as we grow...</li>
</ul>

You don't need to install every dependency by hand. ArchiveBox resolves every extractor dependency through <code>abxpkg</code>: it uses a compatible host installation when
