# inlife/nexrender

📹 Data-driven render automation for After Effects

## features

* data-driven, dynamic, personalized video rendering
* automated video management, processing, and delivery
* network-oriented project structure, render farm
* highly modular nature, extensive plugin support
* works only in cli mode, never launches After Effects GUI application
* does not require licenses for Adobe After Effects on any worker machine
* free to use and open source

### How it works

* rendering: It uses Adobe After Effects' aerender command-line interface application.
* compositing: It creates a temporary folder, copies project and replaces assets with provided ones.
* personalization: It uses AE's expressions, scripting, and compositing (noted above).
* scheduling: It stores projects in a local database, managed from anywhere using http api.
* network: It renders project per machine, and can be used to render several projects simultaneously.
* farm: Can be used to render a single project on several machines via Multi-Machine Sequence.

### Alternatives

The main alternative to our open-source project is [Nexrender Cloud](https://www.nexrender.com/products/cloud) - our hosted SaaS platform with easy setup, additional features and best price on the market.

Among more expensive and less flexible alternatives, there is Plainly, a tool built on **Nexrender** infrastructure that offers cloud rendering. Another noteworthy option currently available is Dataclay's Templater bot edition.

## installation

You can download binaries directly from the [releases](https://github.com/inlife/nexrender/releases) section,
or install them using npm, whichever option works better for you.

However, please note: the npm version of the binaries doesn't include all optional `plugin` packages that are covered in the usage section.
If you wish to install them as well, please do so by providing each one individually:

```
npm i -g @nexrender/cli @nexrender/action-copy @nexrender/action-encode ...
```

## tools

We will be using `nexrender-cli` binary for this example. It's recommended to download/install it if you haven't already.

>⚠ If using WSL check out [wsl support](#wsl)

## Job

A job is a single working unit in the nexrender ecosystem. It is a json document, that describes what should be done, and how it should be done.
Minimal job description always should contain a pointer onto Adobe After Effects project, which is needed to be rendered, and a composition that will be used to render.

The pointer is `src` (string) field containing a URI pointing towards specified file, followed by `composition` (string) field, containing the name of the composition that needs to be rendered.

>Note: check out [supported protocols](#protocols) for `src` field.

```json
// myjob.json
{
    "template": {
        "src": "file:///users/myuser/documents/myproject.aep",
        "composition": "main"
    }
}
```

or for remote file accessible via http

```json
// myjob.json
{
    "template": {
        "src": "http://example.com/myproject.aep",
        "composition": "main"
    }
}
```

Submitting this data to the binary will result in start of the rendering process:

```sh
$ nexrender-cli '{"template":{"src":"file:///home/documents/myproject.aep","composition":"main"}}'
```

> Note: on MacOS you might need to change the permissions for downloaded file, so it would be considered as an executable.
> You can do it by running: `$ chmod 755 nexrender-cli-macos`

or more conveniently using the `--file` option

```sh
$ nexrender-cli --file myjob.json
```

> Note: its recommended to run `nexrender-cli -h` at least once, to read all useful information about available options.

More info: [@nexrender/cli](packages/nexrender-cli)

#### After Effects 2023

Please note that for After Effects 2023, it's vital to set up an Output Module, even if you want to rely on the default output module. After Effects 2023 rendering binary (aerender) in a lot of cases will not render a composition unless it has a configured output module. Additionally, AE2023 now allows rendering directly to mp4, so consider setting up a custom value for `outputExt` as well. To do that, take a look at following example:

```json
// myjob.json
{
    "template": {
        "src": "file:///users/myuser/documents/myproject_ae2023.aep",
        "composition": "main",
        "outputModule": "H.264 - Match Render Settings - 15 Mbps",
        "outputExt": "mp4",
        "settingsTemplate": "Best Settings"
    }
}
```

### Assets

We've successfully rendered a static project file using nexrender, however, there is not much point doing that unless we
are going to add some dynamic data into the mix.

A way to implement something like that is to add an `asset` to our job definition:

```json
// myjob.json
{
    "template": {
        "src": "file:///d:/documents/myproject.aep",
        "composition": "main"
    },
    "assets": [
        {
            "src": "file:///d:/images/myimage.png",
            "type": "image",
            "layerName": "background.png"
        }
    ]
}
```

What we've done there is we told nexrender to use a particular asset as a replacement for something that we had defined in our `aep` project.
More specifically, when rendering is gonna happen, nexrender will copy/download this asset file, and attempt to find and replace `footage` entry by specified layer name.

Check out: [detailed information about footage items](#footage-items).

### Actions

You might've noticed that unless you added `--skip-cleanup` flag to our command, all rendered results will be deleted,
and a big warning message will be shown every time you attempt to run the `nexrender-cli` with our job.

The reason is that we haven't defined any actions that we need to do after we finished actual rendering. Let's fix that and add a simple one, copy.

```json
// myjob.json
{
    "template": {
        "src": "http://example.com/assets/myproject.aep",
        "composition": "main"
    },
    "assets": [
        {
      
