# dgtlmoon/changedetection.io

Best and simplest tool for website change detection, web page monitoring, and website change alerts. Perfect for tracking content changes, price drops, restock alerts, and website defacement monitorin

## installation

### Docker

With Docker composer, just clone this repository and..

```bash
$ docker compose up -d
```

Docker standalone
```bash
$ docker run -d --restart always -p "127.0.0.1:5000:5000" -v datastore-volume:/datastore --name changedetection.io dgtlmoon/changedetection.io
```

`:latest` tag is our latest stable release, `:dev` tag is our bleeding edge `master` branch.

Alternative docker repository over at ghcr - [ghcr.io/dgtlmoon/changedetection.io](https://ghcr.io/dgtlmoon/changedetection.io)

### Windows

See the install instructions at the wiki https://github.com/dgtlmoon/changedetection.io/wiki/Microsoft-Windows

### Python Pip

Check out our pypi page https://pypi.org/project/changedetection.io/

```bash
$ pip3 install changedetection.io
$ changedetection.io -d /path/to/empty/data/dir -p 5000
```

Then visit http://127.0.0.1:5000 , You should now be able to access the UI.

_Now with per-site configurable support for using a fast built in HTTP fetcher or use a Chrome based fetcher for monitoring of JavaScript websites!_

## Updating changedetection.io

### Docker
```
docker pull dgtlmoon/changedetection.io
docker kill $(docker ps -a -f name=changedetection.io -q)
docker rm $(docker ps -a -f name=changedetection.io -q)
docker run -d --restart always -p "127.0.0.1:5000:5000" -v datastore-volume:/datastore --name changedetection.io dgtlmoon/changedetection.io
```

### docker compose

```bash
docker compose pull && docker compose up -d
```

See the wiki for more information https://github.com/dgtlmoon/changedetection.io/wiki

## Different browser viewport sizes (mobile, desktop etc)

If you are using the recommended `sockpuppetbrowser` (which is in the docker-compose.yml as a setting to be uncommented) you can easily set different viewport sizes for your web page change detection, [see more information here about setting up different viewport sizes](https://github.com/dgtlmoon/sockpuppetbrowser?tab=readme-ov-file#setting-viewport-size).

## Filters

XPath(1.0), JSONPath, jq, and CSS support comes baked in! You can be as specific as you need, use XPath exported from various XPath element query creation tools. 
(We support LXML `re:test`, `re:match` and `re:replace`.)

## Notifications

ChangeDetection.io supports a massive amount of notifications (including email, office365, custom APIs, etc) when a web-page has a change detected thanks to the <a href="https://github.com/caronc/apprise">apprise</a> library.
Simply set one or more notification URL's in the _[edit]_ tab of that watch.

Just some examples

    discord://webhook_id/webhook_token
    flock://app_token/g:channel_id
    gitter://token/room
    gchat://workspace/key/token
    msteams://TokenA/TokenB/TokenC/
    o365://TenantID:AccountEmail/ClientID/ClientSecret/TargetEmail
    rocket://user:password@hostname/#Channel
    mailto://user:pass@example.com?to=receivingAddress@example.com
    json://someserver.com/custom-api
    syslog://
 
<a href="https://github.com/caronc/apprise#popular-notification-services">And everything else in this list!</a>

<img src="https://raw.githubusercontent.com/dgtlmoon/changedetection.io/master/docs/screenshot-notifications.png" style="max-width:100%;" alt="Self-hosted web page change monitoring notifications"  title="Self-hosted web page change monitoring notifications"  />

Now you can also customise your notification content and use <a target="_new" href="https://jinja.palletsprojects.com/en/3.0.x/templates/">Jinja2 templating</a> for their title and body!

## tools

Detect changes and monitor data in JSON API's by using either JSONPath or jq to filter, parse, and restructure JSON as needed.

![image](https://raw.githubusercontent.com/dgtlmoon/changedetection.io/master/docs/json-filter-field-example.png)

This will re-parse the JSON and apply formatting to the text, making it super easy to monitor and detect changes in JSON API results

![image](https://raw.githubusercontent.com/dgtlmoon/changedetection.io/master/docs/json-diff-example.png)

### JSONPath or jq?

For more complex parsing, filtering, and modifying of JSON data, jq is recommended due to the built-in operators and functions. Refer to the [documentation](https://stedolan.github.io/jq/manual/) for more specific information on jq.

One big advantage of `jq` is that you can use logic in your JSON filter, such as filters to only show items that have a value greater than/less than etc.

See the wiki https://github.com/dgtlmoon/changedetection.io/wiki/JSON-Selector-Filter-help for more information and examples

### Parse JSON embedded in HTML!

When you enable a `json:` or `jq:` filter, you can even automatically extract and parse embedded JSON inside a HTML page! Amazingly handy for sites that build content based on JSON, such as many e-commerce websites. 

```
<html>
...
<script type="application/ld+json">

{
   "@context":"http://schema.org/",
   "@type":"Product",
   "offers":{
      "@type":"Offer",
      "availability":"http://schema.org/InStock",
      "price":"3949.99",
      "priceCurrency":"USD",
      "url":"https://www.newegg.com/p/3D5-000D-001T1"
   },
   "description":"Cobratype King Cobra Hero Desktop Gaming PC",
   "name":"Cobratype King Cobra Hero Desktop Gaming PC",
   "sku":"3D5-000D-001T1",
   "itemCondition":"NewCondition"
}
</script>
```  

`json:$..price` or `jq:..price` would give `3949.99`, or you can extract the whole structure (use a JSONpath test website to validate with)

The application also supports notifying you that it can follow this information automatically

## configuration

See the wiki https://github.com/dgtlmoon/changedetection.io/wiki/Proxy-configuration , we also support using [Bright Data proxy services where possible](https://github.com/dgtlmoon/changedetection.io/wiki/Proxy-configuration#brightdata-proxy-support) and [Oxylabs](https://oxylabs.go2cloud.org/SH2d) proxy services.

## Raspberry Pi support?

Raspberry Pi and linux/arm/v6 linux/arm/v7 arm64 devices are supported! See the wiki for [details](https://github.com/dgtlmoon/changedetection.io/wiki/Fetching-pages-with-WebDriver)

## Import support

Easily [import your list of websites to watch for changes in Excel .xslx file format](https://changedetection.io/tutorial/how-import-your-website-change-detection-lists-excel), or paste in lists of website URLs as plaintext. 

Excel import is recommended - that way you can better organise tags/groups of websites and other features.

## features

If you choose to enable AI / LLM features, content detected on monitored websites — including page diffs and extracted text — will be transmitted to a third-party AI provider of your choosing, outside of this installation. You are solely responsible for:

- Ensuring such transmission is permitted by the terms of service of every website you monitor.
- Compliance with all applicable data-protection and privacy laws (including but not limited to GDPR) with respect to any personal data that may appear in monitored content.
- All API costs and charges levied by your chosen AI provider. This software has no visibility into or control over those charges.
- Any consequences arising from acting on AI-generated output.

**AI and LLM models are known to hallucinate** — producing plausible-sounding but factually incorrect, incomplete, or entirely fabricated output with apparent confidence. By design, LLMs may also omit or silently truncate relevant information during summarisation. **AI output must never be relied upon as complete or accurate.**

By using this software, and in particular any AI / LLM features, you personally indemnify and hold harmless the author(s), contributor(s), and any associated parties from and against any and all claims, damages, losses, costs, and expenses (including reasonable legal fees) arising out of or in connection with your use of this software.

## Third-party licenses

changedetectionio.html_tools.elementpath_tostring: Copyright (c), 2018-2021, SISSA (Scuola Internazionale Superiore di Studi Avanzati), Licensed under [MIT license](https://github.com/sissaschool/elementpath/blob/master/LICENSE)

## Contributors

Recognition of fantastic contributors to the project

<sub>Developer note: see [translation guide](changedetectionio/translations/README.md) for i18n template patterns and workflow.</sub>

- Constantin Hong https://github.com/Constantin1489
