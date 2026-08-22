# HelixDB/helix-db

HelixDB is an OLTP graph-vector database built in Rust on Object Storage.

## installation

### 1. Install the CLI

The Helix CLI runs and manages local instances and talks to Helix Cloud.

```bash
curl -sSL "https://install.helix-db.com" | bash
```

Already installed? Update to the latest version with `helix update`.

### 2. The quickest path — `helix chef`

`helix chef` is an interactive, one-shot bootstrapper. It installs the HelixDB query skills and docs MCP, scaffolds a project, starts a local instance, seeds some example data, and writes a `HELIX_CHEF_PROMPT.md`. If a coding agent is available (Claude Code, Codex, or OpenCode), it can hand off and build a working app — frontend and all — from a one-line description of what you want.

```bash
helix chef
```

That's it — no flags. Answer "what do you want to build?" and follow the prompts.

### 3. Manual local setup

If you'd rather wire things up yourself:

1. **Initialize a project.** This scaffolds `helix.toml`, a `.helix/` workspace dir, and a ready-to-run `examples/request.json`.
  ```bash
   mkdir my-helix-app && cd my-helix-app
   helix init
  ```
2. **Start a local instance.** Runs `ghcr.io/helixdb/helixdb:v0.0.4` in a background container on port `6969` and waits for `GET /healthz` to report ready.
  ```bash
   helix start dev
  ```
  > ⚠️ The default storage mode is **in-memory** — stopping the instance wipes its data. Use `helix start dev --disk` to persist with a Helix-managed MinIO volume, or `helix start dev --storage-uri s3://my-bucket/my-prefix --persist` to use your own S3/S3-compatible object-store prefix.
3. **Send a query.**
  ```bash
   helix query dev --file examples/request.json
  ```
4. **Stop the instance when you're done.**
  ```bash
   helix stop dev
  ```

## Writing queries with the SDKs

Queries are authored with the Rust, TypeScript, Go, or Python DSL and sent straight to a running instance through `POST /v2/query` — no build or deploy step. The SDKs produce the same JSON AST. The examples below talk to a local instance on `http://localhost:6969` (the default `helix start dev` port). See the [Querying Guide](https://docs.helix-db.com/database/querying-guide/overview) for the full builder catalog and query wire format.

### Rust

Install the crate (published as `helix-db`, imported as `helix_db`):

```bash
cargo init && cargo add helix-db tokio sonic-rs
```

Define queries as `#[query]` functions, then run them directly through the client:

```rust
use helix_db::Client;
use helix_db::dsl::prelude::*;

#[query]
pub fn add_user(name: String) -> WriteBatch {
    write_batch()
        .var_as(
            "user",
            g().add_n("User", vec![("name", name)])
                .value_map(None::<Vec<String>>),
        )
        .returning(["user"])
}

#[query]
pub fn get_user(name: String) -> ReadBatch {
    read_batch()
        .var_as(
            "user",
            g().n_with_label("User")
                .where_(Predicate::eq("name", name))
                .value_map(None::<Vec<String>>),
        )
        .returning(["user"])
}

#[tokio::main]
async fn main() {
    let client = Client::new(None).unwrap(); // defaults to http://localhost:6969

    // add user
    let new_user: sonic_rs::Value = client
        .query(add_user("John Doe".to_string()))
        .send()
        .await
        .unwrap();
    println!("new user: {:#}", sonic_rs::to_string_pretty(&new_user).unwrap());

    // get user
    let user: sonic_rs::Value = client
        .query(get_user("John Doe".to_string()))
        .send()
        .await
        .unwrap();
    println!("user: {:#}", sonic_rs::to_string_pretty(&user).unwrap());
}
```

### TypeScript

Install the package (Node.js 20+):

```bash
npm init -y && npm install @helix-db/helix-db
```

Define your queries as functions, then `POST` them to the running instance:

```ts
import {
  Predicate, PropertyInput, PropertyProjection,
  defineParams, g, param, readBatch, writeBatch,
} from "@helix-db/helix-db";

const addUserParams = defineParams({ name: param.string() });
function addUser(p = addUserParams) {
  
