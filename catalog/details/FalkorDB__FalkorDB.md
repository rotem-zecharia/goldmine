# FalkorDB/FalkorDB

A super fast Graph Database uses GraphBLAS under the hood for its sparse adjacency matrix graph representation. Our goal is to provide the best Knowledge Graph for LLM (GraphRAG).

## features

Our goal is to build a high-performance Knowledge Graph tailored for Large Language Models (LLMs), prioritizing exceptionally low latency to ensure fast and efficient information delivery through our Graph Database.

🆕 [FalkorDB](https://www.falkordb.com/) is the first **queryable [Property Graph](https://github.com/opencypher/openCypher/blob/master/docs/property-graph-model.adoc) database to leverage sparse matrices** for representing the [adjacency matrix](https://en.wikipedia.org/wiki/Adjacency_matrix) in graphs and [linear algebra](https://en.wikipedia.org/wiki/Adjacency_matrix) for querying.

## installation

The easiest way to get started is using the development container, which includes all dependencies pre-installed:

1. Install [Docker](https://docs.docker.com/get-docker/) and [VS Code](https://code.visualstudio.com/)
2. Install the [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)
3. Open this project in VS Code
4. Click "Reopen in Container" when prompted (or press F1 and select "Dev Containers: Reopen in Container")
5. Wait for the container to build (first time takes ~10-15 minutes)
6. Start developing! All dependencies are ready to use.

See [.devcontainer/README.md](.devcontainer/README.md) for more details.
