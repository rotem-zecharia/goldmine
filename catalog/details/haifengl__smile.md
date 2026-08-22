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

## tools

> Idiomatic Scala shim — concise wrappers, symbolic operators, Scala collections integration

| Document | Topics |
|---|---|
| [README](scala/README.md) | API overview, `smile.classification`, `smile.regression`, `smile.clustering`, `smile.plot` in Scala |

## installation

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
