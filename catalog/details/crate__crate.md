# crate/crate

CrateDB is a distributed and scalable SQL database for storing and analyzing massive amounts of data in near real-time, even with complex queries. It is PostgreSQL-compatible, and based on Lucene.

## features

- Use `standard SQL`_ via the `PostgreSQL wire protocol`_ or an `HTTP API`_.

- Dynamic table schemas and queryable objects provide
  document-oriented features in addition to the relational features of SQL.

- Support for time-series data, real-time full-text search, geospatial data
  types and search capabilities.

- Horizontally scalable, highly available and fault-tolerant clusters that run
  very well in virtualized and containerized environments.

- Extremely fast distributed query execution.

- Auto-partitioning, auto-sharding, and auto-replication.

- Self-healing and auto-rebalancing.

- `User-defined functions`_ (UDFs) can be used to extend the functionality of CrateDB.


Screenshots
===========

CrateDB provides an `Admin UI`_:

.. image:: crate-admin.gif
    :alt: Screenshots of the CrateDB Admin UI


Try CrateDB
===========

Run CrateDB via the official `Docker Image`_:

.. code-block:: console

    sh$ docker run --publish 4200:4200 --publish 5432:5432 --env CRATE_HEAP_SIZE=1g crate '-Cdiscovery.type=single-node'

Or visit the `installation documentation`_ to see all the available download and
install options.

Once you're up and running, head over to the `introductory docs`_. To interact
with CrateDB, you can use the Admin UI `sql console`_ or the `CrateDB shell`_
CLI tool. Alternatively, review the list of recommended `clients and tools`_
that work with CrateDB.

For container-specific documentation, check out the `CrateDB on Docker how-to
guide`_ or the `CrateDB on Kubernetes how-to guide`_.


Contributing
============

This project is primarily maintained by `Crate.io`_, but we welcome community
contributions!

See the `developer docs`_ and the `contribution docs`_ for more information.


Security
========

The CrateDB team and community take security bugs seriously. We appreciate your
efforts to `responsibly disclose`_ your findings, and will make every effort to
acknowledge your contributions.

If you think you discovered a security flaw, please follow the guidelines at
`SECURITY.md`_.


Help
====

Looking for more help?

- Try one of our `beginner tutorials`_, `how-to guides`_, or consult the
  `reference manual`_.

- Check out our `support channels`_.

- `Crate.io`_ also offers `CrateDB Cloud`_, a fully-managed *CrateDB Database
  as a Service* (DBaaS). The `CrateDB Cloud Tutorials`_ will get you started.


.. _Admin UI: https://cratedb.com/docs/crate/admin-ui/
.. _AWS: https://cratedb.com/docs/crate/tutorials/en/latest/cloud/aws/index.html
.. _Azure: https://cratedb.com/docs/crate/tutorials/en/latest/cloud/azure/index.html
.. _beginner tutorials: https://cratedb.com/docs/crate/tutorials/
.. _benefits: https://cratedb.com/product#compare
.. _clients and tools: https://cratedb.com/docs/crate/clients-tools/
.. _containerization: https://cratedb.com/docs/crate/tutorials/en/latest/containers/docker.html
.. _contribution docs: CONTRIBUTING.rst
.. _Crate.io: https://cratedb.com/company/team
.. _CrateDB clients and tools: https://cratedb.com/docs/crate/clients-tools/
.. _CrateDB Cloud Tutorials: https://cratedb.com/docs/cloud/
.. _CrateDB Cloud: https://cratedb.com/product/pricing
.. _CrateDB on Docker how-to guide: https://cratedb.com/docs/crate/tutorials/en/latest/containers/docker.html
.. _CrateDB on Kubernetes how-to guide: https://cratedb.com/docs/crate/tutorials/en/latest/containers/kubernetes/index.html
.. _CrateDB shell: https://cratedb.com/docs/crate/crash/
.. _developer docs: devs/docs/index.rst
.. _Docker image: https://hub.docker.com/_/crate/
.. _document-oriented: https://en.wikipedia.org/wiki/Document-oriented_database
.. _Dynamic table schemas: https://cratedb.com/docs/crate/reference/en/master/general/ddl/column-policy.html
.. _fulltext search: https://cratedb.com/docs/crate/reference/en/latest/general/dql/fulltext.html
.. _geospatial features: https://cratedb.com/docs/crate/reference/en/master/general/dql/geo.html
.. _how-to guides: https://cratedb.com/docs/crate/howtos/
.. _HTTP API: https://cr
