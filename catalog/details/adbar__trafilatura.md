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
