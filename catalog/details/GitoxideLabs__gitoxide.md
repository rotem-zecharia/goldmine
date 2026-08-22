# GitoxideLabs/gitoxide

An idiomatic, lean, fast & safe pure Rust implementation of Git

## features

> Can `gix` do what I need it to do?

The above can be hard to answer and this paragraph is here to help with feature discovery.

Look at [`crate-status.md`](https://github.com/GitoxideLabs/gitoxide/blob/main/crate-status.md) for a rather exhaustive document that contains
both implemented and planned features.

Further, the [`gix` crate documentation with the `git2` search term](https://docs.rs/gix/latest/gix?search=git2) helps to find all currently
known `git2` equivalent method calls. Please note that this list is definitely not exhaustive yet, but might help if you are coming from `git2`.

What follows is a high-level list of features and those which are planned:

* [x] clone
* [x] fetch
* [ ] push
* [x] blame (*plumbing*)
* [x] status
* [x] blob and tree-diff
* [ ] merge
    - [x] blobs
    - [x] trees
    - [ ] commits
* [x] commit
    - [ ] hooks
* [x] commit-graph traversal
* [ ] rebase
* [x] worktree checkout and worktree stream
* [ ] reset
* [x] reading and writing of objects
* [x] reading and writing of refs
* [x] reading and writing of `.git/index`
* [x] reading and writing of git configuration
* [x] pathspecs
* [x] revspecs
* [x] `.gitignore` and `.gitattributes`

## installation

For macOS and Linux, `gitoxide` can be installed from [Homebrew](https://brew.sh):

```sh
brew install gitoxide
```

## tools

Once installed, there are two binaries:

* **ein**
  * high level commands, _porcelain_, for every-day use, optimized for a pleasant user experience
* **gix**
  * low level commands, _plumbing_, for use in more specialized cases and to validate newly written code in real-world scenarios

## limitations

Please take a look at the [`SHORTCOMINGS.md` file](https://github.com/GitoxideLabs/gitoxide/blob/main/SHORTCOMINGS.md) for details.
