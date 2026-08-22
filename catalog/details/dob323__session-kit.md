# dob323/session-kit

Close the terminal windows, not the AI coding sessions. One number takes you back in. Every Claude Code and Codex session in one menu: named, numbered, colour-coded. Open, close, and jump to whichever

## features

I run several Claude Code and Codex sessions at the same time. Keeping them alive turned out to be the easy part. Remembering which one was doing what, which one had finished, and which one had been sitting there waiting on me the whole time was not. I kept opening window after window just to find the session that had asked me something.

Session Kit is the small home screen I wanted for that. I use it every day, on a local machine and over SSH to the host where the work actually runs.

It is a passion project. There is no company behind it, no paid tier, and nothing to buy. It is MIT licensed, it collects nothing, and it talks to no server of mine. I published it because it fixed a problem I hit every single day, and if you hit the same one, it will probably fix yours.

## What it does

- **See every session in one list.** Claude Code and Codex together, on one screen.
- **Know what needs you.** `question`, `needs you`, `working`, and `idle` make the next session to check obvious.
- **Jump back in by number.** Every session keeps a stable number that does not move.
- **Survive terminal and SSH disconnects.** The session keeps running on the host.
- **Know which window is which.** Sessions name and colour themselves, and the name, number, and colour follow the session into its own window.
- **Use a different account per session.** The subscription belongs to the session, not to the terminal that launched it.
- **Get a closed conversation back.** Closing a session records the exact conversation for restore.
- **Keep delegated work apart.** A machine-origin session gets its own git worktree on its own branch, and hands it back when it closes.
- **Stay local.** No hosted account, no analytics, no telemetry, no update beacon.

## Is this for you?

If you regularly have enough sessions open that you lose track of which one needs you, this was built for exactly that, and you will feel it on the first run.

If you usually keep one or two sessions going, you probably do not need it yet.

It works the same on a local workstation or on a remote host over SSH.

## Simple on purpose

The interface is deliberately small: open `kit`, see what needs you, press a number.

More is going on underneath. Before Session Kit changes a live session, it re-proves that the session is still the exact provider conversation and the exact process it expects. If it cannot prove that, it refuses instead of guessing.

The picker is a view of your sessions. It is never trusted as evidence of which live session an action should affect. That distinction is the whole design, and [Safety model](#safety-model) has it in full.

## installation

Session Kit installs per user, on the Linux or macOS machine where the work runs.

### Installing with an AI assistant

The shortest path, if Claude Code, Codex, or another terminal agent is already open: give it this.

> Install Session Kit from `https://github.com/dob323/session-kit`. Use the latest release artifact, not a clone of `main`. Download the release archive with its `.sha256` and `.provenance.json` files, verify the checksum, extract it, and run `./install.sh --check` first. Fix only the remedies that preflight explicitly names. Then run `./install.sh`, `session-kit doctor`, `session-kit services enable`, and `session-kit doctor` again. Never bypass a refused step. Show me the final doctor output and finish by telling me to type `kit`.

### Installing it yourself

Artifacts are named by the exact commit they were built from, so there is no fixed download URL. This asks the release API which files belong to the current release, checks what arrived, and only then unpacks it. It needs nothing but Python 3 and `tar`, both of which the install needs anyway.

```bash
mkdir session-kit-download
cd session-kit-download

python3 - <<'PY'
import json, urllib.request
url = "https://api.github.com/repos/dob323/session-kit/releases/latest"
with urllib.request.urlopen(url) as response:
    release = json.load(response)
for asset in release["assets"]:
    urllib.request.urlretrieve(asset["browser_download_url"], asset["name"])
    print("downloaded", asset["name"])
PY

if command -v sha256sum >/dev/null; then
  sha256sum --check session-kit-*.sha256
else
  shasum -a 256 --check session-kit-*.sha256
fi

tar -xzf session-kit-*.tar.gz
cd session-kit-*/

./install.sh --check
./install.sh

session-kit doctor
session-kit services enable
session-kit doctor
```

`./install.sh --check` is read-only. Do not work around a refusal. Session Kit prints the reason and the remedy it expects.

## requirements

- shpool `0.11.0`, the stock build. The optional patches in [`shpool-patch/`](shpool-patch/) are **not** needed to install or to start using this; that decision can wait until something makes you want them
- Claude Code, Codex, or both
- one trusted Unix account, with per-user service access

**Linux** additionally needs a readable `/proc`, a systemd user manager, Bash 4+, and Python 3.10+.
**macOS** additionally needs macOS 14+, an active desktop login for the per-user launchd GUI domain, Homebrew Bash 4+, and Python 3.11+.

Prefer the GitHub CLI, installing without a network path to the API, or checking the provenance file by hand? [Install Session Kit](docs/install.md) has every route, plus supported shpool paths, provider setup, project import, and activation.

## First run

```bash
kit
```

New session defaults to Claude Code. A session can also be started directly:

```bash
sp new claude
sp new codex
```

Project aliases, provider choice, account selection, and configured models make those launches more specific. See [Projects](docs/projects.md) and [Use Session Kit](docs/usage.md).

## The picker

Ready sessions come first. Sessions already attached to another window appear under **Open elsewhere**. Within a group, attention state determines the first part of the order, followed by provider and activity.

The state words are deliberately small and literal:

| State | Meaning |
|---|---|
| `question` | Claude has a blocking prompt open now. Codex does not claim this state yet. |
| `needs you` | The provider finished its turn and is waiting for you. |
| `working` | The provider is driving the current turn. |
| `idle` | A needs-you transcript has not moved for the configured idle window. |
| `pending` | A launch that has not finished, or a value Session Kit cannot currently read. It is not a fifth state. |

One limit worth stating plainly: Claude Code reports a blocking prompt the moment it opens one, so `question` is exact. Codex does not expose that yet, so a Codex session reads `needs you` when its turn ends rather than the instant it asks you something.

Pressing `a` narrows the list to just those sessions, with how long each has
waited.

<p align="center">
  <img src="docs/assets/readme/needs-you.png" alt="The needs-you screen: a count of four, then the four sessions waiting on a reply, each with its number, name, provider, state, and how long it has waited" width="100%">
</p>

The home screen keeps the common actions one key away:

| Input | Action |
|---|---|
| `Enter` or a session number | Open the first visible session, or the numbered session. |
| `k <numbers>` | Close one or more visible sessions. Lists and ranges work. |
| `n` | Start a new session. |
| `m` | Open More. |
| `a` | Show everything that needs you. |
| `h <number>` | Read settled history without opening the session. |
| `?` | Show picker help. |
| `b` or `q` | Leave the home screen for an ordinary shell. |

A session that is open elsewhere defaults to **Move it here** after a fresh identity check. The earlier window returns to its picker, and the provider conversation is not duplicated.

Every session also names and colours itself. It takes a short title from its own first piece of work, keeps a number that does not move, and gets a colour no other live session has. All three follow the session into its own window: the tab title carries the name and number, and the session is tinted its colour inside Claude Code and Codex themselves. So the window you are typing in tells you which session it is, and the picker and the session never disagree.

Press `?` for the full key reference: filtering, ranges, grouping, forking, renaming, and `g` to jump to the next session that needs you are all there. See [Picker navigation](docs/picker-navigation.md) for the cursor-driven picker, mouse behavior, action panels, machine sessions, and closed-session restore.

## Safety model

Session Kit deliberately separates **what you see** from **what it trusts**.

<p alig
