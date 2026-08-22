# spider-rs/spider

Get web data for AI agents and LLMs

## installation

| You want… | Run |
|---|---|
| Rust library | `cargo add spider` |
| Command-line tool | `cargo install spider_cli` |
| Node.js package | `npm i @spider-rs/spider-rs` |
| Python package | `pip install spider_rs` |
| MCP server (Claude, Cursor, …) | `cargo install spider_mcp` |
| Managed crawling | [spider.cloud](https://spider.cloud?utm_source=github&utm_medium=readme&utm_campaign=spider_rs) |

## configuration

Every option has a sensible default, so set only what you need.

```rust
let mut website = Website::new("https://example.com")
    .with_limit(50)                    // concurrent requests
    .with_depth(10)                    // how deep to follow links
    .with_delay(500)                   // pause between requests (ms)
    .with_respect_robots_txt(true)
    .with_subdomains(true)
    .with_user_agent(Some("MyBot/1.0"))
    .with_stealth(true)
    .build()
    .unwrap();
```

Full reference in the [`Configuration` docs](https://docs.rs/spider/latest/spider/configuration/struct.Configuration.html).

For JavaScript-heavy sites, enable `features = ["chrome"]` and call `crawl_smart()`. Spider tries HTTP first and only launches Chrome on pages that need it.
