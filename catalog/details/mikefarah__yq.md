# mikefarah/yq

yq is a portable command-line YAML, JSON, XML, CSV, TOML, HCL and properties processor

## tools

### Basic Operations

**Read a value:**
```bash
yq '.a.b[0].c' file.yaml
```

**Pipe from STDIN:**
```bash
yq '.a.b[0].c' < file.yaml
```

**Update a yaml file in place:**
```bash
yq -i '.a.b[0].c = "cool"' file.yaml
```

**Update using environment variables:**
```bash
NAME=mike yq -i '.a.b[0].c = strenv(NAME)' file.yaml
```

### Advanced Operations

**Merge multiple files:**
```bash
# merge two files
yq -n 'load("file1.yaml") * load("file2.yaml")'

# merge using globs (note: `ea` evaluates all files at once instead of in sequence)
yq ea '. as $item ireduce ({}; . * $item )' path/to/*.yml
```

**Multiple updates to a yaml file:**
```bash
yq -i '
  .a.b[0].c = "cool" |
  .x.y.z = "foobar" |
  .person.name = strenv(NAME)
' file.yaml
```

**Find and update an item in an array:**
```bash
# Note: requires input file - add your file at the end
yq -i '(.[] | select(.name == "foo") | .address) = "12 cat st"' data.yaml
```

**Convert between formats:**
```bash
# Convert JSON to YAML (pretty print)
yq -Poy sample.json

# Convert YAML to JSON
yq -o json file.yaml

# Convert XML to YAML
yq -o yaml file.xml
```

See [recipes](https://mikefarah.gitbook.io/yq/recipes) for more examples and the [documentation](https://mikefarah.gitbook.io/yq/) for more information.

Take a look at the discussions for [common questions](https://github.com/mikefarah/yq/discussions/categories/q-a), and [cool ideas](https://github.com/mikefarah/yq/discussions/categories/show-and-tell)

## installation

### [Download the latest binary](https://github.com/mikefarah/yq/releases/latest)

### wget
Use wget to download pre-compiled binaries. Choose your platform and architecture:

**For Linux (example):**
```bash
# Set your platform variables (adjust as needed)
VERSION=v4.2.0
PLATFORM=linux_amd64

# Download compressed binary
wget https://github.com/mikefarah/yq/releases/download/${VERSION}/yq_${PLATFORM}.tar.gz -O - |\
  tar xz && sudo mv yq_${PLATFORM} /usr/local/bin/yq

# Or download plain binary
wget https://github.com/mikefarah/yq/releases/download/${VERSION}/yq_${PLATFORM} -O /usr/local/bin/yq &&\
    chmod +x /usr/local/bin/yq
```

**Latest version (Linux AMD64):**
```bash
wget https://github.com/mikefarah/yq/releases/latest/download/yq_linux_amd64 -O /usr/local/bin/yq &&\
    chmod +x /usr/local/bin/yq
```

**Available platforms:** `linux_amd64`, `linux_arm64`, `linux_arm`, `linux_386`, `darwin_amd64`, `darwin_arm64`, `windows_amd64`, `windows_386`, etc.

### MacOS / Linux via Homebrew:
Using [Homebrew](https://brew.sh/)
```
brew install yq
```

### Linux via snap:
```
snap install yq
```

#### Snap notes
`yq` installs with [_strict confinement_](https://docs.snapcraft.io/snap-confinement/6233) in snap, this means it doesn't have direct access to root files. To read root files you can:

```
sudo cat /etc/myfile | yq '.a.path'
```

And to write to a root file you can either use [sponge](https://linux.die.net/man/1/sponge):
```
sudo cat /etc/myfile | yq '.a.path = "value"' | sudo sponge /etc/myfile
```
or write to a temporary file:
```
sudo cat /etc/myfile | yq '.a.path = "value"' | sudo tee /etc/myfile.tmp
sudo mv /etc/myfile.tmp /etc/myfile
rm /etc/myfile.tmp
```

### Run with Docker or Podman

#### One-time use:
```bash
# Docker - process files in current directory
docker run --rm -v "${PWD}":/workdir mikefarah/yq '.a.b[0].c' file.yaml

## features

- [Detailed documentation with many examples](https://mikefarah.gitbook.io/yq/)
- Written in portable go, so you can download a lovely dependency free binary
- Uses similar syntax as `jq` but works with YAML, INI, [JSON](https://mikefarah.gitbook.io/yq/usage/convert) and [XML](https://mikefarah.gitbook.io/yq/usage/xml) files
- Fully supports multi document yaml files
- Supports yaml [front matter](https://mikefarah.gitbook.io/yq/usage/front-matter) blocks (e.g. jekyll/assemble)
- Colorized yaml output
- [Date/Time manipulation and formatting with TZ](https://mikefarah.gitbook.io/yq/operators/datetime)
- [Deep data structures](https://mikefarah.gitbook.io/yq/operators/traverse-read)
- [Sort keys](https://mikefarah.gitbook.io/yq/operators/sort-keys)
- Manipulate yaml [comments](https://mikefarah.gitbook.io/yq/operators/comment-operators), [styling](https://mikefarah.gitbook.io/yq/operators/style), [tags](https://mikefarah.gitbook.io/yq/operators/tag) and [anchors and aliases](https://mikefarah.gitbook.io/yq/operators/anchor-and-alias-operators).
- [Update in place](https://mikefarah.gitbook.io/yq/v/v4.x/commands/evaluate#flags)
- [Complex expressions to select and update](https://mikefarah.gitbook.io/yq/operators/select#select-and-update-matching-values-in-map)
- Keeps yaml formatting and comments when updating (though there are issues with whitespace)
- [Decode/Encode base64 data](https://mikefarah.gitbook.io/yq/operators/encode-decode)
- [Load content from other files](https://mikefarah.gitbook.io/yq/operators/load)
- [Convert to/from json/ndjson](https://mikefarah.gitbook.io/yq/v/v4.x/usage/convert)
- [Convert to/from xml](https://mikefarah.gitbook.io/yq/v/v4.x/usage/xml)
- [Convert to/from hcl (terraform)](https://mikefarah.gitbook.io/yq/v/v4.x/usage/hcl)
- [Convert to/from toml](https://mikefarah.gitbook.io/yq/v/v4.x/usage/toml)
- [Convert to/from properties](https://mikefarah.gitbook.io/yq/v/v4.x/usage/properties)
- [Convert to/from csv/tsv](https://mikefarah.gitbook.io/yq/usage/csv-tsv)
- [General shell completion scripts (bash/zsh/fish/powershell)](https://mikefarah.gitbook.io/yq/v/v4.x/commands/shell-completion)
- [Reduce](https://mikefarah.gitbook.io/yq/operators/reduce) to merge multiple files or sum an array or other fancy things.
- [Github Action](https://mikefarah.gitbook.io/yq/usage/github-action) to use in your automated pipeline (thanks @devorbitus)
