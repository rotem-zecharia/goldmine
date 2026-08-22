# Unstructured-IO/unstructured

Convert documents to structured data effortlessly. Unstructured is open-source ETL solution for transforming complex documents into clean, structured formats for language models. Visit our website to 

## installation

1. **Pick your MCP client.** Transform works with virtually any MCP-compatible host or agent framework — Claude Code, Cursor, Codex CLI and more.

2. **Add the Transform MCP server** to your client's MCP configuration (via the CLI `mcp add` command or the client's MCP settings/config file, depending on the tool).

3. **Authenticate once** when your client prompts you. Sign in, and the Transform tools become available to your agent on its next message.

4. **Point your agent at a file.** Drag and drop or reference a local file or URL. Transform handles 60+ formats (PDFs, emails, images, scanned files, and more).

5. **Describe what you need in plain language.** Tell the agent your intent (e.g. "parse and chunk this contract for a vector store") and Transform partitions, enriches, chunks, and embeds the file, returning structured data ready to use. 

15,000 free pages a month, 3 cents per page after!

📄 Full docs: https://docs.unstructured.io/transform/overview


## Unstructured Pipelines

Ready to move your data processing pipeline to production, and take advantage of advanced features? Check out [Unstructured Pipelines](https://unstructured.io/enterprise). In addition to better processing performance, take advantage of chunking, embedding, and image and table enrichment generation, all from a low code UI or an API. [Request a demo](https://unstructured.io/?modal=contact-sales) from our sales team to learn more about how to get started.

## :eight_pointed_black_star: Quick Start

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

Once in the running container, you can try things directly in Python interpreter's int
