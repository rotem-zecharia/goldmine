# web-platform-tests/wpt

Test suites for Web platform specs — including WHATWG, W3C, and others

## tools

The `wpt` command provides a frontend to a variety of tools for
working with and running web-platform-tests. Some of the most useful
commands are:

* `wpt serve` - For starting the wpt http server
* `wpt run` - For running tests in a browser
* `wpt lint` - For running the lint against all tests
* `wpt manifest` - For updating or generating a `MANIFEST.json` test manifest
* `wpt install` - For installing the latest release of a browser or
  webdriver server on the local machine.
* `wpt serve-wave` - For starting the wpt http server and the WAVE test runner.
For more details on how to use the WAVE test runner see the [documentation](./tools/wave/docs/usage/usage.md).

<span id="windows-notes">Windows Notes</span>
=============================================

On Windows `wpt` commands must be prefixed with `python` or the path
to the python binary (if `python` is not in your `%PATH%`).

```bash
python wpt [command]
```

Alternatively, you may also use
[Bash on Ubuntu on Windows](https://msdn.microsoft.com/en-us/commandline/wsl/about)
in the Windows 10 Anniversary Update build, then access your windows
partition from there to launch `wpt` commands.

Please make sure git and your text editor do not automatically convert
line endings, as it will cause lint errors. For git, please set
`git config core.autocrlf false` in your working tree.

Publication
===========

The master branch is automatically synced to [wpt.live](https://wpt.live/) and
[w3c-test.org](https://w3c-test.org/).

Contributing
============

Save the Web, Write Some Tests!

Absolutely everyone is welcome to contribute to test development. No
test is too small or too simple, especially if it corresponds to
something for which you've noted an interoperability bug in a browser.

The way to contribute is just as usual:

* Fork this repository (and make sure you're still relatively in sync
  with it if you forked a while ago).
* Create a branch for your changes:
  `git checkout -b topic`.
* Make your changes.
* Run `./wpt lint` as described above.
* Commit locally and push that to your repo.
* Create a pull request based on the above.

Issues with web-platform-tests
------------------------------

If you spot an issue with a test and are not comfortable providing a
pull request per above to fix it, please
[file a new issue](https://github.com/web-platform-tests/wpt/issues/new).
Thank you!
