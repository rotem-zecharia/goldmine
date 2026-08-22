# autogluon/autogluon

Fast and Accurate ML in 3 Lines of Code

## installation

AutoGluon is supported on Python 3.10 - 3.13 and is available on Linux, MacOS, and Windows.

You can install AutoGluon with:

```python
pip install autogluon
```

Visit our [Installation Guide](https://auto.gluon.ai/stable/install.html) for detailed instructions, including GPU support, Conda installs, and optional dependencies.

## :zap: Quickstart

Build accurate end-to-end ML models in just 3 lines of code!

```python
from autogluon.tabular import TabularPredictor
predictor = TabularPredictor(label="class").fit("train.csv", presets="best")
predictions = predictor.predict("test.csv")
```

| AutoGluon Task      |                                                                                Quickstart                                                                                |                                                                                API                                                                                |
|:--------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------:|
| TabularPredictor    | [![Quick Start](https://img.shields.io/static/v1?label=&message=tutorial&color=grey)](https://auto.gluon.ai/stable/tutorials/tabular/tabular-quick-start.html) |                 [![API](https://img.shields.io/badge/api-reference-blue.svg)](https://auto.gluon.ai/stable/api/autogluon.tabular.TabularPredictor.html)                 |
| TimeSeriesPredictor | [![Quick Start](https://img.shields.io/static/v1?label=&message=tutorial&color=grey)](https://auto.gluon.ai/stable/tutorials/timeseries/forecasting-quick-start.html)            | [![API](https://img.shields.io/badge/api-reference-blue.svg)](https://auto.gluon.ai/stable/api/autogluon.timeseries.TimeSeriesPredictor.html) |
| MultiModalPredictor | [![Quick Start](https://img.shields.io/static/v1?label=&message=tutorial&color=grey)](https://auto.gluon.ai/stable/tutorials/multimodal/multimodal_prediction/multimodal-quick-start.html)            | [![API](https://img.shields.io/badge/api-reference-blue.svg)](https://auto.gluon.ai/stable/api/autogluon.multimodal.MultiModalPredictor.html) |

## :mag: Resources

### Hands-on Tutorials / Talks

Below is a curated list of recent tutorials and talks on AutoGluon. A comprehensive list is available [here](AWESOME.md#videos--tutorials).

| Title                                                                                                                    | Format   | Location                                                                         | Date       |
|--------------------------------------------------------------------------------------------------------------------------|----------|----------------------------------------------------------------------------------|------------|
| :tv: [Structured Foundation Models Meets AutoML](https://icml.cc/virtual/2025/46786)                                                                               | Expo Talk       | [ICML 2025](https://icml.cc/Conferences/2025)                                                                                      | 2025/07/13  |
| :tv: [AutoGluon 1.2: Advancing AutoML with Foundational Models and LLM Agents](https://neurips.cc/virtual/2024/expo-workshop/100328)                               | Expo Workshop   | [NeurIPS 2024](https://neurips.cc/Conferences/2024)                                                                                | 2024/12/10  |
| :tv: [AutoGluon: Towards No-Code Automated Machine Learning](https://www.youtube.com/watch?v=SwPq9qjaN2Q)                | Tutorial | [AutoML 2024](https://2024.automl.cc/)                                           | 2024/09/09 |
| :tv: [AutoGluon 1.0: Shattering the AutoML Ceiling with Zer
