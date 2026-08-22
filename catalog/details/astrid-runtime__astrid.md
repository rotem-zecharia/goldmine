# astrid-runtime/astrid

Astrid is a portable, capability-secure operating system for composable software.

## installation

```bash
brew tap astrid-runtime/tap && brew install astrid
astrid init --distro @yourorg/your-distro
astrid start
astrid status
astrid capsule list
```

Astrid Runtime does not select or bundle a product distro. Choose a distro you
trust and pass its name, repository, local `Distro.toml`, or signed `.shuttle`
archive explicitly with `--distro`. Operators running an uncomposed runtime can
skip `init` and start the daemon directly.

Start with [the Book](https://github.com/astrid-runtime/book) for the
architecture or the [Contributor Handbook](https://github.com/astrid-runtime/handbook)
to contribute.

## features

Agent frameworks put trust in the prompt. Astrid puts it in the runtime. An agent is untrusted code
executing on your machine with access to your files, your network, and your credentials. Telling it
to behave is not a security boundary. An OS-grade boundary is.

- **Cryptographic capability model.** Every file path, network host, and tool is a signed ed25519
  grant scoped to a resource pattern, principal-bound, expiry-checked, and globally revocable. No
  grant, no access.
- **WASM sandbox with no ambient authority.** Capsules run in Wasmtime with no syscalls, no file
  descriptors, and no host memory. Every external effect is a capability-checked host call over a
  WIT-typed ABI.
- **The kernel is dumb.** It instantiates an event bus, loads capsules, and routes IPC bytes under a
  capability ACL. It has no LLM handles, no conversation state, and no tool registry. All
  intelligence lives in capsules, so a capsule bug cannot corrupt shared kernel state.
- **Per-principal everything.** Each identity gets isolated capsule access, KV data, secrets, home
  directory, quotas, and audit chain. One principal can never read another's namespace, and it fails
  closed if the caller cannot be resolved.
- **Signed, hash-linked audit chain.** Each entry seals the hash of the one before it and is signed.
  Break the chain and the tampering shows.
- **Live capsule lifecycle.** Install, upgrade, and remove capsules on a running daemon. No restart.
