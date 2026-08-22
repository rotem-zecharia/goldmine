# dolthub/dolt

Dolt – Git for Data

## installation

Dolt is a single ~103 megabyte program. 

```bash
dolt $ du -h /Users/timsehn/go/bin/dolt
103M	/Users/timsehn/go/bin/dolt
```

It's really easy to install. Download it and put it on your `PATH`. 
We have a bunch of ways to make this even easier for most platforms.

## From Latest Release

To install on Linux or Mac based systems run this command in your
terminal:

```
sudo bash -c 'curl -L https://github.com/dolthub/dolt/releases/latest/download/install.sh | bash'
```

This will download the latest `dolt` release and put it in
`/usr/local/bin/`, which is probably on your `$PATH`.

The install script needs sudo in order to put `dolt` in `/usr/local/bin`. If you don't have root
privileges or aren't comfortable running a script with them, you can download the dolt binary
for your platform from [the latest release](https://github.com/dolthub/dolt/releases), unzip it,
and put the binary somewhere on your `$PATH`.

### Linux

#### Arch Linux

Dolt is packaged in the official repositories for Arch Linux.

```
pacman -S dolt
```

### Mac

#### Homebrew

Dolt is on Homebrew, updated every release.

```
brew install dolt
```
#### MacPorts

On macOS, Dolt can also be installed via a [community-managed port](https://ports.macports.org/port/dolt/) via [MacPorts](https://www.macports.org):

```sh
sudo port install dolt
```

### Windows

Download the latest Microsoft Installer (`.msi` file) in
[releases](https://github.com/dolthub/dolt/releases) and run
it.

For information on running on Windows, see [here](https://dolthub.com/docs/introduction/installation/windows).

#### Chocolatey

You can install `dolt` using [Chocolatey](https://chocolatey.org/):

```sh
choco install dolt
```

#### Docker

There are following official Docker images for Dolt:

* [`dolthub/dolt`](https://hub.docker.com/r/dolthub/dolt) for running Dolt
as CLI tool.
* [`dolthub/dolt-sql-server`](https://hub.docker.com/r/dolthub/dolt-sql-server) for running Dolt in server mode.

## From Source

Make sure you have Go installed, and that `go` is in your path. Dolt has a dependency on [cgo](https://pkg.go.dev/cmd/cgo), so you will need a working C compiler and toolchain as well.

Clone this repository and cd into the `go` directory. Then run:

```
go install ./cmd/dolt
```

The output will be in `$GOPATH/bin`, which defaults to `~/go/bin`. To test your build, try:

```
~/go/bin/dolt version
```

## configuration

Verify that your installation has succeeded by running `dolt` in your
terminal.

```
$ dolt
Valid commands for dolt are
[...]
```

Configure `dolt` with your user name and email, which you'll need to
create commits. The commands work exactly the same as git.

```
$ dolt config --global --add user.email YOU@DOMAIN.COM
$ dolt config --global --add user.name "YOUR NAME"
```
