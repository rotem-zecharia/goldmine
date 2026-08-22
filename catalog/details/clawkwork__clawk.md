# clawkwork/clawk

Give coding agents a disposable Linux VM, not your laptop

## features

clawk is a general-purpose local environment for autonomous coding agents.
The VM is the point: it's a whole machine the agent can own, not a process
wrapped in policy on the one you're using.

- **A separate kernel.** The guest runs its own Linux kernel, so the host
  filesystem isn't hidden behind deny rules; it was never mounted.
- **A conventional Linux environment.** Standard kernel, standard userland,
  `/dev/kvm`-shaped expectations, so tools behave the way their docs say,
  without a syscall-filter surprise.
- **Root in the guest.** Install system packages, edit `/etc`, load a module,
  bind a privileged port. It's the agent's box to reconfigure.
- **A disposable lifecycle.** Cheap to break and quick to recreate; a wrecked
  VM is one `clawk destroy && clawk` away, with your repo and conversations
  untouched on the host.
- **Stronger separation from the host.** Isolation rests on the hypervisor
  boundary rather than on getting a process-sandbox policy exactly right.

That combination runs workloads a restricted process sandbox tends to fight
you on:

- installing packages and native dependencies;
- running background services (databases, queues, dev servers);
- executing untrusted builds and tests at full speed;
- using system-level Linux tooling that expects a real machine;
- and, with a KVM-enabled guest kernel on supported hardware, container and
  Kubernetes dev workflows such as Docker or Kind running *inside* the
  sandbox. This is opt-in and hardware-gated; see
  [Images](docs/images.md#guest-kernel-override) for the exact requirements.

None of this is the *product*; clawk is for local agent work in general.
Docker and Kubernetes are just the sharpest example of "needs a real machine,
not a sandboxed process."

## installation

Requires macOS 14+ on Apple silicon. (Linux is supported via firecracker and
currently experimental — start with
**[docs/linux-quickstart.md](docs/linux-quickstart.md)**, which covers setup,
the workflow, and the gaps. This README is macOS-first.)

```sh
brew install clawkwork/tap/clawk
```

**From source** (contributors, or if you don't use Homebrew), needs Go 1.26+:

```sh
git clone https://github.com/clawkwork/clawk && cd clawk
make install
```

Either way there's no extra host tooling: no Docker, no qemu, no sudo. The
hypervisor is Apple's Virtualization.framework, linked into the binary, and the
release binaries carry the in-guest agent prebuilt — so a Go toolchain is only
needed if you build from source, in which case you have one. First run probes
for anything missing and offers to fix it.

**Uninstall:** `clawk destroy` your sandboxes, `rm -rf ~/.clawk`, then remove
the binary with `brew uninstall clawk` (or delete it from `$GOBIN` for a
source install). Nothing else was installed: there are no launchd jobs; the
per-sandbox daemons are ordinary processes that exit with their VMs.

## configuration

No config file is required; defaults are sensible. When a project needs
more, a `clawk.mod` file describes it, in a go.mod-style syntax:

```text
sandbox my-project (
    vm (
        cpu    4
        memory 8GiB
        image  golang:1.25          # any OCI image is the rootfs
    )
    network ( allow api.example.com )
    forwards ( 3000 )
    env ( DATABASE_URL )            # forward a host var; values come from your shell
    # also: GH=${OTHER_NAME}, LOG=${LOG:-info} defaults, API=${API:?required}
    mcp (                           # MCP servers, ready on first boot
        linear https://mcp.linear.app/mcp header "Authorization: Bearer ${LINEAR_TOKEN}"
    )
    on create ( "go mod download" )
    agent (
        instructions "Ask before running destructive commands."
    )

## limitations

Next up: running more sandboxes than your RAM can hold at once.

- **Idle stops that snapshot.** Manual suspend-to-disk shipped as
  `clawk snapshot` / `clawk resume`; next, the *automatic* idle stop uses it
  too, so dev servers survive the stop and a suspended sandbox costs only
  disk.
- **A cap on running VMs.** Instead of refusing a new VM when RAM is
  committed, suspend the least-recently-used sandbox to disk and start the
  new one.
- **Firecracker parity.** Live worktree propagation and host-file push on
  Linux.
