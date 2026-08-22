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
