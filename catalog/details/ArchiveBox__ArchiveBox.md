# ArchiveBox/ArchiveBox

🗃 Open source self-hosted web archiving. Takes URLs/browser history/bookmarks/Pocket/Pinboard/etc., saves HTML, JS, PDFs, media, and more...

## installation

# docker compose run --rm archivebox add 'https://example.com'
# docker compose run --rm archivebox help
<br/>
<br/>
# Option B: Or use it as a plain Docker container:
mkdir -p ~/archivebox/data && cd ~/archivebox/data
docker run --rm -it -v "$PWD:/data" archivebox/archivebox:dev init
docker run --rm -it -v "$PWD:/data" archivebox/archivebox:dev install
docker run -d --name archivebox -v "$PWD:/data" -p 8000:8000 archivebox/archivebox:dev
# open http://admin.archivebox.localhost:8000 to finish setup
# docker run -it -v $PWD:/data archivebox/archivebox:dev add 'https://example.com'
# docker run -it -v $PWD:/data archivebox/archivebox:dev help
<br/>
<br/>
# Option C: Or install it with uv (see Quickstart below for apt, brew, and more)
uv tool install --python 3.13 --prerelease explicit --upgrade 'archivebox>=0.9.0rc0,<0.10'
mkdir -p ~/archivebox/data && cd ~/archivebox/data
archivebox init
archivebox install
# archivebox add 'https://example.com'
# archivebox help
# archivebox server 0.0.0.0:8000
<br/>
<br/>
# Option D: Or use the optional auto setup script to install it
curl -fsSL 'https://get.archivebox.io' | bash
</code></pre>
<br/>
<sub>Open <a href="http://web.archivebox.localhost:8000"><code>http://web.archivebox.localhost:8000</code></a> for the public UI and <a href="http://admin.archivebox.localhost:8000"><code>http://admin.archivebox.localhost:8000</code></a> for the admin UI ➡️</sub><br/>
<sub>Set <code>BASE_URL</code> to change the public base domain. The default <code>auto</code> mode uses <code>web.</code> and <code>admin.</code> subdomains on <code>*.localhost</code>, but one host for ordinary DNS names. <code>BIND_ADDR</code> only controls the local listen address.</sub>
</details>
<br/>


<div align="center" style="text-align: center">
<br/><br/>
<img src="https://github.com/ArchiveBox/ArchiveBox/assets/511499/5a7d95f2-6977-4de6-9f08-42851a1fe1d2" height="70px" alt="bookshelf graphic"> &nbsp; <img src="https://github.com/ArchiveBox/ArchiveBox/assets/511499/b2765a33-0d1e-4019-a1db-920c7e00e20e" height="75px" alt="logo" align="top"/> &nbsp; <img src="https://github.com/ArchiveBox/ArchiveBox/assets/511499/5a7d95f2-6977-4de6-9f08-42851a1fe1d2" height="70px" alt="bookshelf graphic">
<br/><br/>
<small><a href="https://demo.archivebox.io">Demo</a> | <a href="#screenshots">Screenshots</a> | <a href="https://github.com/ArchiveBox/ArchiveBox/wiki/Usage">Usage</a></small>
<br/>
<sub>. . . . . . . . . . . . . . . . . . . . . . . . . . . .</sub>
<br/><br/>
<img src="https://github.com/ArchiveBox/ArchiveBox/assets/511499/8d67382c-e0ce-4286-89f7-7915f09b930c" width="22%" alt="cli init screenshot" align="top">
<img src="https://github.com/ArchiveBox/ArchiveBox/assets/511499/dad2bc51-e7e5-484e-bb26-f956ed692d16" width="22%" alt="cli init screenshot" align="top">
<img src="https://github.com/ArchiveBox/ArchiveBox/assets/511499/e8e0b6f8-8fdf-4b7f-8124-c10d8699bdb2" width="22%" alt="server snapshot admin screenshot" align="top">
<img src="https://github.com/ArchiveBox/ArchiveBox/assets/511499/ace0954a-ddac-4520-9d18-1c77b1ec50b2" width="28.6%" alt="server snapshot details page screenshot" align="top"/>
<br/><br/>
</div>

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

## 🤝 Professional Integration

ArchiveBox is free for everyone to self-host, but we also provide support, security review, and custom integrations to help NGOs, governments, and other organizations [run ArchiveBox professionally](https://zulip.archivebox.io/#narrow/stream/167-enterprise/topic/welcome/near/1191102):

- **Journalists:**
  `crawling during research`, `preserving cited pages`, `fact-checking & review`  
- **Lawyers:**
  `collecting & preserving evidence`, `detecting changes`, `tagging & review`  
- **Researchers:**
  `analyzing social media trends`, `getting LLM training data`, `crawling pipelines`
- **Individuals:**
  `saving bookmarks`, `preserving portfolio content`, `legacy / memoirs archival`
- **Governments:**
  `snapshotting public service sites`, `recordkeeping compliance`

> ***[Contact us](https://zulip.archivebox.io/#narrow/stream/167-enterprise/topic/welcome/near/1191102)** if your org wants help using ArchiveBox professionally.*  
> We offer: setup & support, CAPTCHA/ratelimit unblocking, SSO, audit logging/chain-of-custody, and more  
> *ArchiveBox is a 🏛️ 501(c)(3) [nonprofit FSP](https://hackclub.com/hcb/) and all our work supports open-source development.* 

<br/>

<div align="center" style="text-align: center">
<br/>
<img src="https://github.com/ArchiveBox/ArchiveBox/assets/511499/0db52ea7-4a2c-441d-b47f-5553a5d8fe96" width="49%" alt="grass"/><img src="https://github.com/ArchiveBox/ArchiveBox/assets/511499/0db52ea7-4a2c-441d-b47f-5553a5d8fe96" width="49%" alt="grass"/>
</div>

<a name="install"></a>

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
# completely optional, CLI can always be used without running a server
# docker run -v $PWD:/data -it archivebox/archivebox:dev [subcommand] [--help]
docker run -v $PWD:/data -it archivebox/archivebox:dev help
</code></pre>
<i>For more info, see <a href="https://github.com/ArchiveBox/ArchiveBox/wiki/Install#option-a-docker--docker-compose-setup-%EF%B8%8F">Install: Docker Compose</a> in the Wiki. ➡️</i>
</li>
</ol>

See <a href="#%EF%B8%8F-cli-usage">below</a> for more usage examples using the CLI, Web UI, or filesystem/SQL/Python to manage your archive.
<br/><br/>
</details>

<details>
<summary><b><img src="https://user-images.githubusercontent.com/511499/117456282-08665e80-af16-11eb-91a1-8102eff54091.png" alt="curl sh automatic setup script" height="28px" align="top"/> <code>bash</code> auto-setup script</b>  (macOS/Linux)</summary>
<br/>
<ol>
<li>Install <a href="https://docs.docker.com/get-docker/">Docker</a> on your system (optional, highly recommended but not required).</li>
<li>Run the automatic setup script.
<pre lang="bash"><code style="white-space: pre-line">curl -fsSL 'https://get.archivebox.io' | bash</code></pre>
<i>For more info, see <a href="https://github.com/ArchiveBox/ArchiveBox/wiki/Install#option-b-automatic-setup-script">Install: Bare Metal</a> in the Wiki. ➡️</i>
</li>
</ol>

See <a href="#%EF%B8%8F-cli-usage">below</a> for more usage examples using the CLI, Web UI, or filesystem/SQL/Python to manage your archive.<br/>
See <a href="https://github.com/ArchiveBox/ArchiveBox/blob/dev/bin/setup.sh"><code>setup.sh</code></a> for the source code of the auto-install script.<br/>
See <a href="https://docs.sweeting.me/s/against-curl-sh">"Against curl | sh as an install method"</a> blog post for my thoughts on the shortcomings of this install method.
<br/><br/>
</details>

<br/>

#### 🛠&nbsp; Package Manager Setup

<a name="Manual-Setup"></a>


<details>
<summary><b><img src="https://user-images.githubusercontent.com/511499/117447613-ba4c5d80-af0b-11eb-8f89-1d98e31b6a79.png" alt="uv" height="28px" align="top"/> <code>uv</code></b> (macOS/Linux/BSD)</summary>
<br/>
<ol>

<li>Install <a href="https://docs.astral.sh/uv/getting-started/installation/">uv</a> on your system (if not already installed).</li>
<li>Install the Arch

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

## limitations

### Archiving Private Content

<a id="archiving-private-urls"></a>

If you're importing pages with private content or URLs containing secret tokens you don't want public (e.g Google Docs, paywalled content, unlisted videos, etc.), **you may want to disable some of the extractor methods to avoid leaking that content to 3rd party APIs or the public**.

<br/>
<details>
<summary><i>Expand to learn about privacy, permissions, and user accounts...</i></summary>


<pre lang="bash"><code style="white-space: pre-line"># don't save private content to ArchiveBox, e.g.:
archivebox add 'https://docs.google.com/document/d/12345somePrivateDocument'
archivebox add 'https://vimeo.com/somePrivateVideo'

# restrict the main index, Snapshot content, and Add Page to authenticated users as-needed:
archivebox config --set PUBLIC_INDEX=False
archivebox config --set PERMISSIONS=private
archivebox config --set PUBLIC_ADD_VIEW=False
archivebox manage createsuperuser
</code></pre>

<blockquote>
<p><em>CAUTION: Assume anyone <em>viewing</em> your archives will be able to see any cookies, session tokens, or private URLs passed to ArchiveBox during archiving.</em>
<em>Make sure to secure your ArchiveBox data and don't share snapshots with others without stripping out sensitive headers and content first.</em></p>
</blockquote>

<h4>Learn More</h4>

<ul>
<li><a href="https://github.com/ArchiveBox/ArchiveBox/wiki/Publishing-Your-Archive">Wiki: Publishing Your Archive</a></li>
<li><a href="https://github.com/ArchiveBox/ArchiveBox/wiki/Security-Overview">Wiki: Security Overview</a></li>
<li><a href="https://github.com/ArchiveBox/ArchiveBox/wiki/Chromium-Install#setting-up-a-chromium-user-profile">Wiki: Chromium Install (Setting Up a User Profile)</a></li>
<li><a href="https://github.com/ArchiveBox/ArchiveBox/wiki/Personas">Wiki: Personas (browser profiles and cookies)</a></li>
<li><a href="https://github.com/ArchiveBox/ArchiveBox/wiki/Configuration#default_persona">Wiki: Configuration (<code>DEFAULT_PERSONA</code>)</a></li>
</ul>

</details>
<br/>


### Security Risks of Viewing Archived JS

Archived JavaScript is untrusted content. The default <code>SERVER_SECURITY_MODE=auto</code> uses isolated subdomains with full replay on <code>*.localhost</code>, and a one-domain no-JS replay policy on ordinary public or LAN hostnames. Choose <code>safe-subdomains-fullreplay</code> only when wildcard DNS and TLS are configured. See the [Security Overview](https://github.com/ArchiveBox/ArchiveBox/wiki/Security-Overview) and [Issue #239](https://github.com/ArchiveBox/ArchiveBox/issues/239) for details.


<br/>
<details>
<summary><i>Expand to see risks and mitigations...</i></summary>


<pre lang="bash"><code style="white-space: pre-line"># Explicit wildcard mode: full replay on isolated snapshot subdomains
archivebox config --set SERVER_SECURITY_MODE=safe-subdomains-fullreplay

# Alternative for deployments without wildcard subdomains: disable JS replay
archivebox config --set SERVER_SECURITY_MODE=safe-onedomain-nojsreplay
</code></pre>

<blockquote>
<p><em>NOTE: Only the <code>wget</code> &amp; <code>dom</code> extractor methods execute archived JS when viewing snapshots, all other archive methods produce static output that does not execute JS on viewing.</em><br/>
<em>If you do not need JavaScript-capable replay at all, you can also disable those extractors with:<br/> <code>archivebox config --set WGET_ENABLED=False DOM_ENABLED=False</code>.</em></p>
</blockquote>

<h4>Learn More</h4>
<ul>
<li><a href="https://github.com/ArchiveBox/ArchiveBox/wiki/Security-Overview">Wiki: Security Overview</a></li>
<li><a href="https://github.com/ArchiveBox/ArchiveBox/issues/239">ArchiveBox Github Issue: #239</a></li>
<li><a href="https://github.com/ArchiveBox/ArchiveBox/security/advisories/GHSA-cr45-98w9-gwqx">Security Advisory: <code>CVE-2023-45815</code></a></li>
<li><a href="https://github.com/ArchiveBox/ArchiveBox/wiki/Security-Overview#publishing">Wiki: Security Overview (Publishing)
