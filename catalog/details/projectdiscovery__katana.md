# projectdiscovery/katana

A next-generation crawling and spidering framework.

## features

![image](https://user-images.githubusercontent.com/8293321/199371558-daba03b6-bf9c-4883-8506-76497c6c3a44.png)

 - Fast And fully configurable web crawling
 - **Standard** and **Headless** mode
 - **JavaScript** parsing / crawling
 - Customizable **automatic form filling**
 - **Scope control** - Preconfigured field / Regex 
 - **Knowledge base** - ML page-type / form classification (auto-downloaded model)
 - **Customizable output** - Preconfigured fields
 - INPUT - **STDIN**, **URL** and **LIST**
 - OUTPUT - **STDOUT**, **FILE** and **JSON**

## installation

katana requires Go 1.26+ to install successfully. If you encounter any installation issues, we recommend trying with the latest available version of Go, as the minimum required version may have changed. Run the command below or download a pre-compiled binary from the [release page](https://github.com/projectdiscovery/katana/releases).

```console
CGO_ENABLED=1 go install github.com/projectdiscovery/katana/cmd/katana@latest
```

**More options to install / run katana-**

<details>
  <summary>Docker</summary>

> To install / update docker to latest tag -

```sh
docker pull projectdiscovery/katana:latest
```

> To run katana in standard mode using docker -


```sh
docker run projectdiscovery/katana:latest -u https://tesla.com
```

> To run katana in headless mode using docker -

```sh
docker run projectdiscovery/katana:latest -u https://tesla.com -system-chrome -headless
```

</details>

<details>
  <summary>Ubuntu</summary>

> It's recommended to install the following prerequisites -

```sh
sudo apt update
sudo apt install zip curl wget git snapd
sudo snap refresh
sudo snap install golang --classic

sudo install -d -m 0755 /etc/apt/keyrings
curl -fsSL https://dl.google.com/linux/linux_signing_key.pub \
  | sudo gpg --dearmor -o /etc/apt/keyrings/google-chrome.gpg

echo "deb [arch=amd64 signed-by=/etc/apt/keyrings/google-chrome.gpg] \
  http://dl.google.com/linux/chrome/deb/ stable main" \
  | sudo tee /etc/apt/sources.list.d/google-chrome.list > /dev/null

sudo apt update
sudo apt install google-chrome-stable
```

> install katana -


```sh
go install github.com/projectdiscovery/katana/cmd/katana@latest
```

</details>

## tools

```console
katana -h
```

This will display help for the tool. Here are all the switches it supports.

```console
Katana is a fast crawler focused on execution in automation
pipelines offering both headless and non-headless crawling.

Usage:
  ./katana [flags]

Flags:
INPUT:
   -u, -list string[]     target url / list to crawl
   -resume string         resume scan using resume.cfg
   -e, -exclude string[]  exclude host matching specified filter ('cdn', 'private-ips', cidr, ip, regex)

CONFIGURATION:
   -r, -resolvers string[]       list of custom resolver (file or comma separated)
   -d, -depth int                maximum depth to crawl (default 3)
   -jc, -js-crawl                enable endpoint parsing / crawling in javascript file
   -jsl, -jsluice                enable jsluice parsing in javascript file (memory intensive)
   -ct, -crawl-duration value    maximum duration to crawl the target for (s, m, h, d) (default s)
   -kf, -known-files string      enable crawling of known files (all,robotstxt,sitemapxml), a minimum depth of 3 is required to ensure all known files are properly crawled.
   -mrs, -max-response-size int  maximum response size to read (default 4194304)
   -timeout int                  time to wait for request in seconds (default 10)
   -aff, -automatic-form-fill    enable automatic form filling (experimental)
   -fx, -form-extraction         extract form, input, textarea & select elements in jsonl output
   -retry int                    number of times to retry the request (default 1)
   -proxy string                 http/socks5 proxy to use
   -td, -tech-detect             enable technology detection
   -H, -headers string[]         custom header/cookie to include in all http request in header:value format (file)
   -config string                path to the katana configuration file
   -fc, -form-config string      path to custom form configuration file
   -flc, -field-config string    path to custom field configuration file
   -s, -strategy string          Visit strategy (depth-first, breadth-first) (default "depth-first")
   -iqp, -ignore-query-params    Ignore crawling same path with different query-param values
   -fsu, -filter-similar         filter crawling of similar looking URLs (e.g., /users/123 and /users/456)
   -fst, -filter-similar-threshold int  number of distinct values before a path position is treated as parameter (default 10)
   -tlsi, -tls-impersonate       enable experimental client hello (ja3) tls randomization
   -dr, -disable-redirects       disable following redirects (default false)
   -pcs, -page-content-similar   enable page content similarity filtering (simhash|tfidf|bm25)
   -pcsm, -page-content-similar-mode string  similarity mode: simhash, tfidf, or bm25 (default simhash)
   -pcsd, -page-content-similar-distance int  simhash max hamming distance (default 3)
   -pcst, -page-content-similar-threshold float  tfidf/bm25 min score 0-1 (default 0.85)
   -pcsn, -page-content-similar-budget int  pages to fully process per similarity cluster (default 1)
   -sdd, -similarity-deduplication  alias for -pcs
   -kb, -knowledge-base          enable knowledge base classification
   -kb-secrets                   enable secrets extractor in the knowledge base
   -kb-validate-secrets          validate detected secrets against their provider (sends live API calls)
   -kb-endpoints                 enable endpoints extractor (classifies REST/GraphQL/SOAP/XHR requests)
   -mdp, -max-domain-pages int   maximum number of pages to crawl per domain (default unlimited)

DEBUG:
   -health-check, -hc        run diagnostic check up
   -elog, -error-log string  file to write sent requests error log
   -pprof-server             enable pprof server

HEADLESS:
   -hl, -headless                    enable headless hybrid crawling (experimental)
   -sc, -system-chrome               use local installed chrome browser instead of katana installed
   -sb, -show-browser                show the browser on the screen wit

## configuration

Katana comes with multiple options to configure and control the crawl as the way we want.

*`-depth`*
----

Option to define the `depth` to follow the urls for crawling, the more depth the more number of endpoint being crawled + time for crawl.

```
katana -u https://tesla.com -d 5
```

*`-js-crawl`*
----

Option to enable JavaScript file parsing + crawling the endpoints discovered in JavaScript files, disabled as default.

```
katana -u https://tesla.com -jc
```

*`-crawl-duration`*
----

Option to predefined crawl duration, disabled as default.

```
katana -u https://tesla.com -ct 2
```

*`-known-files`*
----
Option to enable crawling `robots.txt` and `sitemap.xml` file, disabled as default.

```
katana -u https://tesla.com -kf robotstxt,sitemapxml
```

*`-automatic-form-fill`*
----

Option to enable automatic form filling for known / unknown fields, known field values can be customized as needed by updating form config file at `$HOME/.config/katana/form-config.yaml`.

Automatic form filling is experimental feature.

```
katana -u https://tesla.com -aff
```

Form config values support DSL helper functions for dynamic data generation. All `rand_*` functions from the [projectdiscovery/dsl](https://github.com/projectdiscovery/dsl) library are available:

```yaml
# $HOME/.config/katana/form-config.yaml
email: "rand_email()"
phone: "rand_phone()"
placeholder: "rand_first_name()"
password: 'rand_base(16, "")'
color: "#e66465"
```

*`-filter-similar`*
----

Option to filter crawling of similar looking URLs by normalizing variable path segments. This detects IDs, UUIDs, hashes, dates, and other dynamic values, and also learns repeating patterns at runtime. For example, `/users/123` and `/users/456` are treated as the same endpoint.

```
katana -u https://tesla.com -fsu
```

The promotion threshold (how many distinct values at a path position before it's treated as a parameter) can be tuned with `-fst`. Lower values are more aggressive (fewer URLs crawled), higher values are more permissive. Default is `10`.

```
katana -u https://tesla.com -fsu -fst 5
```

*`-max-domain-pages`*
----

Option to limit the number of pages crawled per domain. Prevents any single domain from consuming the entire crawl budget, useful for large sites or crawler trap protection.

```
katana -u https://tesla.com -mdp 100
```

## Knowledge Base Classification

Katana can enrich crawl results with a **knowledge base** — machine-learning classification of each crawled page powered by [dit](https://github.com/HappyHackingSpace/dit). When enabled, every response is classified by **page type** (e.g. `login`, `error`, `captcha`, `parked`) and any forms on the page are identified, with the result attached to the `knowledgebase` field of the JSONL output. This works across **all engines** (standard and headless).

> **Note**: The classification model is **downloaded automatically** on first use to `~/.dit/model.json` (from [Hugging Face](https://huggingface.co/datasets/happyhackingspace/dit)). This is a one-time, per-machine cost — subsequent runs reuse the cached model. No manual installation of `dit` is required.

*`-knowledge-base`*
----

Enable knowledge base classification. Page-type and form classification is added to the `knowledgebase` field of each result.

```console
katana -u https://example.com -kb -jsonl
```

```json
{
  "timestamp": "...",
  "request": { "...": "..." },
  "response": {
    "...": "...",
    "knowledgebase": {
      "PageType": "login",
      "Forms": [{ "type": "login", "fields": { "username": "username or email", "password": "password" } }]
    }
  }
}
```

*`-filter-page-type`*
----

Filter results to only the given page type(s). Enabling this implies `-kb` (the classifier is initialized automatically).

```console
katana -u https://example.com -fpt login,error
```

*`-kb-secrets`*
----

Enable the secrets extractor in the knowledge base, surfacing detected secrets (API keys, tokens, etc.) under the `secrets` key. Add `-kb-validate-se
