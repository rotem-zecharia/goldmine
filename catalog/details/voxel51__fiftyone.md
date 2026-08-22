# voxel51/fiftyone

Refine high-quality datasets and visual AI models

## installation

As simple as:

```shell
pip install fiftyone
```

<details>
<summary>More details</summary>

### Installation options

FiftyOne supports Python 3.10 - 3.14.

For most users, we recommend installing the latest release version of FiftyOne
via `pip` as shown above.

If you want to contribute to FiftyOne or install the latest development
version, then you can also perform a [source install](#source-install).

See the [prerequisites section](#prerequisites) for system-specific setup
information.

We strongly recommend that you install FiftyOne in a
[virtual environment](https://docs.voxel51.com/installation/virtualenv.html) to
maintain a clean workspace.

Consult the
[installation guide](https://docs.voxel51.com/installation/index.html) for
troubleshooting and other information about getting up-and-running with
FiftyOne.

</details>

<div id='source-install'/>

<details>
<summary>Install from source</summary>

### Source installations

Follow the instructions below to install FiftyOne from source and build the
App.

You'll need the following tools installed:

- [Python](https://www.python.org) (3.10 - 3.14)
- [Node.js](https://nodejs.org) - on Linux, we recommend using
  [nvm](https://github.com/nvm-sh/nvm) to install an up-to-date version.
- [Yarn](https://yarnpkg.com) - once Node.js is installed, you can
  [enable Yarn](https://yarnpkg.com/getting-started/install) via
  `corepack enable`

We strongly recommend that you install FiftyOne in a
[virtual environment](https://docs.voxel51.com/installation/virtualenv.html) to
maintain a clean workspace.

If you are working in Google Colab,
[skip to here](#source-installs-in-google-colab).

First, clone the repository:

```shell
git clone https://github.com/voxel51/fiftyone
cd fiftyone
```

Then run the install script:

```shell
# Mac or Linux
bash install.sh

# Windows
.\install.bat
```

If you run into issues importing FiftyOne, you may need to add the path to the
cloned repository to your `PYTHONPATH`:

```shell
export PYTHONPATH=$PYTHONPATH:/path/to/fiftyone
```

Note that the install script adds to your `nvm` settings in your `~/.bashrc` or
`~/.bash_profile`, which is needed for installing and building the App.

### Upgrading your source installation

To upgrade an existing source installation to the bleeding edge, simply pull
the latest `develop` branch and rerun the install script:

```shell
git checkout develop
git pull

# Mac or Linux
bash install.sh

# Windows
.\install.bat
```

### Rebuilding the App

When you pull in new changes to the App, you will need to rebuild it, which you
can do either by rerunning the install script or just running `yarn build` in
the `./app` directory.

### Developer installation

If you would like to
[contribute to FiftyOne](https://github.com/voxel51/fiftyone/blob/develop/CONTRIBUTING.md),
you should perform a developer installation using the `-d` flag of the install
script:

```shell
# Mac or Linux
bash install.sh -d

# Windows
.\install.bat -d
```

Although not required, developers typically prefer to configure their FiftyOne
installation to connect to a self-installed and managed instance of MongoDB,
which you can do by following
[these simple steps](https://docs.voxel51.com/user_guide/config.html#configuring-a-mongodb-connection).

### Source installs in Google Colab

You can install from source in
[Google Colab](https://colab.research.google.com) by running the following in a
cell and then **restarting the runtime**:

```shell
%%shell

git clone --depth 1 https://github.com/voxel51/fiftyone.git
cd fiftyone

# Mac or Linux
bash install.sh

# Windows
.\install.bat
```

### Generating documentation

See the
[docs guide](https://github.com/voxel51/fiftyone/blob/develop/docs/README.md)
for information on building and contributing to the documentation.

### Uninstallation

You can uninstall FiftyOne as follows:

```shell
pip uninstall fiftyone fiftyone-brain fiftyone-db
```

</details>

<div id='prerequisites'/>

<details>
<summary>Prerequisites for

## features

- **[Native Annotation:](https://docs.voxel51.com/user_guide/annotation.html)**
  Create and edit 2D and 3D labels directly in the App or integrate with your
  favorite annotation tools — then curate, QA, and iterate, all in one
  platform.

https://github.com/user-attachments/assets/b06bcdac-d64f-4465-8668-12007dc0eeaa

- **[Visualize Complex Datasets:](https://docs.voxel51.com/user_guide/app.html)**
  Easily explore images, videos, and associated labels in a powerful visual
  interface.

https://github.com/user-attachments/assets/9dc2db88-967d-43fa-bda0-85e4d5ab6a7a

- **[Explore Embeddings:](https://docs.voxel51.com/user_guide/app.html#embeddings-panel)**
  Select points of interest and view the corresponding samples/labels.

https://github.com/user-attachments/assets/246faeb7-dcab-4e01-9357-e50f6b106da7

- **[Analyze and Improve Models:](https://docs.voxel51.com/user_guide/evaluation.html)**
  Evaluate model performance, identify failure modes, and fine-tune your
  models.

https://github.com/user-attachments/assets/8c32d6c4-51e7-4fea-9a3c-2ffd9690f5d6

- **[Advanced Data Curation:](https://docs.voxel51.com/brain.html)** Quickly
  find and fix data issues, annotation errors, and edge cases.

https://github.com/user-attachments/assets/24fa1960-c2dd-46ae-ae5f-d58b3b84cfe4

- **[Rich Integrations:](https://docs.voxel51.com/integrations/index.html)**
  Works with popular deep learning libraries like PyTorch, Hugging Face,
  Ultralytics, and more.

https://github.com/user-attachments/assets/de5f25e1-a967-4362-9e04-616449e745e5

- **[Open and Extensible:](https://docs.voxel51.com/plugins/index.html)**
  Customize and extend FiftyOne to fit your specific needs.

https://github.com/user-attachments/assets/c7ed496d-0cf7-45d6-9853-e349f1abd6f8

<div id='getting-started'/>

## <img src="https://user-images.githubusercontent.com/25985824/106288517-2422e000-6216-11eb-871d-26ad2e7b1e59.png" height="20px"> &nbsp; documentation &nbsp; 🪪

Check out these resources to get up and running with FiftyOne:

| [Getting Started Guides](https://docs.voxel51.com/getting_started_guides/index.html) | [Tutorials](https://docs.voxel51.com/tutorials/index.html) | [Recipes](https://docs.voxel51.com/recipes/index.html) | [User Guide](https://docs.voxel51.com/user_guide/index.html) | [Examples](https://github.com/voxel51/fiftyone-examples) | [API Reference](https://docs.voxel51.com/api/fiftyone.html) | [CLI Reference](https://docs.voxel51.com/cli/index.html) |
| ------------------------------------------------------------------------------------ | ---------------------------------------------------------- | ------------------------------------------------------ | ------------------------------------------------------------ | -------------------------------------------------------- | ----------------------------------------------------------- | -------------------------------------------------------- |

Full documentation is available at [fiftyone.ai](https://fiftyone.ai).

</div>

<div id='additional-resources'>

## <img src="https://user-images.githubusercontent.com/25985824/106288517-2422e000-6216-11eb-871d-26ad2e7b1e59.png" height="20px"> &nbsp; additional resources &nbsp; 🚁

| [FiftyOne Enterprise](https://voxel51.com/enterprise) | [Building Plugins](https://docs.voxel51.com/plugins/index.html) | [Vector Search](https://voxel51.com/blog/the-computer-vision-interface-for-vector-search) | [Dataset Zoo](https://docs.voxel51.com/dataset_zoo/index.html) | [Model Zoo](https://docs.voxel51.com/model_zoo/index.html) | [FiftyOne Brain](https://docs.voxel51.com/brain.html) | [VoxelGPT](https://github.com/voxel51/voxelgpt) |
| ----------------------------------------------------- | --------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | -------------------------------------------------------------- | ---------------------------------------------------------- | ---
