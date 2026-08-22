# VictoriaMetrics/VictoriaMetrics

VictoriaMetrics: fast, cost-effective monitoring solution and time series database

## features

VictoriaMetrics is optimized for timeseries data, even when old time series are constantly replaced by new ones at a high rate, it offers a lot of features:

* **Long-term storage for Prometheus** or as a drop-in replacement for Prometheus and Graphite in Grafana.
* **Powerful stream aggregation**: Can be used as a StatsD alternative.
* **Ideal for big data**: Works well with large amounts of time series data from APM, Kubernetes, IoT sensors, connected cars, industrial telemetry, financial data and various [Enterprise workloads](https://docs.victoriametrics.com/victoriametrics/enterprise/).
* **Query language**: Supports both PromQL and the more performant MetricsQL.
* **Easy to setup**: No dependencies, single [small binary](https://medium.com/@valyala/stripping-dependency-bloat-in-victoriametrics-docker-image-983fb5912b0d), configuration through command-line flags, but the default is also fine-tuned; backup and restore with [instant snapshots](https://medium.com/@valyala/how-victoriametrics-makes-instant-snapshots-for-multi-terabyte-time-series-data-e1f3fb0e0282).
* **Global query view**: Multiple Prometheus instances or any other data sources may ingest data into VictoriaMetrics and be queried via a single query.
* **Various Protocols**: Support metric scraping, ingestion and backfilling in various protocols.
    * [Prometheus exporters](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#how-to-scrape-prometheus-exporters-such-as-node-exporter), [Prometheus remote write API](https://docs.victoriametrics.com/victoriametrics/integrations/prometheus/), [Prometheus exposition format](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#how-to-import-data-in-prometheus-exposition-format).
    * [InfluxDB line protocol](https://docs.victoriametrics.com/victoriametrics/integrations/influxdb/) over HTTP, TCP and UDP.
    * [Graphite plaintext protocol](https://docs.victoriametrics.com/victoriametrics/integrations/graphite/#ingesting) with [tags](https://graphite.readthedocs.io/en/latest/tags.html#carbon).
    * [OpenTSDB put message](https://docs.victoriametrics.com/victoriametrics/integrations/opentsdb/#sending-data-via-telnet).
    * [HTTP OpenTSDB /api/put requests](https://docs.victoriametrics.com/victoriametrics/integrations/opentsdb/#sending-data-via-http).
    * [JSON line format](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#how-to-import-data-in-json-line-format).
    * [Arbitrary CSV data](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#how-to-import-csv-data).
    * [Native binary format](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#how-to-import-data-in-native-format).
    * [DataDog agent or DogStatsD](https://docs.victoriametrics.com/victoriametrics/integrations/datadog/).
    * [NewRelic infrastructure agent](https://docs.victoriametrics.com/victoriametrics/integrations/newrelic/#sending-data-from-agent).
    * [OpenTelemetry metrics format](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#sending-data-via-opentelemetry).
* **NFS-based storages**: Supports storing data on NFS-based storages such as Amazon EFS, Google Filestore.
* And many other features such as metrics relabeling, cardinality limiter, etc.

## tools

#### Font

* Font Used: Lato Black
* Download here: [Lato Font](https://fonts.google.com/specimen/Lato)

#### Color Palette

* Black [#000000](https://www.color-hex.com/color/000000)
* Purple [#4d0e82](https://www.color-hex.com/color/4d0e82)
* Orange [#ff2e00](https://www.color-hex.com/color/ff2e00)
* White [#ffffff](https://www.color-hex.com/color/ffffff)
