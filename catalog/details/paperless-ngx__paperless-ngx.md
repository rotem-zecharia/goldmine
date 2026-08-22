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

### Documentation

The documentation for Paperless-ngx is available at [https://docs.paperless-ngx.com](https://docs.paperless-ngx.com/).

# Contributing

If you feel like contributing to the project, please do! Bug fixes, enhancements, visual fixes etc. are always welcome. If you want to implement something big: Please start a discussion about that! The [documentation](https://docs.paperless-ngx.com/development/) has some basic information on how to get started.

## Community Support

People interested in continuing the work on paperless-ngx are encouraged to reach out here on github and in the [Matrix Room](https://matrix.to/#/#paperless:matrix.org). If you would like to contribute to the project on an ongoing basis there are multiple [teams](https://github.com/orgs/paperless-ngx/people) (frontend, ci/cd, etc) that could use your help so please reach out!

## Translation

Paperless-ngx is available in many languages that are coordinated on Crowdin. If you want to help out by translating paperless-ngx into your language, please head over to https://crowdin.com/project/paperless-ngx, and thank you! More details can be found in [CONTRIBUTING.md](https://github.com/paperless-ngx/paperless-ngx/blob/main/CONTRIBUTING.md#translating-paperless-ngx).
