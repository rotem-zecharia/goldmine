# treeverse/dvc

🦉 Data Versioning and ML Experiments

## installation

Please read our `Command Reference <https://dvc.org/doc/command-reference>`_ for a complete list.

A common CLI workflow includes:


+-----------------------------------+----------------------------------------------------------------------------------------------------+
| Task                              | Terminal                                                                                           |
+===================================+====================================================================================================+
| Track data                        | | ``$ git add train.py params.yaml``                                                               |
|                                   | | ``$ dvc add images/``                                                                            |
+-----------------------------------+----------------------------------------------------------------------------------------------------+
| Connect code and data             | | ``$ dvc stage add -n featurize -d images/ -o features/ python featurize.py``                     |
|                                   | | ``$ dvc stage add -n train -d features/ -d train.py -o model.p -M metrics.json python train.py`` |
+-----------------------------------+----------------------------------------------------------------------------------------------------+
| Make changes and experiment       | | ``$ dvc exp run -n exp-baseline``                                                                |
|                                   | | ``$ vi train.py``                                                                                |
|                                   | | ``$ dvc exp run -n exp-code-change``                                                             |
+-----------------------------------+----------------------------------------------------------------------------------------------------+
| Compare and select experiments    | | ``$ dvc exp show``                                                                               |
|                                   | | ``$ dvc exp apply exp-baseline``                                                                 |
+-----------------------------------+----------------------------------------------------------------------------------------------------+
| Share code                        | | ``$ git add .``                                                                                  |
|                                   | | ``$ git commit -m 'The baseline model'``                                                         |
|                                   | | ``$ git push``                                                                                   |
+-----------------------------------+----------------------------------------------------------------------------------------------------+
| Share data and ML models          | | ``$ dvc remote add myremote -d s3://mybucket/image_cnn``                                         |
|                                   | | ``$ dvc push``                                                                                   |
+-----------------------------------+----------------------------------------------------------------------------------------------------+

How DVC works
=============

    We encourage you to read our `Get Started
    <https://dvc.org/doc/get-started>`_ docs to better understand what DVC
    does and how it can fit your scenarios.

The closest *analogies* to describe the main DVC features are these:

#. **Git for data**: Store and share data artifacts (like Git-LFS but without a server) and models, connecting them with a Git repository. Data management meets GitOps!
#. **Makefiles** for ML: Describes how data or model artifacts are built from other data and code in a standard format. Now you can version your data pipelines with Git.
#. Local **experiment tracking**: Turn your machine into an ML ex
