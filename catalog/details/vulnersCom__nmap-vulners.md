# vulnersCom/nmap-vulners

Nmap NSE scripts that turn a service scan into CVEs, CVSS scores and known exploits — fingerprints software from HTTP responses and checks every detected CPE against the Vulners database.

## features

nmap already tells you **what software** is listening on a port. This tells you
**what is wrong with it**.

You run one command. For every open port, the script takes the software nmap
identified, asks vulners.com what is known about it, and prints the answer
under that port - ordered so the things people are actually being attacked with
come first, rather than merely the things with the highest score.

It works with no account and no API key. A free key makes each answer richer,
and [With a key and without](#with-a-key-and-without) shows exactly how, with
the same scan run both ways.

## installation

**macOS, Linux, Kali, WSL** - one line, no arguments:

```sh
curl -fsSL https://raw.githubusercontent.com/vulnersCom/nmap-vulners/master/install.sh | sh
```

**Windows** - PowerShell as Administrator:

```powershell
irm https://raw.githubusercontent.com/vulnersCom/nmap-vulners/master/install.ps1 | iex
```

The installer asks nmap where it keeps its data, copies the script there,
rebuilds the script database, and then checks that `--script vulners` really
resolves to what it just installed - nmap ships a `vulners.nse` of its own, and
this replaces it. It also offers to store an API key, if you have one.

<details>
<summary><b>Without root, and other options</b></summary>

```sh

## configuration

All are passed with `--script-args`. A bare name works too, so
`--script-args mincvss=7` is enough.

**The ones you are likely to want:**

| Argument | Default | Meaning |
|---|---|---|
| `vulners.mincvss` | `0` | Hide findings scored below this. Unscored bulletins and anything with a known exploit are shown whatever the threshold |
| `vulners.width` | `80` | Terminal width the table is laid out for |
| `vulners.paths` | all 939 | Paths for the web sweep. `none` switches the sweep off; a Lua list, or one string naming a file with one path per line, replaces it. A file you name that cannot be read stops the sweep and says so, rather than quietly falling back to the published list |
| `vulners.max_items` | `32` | Ceiling on paid identifications for the whole scan. `0` disables spending entirely |

**Telling it about your key** - see [Where to keep the API
key](#where-to-keep-the-api-key) for which of these to prefer:

| Argument | Default | Meaning |
|---|---|---|
| `vulners.api_key_file` | - | Absolute path to a file whose first line is the token |
| `vulners.api_key` | - | The token itself. Leaky: nmap copies its own command line into `-oX` |

**Rarely needed:**

| Argument | Default | Meaning |
|---|---|---|
| `vulners.catalog_url` | GitHub | Fetch the fingerprint data from a mirror instead |
| `vulners.catalog` | fetch it | `none` to run with no web fingerprinting and no request for it |
| `vulners.api_host` | `vulners.com` | Host name of the API |
| `vulners.api_port` | `443` | Port on `api_host` |

The 1.x argument names still work for one release: `vulners_enterprise.*` for
the key, host, port and mincvss arguments, and `http-vulners-regex.paths` for
the sweep. Using one prints a deprecation notice naming its replacement.

## tools

```sh
