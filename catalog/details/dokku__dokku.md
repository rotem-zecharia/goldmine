# dokku/dokku

A docker-powered PaaS that helps you build and manage the lifecycle of applications

## requirements

A fresh VM running any of the following operating systems:

- Ubuntu 22.04 / 24.04 (amd64/arm64) - Any currently supported release
- Debian 11+ (amd64/arm64)

An SSH keypair that can be used for application deployment. If this exists before installation, it will be automatically imported into dokku.
Otherwise, you will need to import the keypair manually after installation using `dokku ssh-keys:add`.

## installation

To install the latest stable release, run the following commands as a user who has access to `sudo`:

```shell
wget -NP . https://dokku.com/install/v0.38.27/bootstrap.sh
sudo DOKKU_TAG=v0.38.27 bash bootstrap.sh
```

You can then proceed to configure your server domain (via `dokku domains:set-global`) and user access (via `dokku ssh-keys:add`) to complete the installation.

If you wish for a more unattended installation method, see [these](https://dokku.com/docs/getting-started/install/debian/#unattended-installation) docs.

### Upgrade

[View the docs](https://dokku.com/docs/getting-started/upgrading/) for upgrading from an older version of Dokku.

## Documentation

Full documentation - including advanced installation docs - are available online at <https://dokku.com/docs/getting-started/installation/>.

## Support

You can use [GitHub Issues](https://github.com/dokku/dokku/issues), check [Troubleshooting](https://dokku.com/docs/getting-started/troubleshooting/) in the documentation, or join us on [Gliderlabs Slack in the #dokku channel](https://slack.dokku.com/).

## Contribution

After checking [GitHub Issues](https://github.com/dokku/dokku/issues), the [Troubleshooting Guide](https://dokku.com/docs/getting-started/troubleshooting/) or having a chat with us on [Gliderlabs Slack in the #dokku channel](https://slack.dokku.com/), feel free to fork and create a Pull Request.

While we may not merge your PR as is, they serve to start conversations and improve the general Dokku experience for all users.

## License

[MIT License](https://github.com/dokku/dokku/blob/master/LICENSE) © Jeff Lindsay
