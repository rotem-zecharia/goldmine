# sqdshguy/wreq-js

HTTP client for Node.js with browser TLS fingerprint impersonation

## installation

```bash
npm install wreq-js

## features

- Browser TLS and HTTP fingerprint profiles for Chrome, Firefox, Safari, Edge, Opera and OkHttp, currently up to Chrome 149 and Firefox 151
- JA3, JA4 and Akamai HTTP/2 fingerprints that match what the real browser sends, verified against live capture (see [Alternatives](#alternatives))
- Native Rust engine running in-process, no subprocess and no browser
- `fetch` style API, plus sessions with a persistent cookie jar
- WebSockets, both a one-await helper and a WHATWG style constructor, able to reuse session cookies and transport settings
- Streaming request and response bodies with backpressure
- Proxy support including SOCKS, per-request transport overrides, and connection pool tuning
- Custom emulation if a preset gets you close but not all the way, with control over cipher order, extensions, ALPN, ALPS, GREASE, HTTP/2 SETTINGS and pseudo-header order
- Written in TypeScript with generated definitions
