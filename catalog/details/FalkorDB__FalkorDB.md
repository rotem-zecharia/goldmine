# FalkorDB/FalkorDB

A super fast Graph Database uses GraphBLAS under the hood for its sparse adjacency matrix graph representation. Our goal is to provide the best Knowledge Graph for LLM (GraphRAG).

## features

Our goal is to build a high-performance Knowledge Graph tailored for Large Language Models (LLMs), prioritizing exceptionally low latency to ensure fast and efficient information delivery through our Graph Database.

🆕 [FalkorDB](https://www.falkordb.com/) is the first **queryable [Property Graph](https://github.com/opencypher/openCypher/blob/master/docs/property-graph-model.adoc) database to leverage sparse matrices** for representing the [adjacency matrix](https://en.wikipedia.org/wiki/Adjacency_matrix) in graphs and [linear algebra](https://en.wikipedia.org/wiki/Adjacency_matrix) for querying.

### Key Features

* **Sparse Matrix Representation**: Utilizes sparse matrices to represent adjacency matrices, optimizing storage and performance.


* **Linear Algebra Querying**: Employs linear algebra for query execution, enhancing computational efficiency.


* **Property Graph Model Compliance**: Supports nodes and relationships with attributes, adhering to the Property Graph Model.


* **OpenCypher Support:** Compatible with [OpenCypher](https://github.com/opencypher/openCypher/blob/master/docs/property-graph-model.adoc) query language, including proprietary extensions for advanced querying capabilities.

>Explore FalkorDB in action by visiting the [Demos](https://github.com/FalkorDB/FalkorDB/tree/master/demo).

## GET STARTED

### Step 1

To quickly try out FalkorDB, launch an instance using docker:

```
docker run -p 6379:6379 -p 3000:3000 -it --rm -v ./data:/var/lib/falkordb/data falkordb/falkordb
```

### Step 2

Then, open your browser and navigate to `http://localhost:3000`.


You can also interact with FalkorDB using any of the supported [Client Libraries](https://docs.falkordb.com/clients.html)

### MotoGP League Example

In this example, we'll use the [FalkorDB Python client](https://pypi.org/project/FalkorDB/) to create a small graph representing a subset of motorcycle riders and teams participating in the MotoGP league. After creating the graph, we'll query the data to explore its structure and relationships.

```python
from falkordb import FalkorDB

# Connect to FalkorDB
db = FalkorDB(host='localhost', port=6379)

# Create the 'MotoGP' graph
g = db.select_graph('MotoGP')
g.query("""CREATE (:Rider {name:'Valentino Rossi'})-[:rides]->(:Team {name:'Yamaha'}),
                  (:Rider {name:'Dani Pedrosa'})-[:rides]->(:Team {name:'Honda'}),
                  (:Rider {name:'Andrea Dovizioso'})-[:rides]->(:Team {name:'Ducati'})""")

# Query which riders represents Yamaha?
res = g.query("""MATCH (r:Rider)-[:rides]->(t:Team)
                 WHERE t.name = 'Yamaha'
                 RETURN r.name""")

for row in res.result_set:
	print(row[0])

# Prints: "Valentino Rossi"

# Query how many riders represent team Ducati ?
res = g.query("""MATCH (r:Rider)-[:rides]->(t:Team {name:'Ducati'})
                 RETURN count(r)""")

print(res.result_set[0][0])
# Prints: 1
```

## USING FALKORDB

You can call FalkorDB's commands from any Redis client. Here are several methods:

### With `redis-cli`

```sh
$ redis-cli
127.0.0.1:6379> GRAPH.QUERY social "CREATE (:person {name: 'roi', age: 33, gender: 'male', status: 'married'})"
```

### With any other client

You can interact with FalkorDB using your client's ability to send raw Redis commands.

>Note: Depending on your client of choice, the exact method for doing that may vary.

#### Example: Using FalkorDB with a Python client

This code snippet shows how to use FalkorDB with from Python using [falkordb-py](https://github.com/FalkorDB/falkordb-py):

```Python
from falkordb import FalkorDB

# Connect to FalkorDB
db = FalkorDB(host='localhost', port=6379)

# Select the social graph
g = db.select_graph('social')

reply = g.query("CREATE (:person {name:'roi', age:33, gender:'male', status:'married'})")
```

## CLIENT LIBRARIES

>Note: Some languages have client libraries that provide support for FalkorDB's commands:

### Official Clients


| Project                                        

## installation

The easiest way to get started is using the development container, which includes all dependencies pre-installed:

1. Install [Docker](https://docs.docker.com/get-docker/) and [VS Code](https://code.visualstudio.com/)
2. Install the [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)
3. Open this project in VS Code
4. Click "Reopen in Container" when prompted (or press F1 and select "Dev Containers: Reopen in Container")
5. Wait for the container to build (first time takes ~10-15 minutes)
6. Start developing! All dependencies are ready to use.

See [.devcontainer/README.md](.devcontainer/README.md) for more details.

### Manual Setup

If you prefer to set up the environment manually:

#### Build

```
cargo build
```

#### Dependencies:

GraphBLAS, LAGraph, and RediSearch must be built and installed before building this project.

##### Toolchain prerequisites

| Host | Compiler | OpenMP runtime |
| --- | --- | --- |
| macOS | `brew install llvm` (provides `clang` with OpenMP support) | `brew install libomp` |
| Linux | `clang-22` (e.g. from [apt.llvm.org](https://apt.llvm.org/)) | `apt install libomp-22-dev` |

Local builds use whatever OpenMP package is on the system — `build/libomp.sh`
is **not** required for local development. It is only invoked by the Docker
toolchain image (`build/Dockerfile`) to produce `/opt/libomp/lib/libomp.a`,
which lets the published `libfalkordb.{so,dylib}` embed libomp statically
and have no `libomp.so.5` / `libgomp.so.1` / `libomp.dylib` runtime
dependency. A locally-built artifact will dynamically link the system
libomp instead — fine for dev, but CI/Docker is the source of truth for
the self-contained image.

If you do want a self-contained local artifact (e.g. to mirror the Docker
build), run `build/libomp.sh` with a writable `PREFIX` and point
`graph/build.rs` at it via `LIBOMP_PREFIX`:

```bash
CC=$(brew --prefix llvm)/bin/clang PREFIX=$HOME/libomp ./build/libomp.sh
LIBOMP_PREFIX=$HOME/libomp cargo build
```

The script auto-detects the libomp source release from `${CC:-clang}
--version`, so it stays ABI-matched to your compiler with no manual
version arg. In Docker the same auto-detection runs against
`clang-${CLANG_MAJOR}`, eliminating the prior drift risk between the
apt-installed clang and a hand-pinned `LLVMORG_VERSION`.

##### Building GraphBLAS + LAGraph

[GraphBLAS](https://github.com/DrTimothyAldenDavis/GraphBLAS.git) and
[LAGraph](https://github.com/GraphBLAS/LAGraph.git) are built by a single
script: GraphBLAS is installed system-wide, LAGraph is emitted under
`./lagraph_lib`.

On macOS, point the script at homebrew clang first:

```bash
export CC=$(brew --prefix llvm)/bin/clang
export CXX=$(brew --prefix llvm)/bin/clang++
./graphblas.sh
```

On Linux:

```bash
CC=clang-22 CXX=clang++-22 ./graphblas.sh
```

##### Building RediSearch

```bash
./redisearch.sh
```

- pytest - create virtualenv and install tests/requirements.txt

The virtual environment should be activated before running tests.

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r tests/requirements.txt
```

### Testing

- run unit tests with `cargo test -p graph`

- run e2e and function tests with `pytest tests/test_e2e.py tests/test_functions.py -vv`

- run MVCC and concurrency tests with `pytest tests/test_mvcc.py tests/test_concurrency.py -vv`

- run flow tests with `./flow.sh`

- run tck tests with `pytest tests/tck/test_tck.py -s`

There is an option to run only part of the TCK tests and stop on the first fail

```bash
TCK_INCLUDE=tests/tck/features/expressions/list pytest tests/tck/test_tck.py -s
```

To run all passing TCK tests use:

```bash
TCK_DONE=tck_done.txt pytest tests/tck/test_tck.py -s
```

## LICENSE

Licensed under the Server Side Public License v1 (SSPLv1). See [LICENSE](LICENSE).

### Support our work

⭐️ If you find this repository helpful, please consider giving it a star!

↗️ Graph, graph database, RAG, graphrag, Ret
