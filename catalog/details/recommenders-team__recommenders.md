# recommenders-team/recommenders

Best Practices on Recommendation Systems

## installation

We recommend [uv](https://docs.astral.sh/uv/) for environment management (10-100x faster than conda/pip), and [VS Code](https://code.visualstudio.com/) for development. To install the recommenders package and run an example notebook on Linux/WSL:

```bash
# 1. Install gcc if it is not installed already. On Ubuntu, this could done by using the command
# sudo apt install gcc

# 2. Install uv (if not already installed)
curl -LsSf https://astral.sh/uv/install.sh | sh

## configuration

uv venv ~/.venvs/recommenders --python 3.11
source ~/.venvs/recommenders/bin/activate

## tools

#   b. Select Jupyter kernel "Python (recommenders)";
#   c. Run the notebook.
```

For more information about setup on other platforms (e.g., Windows and macOS) and different configurations (e.g., GPU, Spark and experimental features), see the [Setup Guide](SETUP.md).

In addition to the core package, several extras are also provided, including:
+ `[gpu]`: Needed for running GPU models.
+ `[spark]`: Needed for running Spark models.
+ `[dev]`: Needed for development for the repo.
+ `[all]`: `[gpu]`|`[spark]`|`[dev]`
+ `[experimental]`: Models that are not thoroughly tested and/or may require additional steps in installation.

## Algorithms

The table below lists the recommendation algorithms currently available in the repository. Notebooks are linked under the Example column as Quick start, showcasing an easy to run example of the algorithm, or as Deep dive, explaining in detail the math and implementation of the algorithm.

| Algorithm | Type | Description | Example |
|-----------|------|-------------|---------|
| Alternating Least Squares (ALS) | Collaborative Filtering | Matrix factorization algorithm for explicit or implicit feedback in large datasets, optimized for scalability and distributed computing capability. It works in the PySpark environment. | [Quick start](examples/00_quick_start/als_movielens.ipynb) / [Deep dive](examples/02_model_collaborative_filtering/als_deep_dive.ipynb) |
| Attentive Asynchronous Singular Value Decomposition (A2SVD)<sup>*</sup> | Collaborative Filtering | Sequential-based algorithm that aims to capture both long and short-term user preferences using attention mechanism. It works in the CPU/GPU environment. | [Quick start](examples/00_quick_start/sequential_recsys_amazondataset.ipynb) |
| Cornac/Bayesian Personalized Ranking (BPR) | Collaborative Filtering | Matrix factorization algorithm for predicting item ranking with implicit feedback. It works in the CPU environment. | [Deep dive](examples/02_model_collaborative_filtering/cornac_bpr_deep_dive.ipynb) |
| Cornac/Bilateral Variational Autoencoder (BiVAE) | Collaborative Filtering | Generative model for dyadic data (e.g., user-item interactions). It works in the CPU/GPU environment. | [Deep dive](examples/02_model_collaborative_filtering/cornac_bivae_deep_dive.ipynb) |
| Convolutional Sequence Embedding Recommendation (Caser) | Collaborative Filtering | Algorithm based on convolutions that aim to capture both user’s general preferences and sequential patterns. It works in the CPU/GPU environment. | [Quick start](examples/00_quick_start/sequential_recsys_amazondataset.ipynb) |
| Deep Knowledge-Aware Network (DKN)<sup>*</sup> | Content-Based Filtering | Deep learning algorithm incorporating a knowledge graph and article embeddings for providing news or article recommendations. It works in the CPU/GPU environment. | [Quick start](examples/00_quick_start/dkn_MIND.ipynb) / [Deep dive](examples/02_model_content_based_filtering/dkn_deep_dive.ipynb) |
| Extreme Deep Factorization Machine (xDeepFM)<sup>*</sup> | Collaborative Filtering | Deep learning based algorithm for implicit and explicit feedback with user/item features. It works in the CPU/GPU environment. | [Quick start](examples/00_quick_start/xdeepfm_criteo.ipynb) |
| Embedding Dot Bias | Collaborative Filtering | General purpose algorithm with embeddings and biases for users and items. It works in the CPU/GPU environment. | [Quick start](examples/00_quick_start/embdotbias_movielens.ipynb) |
| LightFM/Factorization Machine | Collaborative Filtering | Factorization Machine algorithm for both implicit and explicit feedbacks. It works in the CPU environment. | [Quick start](examples/02_model_collaborative_filtering/lightfm_deep_dive.ipynb) |
| LightGBM/Gradient Boosting Tree<sup>*</sup> | Content-Based Filtering | Gradient Boosting Tree algorithm for fast training and low memory usage in content-based problems. It works in the CPU/GPU/PySpark environments. | [Quick start in CPU](examples/00_q
