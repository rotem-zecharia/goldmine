# dob323/session-kit

Close the terminal windows, not the AI coding sessions. One number takes you back in. Every Claude Code and Codex session in one menu: named, numbered, colour-coded. Open, close, and jump to whichever

## features

I run several Claude Code and Codex sessions at the same time. Keeping them alive turned out to be the easy part. Remembering which one was doing what, which one had finished, and which one had been sitting there waiting on me the whole time was not. I kept opening window after window just to find the session that had asked me something.

Session Kit is the small home screen I wanted for that. I use it every day, on a local machine and over SSH to the host where the work actually runs.

It is a passion project. There is no company behind it, no paid tier, and nothing to buy. It is MIT licensed, it collects nothing, and it talks to no server of mine. I published it because it fixed a problem I hit every single day, and if you hit the same one, it will probably fix yours.

## installation

Session Kit installs per user, on the Linux or macOS machine where the work runs.

## requirements

- shpool `0.11.0`, the stock build. The optional patches in [`shpool-patch/`](shpool-patch/) are **not** needed to install or to start using this; that decision can wait until something makes you want them
- Claude Code, Codex, or both
- one trusted Unix account, with per-user service access

**Linux** additionally needs a readable `/proc`, a systemd user manager, Bash 4+, and Python 3.10+.
**macOS** additionally needs macOS 14+, an active desktop login for the per-user launchd GUI domain, Homebrew Bash 4+, and Python 3.11+.

Prefer the GitHub CLI, installing without a network path to the API, or checking the provenance file by hand? [Install Session Kit](docs/install.md) has every route, plus supported shpool paths, provider setup, project import, and activation.
