# haifengl/smile

Statistical Machine Intelligence & Learning Engine

## features

| Area | Highlights |
|---|---|
| **LLM** | LLaMA-3 inference, tiktoken BPE tokenizer, OpenAI-compatible REST server, SSE chat streaming |
| **Deep Learning** | LibTorch/GPU backend, EfficientNet-V2 image classification, custom layer API |
| **Classification** | SVM, Decision Trees, Random Forest, AdaBoost, Gradient Boosting, Logistic Regression, Neural Networks, RBF Networks, MaxEnt, KNN, Naïve Bayes, LDA/QDA/RDA |
| **Regression** | SVR, Gaussian Process, Regression Trees, GBDT, Random Forest, RBF, OLS, LASSO, ElasticNet, Ridge |
| **Clustering** | BIRCH, CLARANS, DBSCAN, DENCLUE, Deterministic Annealing, K-Means, X-Means, G-Means, Neural Gas, Growing Neural Gas, Hierarchical, SIB, SOM, Spectral, Min-Entropy |
| **Manifold Learning** | IsoMap, LLE, Laplacian Eigenmap, t-SNE, UMAP, PCA, Kernel PCA, Probabilistic PCA, GHA, Random Projection, ICA |
| **Feature Engineering** | Genetic Algorithm selection, Ensemble selection, TreeSHAP, SNR, Sum-Squares ratio, data transformations, formula API |
| **NLP** | Sentence / word tokenization, Bigram test, Phrase & Keyword extraction, Stemmer, POS tagging, Relevance ranking |
| **Association Rules** | FP-growth frequent itemset mining |
| **Sequence Learning** | Hidden Markov Model, Conditional Random Field |
| **Nearest Neighbor** | BK-Tree, Cover Tree, KD-Tree, SimHash, LSH |
| **Numerical Methods** | Linear algebra, numerical optimization (BFGS, L-BFGS), interpolation, wavelets, RBF, distributions, hypothesis tests |
| **Visualization** | Swing plots (scatter, line, bar, box, histogram, surface, heatmap, contour, …) and declarative Vega-Lite charts |

---

## Module Map

Each module has its own detailed user guide.  Click the **README** link for
the module overview, or drill into individual topic guides.

### `base/` — Foundation
> Data structures, math, linear algebra, statistical utilities, I/O

| Document | Topics |
|---|---|
| [README](base/README.md) | Module overview and dependency setup |
| [DATA_FRAME.md](base/DATA_FRAME.md) | DataFrame API — creation, selection, transformation |
| [DATA_IO.md](base/DATA_IO.md) | CSV, JSON, Parquet, Arrow, JDBC, Avro readers/writers |
| [DATA_TRANSFORMATION.md](base/DATA_TRANSFORMATION.md) | Scalers, encoders, imputers, feature transforms |
| [DATASET.md](base/DATASET.md) | Built-in benchmark and real-world datasets |
| [FORMULA.md](base/FORMULA.md) | R-style formula language for model matrices |
| [DISTRIBUTIONS.md](base/DISTRIBUTIONS.md) | Probability distributions (Normal, Poisson, Beta, …) |
| [HYPOTHESIS_TESTING.md](base/HYPOTHESIS_TESTING.md) | t-test, chi-squared, ANOVA, KS-test, … |
| [DISTANCES.md](base/DISTANCES.md) | Euclidean, Mahalanobis, Hamming, edit distance, … |
| [NEAREST_NEIGHBOR.md](base/NEAREST_NEIGHBOR.md) | KD-Tree, Cover Tree, BK-Tree, LSH |
| [KERNELS.md](base/KERNELS.md) | Gaussian, polynomial, Laplacian, and other kernel functions |
| [RBF.md](base/RBF.md) | Radial basis function networks |
| [INTERPOLATION.md](base/INTERPOLATION.md) | Linear, cubic spline, bilinear, bicubic |
| [GRAPH.md](base/GRAPH.md) | Adjacency list/matrix graph, BFS/DFS, spanning trees |
| [SORT.md](base/SORT.md) | Quick sort, heap sort, counting sort, index sort |
| [HASH.md](base/HASH.md) | Locality-sensitive hashing, SimHash |
| [RNG.md](base/RNG.md) | Random number generators, sampling, permutations |
| [BFGS.md](base/BFGS.md) | L-BFGS and BFGS numerical optimizers |
| [ICA.md](base/ICA.md) | Independent Component Analysis |
| [TENSOR.md](base/TENSOR.md) | N-dimensional array (CPU tensor without LibTorch) |
| [WAVELET.md](base/WAVELET.md) | DWT, CWT, and wavelet families |
| [GAP.md](base/GAP.md) | GAP statistic for optimal cluster count estimation |
| [COMPRESSED_SENSING.md](base/COMPRESSED_SENSING.md) | Compressed sensing and basis pursuit |

### `core/` — Machine Learning Algorithms
> Classification, regression, clustering, manifold learning, and more

| Document | Topics |
|---|---|
| [README](core/README.md) | Module overview |
| [CLAS

## tools

> Idiomatic Scala shim — concise wrappers, symbolic operators, Scala collections integration

| Document | Topics |
|---|---|
| [README](scala/README.md) | API overview, `smile.classification`, `smile.regression`, `smile.clustering`, `smile.plot` in Scala |

### `kotlin/` — Kotlin API
> Idiomatic Kotlin shim — extension functions, named parameters, builder DSLs

| Document | Topics |
|---|---|
| [README](kotlin/README.md) | API overview, extension functions, Kotlin-style builders |
| [packages.md](kotlin/packages.md) | Full package-by-package listing of all Kotlin extension functions |

### `json/` — JSON Library (Scala)
> Lightweight zero-dependency JSON library for Scala with a clean DSL

| Document | Topics |
|---|---|
| [README](json/README.md) | Parsing, building, pattern matching, path navigation, serialization |

### `spark/` — Apache Spark Integration
> Use SMILE models inside Spark ML pipelines

| Document | Topics |
|---|---|
| [README](spark/README.md) | `SmileTransformer`, `SmileClassifier`, `SmileRegressor`; training and scoring in Spark DataFrames |

---

## installation

### Maven

```xml
<!-- Core ML algorithms -->
<dependency>
  <groupId>com.github.haifengl</groupId>
  <artifactId>smile-core</artifactId>
  <version>6.3.0</version>
</dependency>

<!-- Deep learning + LLMs (requires LibTorch) -->
<dependency>
  <groupId>com.github.haifengl</groupId>
  <artifactId>smile-deep</artifactId>
  <version>6.3.0</version>
</dependency>

<!-- Natural language processing -->
<dependency>
  <groupId>com.github.haifengl</groupId>
  <artifactId>smile-nlp</artifactId>
  <version>6.3.0</version>
</dependency>

<!-- Data visualization -->
<dependency>
  <groupId>com.github.haifengl</groupId>
  <artifactId>smile-plot</artifactId>
  <version>6.3.0</version>
</dependency>
```

### SBT (Scala)

```scala
libraryDependencies += "com.github.haifengl" %% "smile-scala" % "6.3.0"
```

### Gradle (Kotlin)

```kotlin
dependencies {
    implementation("com.github.haifengl:smile-kotlin:6.3.0")
}
```

### Native Libraries (BLAS / LAPACK)

Several algorithms (manifold learning, Gaussian Process, MLP, some clustering)
require BLAS and LAPACK.

**Linux (Ubuntu / Debian)**
```shell
sudo apt update
sudo apt install libopenblas-dev libarpack2-dev
```

**macOS (Homebrew)**
```shell
brew install arpack
# If macOS SIP strips DYLD_LIBRARY_PATH, create a symlink to the dylib in your working dir:
ln -s /opt/homebrew/lib/libarpack.dylib .
```

**Windows** — pre-built DLLs are included in the `bin/` directory of the
[release package](https://github.com/haifengl/smile/releases).
Add that directory to `PATH`.

**GPU (CUDA)** — make sure the LibTorch CUDA native libraries are on
PATH (Windows) or LD_LIBRARY_PATH (Linux).

---

## Quick Start

```java
import smile.classification.RandomForest;
import smile.data.formula.Formula;
import smile.io.Read;

// Load data
var data = Read.csv("src/test/resources/iris.csv");

// Train a random forest
var forest = RandomForest.fit(Formula.lhs("species"), data);

// Predict
int label = forest.predict(data.get(0));
System.out.println("Predicted class: " + label);
```

For deep learning and LLM examples, see [deep/README.md](deep/README.md).
For visualization examples, see [plot/README.md](plot/README.md).

---

## SMILE Studio

SMILE Studio is an agentic IDE for data science using Python or [SMILE](https://haifengl.github.io/) on JVM.
See [studio/README.md](studio/README.md) for full documentation.

Download a pre-packaged release from the
[releases page](https://github.com/haifengl/smile/releases), then:

```shell
path/to/smile/bin/setup      # install required native dependencies
path/to/smile/bin/smile      # launch SMILE Studio from your project directory
```

Other entry points:

| Command         | Description                                    |
|-----------------|------------------------------------------------|
| `smile`         | Desktop agentic IDE                            |
| `smile shell`   | Java REPL with all SMILE packages pre-imported |
| `smile scala`   | Scala REPL                                     |
| `smile train`   | Train a supervised learning model              |
| `smile predict` | Predict on a file using a saved model          |
| `smile serve`   | Start the LLM inference server                 |

To increase the JVM heap:
```shell
path/to/smile/bin/smile -J-Xmx30G
```

---

## Model Serialization

Most SMILE models implement `java.io.Serializable`.  You can serialize a
trained model to disk and load it in a production environment or inside a
Spark job:

```java
// Save
try (var out = new ObjectOutputStream(new FileOutputStream("model.ser"))) {
    out.writeObject(forest);
}

// Load
try (var in = new ObjectInputStream(new FileInputStream("model.ser"))) {
    var loaded = (RandomForest) in.readObject();
}
```

---

## Visualization

SMILE provides two visualization layers:

- **`smile.plot.swing`** — Swing-based interactive 2D/3D plots.  See [plot/README.md](plot/README.md).
- **`smile.plot.vega`** — Declarative Vega-Lite charts for browsers and Jupyter.  See [plot/VEGA.md](plo
