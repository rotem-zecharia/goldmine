# pyload/pyload

The free and open-source Download Manager written in pure Python

## features

pyLoad is a lightweight, pure-Python download manager with a modern web UI and rich plugin ecosystem. It automates downloads from one-click hosters, cloud drives, and many other sources; supports premium accounts, captcha-solving services, and link decryption; and can run headless on servers, NAS devices, or desktops. Designed for extensibility and low resource usage.

## installation

Open a terminal window and install pyLoad typing:

    pip install --pre pyload-ng[all]

To start pyLoad use the command:

    pyload

See the [usage section](#usage) for information on all available options.

If you want to uninstall pyLoad:

    pip uninstall pyload-ng

## tools

usage: pyload [-h] [-d] [-r] [--storagedir STORAGEDIR] [--userdir USERDIR]
                  [--tempdir TEMPDIR] [--dry-run] [--daemon] [--version]

    The free and open-source Download Manager written in pure Python

    optional arguments:
      -h, --help                    show this help message and exit
      -d, --debug                   enable debug mode
      -r, --reset                   reset default username/password
      --storagedir STORAGEDIR       use this location to save downloads
      --userdir USERDIR             use this location to store user data files
      --tempdir TEMPDIR             use this location to store temporary files
      --dry-run                     test start-up and exit
      --daemon                      run as daemon
      --version                     show program's version number and exit

To start pyLoad, type the command:

    pyload

This will create the following directories (if they don't exist already):

-   `~/Downloads/pyLoad`: where downloads will be saved.
-   `~/.pyload`: where user data and configuration files are stored.
-   `<TMPDIR>/pyLoad`: where temporary files are stored. `<TMPDIR>` is [platform-specific](https://docs.python.org/3/library/tempfile.html#tempfile.gettempdir).

> **Note**:
> On Windows, user data and configuration files are stored in the directory `~\AppData\Roaming\pyLoad`.

## requirements

Extra dependencies are non-essential packages that enable additional features of pyLoad.

To install them you have to append a specific tag name to the installation command.

#### Available tags

-   `plugins`: includes packages used by several plugins.
-   `build`: includes packages used to [build translations](#build-translations).
-   `all`: includes both plugins and build packages.

You can use a tag in this way:

    pip install pyload-ng[plugins]

Or group more together:

    pip install pyload-ng[plugins][build]

## configuration

* Clone the repository
* Recommended: create a virtual environment for pyLoad
```
python3 -m venv .venv
source .venv/bin/activate
```
* Install pyLoad as editable install with main and test dependencies
```
pip install -e ".[test]"
```
* Run pyLoad in debug mode
```
pyload -d
```
* To run the tests locally
```
pytest tests
```
