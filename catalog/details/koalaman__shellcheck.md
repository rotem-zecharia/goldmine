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
# Or :v0.4.7 for that version, or :latest for daily builds
```

or use `koalaman/shellcheck-alpine` if you want a larger Alpine Linux based image to extend. It works exactly like a regular Alpine image, but has shellcheck preinstalled.

Using the [nix package manager](https://nixos.org/nix):
```sh
nix-env -iA nixpkgs.shellcheck
```

Using the [Flox package manager](https://flox.dev/)
```sh
flox install shellcheck
```

Alternatively, you can download pre-compiled binaries for the latest release here:

* [Linux, x86_64](https://github.com/koalaman/shellcheck/releases/download/stable/shellcheck-stable.linux.x86_64.tar.xz) (statically linked)
* [Linux, armv6hf](https://github.com/koalaman/shellcheck/releases/download/stable/shellcheck-stable.linux.armv6hf.tar.xz), i.e. Raspberry Pi (statically linked)
* [Linux, aarch64](https://github.com/koalaman/shellcheck/releases/download/stable/shellcheck-stable.linux.aarch64.tar.xz) aka ARM64 (statically linked)
* [macOS, aarch64](https://github.com/koalaman/shellcheck/releases/download/stable/shellcheck-stable.darwin.aarch64.tar.xz)
* [macOS, x86_64](https://github.com/koalaman/shellcheck/releases/download/stable/shellcheck-stable.darwin.x86_64.tar.xz)
* [Windows, x86](https://github.com/koalaman/shellcheck/releases/download/stable/shellcheck-stable.zip)

or see the [GitHub Releases](https://github.com/koalaman/shellcheck/releases) for other releases
(including the [latest](https://github.com/koalaman/shellcheck/releases/tag/latest) meta-release for daily git builds).

There are currently no official binaries for Apple Silicon, but third party builds are available via
[ShellCheck for Visual Studio Code](https://github.com/vscode-shellcheck/shellcheck-binaries/releases).

Distro packages already come with a `man` page. If you are building from source, it can be installed with:

```console
pandoc -s -f markdown-smart -t man shellcheck.1.md -o shellcheck.1
sudo mv shellcheck.1 /usr/share/man/man1
```

### pre-commit

To run ShellCheck via [pre-commit](https://pre-commit.com/), add the hook to your `.pre-commit-config.yaml`:

```
repos:
-   repo: https://github.com/koalaman/shellcheck-precommit
    rev: v0.11.0
    hooks:
    -   id: shellcheck
#       args: ["--severity=warning"]  # Optionally only show errors and warnings
```

### Travis CI

Travis CI has now integrate

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
# find . -exec foo > bar \;       # Redirections in find
f() { whoami; }; sudo f           # External use of internal functions
```

### Common beginner's mistakes

ShellCheck recognizes many common beginner's syntax errors:

```sh
var = 42                          # Spaces around = in assignments
$foo=42                           # $ in assignments
for $var in *; do ...             # $ in for loop variables
var$n="Hello"                     # Wrong indirect assignment
echo ${var$n}                     # Wrong indirect reference
var=(1, 2, 3)                     # Comma separated arrays
array=( [index] = value )         # Incorrect index initialization
echo $var[14]                     # Missing {} in array references
echo "Argument 10 is $10"         # Positional parameter misreference
if $(myfunction); then ..; fi     # Wrapping commands in $()
else if othercondition; then ..   # Using 'else if'
f; f() { echo "hello world; }     # Using function before definition
[ false ]                         # 'false' being true
if ( -f file )                    # Using (..) instead of test
```

### Style

ShellCheck can make suggestions to improve style:

```sh
[[ -z $(find /tmp | grep mpg) ]]  # Use grep -q instead
a >> log; b >> log; c >> log      # Use a redirection block instead
echo "The time is `date`"         # Use $() instead
cd dir; process *; cd ..;         # Use subshells instead
echo $[1+2]                       # Use standard $((..)) instead of old $[]
echo $(($RANDOM % 6))             # Don't use $ on variables in $((..))
echo "$(date)"                    # Useless use of echo
cat file | grep foo               # Useless use of cat
```

### Data and typing errors

ShellCheck can recognize issues related to data and typing:

```sh
args="$@"                         # Assigning arrays to strings
files=(foo bar); echo "$files"    # Referencing arrays as strings
declare -A arr=(foo bar)          # Associative arrays without index
printf "%s\n" "Arguments: $@."    # Concatenating strings and arrays
[[ $# > 2 ]]                      # Comparing numbers as strings
var=World; echo "Hello " var      # Unused lowercase variables
echo "Hello $name"                # Unassigned lowercase variables
cmd | read bar; echo $bar         # Assignments in subshells
cat foo | cp bar                  # Piping to commands that don't read
printf '%s: %s\n' foo             # Mismatches in printf argument count
eval "${array[@]}"                # Lost word boundaries in array eval
for i in "${x[@]}"; do ${x[$i]}   # Using array value as key
```

### Robustness

ShellCheck can make suggestions for improving the robustness of a script:

```sh
rm -rf "$STEAMROOT/"*            # Catastrophic rm
touch ./-l; ls *                 # Globs that could become options
find . -exec sh -c 'a && b {}' \; # Find -exec shell injection
printf "Hello $name"             # Variables in printf format
for f in $(ls *.txt); do         # Iterating over ls output
export MYVAR=$(cmd)              # Masked exit codes
case $version in 2.*) :;; 2.6.*) # Shadowed case branches
```

### Portability

ShellCheck will warn when using features not supported by the shebang. For example, if you set the shebang to `#!/bin/sh`, ShellCheck will warn about portability issues similar to `checkbashisms`:

```sh
echo {1..$n}                     # Works i
