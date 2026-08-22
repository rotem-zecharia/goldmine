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

## tools

The Elasticsearch index will turn to ***read only*** if the disk usage of the container goes above 95% until the usage drops below 90% again, you will see error messages like `disk usage exceeded flood-stage watermark`.

Similar to that, TubeArchivist will become all sorts of messed up when running out of disk space. There are some error messages in the logs when that happens, but it's best to make sure to have enough disk space before starting to download.

## limitations

* Video files created by Tube Archivist need to be playable in your browser of choice. Not every codec is compatible with every browser and might require some testing with format selection.
* Every limitation of **yt-dlp** will also be present in Tube Archivist. If **yt-dlp** can't download or extract a video for any reason, Tube Archivist won't be able to either.
* There is no flexibility in naming of the media files.

<!-- The Roadmap section is parsed by frontend/src/pages/About.tsx -->
