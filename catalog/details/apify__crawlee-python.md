# apify/crawlee-python

Crawlee—A web scraping and browser automation library for Python to build reliable crawlers. Extract data for AI, LLMs, RAG, or GPTs. Download HTML, PDF, JPG, PNG, and other files from websites. Works

## installation

We recommend visiting the [Introduction tutorial](https://crawlee.dev/python/docs/introduction) in Crawlee documentation for more information.

Crawlee is available as [`crawlee`](https://pypi.org/project/crawlee/) package on PyPI. This package includes the core functionality, while additional features are available as optional extras to keep dependencies and package size minimal.

To install Crawlee with all features, run the following command:

```sh
python -m pip install 'crawlee[all]'
```

Then, install the [Playwright](https://playwright.dev/) dependencies:

```sh
playwright install
```

Verify that Crawlee is successfully installed:

```sh
python -c 'import crawlee; print(crawlee.__version__)'
```

For detailed installation instructions see the [Setting up](https://crawlee.dev/python/docs/introduction/setting-up) documentation page.

## tools

Here are some practical examples to help you get started with different types of crawlers in Crawlee. Each example demonstrates how to set up and run a crawler for specific use cases, whether you need to handle simple HTML pages or interact with JavaScript-heavy sites. A crawler run will create a `storage/` directory in your current working directory.

## features

Why Crawlee is the preferred choice for web scraping and crawling?
