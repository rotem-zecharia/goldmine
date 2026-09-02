# Orange-OpenSource/hurl

Hurl, run and test HTTP requests with plain text.

## features

<ul class="showcase-container">
    <li><b>Text Format:</b> for both devops and developers</li>
    <li><b>Fast CLI:</b> a command line for local dev and continuous integration</li>
    <li><b>Single Binary:</b> easy to install, with no runtime required</li>
</ul>

# Powered by curl

Hurl is a lightweight binary written in [Rust]. Under the hood, Hurl HTTP engine is
powered by [libcurl], one of the most powerful and reliable file transfer libraries.
With its text file format, Hurl adds syntactic sugar to run and test HTTP requests,
but it's still the [curl] that we love: __fast__, __efficient__ and __IPv6 / HTTP/3 ready__.

# Feedbacks

To support its development, [star Hurl on GitHub]!

[Feedback, suggestion, bugs or improvements] are welcome.

```hurl
POST https://hurl.dev/api/feedback
{
  "name": "John Doe",
  "feedback": "Hurl is awesome!"
}
HTTP 200
```

# Resources

[License]

[Blog]

[Tutorial]

[Documentation] (download [HTML], [PDF], [Markdown]) 

[GitHub]

# Table of Contents

* [Samples](#samples)
    * [Getting Data](#getting-data)
        * [HTTP Headers](#http-headers)
        * [Query Params](#query-params)
        * [Basic Authentication](#basic-authentication)
        * [Passing Data between Requests ](#passing-data-between-requests)
    * [Sending Data](#sending-data)
        * [Sending HTML Form Data](#sending-html-form-data)
        * [Sending Multipart Form Data](#sending-multipart-form-data)
        * [Posting a JSON Body](#posting-a-json-body)
        * [Templating a JSON Body](#templating-a-json-body)
        * [Templating a XML Body](#templating-a-xml-body)
        * [Using GraphQL Query](#using-graphql-query)
        * [Using Dynamic Datas](#using-dynamic-datas)
    * [Testing Response](#testing-response)
        * [Testing Status Code](#testing-status-code)
        * [Testing Response Headers](#testing-response-headers)
        * [Testing REST APIs](#testing-rest-apis)
        * [Testing HTML Response](#testing-html-response)
        * [Testing Set-Cookie Attributes](#testing-set-cookie-attributes)
        * [Testing Bytes Content](#testing-bytes-content)
        * [SSL Certificate](#ssl-certificate)
        * [Checking Full Body](#checking-full-body)
        * [Testing Redirections](#testing-redirections)
    * [Debug Tips](#debug-tips)
        * [Verbose Mode](#verbose-mode)
        * [Error Format](#error-format)
        * [Output Response Body](#output-response-body)
        * [Export curl Commands](#export-curl-commands)
        * [Using Proxy](#using-proxy)
    * [Reports](#reports)
        * [HTML Report](#html-report)
        * [JSON Report](#json-report)
        * [JUnit Report](#junit-report)
        * [TAP Report](#tap-report)
        * [JSON Output](#json-output)
    * [Others](#others)
        * [HTTP Version](#http-version)
        * [IP Address](#ip-address)
        * [Polling and Retry](#polling-and-retry)
        * [Delaying Requests](#delaying-requests)
        * [Skipping Requests](#skipping-requests)
        * [Testing Endpoint Performance](#testing-endpoint-performance)
        * [Using SOAP APIs](#using-soap-apis)
        * [Capturing and Using a CSRF Token](#capturing-and-using-a-csrf-token)
        * [Redacting Secrets](#redacting-secrets)
        * [Checking Byte Order Mark (BOM) in Response Body](#checking-byte-order-mark-bom-in-response-body)
        * [AWS Signature Version 4 Requests](#aws-signature-version-4-requests)
        * [Using curl Options](#using-curl-options)
* [Manual](#manual)
    * [Name](#name)
    * [Synopsis](#synopsis)
    * [Description](#description)
    * [Hurl File Format](#hurl-file-format)
        * [Capturing values](#capturing-values)
        * [Asserts](#asserts)
    * [Configuration](#configuration)
    * [All Options](#all-options)
        * [HTTP options](#http-options)
        * [Output options](#output-options)
        * [Run options](#run-options)
        * [Report options](#report-options)
        * [Other options](#other-options)
    * [

## tools

Asserting JSON body response (node values, collection count etc...) with [JSONPath]:

```hurl
GET https://example.org/order
screencapability: low
HTTP 200
[Asserts]
jsonpath "$.validated" == true
jsonpath "$.userInfo" isObject
jsonpath "$.userInfo.firstName" == "Franck"
jsonpath "$.userInfo.lastName" == "Herbert"
jsonpath "$.hasDevice" == false
jsonpath "$.links" count == 12
jsonpath "$.state" != null
jsonpath "$.order" matches "^order-\\d{8}$"
jsonpath "$.order" matches /^order-\d{8}$/  # Alternative syntax with regex literal
jsonpath "$.id" matches /(?i)[a-z]*/        # See syntax for flags <https://docs.rs/regex/latest/regex/#grouping-and-flags>
jsonpath "$.created" isIsoDate
```

[Doc](https://hurl.dev/docs/asserting-response.html#jsonpath-assert)

### Testing HTML Response

```hurl
GET https://example.org
HTTP 200
Content-Type: text/html; charset=UTF-8
[Asserts]
xpath "string(/html/head/title)" contains "Example" # Check title
xpath "count(//p)" == 2  # Check the number of p
xpath "//p" count == 2  # Similar assert for p
xpath "boolean(count(//h2))" == false  # Check there is no h2  
xpath "//h2" not exists  # Similar assert for h2
xpath "string(//div[1])" matches /Hello.*/
```

[Doc](https://hurl.dev/docs/asserting-response.html#xpath-assert)

### Testing Set-Cookie Attributes

```hurl
GET https://example.org/home
HTTP 200
[Asserts]
cookie "JSESSIONID" == "8400BAFE2F66443613DC38AE3D9D6239"
cookie "JSESSIONID[Value]" == "8400BAFE2F66443613DC38AE3D9D6239"
cookie "JSESSIONID[Expires]" contains "Wed, 13 Jan 2021"
cookie "JSESSIONID[Secure]" exists
cookie "JSESSIONID[HttpOnly]" exists
cookie "JSESSIONID[SameSite]" == "Lax"
```

[Doc](https://hurl.dev/docs/asserting-response.html#cookie-assert)

### Testing Bytes Content

Check the SHA-256 response body hash:

```hurl
GET https://example.org/data.tar.gz
HTTP 200
[Asserts]
sha256 == hex,039058c6f2c0cb492c533b0a4d14ef77cc0f78abccced5287d84a1a2011cfb81;
```

[Doc](https://hurl.dev/docs/asserting-response.html#sha-256-assert)

### SSL Certificate

Check the properties of a SSL certificate:

```hurl
GET https://example.org
HTTP 200
[Asserts]
certificate "Subject" == "CN=example.org"
certificate "Issuer" == "C=US, O=Let's Encrypt, CN=R3"
certificate "Expire-Date" daysAfterNow > 15
certificate "Serial-Number" matches /[\da-f]+/
certificate "Subject-Alt-Name" contains "DNS:example.org"
certificate "Subject-Alt-Name" split "," count == 2
certificate "Value" startsWith "-----BEGIN CERTIFICATE-----"
```

[Doc](https://hurl.dev/docs/asserting-response.html#ssl-certificate-assert)

### Checking Full Body

Use implicit body to test an exact JSON body match:

```hurl
GET https://example.org/api/cats/123
HTTP 200
{
  "name" : "Purrsloud",
  "species" : "Cat",
  "favFoods" : ["wet food", "dry food", "<strong>any</strong> food"],
  "birthYear" : 2016,
  "photo" : "https://learnwebcode.github.io/json-example/images/cat-2.jpg"
}
```

[Doc](https://hurl.dev/docs/asserting-response.html#json-body)

Or an explicit assert file:

```hurl
GET https://example.org/index.html
HTTP 200
[Asserts]
body == file,cat.json;
```

[Doc](https://hurl.dev/docs/asserting-response.html#body-assert)

Implicit asserts supports XML body:

```hurl
GET https://example.org/api/catalog
HTTP 200
<?xml version="1.0" encoding="UTF-8"?>
<catalog>
   <book id="bk101">
      <author>Gambardella, Matthew</author>
      <title>XML Developer's Guide</title>
      <genre>Computer</genre>
      <price>44.95</price>
      <publish_date>2000-10-01</publish_date>
      <description>An in-depth look at creating applications with XML.</description>
   </book>
</catalog>
```

[Doc](https://hurl.dev/docs/asserting-response.html#xml-body)

Plain text:

~~~hurl
GET https://example.org/models
HTTP 200
```
Year,Make,Model,Description,Price
1997,Ford,E350,"ac, abs, moon",3000.00
1999,Chevy,"Venture ""Extended Edition""","",4900.00
1999,Chevy,"Venture ""Extended Edition, Very Large""",,5000.00
1996,Jeep,Grand Cherokee,"MUST SELL! air, moon roof, lo

## configuration

curl options (for instance [`--resolve`] or [`--connect-to`]) can be used as CLI argument. In this case, they're applicable
to each request of an Hurl file.

```shell
$ hurl --resolve foo.com:8000:127.0.0.1 foo.hurl
```

Use  [`[Options]` section](https://hurl.dev/docs/request.html#options) to configure a specific request:

```hurl
GET http://bar.com
HTTP 200


GET http://foo.com:8000/resolve
[Options]
resolve: foo.com:8000:127.0.0.1
HTTP 200
`Hello World!`
```

[Doc](https://hurl.dev/docs/request.html#options)


# Manual

## Name

hurl - run and test HTTP requests.

## Synopsis

**hurl** [OPTIONS] [FILES...]

**hurl** --test [OPTIONS] [FILES...]

## Description

**Hurl** is a command line tool that runs HTTP requests defined in a simple plain text format.

It can chain requests, capture values and evaluate queries on headers and body response. Hurl is very versatile, it can be used for fetching data and testing HTTP sessions: HTML content, REST / SOAP / GraphQL APIs, or any other XML / JSON based APIs.

```shell
$ hurl session.hurl
```

If no input files are specified, input is read from stdin.

```shell
$ echo GET http://httpbin.org/get | hurl
    {
      "args": {},
      "headers": {
        "Accept": "*/*",
        "Accept-Encoding": "gzip",
        "Content-Length": "0",
        "Host": "httpbin.org",
        "User-Agent": "hurl/0.99.10",
        "X-Amzn-Trace-Id": "Root=1-5eedf4c7-520814d64e2f9249ea44e0"
      },
      "origin": "1.2.3.4",
      "url": "http://httpbin.org/get"
    }
```

Hurl can take files as input, or directories. In the latter case, Hurl will search files with `.hurl` extension recursively.

Output goes to stdout by default. To have output go to a file, use the [`-o, --output`](#output) option:

```shell
$ hurl -o output input.hurl
```

By default, Hurl executes all HTTP requests and outputs the response body of the last HTTP call.

To have a test oriented output, you can use [`--test`](#test) option:

```shell
$ hurl --test *.hurl
```


## Hurl File Format

The Hurl file format is fully documented in [https://hurl.dev/docs/hurl-file.html](https://hurl.dev/docs/hurl-file.html)

It consists of one or several HTTP requests

```hurl
GET http://example.org/endpoint1
GET http://example.org/endpoint2
```


### Capturing values

A value from an HTTP response can be-reused for successive HTTP requests.

A typical example occurs with CSRF tokens.

```hurl
GET https://example.org
HTTP 200
# Capture the CSRF token value from html body.
[Captures]
csrf_token: xpath "normalize-space(//meta[@name='_csrf_token']/@content)"

# Do the login !
POST https://example.org/login?user=toto&password=1234
X-CSRF-TOKEN: {{csrf_token}}
```

More information on captures can be found here [https://hurl.dev/docs/capturing-response.html](https://hurl.dev/docs/capturing-response.html)

### Asserts

The HTTP response defined in the Hurl file are used to make asserts. Responses are optional.

At the minimum, response includes assert on the HTTP status code.

```hurl
GET http://example.org
HTTP 301
```

It can also include asserts on the response headers

```hurl
GET http://example.org
HTTP 301
Location: http://www.example.org
```

Explicit asserts can be included by combining a query and a predicate

```hurl
GET http://example.org
HTTP 301
[Asserts]
xpath "string(//title)" == "301 Moved"
```

With the addition of asserts, Hurl can be used as a testing tool to run scenarios.

More information on asserts can be found here [https://hurl.dev/docs/asserting-response.html](https://hurl.dev/docs/asserting-response.html)

## Configuration

Options that exist in curl have exactly the same semantics.

Options specified on the command line are defined for every Hurl file's entry,
except if they are tagged as cli-only (can not be defined in the Hurl request `[Options]` entry)

For instance:

```shell
$ hurl --location foo.hurl
```

will follow redirection for each entry in `foo.hurl`. You can also define an option only for a particular entry with

## installation

## Binaries Installation

### Linux

Precompiled binary (depending on libc >=2.35) is available at [Hurl latest GitHub release]:

```shell
$ INSTALL_DIR=/tmp
$ VERSION=8.0.1
$ curl --silent --location https://github.com/Orange-OpenSource/hurl/releases/download/$VERSION/hurl-$VERSION-x86_64-unknown-linux-gnu.tar.gz | tar xvz -C $INSTALL_DIR
$ export PATH=$INSTALL_DIR/hurl-$VERSION-x86_64-unknown-linux-gnu/bin:$PATH
```

#### Debian / Ubuntu

For Debian >=12 / Ubuntu 22.04 and 24.04, Hurl can be installed using a binary .deb file provided in each Hurl release.

```shell
$ VERSION=8.0.1
$ curl --location --remote-name https://github.com/Orange-OpenSource/hurl/releases/download/$VERSION/hurl_${VERSION}_amd64.deb
$ sudo apt update && sudo apt install ./hurl_${VERSION}_amd64.deb
```

For Ubuntu >=22.04, Hurl can be installed from `ppa:lepapareil/hurl`

```shell
$ VERSION=8.0.1
$ sudo apt-add-repository -y ppa:lepapareil/hurl
$ sudo apt install hurl="${VERSION}"*
```

#### Alpine

Hurl is available on `testing` channel.

```shell
$ apk add --repository http://dl-cdn.alpinelinux.org/alpine/edge/testing hurl
```

#### Arch Linux / Manjaro

Hurl is available on [extra] channel.

```shell
$ pacman -Sy hurl
```

#### NixOS / Nix

[NixOS / Nix package] is available on stable channel.

#### Guix

```shell
$ guix install hurl
```

### macOS

Precompiled binaries for Intel and ARM CPUs are available at [Hurl latest GitHub release].

#### Homebrew

```shell
$ brew install hurl
```

#### MacPorts

```shell
$ sudo port install hurl
```

### FreeBSD

```shell
$ sudo pkg install hurl
```

### Windows

Windows requires the [Visual C++ Redistributable Package] to be installed manually, as this is not included in the installer.

#### Zip File

Hurl can be installed from a standalone zip file at [Hurl latest GitHub release]. You will need to update your `PATH` variable.

#### Installer

An executable installer is also available at [Hurl latest GitHub release].

#### Chocolatey

```shell
$ choco install hurl
```

#### Scoop

```shell
$ scoop install hurl
```

#### Windows Package Manager

```shell
$ winget install hurl
```

### Cargo

If you're a Rust programmer, Hurl can be installed with cargo.

```shell
$ cargo install --locked hurl
```

### conda-forge

```shell
$ conda install -c conda-forge hurl
```

Hurl can also be installed with [`conda-forge`] powered package manager like [`pixi`].

### Docker

```shell
$ docker pull ghcr.io/orange-opensource/hurl:latest
```

### npm

```shell
$ npm install --save-dev @orangeopensource/hurl
```

## Building From Sources

Hurl sources are available in [GitHub].

### Build on Linux

Hurl depends on libssl, libcurl and libxml2 native libraries. You will need their development files in your platform.

#### Debian based distributions

```shell
$ apt install build-essential pkg-config libssl-dev libcurl4-openssl-dev libxml2-dev libclang-dev
```

#### Fedora based distributions

```shell
$ dnf install pkgconf-pkg-config gcc openssl-devel libxml2-devel clang-devel
```

#### Red Hat based distributions

```shell
$ yum install pkg-config gcc openssl-devel libxml2-devel clang-devel
```

#### Arch based distributions

```shell
$ pacman -S pkgconf gcc glibc openssl libxml2 clang
```

#### Alpine based distributions

```shell
$ apk add curl-dev gcc libxml2-dev musl-dev openssl-dev clang-dev
```

### Build on macOS

```shell
$ xcode-select --install
$ brew install pkg-config openssl
```

Hurl is written in [Rust]. You should [install] the latest stable release.

```shell
$ curl https://sh.rustup.rs -sSf | sh -s -- -y
$ source $HOME/.cargo/env
$ rustc --version
$ cargo --version
```

Then build hurl:

```shell
$ git clone https://github.com/Orange-OpenSource/hurl
$ cd hurl
$ cargo build --release
$ ./target/release/hurl --version
```

### Build on Windows

Please follow the [contrib on Windows section].

[XPath]: https://en.wikipedia.org/wiki/XPath
[JSONPath]: https://goessner.net/articles/JsonPath/
[Rust]: https://www.rust-
