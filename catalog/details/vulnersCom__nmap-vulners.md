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
# into ~/.nmap, no sudo; the installer prints the NMAPDIR line to add to your profile
curl -fsSL https://raw.githubusercontent.com/vulnersCom/nmap-vulners/master/install.sh | sh -s -- --user

# a specific directory
./install.sh --prefix /usr/local/share/nmap

# a specific release
./install.sh --ref v2.0

# remove everything it installed
./install.sh --uninstall
```

PowerShell takes the same options: `-User`, `-Prefix`, `-Ref`, `-Uninstall`.

</details>

<details>
<summary><b>From a checkout</b></summary>

```sh
git clone https://github.com/vulnersCom/nmap-vulners
cd nmap-vulners
./install.sh
```

The installer uses the files next to it, so this installs exactly what you
cloned. Running the script straight out of the checkout works too:

```sh
nmap -sV --script "$PWD/vulners.nse" <target>
```

> Use an **absolute** path when running from a checkout. nmap resolves a
> relative `--script ./vulners.nse` against its own `script.db` first, and
> quietly runs the copy that shipped with nmap instead of yours.

</details>

<details>
<summary><b>By hand</b></summary>

One file: copy `vulners.nse` into `<nmap data dir>/scripts/` and run
`sudo nmap --script-updatedb`. There is nothing else to place - the script
downloads its fingerprint data at scan time and writes nothing to disk - and so
nothing to forget, which used to produce a script that ran, found nothing, and
said nothing about why.

If you are upgrading from 1.x, delete `vulners_enterprise.nse` and
`http-vulners-regex.nse` from that directory as well. A leftover
`http-vulners-regex.nse` still carries the `default` category and keeps sweeping
targets under a plain `-sC`. The installer does this for you.

The nmap data directory is usually `/usr/share/nmap` (Debian, Ubuntu, Kali),
`/usr/local/share/nmap` (built from source), `/opt/homebrew/share/nmap`
(Homebrew) or `C:\Program Files (x86)\Nmap` (Windows). To be certain, ask nmap:

```sh
nmap -d2 --script-help probe 2>&1 | grep nse_main.lua
```

The directory holding `nse_main.lua` is the one this nmap uses.

</details>

## Your first scan

```sh
nmap -sV --script vulners scanme.nmap.org
```

That is the whole interface. Two parts of it matter:

* **`-sV` is not optional.** It is the flag that makes nmap work out which
  software is behind each port. Without it nmap reports "port 80 is open" and
  nothing more - there is no software to ask about, and this script has nothing
  to do. This is the single most common reason for an empty result.
* **`--script vulners`** runs the script. It is deliberately not in nmap's
  `default` set, so a plain `-sC` will not run it: sending the identity of your
  target's software to a third party should be something you asked for.

You get your usual nmap report, with a block added under each port that has
something known against it.

## Reading the output

The first line of the block is nmap's own; everything indented under it is this
script. Here is the shape, with three of its rows:

```
80/tcp    open  http    Apache httpd 2.4.7 ((Ubuntu))
| vulners: cpe:/a:apache:http_server:2.4.7  272 findings, 56 exploitable
|   SEVERITY  CVSS    AI  FLAGS    LINK
|   ========  ====  ====  =======  ==============================================================
|   CRITICAL  10.0   8.8  EXP      https://vulners.com/gitee/3E6BA608-776F-5B

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
# only findings scored 7.0 and above
nmap -sV --script vulners --script-args mincvss=7 <target>

# no web sweep - just look up what nmap itself identified
nmap -sV --script vulners --script-args vulners.paths=none <target>

# never spend a credit, whatever the scan turns up
nmap -sV --script vulners --script-args vulners.max_items=0 <target>

# quiet on the target, and patient
nmap -sV -T2 --script vulners <target>

# a wider terminal, and every finding rather than the top ten
nmap -sV --script vulners --script-args vulners.width=140 -v <target>
```

## Where to keep the API key

There are four places the script will find a key. They differ in how safe they
are, and - separately - in which one wins when you have more than one. Those
two orders are opposites, so they are worth reading together:

| Where | How safe | Wins over |
|---|---|---|
| `~/.nmap/vulners.key`, one line, mode 600 | **safest** - never on a command line, never in a report. The installer offers to write it for you | nothing; it is the last resort |
| `VULNERS_API_KEY` in the environment | safe, but inherited by whatever else you launch from that shell | the key file |
| `--script-args vulners.api_key_file=/absolute/path` | safe; only the *path* is on the command line | the environment |
| `--script-args vulners.api_key=<token>` | **leaky** - see below | everything |

Read the table downwards for what to choose, and upwards for what wins. The
most explicit setting takes precedence, which is what you want when you are
overriding a stored key for one scan - and it is exactly why the most explicit
one is also the most exposed.

**Why the last row is leaky:** nmap copies its own command line into every
report, so a token passed that way ends up in the `args` attribute of `-oX`
output and in your shell history. It is fine for a throwaway test and wrong for
anything recorded.

The script itself never writes the token anywhere, including its debug output -
there are regression tests that say so, in the offline suite and against the
live service.

A key file you name explicitly and that cannot be read stops the run rather
than quietly falling back - an operator who names a file means that file - and
the report says which file it was. A mistyped path cannot look like a clean
scan.

## Machine-readable output

Everything printed is also structured, so `-oX` can be parsed without touching
the human text. The script id, the two table levels and the five original
element keys are unchanged from 1.x, which is what DefectDojo, Faraday,
nmap2csv and raven read:

```xml
<script id="vulners">
  <elem key="schema">2.0</elem>
  <elem key="mode">keyed</elem>
  <table key="cpe:/a:apache:http_server:2.4.7">
    <table>
      <elem key="id">CVE-2021-40438</elem>
      <elem key="type">cve</elem>
      <elem key="severity">CRITICAL</elem>
      <elem key="cvss">9.0</elem>
      <elem key="cvss_type">cvss3.1</elem>
      <elem key="is_exploit">false</elem>
      <elem key="exploit_known">true</elem>
      <elem key="kev">true</elem>
      <elem key="epss">0.99612</elem>
      <elem key="exploitation">active</elem>
      <elem key="title">Apache HTTP Server SSRF in mod_proxy</elem>
      <elem key="href">https://vulners.com/cve/CVE-2021-40438</elem>
      <elem key="source_href">https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2021-40438</elem>
    </table>
  </table>
</script>
```

`mode` says which way the scan ran - `free` or `keyed` - so a report can be
read without guessing which fields to expect.

New in 2.0: `schema`, `mode`, `severity`, `exploit_known`, `kev`, `epss`,
`epss_percentile`, `exploitation`, `ai_score`, `title`, `published`, `href`,
`source_href` and `found_on`. Every one is present-or-absent, never empty.
Nothing is nested more deeply than before, because a third table level is
invisible to every importer examined.

`href` is always the vulners.com page for the finding, in both modes. The
endpoint's own `href` is the **upstream** address - nvd.nist.gov for 
