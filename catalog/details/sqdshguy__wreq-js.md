# sqdshguy/wreq-js

HTTP client for Node.js with browser TLS fingerprint impersonation

## installation

```bash
npm install wreq-js
# or: yarn add wreq-js / pnpm add wreq-js / bun add wreq-js
```

Prebuilt native binaries ship for macOS (Intel and Apple Silicon), Linux (x64 and arm64, glibc and musl), and Windows (x64 and arm64). Each one lives in its own `@wreq-js/binding-*` package listed under `optionalDependencies`, so an install downloads only the addon your platform actually loads. Platforms outside that list are not supported; build from source with a Rust toolchain instead (see [docs/BUILD.md](docs/BUILD.md)).

Node.js 20 or newer.

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

## Alternatives

Measured 2026-08-06 on an M-series Mac. "H2 correct" means the Akamai HTTP/2 fingerprint is byte identical to what real Chrome sends. Throughput is 300 sequential requests against a local server, so it reflects the JavaScript to native boundary rather than the network. Reproduce with `npm run bench`.

| Library | Engine | Newest Chrome | H2 correct | req/s | Cold start |
|---|---|---|---|---|---|
| **wreq-js** | Rust `wreq` + BoringSSL, in-process | **149** | **Yes** | **12842** | **7 ms** |
| [node-wreq](https://github.com/StopMakingThatBigFace/node-wreq) | Same Rust core | 149 | Yes | 6500 | 10 ms |
| [impers](https://github.com/lexiforest/impers) | curl-impersonate, in-process | 146 | Yes | 8439 | 16 ms |
| [impit](https://github.com/apify/impit) | Rust `reqwest` + patched `rustls` | 124 | **No** ([#385](https://github.com/apify/impit/issues/385)) | 6710 | 37 ms |
| [node-tls-client](https://github.com/Sahil1337/node-tls-client) | Go shared library over FFI | 131 | Yes | not tested | downloads its native library at runtime |
| [CycleTLS](https://github.com/Danny-Dasilva/CycleTLS) | Go subprocess with IPC | not tested | not tested | not tested | per-request IPC overhead |
| [got-scraping](https://github.com/apify/got-scraping) | Pure JS, headers only | n/a | no TLS control | n/a | end of life |

impit's HTTP/2 SETTINGS are its underlying Rust HTTP library's defaults rather than Chrome's, so it omits `HEADER_TABLE_SIZE` and sends a `MAX_FRAME_SIZE` that Chrome never sends. Anything hashing that frame sees a client claiming to be Chrome while speaking HTTP/2 like a Rust program.

If you are migrating off `got-scraping`, note that it only ever rewrote headers. It never touched the TLS handshake, so anything that was blocking you on JA3 or JA4 was never something it could fix.

## Use sessions

A session keeps the connection pool and the TLS session cache alive across requests. Standalone `fetch()` opens a new connection every call, so you pay a full TLS handshake each time: roughly 53 ms against a typical host versus 15 ms on a session. Cookies persist too. Use a session for anything past a single request.

```ts
import { createSession } from 'wreq-js';

const session = await createSession({ browser: 'chrome_149', os: 'windows' });

try {
  await session.fetch('https://example.com/login', {
    method: 'POST',
    body: new URLSearchParams({ user: 'name', pass: 'secret' }),
  });

  const profile = await session.fetch('https://example.com/profile');
  console.log(await profile.json());
} finally {
  await session.close();
}
```

`withSession` does the cleanup for you:

```ts
import { withSession } from 'wreq-js';

const data = await withSession(async (session) => {
  const res = await session.fetch('https://example.com/api');
  return res.json();
}, { browser: 'chrome_149' });
```

If you want pooled connections without a shared cookie jar, use a transport instead:

```ts
import { createTransport, fetch } from 'wreq-js';

const transport = await createTransport({
  browser: 'chrome_149',
  proxy: 'http://user:
