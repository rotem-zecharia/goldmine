# koalaman/shellcheck

ShellCheck, a static analysis tool for shell scripts

## installation

The easiest way to install ShellCheck locally is through your package manager.

On systems with Cabal (installs to `~/.cabal/bin`):

    cabal update
    cabal install ShellCheck

On systems with Stack (installs to `~/.local/bin`):

    stack update
    stack install ShellCheck

On Debian based distros:

    sudo apt install shellcheck

On Arch Linux based distros:

    pacman -S shellcheck

or get the dependency free [shellcheck-bin](https://aur.archlinux.org/packages/shellcheck-bin/) from the AUR.

On Gentoo based distros:

    emerge --ask shellcheck

On EPEL based distros:

    sudo yum -y install epel-release
    sudo yum install ShellCheck

On Fedora based distros:

    dnf install ShellCheck

On FreeBSD:

    pkg install hs-ShellCheck

On macOS (OS X) with Homebrew:

    brew install shellcheck

Or with MacPorts:

    sudo port install shellcheck

On OpenBSD:

    pkg_add shellcheck

On openSUSE

    zypper in ShellCheck

Or use OneClickInstall - <https://software.opensuse.org/package/ShellCheck>

On Solus:

    eopkg install shellcheck

On Windows (via [chocolatey](https://chocolatey.org/packages/shellcheck)):

```cmd
C:\> choco install shellcheck
```

Or Windows (via [winget](https://github.com/microsoft/winget-pkgs)):

```cmd
C:\> winget install --id koalaman.shellcheck
```

Or Windows (via [scoop](http://scoop.sh)):

```cmd
C:\> scoop install shellcheck
```

From [conda-forge](https://anaconda.org/conda-forge/shellcheck):

    conda install -c conda-forge shellcheck

From Snap Store:

    snap install --channel=edge shellcheck

From Docker Hub:

```sh
docker run --rm -v "$PWD:/mnt" koalaman/shellcheck:stable myscript

## tools

ShellCheck can recognize instances where commands are used incorrectly:

```sh
grep '*foo*' file                 # Globs in regex contexts
find . -exec foo {} && bar {} \;  # Prematurely terminated find -exec
sudo echo 'Var=42' > /etc/profile # Redirecting sudo
time --format=%s sleep 10         # Passing time(1) flags to time builtin
while read h; do ssh "$h" uptime  # Commands eating while loop input
alias archive='mv $1 /backup'     # Defining aliases with arguments
tr -cd '[a-zA-Z0-9]'              # [] around ranges in tr
exec foo; echo "Done!"            # Misused 'exec'
find -name \*.bak -o -name \*~ -delete  # Implicit precedence in find
