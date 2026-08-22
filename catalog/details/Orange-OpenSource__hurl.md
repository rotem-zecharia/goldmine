# Orange-OpenSource/hurl

Hurl, run and test HTTP requests with plain text.

## features

<ul class="showcase-container">
    <li><b>Text Format:</b> for both devops and developers</li>
    <li><b>Fast CLI:</b> a command line for local dev and continuous integration</li>
    <li><b>Single Binary:</b> easy to install, with no runtime required</li>
</ul>

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
