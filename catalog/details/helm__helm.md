# helm/helm

The Kubernetes Package Manager

## installation

Binary downloads of the Helm client can be found on [the Releases page](https://github.com/helm/helm/releases/latest).

Unpack the `helm` binary and add it to your PATH and you are good to go!

If you want to use a package manager:

- [Homebrew](https://brew.sh/) users can use `brew install helm`.
- [Chocolatey](https://chocolatey.org/) users can use `choco install kubernetes-helm`.
- [Winget](https://learn.microsoft.com/en-us/windows/package-manager/) users can use `winget install Helm.Helm`.
- [Scoop](https://scoop.sh/) users can use `scoop install helm`.
- [Snapcraft](https://snapcraft.io/) users can use `snap install helm --classic`.
- [Flox](https://flox.dev) users can use `flox install kubernetes-helm`.
- [Mise-en-place](https://mise.jdx.dev/) users can use `mise use -g helm@latest`

To rapidly get Helm up and running, start with the [Quick Start Guide](https://helm.sh/docs/intro/quickstart/).

See the [installation guide](https://helm.sh/docs/intro/install/) for more options,
including installing pre-releases.

## limitations

The [Helm roadmap uses GitHub milestones](https://github.com/helm/helm/milestones) to track the progress of the project.

Helm v4 development happens on the `main` branch. Helm v3 is in support mode on the `dev-v3` branch and receives only bug and security fixes.
