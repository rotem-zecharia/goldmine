# lissy93/web-check

🕵️‍♂️ All-in-one OSINT tool for analysing any website

## features

<details open>
<summary><b>Click to expand / collapse section</b></summary>

<sup>**Note** _this list needs updating, many more jobs have been added since..._</sup>

The following section outlines the core features, and briefly explains why this data might be useful for you to know, as well as linking to further resources for learning more.

<details>
<summary><b>IP Info</b></summary>

###### Description

An IP address (Internet Protocol address) is a numerical label assigned to each device connected to a network / the internet. The IP associated with a given domain can be found by querying the Domain Name System (DNS) for the domain's A (address) record.

###### Use Cases

Finding the IP of a given server is the first step to conducting further investigations, as it allows us to probe the server for additional info. Including creating a detailed map of a target's network infrastructure, pinpointing the physical location of a server, identifying the hosting service, and even discovering other domains that are hosted on the same IP address.

###### Useful Links

- [Understanding IP Addresses](https://www.digitalocean.com/community/tutorials/understanding-ip-addresses-subnets-and-cidr-notation-for-networking)
- [IP Addresses - Wiki](https://en.wikipedia.org/wiki/IP_address)
- [RFC-791 Internet Protocol](https://tools.ietf.org/html/rfc791)
- [whatismyipaddress.com](https://whatismyipaddress.com/)

</details>
<details>
<summary><b>SSL Chain</b></summary>

<img width="300" src="https://pixelflare.cc/alicia/web-check/wc-ssl" align="right" />

###### Description

SSL certificates are digital certificates that authenticate the identity of a website or server, enable secure encrypted communication (HTTPS), and establish trust between clients and servers. A valid SSL certificate is required for a website to be able to use the HTTPS protocol, and encrypt user + site data in transit. SSL certificates are issued by Certificate Authorities (CAs), which are trusted third parties that verify the identity and legitimacy of the certificate holder.

###### Use Cases

SSL certificates not only provide the assurance that data transmission to and from the website is secure, but they also provide valuable OSINT data. Information from an SSL certificate can include the issuing authority, the domain name, its validity period, and sometimes even organization details. This can be useful for verifying the authenticity of a website, understanding its security setup, or even for discovering associated subdomains or other services.

###### Useful Links

- [TLS - Wiki](https://en.wikipedia.org/wiki/Transport_Layer_Security)
- [What is SSL (via Cloudflare learning)](https://www.cloudflare.com/learning/ssl/what-is-ssl/)
- [RFC-8446 - TLS](https://tools.ietf.org/html/rfc8446)
- [SSL Checker](https://www.sslshopper.com/ssl-checker.html)

</details>
<details>
<summary><b>DNS Records</b></summary>

<img width="300" src="https://pixelflare.cc/alicia/web-check/wc-dns" align="right" />

###### Description

This task involves looking up the DNS records associated with a specific domain. DNS is a system that translates human-readable domain names into IP addresses that computers use to communicate. Various types of DNS records exist, including A (address), MX (mail exchange), NS (name server), CNAME (canonical name), and TXT (text), among others.

###### Use Cases

Extracting DNS records can provide a wealth of information in an OSINT investigation. For example, A and AAAA records can disclose IP addresses associated with a domain, potentially revealing the location of servers. MX records can give clues about a domain's email provider. TXT records are often used for various administrative purposes and can sometimes inadvertently leak internal information. Understanding a domain's DNS setup can also be useful in understanding how its online infrastructure is built and managed.

###### Useful Links

- [What are DNS records? (via Cloudflare learning)](https://www.cloudfla

## configuration

By default, no configuration is needed.

But there are some optional environmental variables that you can set to give you access to some additional checks, or to increase rate-limits for some checks that use external APIs.

**API Keys & Credentials**:

| Key                        | Value                                                                                                                                                 |
| -------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| `GOOGLE_CLOUD_API_KEY`     | A Google API key with the PageSpeed Insights API enabled ([get here](https://developers.google.com/speed/docs/insights/v5/get-started)). This can be used to return quality metrics for a site |
| `REACT_APP_SHODAN_API_KEY` | A Shodan API key ([get here](https://account.shodan.io/)). This will show associated host names for a given domain                                    |
| `REACT_APP_WHO_API_KEY`    | A WhoAPI key ([get here](https://whoapi.com/)). This will show more comprehensive WhoIs records than the default job                                  |

<details>
  <summary><small>Full / Upcoming Vals</small></summary>

- `GOOGLE_CLOUD_API_KEY` - A Google API key with the PageSpeed Insights API enabled ([get here](https://developers.google.com/speed/docs/insights/v5/get-started)). This can be used to return quality metrics for a site
- `REACT_APP_SHODAN_API_KEY` - A Shodan API key ([get here](https://account.shodan.io/)). This will show associated host names for a given domain
- `REACT_APP_WHO_API_KEY` - A WhoAPI key ([get here](https://whoapi.com/)). This will show more comprehensive WhoIs records than the default job
- `SECURITY_TRAILS_API_KEY` - A Security Trails API key ([get here](https://securitytrails.com/corp/api)). This will show org info associated with the IP
- `CLOUDMERSIVE_API_KEY` - API key for Cloudmersive ([get here](https://account.cloudmersive.com/)). This will show known threats associated with the IP
- `TRANCO_USERNAME` - A Tranco email ([get here](https://tranco-list.eu/)). This will show the rank of a site, based on traffic
- `TRANCO_API_KEY` - A Tranco API key ([get here](https://tranco-list.eu/)). This will show the rank of a site, based on traffic
- `URL_SCAN_API_KEY` - A URLScan API key ([get here](https://urlscan.io/)). This will fetch miscalanious info about a site
- `BUILT_WITH_API_KEY` - A BuiltWith API key ([get here](https://api.builtwith.com/)). This will show the main features of a site
- `TORRENT_IP_API_KEY` - A torrent API key ([get here](https://iknowwhatyoudownload.com/en/api/)). This will show torrents downloaded by an IP

</details>

**Configuration Settings**:

| Key                        | Value                                                                      |
| -------------------------- | -------------------------------------------------------------------------- |
| `PORT`                     | Port to serve the API, when running server.js (e.g. `3000`)                |
| `API_ENABLE_RATE_LIMIT`    | Enable rate-limiting for the /api endpoints (e.g. `true`)                  |
| `PUBLIC_API_TIMEOUT_LIMIT` | The timeout limit for API requests, in milliseconds (e.g. `25000`)         |
| `API_CORS_ORIGIN`          | Enable CORS, by setting your allowed hostname(s) here (e.g. `example.com`) |
| `API_DISABLED_CHECKS`      | Comma-separated list of checks to disable (e.g. `trace-route,ports`)       |
| `API_ENABLED_CHECKS`       | If set, only these checks will run (e.g. `get-ip,ssl,dns,headers`)         |
| `API_BLOCKED_HOSTS`        | Hosts that must never be scanned (e.g. `lan.example.com,192.168.0.0/16`)   |
| `CHROME_PATH`              | The path the Chromium executable (e.g. `/usr/bin/chromium`)                |
| `DISABLE_GUI`              | Disable the GUI, and only serve the API (e.g. `false`)                     |
| `REACT_APP_API_ENDPOI
