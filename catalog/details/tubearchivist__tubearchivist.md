# tubearchivist/tubearchivist

Your self hosted YouTube media server

## installation

For minimal system requirements, the Tube Archivist stack needs around 2GB of available memory for a small testing setup and around 4GB of available memory for a mid to large sized installation. Minimal with dual core with 4 threads, better quad core plus.
This project requires docker. Ensure it is installed and running on your system.

The documentation has additional user provided instructions for [Unraid](https://docs.tubearchivist.com/installation/unraid/), [Synology](https://docs.tubearchivist.com/installation/synology/) and [Podman](https://docs.tubearchivist.com/installation/podman/).

The instructions here should get you up and running quickly, for Docker beginners and full explanation about each environment variable, see the [docs](https://docs.tubearchivist.com/installation/docker-compose/).

Take a look at the example [docker-compose.yml](https://github.com/tubearchivist/tubearchivist/blob/master/docker-compose.yml) and configure the required environment variables.

All environment variables are explained in detail in the docs [here](https://docs.tubearchivist.com/installation/env-vars/).

Both `TA_PASSWORD` and `ELASTIC_PASSWORD` can be suffixed with `_FILE` to allow passing in passwords as secrets. `_FILE` is a convention used by some images including [ElasticSearch](https://www.elastic.co/docs/deploy-manage/deploy/self-managed/install-elasticsearch-docker-configure)

### TubeArchivist

| Environment Var               | Value | Required |
| ----------------------------- | ----- | -------- |
| TA_HOST                       | Server IP or hostname `http://tubearchivist.local:8000` | Required |
| TA_USERNAME                   | Initial username when logging into TA | Required |
| TA_PASSWORD                   | Initial password when logging into TA | Required |
| ELASTIC_PASSWORD              | Password for ElasticSearch | Required |
| REDIS_CON                     | Connection string to Redis | Required |
| TZ                            | Set your timezone for the scheduler | Required |
| TA_PORT                       | Overwrite Nginx port | Optional |
| TA_BACKEND_PORT               | Overwrite container internal backend server port | Optional |
| TA_ENABLE_AUTH_PROXY          | Enables support for forwarding auth in reverse proxies | [Read more](https://docs.tubearchivist.com/configuration/forward-auth/) |
| TA_AUTH_PROXY_USERNAME_HEADER | Header containing username to log in | Optional |
| TA_AUTH_PROXY_LOGOUT_URL      | Logout URL for forwarded auth | Optional |
| ES_URL                        | URL That ElasticSearch runs on | Optional |
| ES_DISABLE_VERIFY_SSL         | Disable ElasticSearch SSL certificate verification | Optional |
| ES_SNAPSHOT_DIR               | Custom path where elastic search stores snapshots for master/data nodes | Optional |
| HOST_GID                      | Allow TA to own the video files instead of container user | Optional |
| HOST_UID                      | Allow TA to own the video files instead of container user | Optional |
| ELASTIC_USER                  | Change the default ElasticSearch user | Optional |
| TA_LDAP                       | Configure TA to use LDAP Authentication | [Read more](https://docs.tubearchivist.com/configuration/ldap/) |
| DISABLE_STATIC_AUTH           | Remove authentication from media files, (Google Cast...) | [Read more](https://docs.tubearchivist.com/installation/env-vars/#disable_static_auth) |
| TA_AUTO_UPDATE_YTDLP          | Configure TA to automatically install the latest yt-dlp on container start | Optional |
| DJANGO_DEBUG                  | Return additional error messages, for debug only | Optional |
| TA_LOGIN_AUTH_MODE            | Configure the order of login authentication backends (Default: single) | Optional |

| TA_LOGIN_AUTH_MODE value | Description |
| ------------------------ | ----------- |
| single                   | Only use a single backend (default, or LDAP, or Forward auth, selected by TA_LDAP or TA_ENABLE_AUTH_PROXY) |
| 

## tools

The Elasticsearch index will turn to ***read only*** if the disk usage of the container goes above 95% until the usage drops below 90% again, you will see error messages like `disk usage exceeded flood-stage watermark`.

Similar to that, TubeArchivist will become all sorts of messed up when running out of disk space. There are some error messages in the logs when that happens, but it's best to make sure to have enough disk space before starting to download.

## `error setting rlimit`

If you are seeing errors like `failed to create shim: OCI runtime create failed` and `error during container init: error setting rlimits`, this means docker can't set these limits, usually because they are set at another place or are incompatible because of other reasons. Solution is to remove the `ulimits` key from the ES container in your docker compose and start again.

This can happen if you have nested virtualizations, e.g. LXC running Docker in Proxmox.

## limitations

* Video files created by Tube Archivist need to be playable in your browser of choice. Not every codec is compatible with every browser and might require some testing with format selection.
* Every limitation of **yt-dlp** will also be present in Tube Archivist. If **yt-dlp** can't download or extract a video for any reason, Tube Archivist won't be able to either.
* There is no flexibility in naming of the media files.

<!-- The Roadmap section is parsed by frontend/src/pages/About.tsx -->
## Roadmap

We have come far, nonetheless we are not short of ideas on how to improve and extend this project. Issues waiting for you to be tackled in no particular order:

- [ ] Audio download
- [ ] Podcast mode to serve channel as mp3
- [ ] Random and repeat controls ([#108](https://github.com/tubearchivist/tubearchivist/issues/108), [#220](https://github.com/tubearchivist/tubearchivist/issues/220))
- [ ] Auto play or play next link ([#226](https://github.com/tubearchivist/tubearchivist/issues/226))
- [ ] Multi language support
- [ ] Show total video downloaded vs total videos available in channel
- [ ] Download or Ignore videos by keyword ([#163](https://github.com/tubearchivist/tubearchivist/issues/163))
- [ ] Custom searchable notes to videos, channels, playlists ([#144](https://github.com/tubearchivist/tubearchivist/issues/144))
- [ ] Search comments
- [ ] Per user videos/channel/playlists

Implemented:
- [X] Search download queue [2025-07-31]
- [X] Configure shorts, streams and video sizes per channel [2024-07-15]
- [X] User created playlists [2024-04-10]
- [X] User roles, aka read only user [2023-11-10]
- [X] Add statistics of index [2023-09-03]
- [X] Implement [Apprise](https://github.com/caronc/apprise) for notifications [2023-08-05]
- [X] Download video comments [2022-11-30]
- [X] Show similar videos on video page [2022-11-30]
- [X] Implement complete offline media file import from json file [2022-08-20]
- [X] Filter and query in search form, search by url query [2022-07-23]
- [X] Make items in grid row configurable to use more of the screen [2022-06-04]
- [X] Add passing browser cookies to yt-dlp [2022-05-08]
- [X] Add [SponsorBlock](https://sponsor.ajay.app/) integration [2022-04-16]
- [X] Implement per channel settings [2022-03-26]
- [X] Subtitle download & indexing [2022-02-13]
- [X] Fancy advanced unified search interface [2022-01-08]
- [X] Auto rescan and auto download on a schedule [2021-12-17]
- [X] Optional automatic deletion of watched items after a specified time [2021-12-17]
- [X] Create playlists [2021-11-27]
- [X] Access control [2021-11-01]
- [X] Delete videos and channel [2021-10-16]
- [X] Add thumbnail embed option [2021-10-16]
- [X] Create a github wiki for user documentation [2021-10-03]
- [X] Grid and list view for both channel and video list pages [2021-10-03]
- [X] Un-ignore videos [2021-10-03]
- [X] Dynamic download queue [2021-09-26]
- [X] Backup and restore [2021-09-22]
- [X] Scan your file system to index already downloaded videos [2021-09-14]

## User Scripts

This is a list of useful user scripts, generously created from folks like you to extend this project and its functionality. Make sure to check the respective repository links for detailed license information.

This is your time to shine, [read this](https://github.com/tubearchivist/tubearchivist/blob/master/CONTRIBUTING.md#user-scripts) then open a PR to add your script here.

* [danieljue/ta_dl_page_script](https://github.com/danieljue/ta_dl_page_script): Helper browser script to prioritize a channels' videos in download queue.
* [dot-mike/ta-scripts](https://github.com/dot-mike/ta-scripts): A collection of personal scripts for managing TubeArchivist.
* [DarkFighterLuke/ta_base_url_nginx](https://gist.github.com/DarkFighterLuke/4561b6bfbf83720493dc59171c58ac36): Set base URL with Nginx when you can't use subdomains.
* [lamusmaser/ta_migration_helper](https://github.com/lamusmaser/ta_migration_helper): Advanced helper script for migration issues to
