# derailed/k9s

🐶 Kubernetes CLI To Manage Your Clusters In Style!

## installation

K9s is available on Linux, macOS and Windows platforms.
Binaries for Linux, Windows and Mac are available as tarballs in the [release page](https://github.com/derailed/k9s/releases).

* Via [Homebrew](https://brew.sh/) for macOS or Linux

   ```shell
   brew install derailed/k9s/k9s
   ```

* Via [MacPorts](https://www.macports.org)

   ```shell
   sudo port install k9s
   ```

* Via [snap](https://snapcraft.io/k9s) for Linux

  ```shell
  snap install k9s --devmode
  ```

* On Arch Linux

  ```shell
  pacman -S k9s
  ```

* On OpenSUSE Linux distribution

  ```shell
  zypper install k9s
  ```

* On FreeBSD

  ```shell
  pkg install k9s
  ```

* On Ubuntu

  ```shell
  wget https://github.com/derailed/k9s/releases/latest/download/k9s_linux_amd64.deb && sudo apt install ./k9s_linux_amd64.deb && rm k9s_linux_amd64.deb
  ```

* On Fedora (42+)

  ```shell
  dnf install k9s
  ```

* Via [Winget](https://github.com/microsoft/winget-cli) for Windows

  ```shell
  winget install k9s
  ```

* Via [Scoop](https://scoop.sh) for Windows

  ```shell
  scoop install k9s
  ```

* Via [Chocolatey](https://chocolatey.org/packages/k9s) for Windows

  ```shell
  choco install k9s
  ```

* Via a GO install

  ```shell
  # NOTE: The dev version will be in effect!
  go install github.com/derailed/k9s@latest
  ```

* Via [Webi](https://webinstall.dev) for Linux and macOS

  ```shell
  curl -sS https://webinstall.dev/k9s | bash
  ```

* Via [pkgx](https://pkgx.dev/pkgs/k9scli.io/) for Linux and macOS

  ```shell
  pkgx k9s
  ```

* Via [gah](https://github.com/marverix/gah) for Linux and macOS

  ```shell
  gah install k9s
  ```

* Via [Webi](https://webinstall.dev) for Windows

  ```shell
  curl.exe -A MS https://webinstall.dev/k9s | powershell
  ```

* As a [Docker Desktop Extension](https://docs.docker.com/desktop/extensions/) (for the Docker Desktop built in Kubernetes Server)

  ```shell
  docker extension install spurin/k9s-dd-extension:latest
  ```

---

## Building From Source

 K9s is currently using GO v1.23.X or above.
 In order to build K9s from source you must:

 1. Clone the repo
 2. Build and run the executable

      ```shell
      make build && ./execs/k9s
      ```

---

## Running with Docker

### Running the official Docker image

  You can run k9s as a Docker container by mounting your `KUBECONFIG`:

  ```shell
  docker run --rm -it -v $KUBECONFIG:/root/.kube/config derailed/k9s
  ```

  For default path it would be:

  ```shell
  docker run --rm -it -v ~/.kube/config:/root/.kube/config derailed/k9s
  ```

### Building your own Docker image

  You can build your own Docker image of k9s from the [Dockerfile](Dockerfile) with the following:

  ```shell
  docker build -t k9s-docker:v0.0.1 .
  ```

  You can get the latest stable `kubectl` version and pass it to the `docker build` command with the `--build-arg` option.
  You can use the `--build-arg` option to pass any valid `kubectl` version (like `v1.18.0` or `v1.19.1`).

  ```shell
  KUBECTL_VERSION=$(make kubectl-stable-version 2>/dev/null)
  docker build --build-arg KUBECTL_VERSION=${KUBECTL_VERSION} -t k9s-docker:0.1 .
  ```

  Run your container:

  ```shell
  docker run --rm -it -v ~/.kube/config:/root/.kube/config k9s-docker:0.1
  ```

#### Building a multi-platform image

  The `make imgx` target builds for `linux/amd64` and `linux/arm64` via Docker
  buildx:

  ```shell
  make imgx
  ```

  Cross-architecture builds rely on QEMU emulation. Docker Desktop includes
  this out of the box. On a plain Docker Engine install, see the
  [buildx multi-platform docs](https://docs.docker.com/build/building/multi-platform/)
  for enabling emulation.

  Override the defaults with `BUILD_PLATFORMS`, `IMG_NAME` and `VERSION`:

  ```shell
  make imgx BUILD_PLATFORMS=linux/amd64,linux/arm64 IMG_NAME=your-org/k9s VERSION=v0.0.1
  ```

---

## PreFlight Checks

* K9s uses 256 colors terminal mode. On `Nix system make sure TERM is set accordingly.

    ```shell
    export TERM=xterm-256color

## configuration

k9s info

# List all available CLI options
k9s help

# To run K9s in a given namespace
k9s -n mycoolns

# Start K9s in an existing KubeConfig context
k9s --context coolCtx

## tools

k9s --readonly
```

## Logs And Debug Logs

Given the nature of the ui k9s does produce logs to a specific location.
To view the logs and turn on debug mode, use the following commands:

```shell
# Find out where the logs are stored
k9s info
```

```text
 ____  __.________
|    |/ _/   __   \______
|      < \____    /  ___/
|    |  \   /    /\___ \
|____|__ \ /____//____  >
        \/            \/

Version:           vX.Y.Z
Config:            /Users/fernand/.config/k9s/config.yaml
Logs:              /Users/fernand/.local/state/k9s/k9s.log
Dumps dir:         /Users/fernand/.local/state/k9s/screen-dumps
Benchmarks dir:    /Users/fernand/.local/state/k9s/benchmarks
Skins dir:         /Users/fernand/.local/share/k9s/skins
Contexts dir:      /Users/fernand/.local/share/k9s/clusters
Custom views file: /Users/fernand/.local/share/k9s/views.yaml
Plugins file:      /Users/fernand/.local/share/k9s/plugins.yaml
Hotkeys file:      /Users/fernand/.local/share/k9s/hotkeys.yaml
Alias file:        /Users/fernand/.local/share/k9s/aliases.yaml
```

### View K9s logs

```shell
tail -f /Users/fernand/.local/data/k9s/k9s.log
```

### Start K9s in debug mode

```shell
k9s -l debug
```

### Customize logs destination

You can override the default log file destination either with the `--logFile` argument:

```shell
k9s --logFile /tmp/k9s.log
less /tmp/k9s.log
```

Or through the `K9S_LOGS_DIR` environment variable:

```shell
K9S_LOGS_DIR=/var/log k9s
less /var/log/k9s.log
```

## Key Bindings

K9s uses aliases to navigate most K8s resources.

| Action                                                                          | Command                       | Comment                                                                |
|---------------------------------------------------------------------------------|-------------------------------|------------------------------------------------------------------------|
| Show active keyboard mnemonics and help                                         | `?`                           |                                                                        |
| Show all available resource alias                                               | `ctrl-a`                      |                                                                        |
| To bail out of K9s                                                              | `:quit`, `:q`, `ctrl-c`       |                                                                        |
| To go up/back to the previous view                                              | `esc`                         | If you have crumbs on, this will go to the previous one                |
| View a Kubernetes resource using singular/plural or short-name                  | `:`pod⏎                       | accepts singular, plural, short-name or alias ie pod or pods           |
| View a Kubernetes resource in a given namespace                                 | `:`pod ns-x⏎                  |                                                                        |
| View filtered pods (New v0.30.0!)                                               | `:`pod /fred⏎                 | View all pods filtered by fred                                         |
| View labeled pods (New v0.30.0!)                                                | `:`pod app=fred,env=dev⏎      | View all pods with labels matching app=fred and env=dev                |
| View pods in a given context (New v0.30.0!)                                     | `:`pod @ctx1⏎                 | View all pods in context ctx1. Switches out your current k9s context!  |
| Filter out a resource view given a filter                                       | `/`filter⏎                    | Regex2 supported ie `fred|blee` to filter resources named fred or blee |
| Inverse regex filter                                                            | `/`! filter⏎                  | Keep everything that *doesn't* match.                                 

## limitations

This is still work in progress! If something is broken or there's a feature
that you want, please file an issue and if so inclined submit a PR!

K9s will most likely blow up if...

1. You're running older versions of Kubernetes. K9s works best on later Kubernetes versions.
2. You don't have enough RBAC fu to manage your cluster.

---

## ATTA Girls/Boys!

K9s sits on top of many open source projects and libraries. Our *sincere*
appreciations to all the OSS contributors that work nights and weekends
to make this project a reality!

---

## Meet The Core Team!

If you have chops in GO and K8s and would like to offer your time to help maintain and enhance this project, please reach out to me.

* [Fernand Galiana](https://github.com/derailed)
  * <img src="assets/mail.png" width="16" height="auto" alt="email"/>  fernand@imhotep.io
  * <img src="assets/twitter.png" width="16" height="auto" alt="twitter"/> [@kitesurfer](https://twitter.com/kitesurfer?lang=en)

We always enjoy hearing from folks who benefit from our work!

## Contributions Guideline

* File an issue first prior to submitting a PR!
* Ensure all exported items are properly commented
* If applicable, submit a test suite against your PR

---

<img src="assets/imhotep_logo.png" width="32" height="auto" alt="Imhotep"/> &nbsp;© 2026 Imhotep Software LLC. All materials licensed under [Apache v2.0](http://www.apache.org/licenses/LICENSE-2.0)
