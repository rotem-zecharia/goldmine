# wader/fq

fq - jq for binary formats. Tool, language and decoders for working with binary formats.

## installation

Use one of the methods listed below or download a pre-built [release](https://github.com/wader/fq/releases) for macOS, Linux or Windows. Unarchive it and move the executable to `PATH` etc.

On macOS if you don't install using one of the method below then you might have to manually allow the binary to run. This can be done by trying to run the binary, ignore the warning and then go into security preference and allow it. Same can be done with these commands:

```sh
xattr -d com.apple.quarantine fq
# for macOS version before Sequoia you might need this also
spctl --add fq
```

### Homebrew (macOS)

```sh
brew install wader/tap/fq
```

### MacPorts

On macOS, `fq` can also be installed via [MacPorts](https://www.macports.org).  More details [here](https://ports.macports.org/port/fq/).

```sh
sudo port install fq
```

### Windows

`fq` can be installed via [scoop](https://scoop.sh/).

```powershell
scoop install fq
```

### Arch Linux

`fq` can be installed from the [extra repository](https://archlinux.org/packages/extra/x86_64/fq/) using [pacman](https://wiki.archlinux.org/title/Pacman):

```sh
pacman -S fq
```

You can also build and install the development (VCS) package using an [AUR helper](https://wiki.archlinux.org/index.php/AUR_helpers):

```sh
paru -S fq-git
```

### Gentoo

`fq` can be installed from the Gentoo package repository using `emerge`:

```sh
emerge dev-util/fq
```

### Guix

```sh
guix shell fq -- fq --help # in develompen shell
guix install fq            # into current profile
```

### Nix

```sh
nix-shell -p fq
```

### FreeBSD

Use the [fq](https://cgit.freebsd.org/ports/tree/misc/fq) port.

### Alpine

Currently in edge testing but should work fine in stable also.

```
apk add -X http://dl-cdn.alpinelinux.org/alpine/edge/testing fq
```

### Build from source

Make sure you have [go](https://go.dev) 1.22 or later installed.

To install directly from git repository (no git clone needed):
```sh
# build and install latest release
go install github.com/wader/fq@latest

# build and install latest master
go install github.com/wader/fq@master

# copy binary to $PATH if needed
cp "$(go env GOPATH)/bin/fq" /usr/local/bin
```

To build, run and test from source:
```sh
# build and run
go run .
# build and run with arguments
go run . -d mp3 . file.mp3
# just build
go build -o fq .
# run all tests and build binary
make test fq
```

## Development and adding a new decoder

See [dev.md](doc/dev.md)

## Thanks and related projects

This project would not have been possible without [itchyny](https://github.com/itchyny)'s
jq implementation [gojq](https://github.com/itchyny/gojq). I also want to thank
[HexFiend](https://github.com/HexFiend/HexFiend) for inspiration and ideas and [stedolan](https://github.com/stedolan)
for inventing the [jq](https://github.com/stedolan/jq) language.

### Similar or related works

#### Tools

- [HexFiend](https://github.com/HexFiend/HexFiend) - Hex editor for macOS with format template support.
- [ImHex](https://github.com/WerWolv/ImHex) - A Hex Editor for Reverse Engineers.
- [binspector](https://github.com/binspector/binspector) - Binary format analysis tool with query language and REPL.
- [kaitai](https://kaitai.io) - Declarative binary format parsing.
- [Wireshark](https://www.wireshark.org) - Decodes network traffic (tip: `tshark -T json`).
- [MediaInfo](https://mediaarea.net/en/MediaInfo) - Analyze media files  (tip `mediainfo --Output=JSON` and `mediainfo --Details=1`).
- [GNU poke](https://www.jemarch.net/poke) - The extensible editor for structured binary data.
- [ffmpeg/ffprobe](https://ffmpeg.org) - Powerful media libraries and tools.
- [hexdump](https://git.kernel.org/pub/scm/utils/util-linux/util-linux.git/tree/text-utils/hexdump.c) - Hex viewer tool.
- [hex](https://git.janouch.name/p/hex) - Interactive hex viewer with format support via lua.
- [hachoir](https://github.com/vstinner/hachoir) - General python library for working binary data.
- [scapy](https://scapy.net) - Decode/Encod
