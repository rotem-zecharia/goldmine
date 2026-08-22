# adbar/trafilatura

Python & Command-line tool to gather text and metadata on the Web: Crawling, scraping, extraction, output as CSV, JSON, HTML, MD, TXT, XML

## features

- Advanced web crawling and text discovery:
  - Support for sitemaps (TXT, XML) and feeds (ATOM, JSON, RSS)
  - Smart crawling and URL management (filtering and deduplication)

- Parallel processing of online and offline input:
  - Live URLs, efficient and polite processing of download queues
  - Previously downloaded HTML files and parsed HTML trees

- Robust and configurable extraction of key elements:
  - Main text (own rule-based extractor with jusText and readability-lxml as fallbacks)
  - Metadata (title, author, date, site name, categories and tags)
  - Formatting and structure: paragraphs, titles, lists, quotes, code, line breaks, in-line text formatting
  - Optional elements: comments, links, images, tables
  - Optional add-ons: language detection, speed optimizations

- Multiple output formats:
  - TXT and Markdown
  - CSV
  - JSON
  - HTML, XML and [XML-TEI](https://tei-c.org/)


### Evaluation

Trafilatura consistently outperforms other open-source libraries in text
extraction benchmarks. For more information see the
[benchmark section](https://trafilatura.readthedocs.io/en/latest/evaluation.html)
and the [evaluation readme](https://github.com/adbar/trafilatura/blob/master/tests/README.rst)
to run the evaluation with the latest data and packages.


#### Other evaluations

- Most efficient open-source library in *ScrapingHub*'s [article extraction benchmark](https://github.com/scrapinghub/article-extraction-benchmark)
- Best overall tool according to [Bien choisir son outil d'extraction de contenu à partir du Web](https://hal.archives-ouvertes.fr/hal-02768510v3/document)
  (Lejeune & Barbaresi 2020)
- Best single tool by ROUGE-LSum Mean F1 Page Scores in [An Empirical Comparison of Web Content Extraction Algorithms](https://webis.de/downloads/publications/papers/bevendorff_2023b.pdf)
  (Bevendorff et al. 2023)


## Documentation

[Getting started with Trafilatura](https://trafilatura.readthedocs.io/en/latest/quickstart.html)
is straightforward. For more information and detailed guides, visit
[Trafilatura's documentation](https://trafilatura.readthedocs.io/):

- [Installation](https://trafilatura.readthedocs.io/en/latest/installation.html)
- Usage:
  [On the command-line](https://trafilatura.readthedocs.io/en/latest/usage-cli.html),
  [With Python](https://trafilatura.readthedocs.io/en/latest/usage-python.html),
  [With R](https://trafilatura.readthedocs.io/en/latest/usage-r.html)
- [Core Python functions](https://trafilatura.readthedocs.io/en/latest/corefunctions.html)
- Interactive Python Notebook: [Trafilatura Overview](docs/Trafilatura_Overview.ipynb) (in the repository)
- [Tutorials and use cases](https://trafilatura.readthedocs.io/en/latest/tutorials.html)

See the [video tutorials playlist](https://www.youtube.com/watch?v=8GkiOM17t0Q&list=PL-pKWbySIRGMgxXQOtGIz1-nbfYLvqrci) (multiple languages).


## License

This package is distributed under the [Apache 2.0 license](https://www.apache.org/licenses/LICENSE-2.0.html).

Versions prior to v1.8.0 are under GPLv3+ license.


## Contributing

Contributions of all kinds are welcome. Visit the [Contributing
page](https://github.com/adbar/trafilatura/blob/master/CONTRIBUTING.md)
for more information. Bug reports can be filed on the [dedicated issue
page](https://github.com/adbar/trafilatura/issues).

Many thanks to the
[contributors](https://github.com/adbar/trafilatura/graphs/contributors)
who extended the docs or submitted bug reports, features and bugfixes!


## Support

**If you value this software or depend on it for your product, consider
sponsoring it and contributing to its codebase.** Your support
[on GitHub](https://github.com/sponsors/adbar) or [ko-fi.com](https://ko-fi.com/adbarbaresi)
will help maintain and enhance this package.


## Context

This work started as a PhD project at the crossroads of linguistics and
NLP. This expertise has been instrumental in shaping Trafilatura over
the years. Initially launched to create text databases for research purpose
