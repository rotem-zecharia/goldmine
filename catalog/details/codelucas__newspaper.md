# codelucas/newspaper

newspaper3k is a news, full-text, and article metadata extraction in Python 3. Advanced docs:

## tools

.. image:: https://badge.fury.io/py/newspaper3k.svg
    :target: http://badge.fury.io/py/newspaper3k.svg
        :alt: Latest version

.. image:: https://travis-ci.org/codelucas/newspaper.svg
        :target: http://travis-ci.org/codelucas/newspaper/
        :alt: Build status

.. image:: https://coveralls.io/repos/github/codelucas/newspaper/badge.svg?branch=master
        :target: https://coveralls.io/github/codelucas/newspaper
        :alt: Coverage status

Inspired by `requests`_ for its simplicity and powered by `lxml`_ for its speed:

    "Newspaper is an amazing python library for extracting & curating articles."
    -- `tweeted by`_ Kenneth Reitz, Author of `requests`_

    "Newspaper delivers Instapaper style article extraction." -- `The Changelog`_

.. _`tweeted by`: https://twitter.com/kennethreitz/status/419520678862548992
.. _`The Changelog`: http://thechangelog.com/newspaper-delivers-instapaper-style-article-extraction/

**Newspaper is a Python3 library**! Or, view our **deprecated and buggy** `Python2 branch`_

.. _`Python2 branch`: https://github.com/codelucas/newspaper/tree/python-2-head

## features

- Multi-threaded article download framework
- News url identification
- Text extraction from html
- Top image extraction from html
- All image extraction from html
- Keyword extraction from text
- Summary extraction from text
- Author extraction from text
- Google trending terms extraction
- Works in 10+ languages (English, Chinese, German, Arabic, ...)

.. code-block:: pycon

    >>> import newspaper
    >>> newspaper.languages()

    Your available languages are:
    input code      full name

      ar              Arabic
      be              Belarusian
      bg              Bulgarian
      da              Danish
      de              German
      el              Greek
      en              English
      es              Spanish
      et              Estonian
      fa              Persian
      fi              Finnish
      fr              French
      he              Hebrew
      hi              Hindi
      hr              Croatian
      hu              Hungarian
      id              Indonesian
      it              Italian
      ja              Japanese
      ko              Korean
      lt              Lithuanian
      mk              Macedonian
      nb              Norwegian (Bokmål)
      nl              Dutch
      no              Norwegian
      pl              Polish
      pt              Portuguese
      ro              Romanian
      ru              Russian
      sl              Slovenian
      sr              Serbian
      sv              Swedish
      sw              Swahili
      th              Thai
      tr              Turkish
      uk              Ukrainian
      vi              Vietnamese
      zh              Chinese
