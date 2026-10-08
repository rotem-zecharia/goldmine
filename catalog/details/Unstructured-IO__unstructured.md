# Unstructured-IO/unstructured

Convert documents to structured data effortlessly. Unstructured is open-source ETL solution for transforming complex documents into clean, structured formats for language models. Visit our website to 

## installation

There are several ways to use the `unstructured` library:
* [Run the library in a container](https://github.com/Unstructured-IO/unstructured#run-the-library-in-a-container) or
* Install the library
    1. [Install from PyPI](https://github.com/Unstructured-IO/unstructured#installing-the-library)
    2. [Install for local development](https://github.com/Unstructured-IO/unstructured#installation-instructions-for-local-development)
* For installation with `conda` on Windows system, please refer to the [documentation](https://unstructured-io.github.io/unstructured/installing.html#installation-with-conda-on-windows)

### Run the library in a container

The following instructions are intended to help you get up and running using Docker to interact with `unstructured`.
See [here](https://docs.docker.com/get-docker/) if you don't already have docker installed on your machine.

NOTE: we build multi-platform images to support both x86_64 and Apple silicon hardware. `docker pull` should download the corresponding image for your architecture, but you can specify with `--platform` (e.g. `--platform linux/amd64`) if needed.

We build Docker images for all pushes to `main`. We tag each image with the corresponding short commit hash (e.g. `fbc7a69`) and the application version (e.g. `0.5.5-dev1`). We also tag the most recent image with `latest`. To leverage this, `docker pull` from our image repository.

```bash
docker pull downloads.unstructured.io/unstructured-io/unstructured:latest
```

Once pulled, you can create a container from this image and shell to it.

```bash
# create the container
docker run -dt --name unstructured downloads.unstructured.io/unstructured-io/unstructured:latest

# this will drop you into a bash shell where the Docker image is running
docker exec -it unstructured bash
```

You can also build your own Docker image. Note that the base image is `wolfi-base`, which is
updated regularly. If you are building the image locally, it is possible `docker-build` could
fail due to upstream changes in `wolfi-base`.

If you only plan on parsing one type of data you can speed up building the image by commenting out some
of the packages/requirements necessary for other data types. See Dockerfile to know which lines are necessary
for your use case.

```bash
make docker-build

# this will drop you into a bash shell where the Docker image is running
make docker-start-bash
```

Once in the running container, you can try things directly in Python interpreter's interactive mode.
```bash
# this will drop you into a python console so you can run the below partition functions
python3

>>> from unstructured.partition.pdf import partition_pdf
>>> elements = partition_pdf(filename="example-docs/layout-parser-paper-fast.pdf")

>>> from unstructured.partition.text import partition_text
>>> elements = partition_text(filename="example-docs/fake-text.txt")
```

### Installing the library
Use the following instructions to get up and running with `unstructured` and test your
installation.

- Install the Python SDK to support all document types with `pip install "unstructured[all-docs]"`
  - For plain text files, HTML, XML, JSON and Emails that do not require any extra dependencies, you can run `pip install unstructured`
  - To process other doc types, you can install the extras required for those documents, such as `pip install "unstructured[docx,pptx]"`
- Install the following system dependencies if they are not already available on your system.
  Depending on what document types you're parsing, you may not need all of these.
    - `libmagic-dev` (filetype detection)
    - `poppler-utils` (images and PDFs)
    - `tesseract-ocr` (images and PDFs, install `tesseract-lang` for additional language support)
    - `libreoffice` (MS Office docs)
    - `pandoc` is bundled automatically via the `pypandoc-binary` Python package (no system install needed)

- For suggestions on how to install on the Windows and to learn about dependencies for other features, see 
