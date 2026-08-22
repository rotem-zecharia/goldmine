# projectdiscovery/httpx

httpx is a fast and multi-purpose HTTP toolkit that allows running multiple probes using the retryablehttp library.

## features

<h1 align="center">
  <img src="https://user-images.githubusercontent.com/8293321/135731750-4c1d38b1-bd2a-40f9-88e9-3c4b9f6da378.png" alt="httpx" width="700px">
  <br>
</h1>

 - Simple and modular code base making it easy to contribute.
 - Fast And fully configurable flags to probe multiple elements.
 - Supports multiple HTTP based probings.
 - Smart auto fallback from https to http by default. 
 - Supports hosts, URLs and CIDR as input.
 - Handles edge cases doing retries, backoffs etc for handling WAFs.

### Supported probes

| Probes          | Default check | Probes         | Default check |
|-----------------|---------------|----------------|---------------|
| URL             | true          | IP             | true          |
| Title           | true          | CNAME          | true          |
| Status Code     | true          | Raw HTTP       | false         |
| Content Length  | true          | HTTP2          | false         |
| TLS Certificate | true          | HTTP Pipeline  | false         |
| CSP Header      | true          | Virtual host   | false         |
| Line Count      | true          | Word Count     | true          |
| Location Header | true          | CDN            | false         |
| Web Server      | true          | Paths          | false         |
| Web Socket      | true          | Ports          | false         |
| Response Time   | true          | Request Method | true          |
| Favicon Hash    | false         | Probe  Status  | false         |
| Body Hash       | true          | Header  Hash   | true          |
| Redirect chain  | false         | URL Scheme     | true          |
| JARM Hash       | false         | ASN            | false         |

## installation

`httpx` requires **go >=1.25.0** to install successfully. Run the following command to get the repo:

```sh
go install -v github.com/projectdiscovery/httpx/cmd/httpx@latest
```

To learn more about installing httpx, see https://docs.projectdiscovery.io/tools/httpx/install.

| :exclamation:  **Disclaimer**  |
|---------------------------------|
| **This project is in active development**. Expect breaking changes with releases. Review the changelog before updating. |
| This project was primarily built to be used as a standalone CLI tool. **Running it as a service may pose security risks.** It's recommended to use with caution and additional security measures. |

## tools

```sh
httpx -h
```

This will display help for the tool. Here are all the switches it supports.


```console
httpx is a fast and multi-purpose HTTP toolkit that allows running multiple probes using the retryablehttp library.

Usage:
  ./httpx [flags]

Flags:
INPUT:
   -l, -list string              input file containing list of hosts to process
   -rr, -request string          file containing raw request
   -u, -target string[]          input target host(s) to probe
   -im, -input-mode string       mode of input file (burp)

PROBES:
   -sc, -status-code                      display response status-code
   -cl, -content-length                   display response content-length
   -ct, -content-type                     display response content-type
   -location                              display response redirect location
   -favicon                               display mmh3 hash for '/favicon.ico' file
   -hash string                           display response body hash (supported: md5,mmh3,simhash,sha1,sha256,sha512)
   -jarm                                  display jarm fingerprint hash
   -rt, -response-time                    display response time
   -lc, -line-count                       display response body line count
   -wc, -word-count                       display response body word count
   -title                                 display page title
   -bp, -body-preview                     display first N characters of response body (default 100)
   -server, -web-server                   display server name
   -td, -tech-detect                      display technology in use based on wappalyzer dataset
   -cff, -custom-fingerprint-file string  path to a custom fingerprint file for technology detection
   -method                                display http request method
   -ws, -websocket                        display server using websocket
   -ip                                    display host ip
   -cname                                 display host cname
   -extract-fqdn, -efqdn                  get domain and subdomains from response body and header in jsonl/csv output
   -asn                                   display host asn information
   -cdn                                   display cdn/waf in use (default true)
   -probe                                 display probe status

HEADLESS:
   -ss, -screenshot                 enable saving screenshot of the page using headless browser
   -system-chrome                   enable using local installed chrome for screenshot
   -ho, -headless-options string[]  start headless chrome with additional options
   -esb, -exclude-screenshot-bytes  enable excluding screenshot bytes from json output
   -ehb, -exclude-headless-body     enable excluding headless header from json output
   -no-screenshot-full-page         disable saving full page screenshot
   -st, -screenshot-timeout value   set timeout for screenshot in seconds (default 10s)
   -sid, -screenshot-idle value     set idle time before taking screenshot in seconds (default 1s)
   -jsc, -javascript-code string[]  execute JavaScript code after navigation

MATCHERS:
   -mc, -match-code string            match response with specified status code (-mc 200,302)
   -ml, -match-length string          match response with specified content length (-ml 100,102)
   -mlc, -match-line-count string     match response body with specified line count (-mlc 423,532)
   -mwc, -match-word-count string     match response body with specified word count (-mwc 43,55)
   -mfc, -match-favicon string[]      match response with specified favicon hash (-mfc 1494302000)
   -ms, -match-string string[]        match response with specified string (-ms admin)
   -mr, -match-regex string[]         match response with specified regex (-mr admin)
   -mcdn, -match-cdn string[]         match host with specified cdn provider (cloudfront, fastly, google, etc.)
   -mrt, -match-response-time string  match response with specified response time in seconds (-mrt 
