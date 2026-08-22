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

## configuration

k9s info

## tools

k9s --readonly
```

## limitations

This is still work in progress! If something is broken or there's a feature
that you want, please file an issue and if so inclined submit a PR!

K9s will most likely blow up if...

1. You're running older versions of Kubernetes. K9s works best on later Kubernetes versions.
2. You don't have enough RBAC fu to manage your cluster.

---
