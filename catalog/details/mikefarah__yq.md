# mikefarah/yq

yq is a portable command-line YAML, JSON, XML, CSV, TOML, HCL and properties processor

## tools

podman run --rm -v "${PWD}":/workdir mikefarah/yq '.a.b[0].c' file.yaml
```

**Security note:** You can run `yq` in Docker with restricted privileges:
```bash
docker run --rm --security-opt=no-new-privileges --cap-drop all --network none \
  -v "${PWD}":/workdir mikefarah/yq '.a.b[0].c' file.yaml
```

#### Pipe data via STDIN:

You'll need to pass the `-i --interactive` flag to Docker/Podman:

```bash

## installation

```
go install github.com/mikefarah/yq/v4@latest
```

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
