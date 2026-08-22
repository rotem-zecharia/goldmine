# paperless-ngx/paperless-ngx

A community-supported supercharged document management system: scan, index and archive all your documents

## features

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/paperless-ngx/paperless-ngx/main/docs/assets/screenshots/documents-smallcards-dark.png">
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/paperless-ngx/paperless-ngx/main/docs/assets/screenshots/documents-smallcards.png">
  <img src="https://raw.githubusercontent.com/paperless-ngx/paperless-ngx/main/docs/assets/screenshots/documents-smallcards.png">
</picture>

A full list of [features](https://docs.paperless-ngx.com/#features) and [screenshots](https://docs.paperless-ngx.com/#screenshots) are available in the [documentation](https://docs.paperless-ngx.com/).

## installation

The easiest way to deploy paperless is `docker compose`. The files in the [`/docker/compose` directory](https://github.com/paperless-ngx/paperless-ngx/tree/main/docker/compose) are configured to pull the image from the GitHub container registry.

If you'd like to jump right in, you can configure a `docker compose` environment with our install script:

```bash
bash -c "$(curl -L https://raw.githubusercontent.com/paperless-ngx/paperless-ngx/main/install-paperless-ngx.sh)"
```

More details and step-by-step guides for alternative installation methods can be found in [the documentation](https://docs.paperless-ngx.com/setup/#installation).

Migrating from Paperless-ng is easy, just drop in the new docker image! See the [documentation on migrating](https://docs.paperless-ngx.com/setup/#migrating-to-paperless-ngx) for more details.

<!-- omit in toc -->
