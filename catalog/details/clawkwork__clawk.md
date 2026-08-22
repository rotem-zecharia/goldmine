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

## Quickstart

The everyday case, a sandbox for the directory you're in:

```sh
cd ~/code/my-project
clawk                      # boot a sandbox for this dir + attach claude
clawk run shell            # drop into a shell in the same sandbox
clawk run codex            # or another agent: codex, pi, opencode, shell
clawk down                 # stop the VM (repo + agent state persist)
clawk attach               # come back later — boots if stopped, reattaches claude
clawk destroy              # remove the VM (conversation history is kept)
```

Common options:

```sh
clawk run claude -- --resume            # pass args through to the agent
clawk forward add my-project 3000       # expose a guest dev server on localhost:3000
clawk network allow my-project api.example.com
```

Working on a ticket that spans several repositories? One command creates a
sandbox with a git worktree per repo on a fresh branch, and `clawk pr` later
opens cross-linked PRs for whatever changed:

```sh
cd ~/code/my-workspace     # contains a clawk.mod listing the repos
clawk work INFRA-123       # one sandbox, a worktree per repo, claude attached
clawk pr INFRA-123         # push branches + open one PR per repo
```

The full ticket lifecycle (status, follow-up branches after merges,
rebases) is in **[docs/ticket-mode.md](docs/ticket-mode.md)**.

> **Tip:** using Claude Code? Run `claude setup-token` then
> `clawk auth set-token` once, and every sandbox comes up already signed in,
> with no `/login` and no login conflicts between parallel sandboxes. See
> **[docs/claude-auth.md](docs/claude-auth.md)**.

## What survives what

One rule governs persistence: *the VM is disposable; everything you'd miss
lives on the host.*

| | `clawk down` | `clawk destroy` |
| --- | :---: | :---: |
| Your repo (mounted worktree; commits, branches) | ✅ | ✅ |
| Agent state (Claude/Codex/pi/opencode conversations, memory) | ✅ | ✅ |
| The VM disk (apt installs, caches, `$HOME`) | ❌ (rebuilt fresh at every boot*) | ❌ (that's the point) |

\* Two exceptions: resuming a `clawk snapshot` restores the disk and
memory exactly as suspended, and the Linux/firecracker provider keeps
its disk until destroy. Tools every boot needs belong in the image
(`vm ( image … )`); per-boot setup belongs in `on up` hooks.

Agent state is host-mounted per sandbox: each runner's home directory —
claude's `~/.claude/`, codex's `~/.codex/`, pi's `~/.pi/`, opencode's two XDG
dirs — live under
`~/.clawk/namespaces/default/state/<name>/` on the host, so a recreated
sandbox picks up its old conversations with `--resume`. That mount is what
makes the promise real: the VM disk itself is re-cloned from the image on
every boot, so anything a runner writes outside those directories is gone
at the next `clawk up`.

## Full autonomy by default (and the `--safe` opt-out)

Runners launch in their "externally sandboxed" modes: claude gets

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
)
```

The block is a *template*: snapshotted when the sandbox is created, so a
running sandbox never changes unexpectedly. The full reference (shares,
secret files, skills, agent memory seeding, multi-repo workspace roots) is
in **[docs/configuration.md](docs/configuration.md)**; MCP servers and how
their credentials stay off disk are in **[docs/mcp.md](docs/mcp.md)**;
putting a USB-serial board from your Mac inside the sandbox for
microcontroller work is in **[docs/serial.md](docs/serial.md)**; images
and custom guest kernels (including the KVM-enabled kernel used for nested
virtualization) are in **[docs/images.md](docs/images.md)**.

## Lifecycle

```sh
clawk list                  # all sandboxes
clawk status [<name>]       # state, forwards, blocked hosts; --json for scripts
clawk up / down             # boot / stop
clawk pause / resume        # suspend / resume the running VM in memory
clawk snapshot              # save to disk: RAM freed, guest intact; resume restores it
clawk destroy               # remove the VM; host-side state persists
```

`clawk snapshot` is hibernation for sandboxes: the guest's memory is saved
beside its disk and the next boot restores the guest exactly where it was.
Background processes and dev servers continue as if nothing happened, and
`clawk attach` puts you back in front of the agent. The full command surface,
runner dispatch, and the idle-management machinery (ballooning, admission
control, auto-stop) are in **[docs/commands.md](docs/commands.md)**.

## How it works

```text
you ──▶ clawk CLI ──▶ per-sandbox daemon (detached; owns the VM)
                        ├─ gvproxy: in-process userspace TCP/IP stack —
                        │  the DNS-aware outbound filter the guest can't reconfigure
                        ├─ vsock bridge to the in-guest pty-agent (no sshd)
                        ├─ ssh-agent proxy, macOS (signing stays on the host)
                        └─ VM: Virtualization.framework (macOS) / firecracker (Linux)
                             ├─ clawk-init, PID 1 (no systemd, no cloud-init)
                             ├─ your repo, live-mounted over virtio-fs
                             └─ claude / codex / pi / shell on a PTY
```

A few deliberate choices, in brief:

- **The rootfs is an ordinary OCI image.** clawk pulls it (no Docker daemon),
  flattens the layers, and writes an ext4 disk directly, with no root and no
  loop devices. Every sandbox from the same image is a copy-on-write clone
  (APFS `clonefile` / `FICLONE`), so per-sandbox disk cost is what the guest
  writes.
- **The network is filtered below the guest.** The VM's entire L3 (gateway,
  DHCP, DNS, NAT) is a userspace stack inside the daemon process. Every
  outbound connection and DNS answer consults the allow-list there, where
  even root inside the guest cannot change it. No host iptables, no sudo.
- **One way in.** No sshd, no cloud-init: a single vsock agent is the only
  control path into the guest, and each attach is container-exec-style: a
  fresh process, torn down on disconnect.

The full picture (the guest stack, both providers, the frame-level
networking) is in **[ARCHITECTURE.md](ARCHITECTURE.md)**, and the reasonin

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

## Status

Pre-1.0 and under active development, and evolving quickly: expect breaking
changes between releases. The CLI surface changes least and internals most,
but nothing is frozen until 1.0.

## Contributing

Issues and PRs are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md) to build
and test, [ARCHITECTURE.md](ARCHITECTURE.md) for how it's built, and
[DESIGN.md](DESIGN.md) for where it's headed.

## License

[Apache License 2.0](LICENSE). clawk vendors two third-party components under
their own licenses (gvisor-tap-vsock, Apache-2.0; an hcsshim ext4 writer, MIT);
see [NOTICE](NOTICE).
