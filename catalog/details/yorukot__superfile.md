# yorukot/superfile

Pretty fancy and modern terminal file manager

## installation

### macOS and Linux

```bash
bash -c "$(curl -sLo- https://superfile.dev/install.sh)"
```

If you want to inspect the script, see : [install.sh](./website/public/install.sh)

### Windows

#### Powershell

```powershell
powershell -ExecutionPolicy Bypass -Command "Invoke-Expression ((New-Object System.Net.WebClient).DownloadString('https://superfile.dev/install.ps1'))"
```

If you want to inspect the script, see : [install.ps1](./website/public/install.ps1)

#### [Winget](https://winget.run/)

```powershell
winget install --id yorukot.superfile
```

#### [Scoop](https://scoop.sh/)

```
scoop install superfile
```

### More installation methods

[Click me to check on how to install](https://superfile.dev/getting-started/installation/)

## Build

You can build the source code yourself by using these steps:

**Requirements**

- [golang](https://go.dev/doc/install)

**Build Steps**

Clone this repository using the following command:

```
git clone https://github.com/yorukot/superfile.git --depth=1
```

Enter the downloaded directory:

```bash
cd superfile
```

### For macOS/Linux

Run the `build.sh` file:

```bash
./build.sh
```

Add the binary file to your $PATH, e.g., in `/usr/local/bin`:

```bash
sudo mv ./bin/spf /usr/local/bin
```

### For Windows

```bash
go build -o bin/spf.exe
```

Edit System Environment Variables and add superfile repo's `bin` directory to your PATH

## Start superfile

```bash
spf
```

## Supported Systems

- \[x\] Linux
- \[x\] macOS
- \[x\] Windows (Not fully supported yet)

## Tutorial

After you install superfile, you can go [here](https://superfile.dev/getting-started/tutorial/) to briefly understand how to use superfile!

## Plugins

[Click me to the plugins wiki](https://superfile.dev/list/plugin-list/)

## Themes

[Click me to the theme wiki](https://superfile.dev/configure/custom-theme/)

## Hotkeys

> [!WARNING] If you are vim/nvim user please change your default hotkeys config to vim version!

[**Click me to see the hotkey wiki**](https://superfile.dev/configure/custom-hotkeys/)

## Notes

We have an auto update functionality, that fetches superfile's latest released version from github (if last timestamp of last version check was less than 24 hours) and prints a prompt to user, if there is a newer version available.

You can turn this off, by setting `auto_check_update` to false in superfile config. [**Click me to see the config wiki**](https://superfile.dev/configure/superfile-config/)

## Troubleshooting

[**Click me to see common problem fix**](https://superfile.dev/troubleshooting/)

## Uninstalling

### macOS and Linux

```bash
bash -c "$(curl -sLo- https://superfile.dev/uninstall.sh)"
```

If you want to inspect the script, see : [uninstall.sh](./website/public/uninstall.sh)

### Windows

To uninstall superfile on Windows, use this powershell script.

```powershell
powershell -ExecutionPolicy Bypass -Command "Invoke-Expression ((New-Object System.Net.WebClient).DownloadString('https://superfile.dev/uninstall.ps1'))"
```

## Contributing

If you want to contribute please follow the [contribution guide](./CONTRIBUTING.md)

[**Click me to see changelog**](https://superfile.dev/changelog)

## Thanks

### Support

- a Star on my GitHub repository would be nice 🌟
- You can buy a coffee for me 💖

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/G2G1JEGGC)

### Core maintainer

> We welcome anyone who wants to become a core maintainer. Feel free to reach out!

- **[@yorukot](https://github.com/yorukot)** - Original author and maintainer
- **[@lazysegtree](https://github.com/lazysegtree)** - Core maintainer

### Contributors

**Thanks to all the contributors for making this project even greater!**

<a href="https://github.com/yorukot/superfile/graphs/contributors">
  <img src="https://gthanks.yorukot.me/image?target=yorukot%2Fsuperfile" />
</a>

### Powered by

<a href="https://jb.gg/OpenSource"><img alt="JetBrains logo" align="right" width="200" src="https://resources.jet
