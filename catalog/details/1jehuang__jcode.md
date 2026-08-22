# 1jehuang/jcode

The most RAM efficient harness

## installation

</div>

```bash

## configuration

jcode login --provider google --print-auth-url --google-access-tier readonly
jcode login --provider google --callback-url 'http://127.0.0.1:8456?...'
```

Pending scriptable login state is stored under `~/.jcode/pending-login/`, automatically expires, and stale entries are cleaned up when new scriptable logins start or resume.

For the built-in OpenAI login flow, jcode opens a local callback on
`http://localhost:1455/auth/callback` by default.

<img width="2877" height="1762" alt="Screenshot from 2026-04-02 14-28-51" src="https://github.com/user-attachments/assets/530684c0-9d12-4363-aa0e-1b39a0d4e1be" />
The above image is the first page of provider logins

## features

Agents dont like to commit in dirty git state with active changes. Git was clearly not built for multi-agent workflows, and git worktrees is not a good solution. Given this, I believe that is an opporunity for a new git like primitive to be born. 

Build speed improvements: An incremental debug cargo build with cache enabled takes about 1 minute on my machine. The goal is 5-20 seconds. Refactors and crates seams should be able to make this happen. 

<!-- Add iOS / native OpenClaw preview and fuller writeup here. -->

---

<div align="center">
