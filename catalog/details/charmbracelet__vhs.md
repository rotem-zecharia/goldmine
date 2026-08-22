# charmbracelet/vhs

Your CLI home video recorder 📼

## installation

> [!NOTE]
> VHS requires [`ttyd`](https://github.com/tsl0922/ttyd) and [`ffmpeg`](https://ffmpeg.org) to be installed and available on your `PATH`.

Use a package manager:

```sh
# macOS or Linux
brew install vhs

# Arch Linux (btw)
pacman -S vhs

# Nix
nix-env -iA nixpkgs.vhs

# Windows using scoop
scoop install vhs
```

Or, use Docker to run VHS directly, dependencies included:

```sh
docker run --rm -v $PWD:/vhs ghcr.io/charmbracelet/vhs <cassette>.tape
```

Or, download it:

- [Packages][releases] are available in Debian and RPM formats
- [Binaries][releases] are available for Linux, macOS, and Windows

Or, just install it with `go`:

```sh
go install github.com/charmbracelet/vhs@latest
```

<details>
<summary>Windows, Debian, Ubuntu, Fedora, RHEL, Void Instructions</summary>

- Debian / Ubuntu

```sh
# Debian/Ubuntu
sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://repo.charm.sh/apt/gpg.key | sudo gpg --dearmor -o /etc/apt/keyrings/charm.gpg
echo "deb [signed-by=/etc/apt/keyrings/charm.gpg] https://repo.charm.sh/apt/ * *" | sudo tee /etc/apt/sources.list.d/charm.list
# Install ttyd from https://github.com/tsl0922/ttyd/releases
sudo apt update && sudo apt install vhs ffmpeg
```

- Fedora / RHEL

```sh
echo '[charm]
name=Charm
baseurl=https://repo.charm.sh/yum/
enabled=1
gpgcheck=1
gpgkey=https://repo.charm.sh/yum/gpg.key' | sudo tee /etc/yum.repos.d/charm.repo
# Install ttyd from https://github.com/tsl0922/ttyd/releases
sudo yum install vhs ffmpeg
```

- Void

```sh
sudo xbps-install vhs
```

- Windows

```sh
winget install charmbracelet.vhs
# or scoop
scoop install vhs
```

</details>

[releases]: https://github.com/charmbracelet/vhs/releases

## Record Tapes

VHS has the ability to generate tape files from your terminal actions!

To record to a tape file, run:

```bash
vhs record > cassette.tape
```

Perform any actions you want and then `exit` the terminal session to stop
recording. You may want to manually edit the generated `.tape` file to add
settings or modify actions. Then, you can generate the GIF:

```bash
vhs cassette.tape
```

## Publish Tapes

VHS allows you to publish your GIFs to our servers for easy sharing with your
friends and colleagues. Specify which file you want to share, then use the
`publish` sub-command to host it on `vhs.charm.sh`. The output will provide you
with links to share your GIF via browser, HTML, and Markdown.

```bash
vhs publish demo.gif
```

## The VHS Server

VHS has an SSH server built in! When you self-host VHS you can access it as
though it were installed locally. VHS will have access to commands and
applications on the host, so you don't need to install them on your machine.

To start the server run:

```sh
vhs serve
```

<details>
<summary>Configuration Options</summary>

- `VHS_PORT`: The port to listen on (`1976`)
- `VHS_HOST`: The host to listen on (`localhost`)
- `VHS_GID`: The Group ID to run the server as (current user's GID)
- `VHS_UID`: The User ID to run the server as (current user's UID)
- `VHS_KEY_PATH`: The path to the SSH key to use (`.ssh/vhs_ed25519`)
- `VHS_AUTHORIZED_KEYS_PATH`: The path to the authorized keys file (empty, publicly accessible)

</details>

Then, simply access VHS from a different machine via `ssh`:

```sh
ssh vhs.example.com < demo.tape > demo.gif
```

## VHS Command Reference

> [!NOTE]
> You can view all VHS documentation on the command line with `vhs manual`.

There are a few basic types of VHS commands:

- [`Output <path>`](#output): specify file output
- [`Require <program>`](#require): specify required programs for tape file
- [`Set <Setting> Value`](#settings): set recording settings
- [`Type "<characters>"`](#type): emulate typing
- [`Left`](#arrow-keys) [`Right`](#arrow-keys) [`Up`](#arrow-keys) [`Down`](#arrow-keys): arrow keys
- [`Backspace`](#backspace) [`Enter`](#enter) [`Tab`](#tab) [`Space`](#space): special keys
- [`ScrollUp`](#scroll-up--down) [`ScrollDown`](#scroll-up--down): scroll terminal viewport
- [`Ctrl[+Alt][+Shift]+<ch
