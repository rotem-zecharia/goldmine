# ccfos/nightingale

Nightingale is to monitoring and alerting what Grafana is to visualization.

## tools

74 fine-grained tools (42 read, 32 write) across 13 toolsets: `alerts`, `targets`, `datasource`, `mutes`, `busi_groups`, `notify_rules`, `alert_subscribes`, `event_pipelines`, `users`, `metrics`, `logs`, `dashboards`, `roles`.

**The endpoint is read-only by default** — the write tools (create / update / delete) are an explicit config opt-in.

## configuration

Everything below is optional; `/mcp` is enabled out of the box (`etc/config.toml`):

```toml
[HTTP.A2A]
# DisableMCP = true                        # turn off /mcp (Disable = true turns off /a2a as well)

## features

![Nightingale Alerting rules](doc/img/readme/alerting-rules-en.png)

- Nightingale supports alerting rules, mute rules, subscription rules, and notification rules. It natively supports 20 types of notification media and allows customization of message templates.  
- It supports event pipelines for Pipeline processing of alarms, facilitating automated integration with in-house systems. For example, it can append metadata to alarms or perform relabeling on events. 
- It introduces the concept of business groups and a permission system to manage various rules in a categorized manner.  
- Many databases and middleware come with built-in alert rules that can be directly imported and used. It also supports direct import of Prometheus alerting rules.  
- It supports alerting self-healing, which automatically triggers a script to execute predefined logic after an alarm is generated—such as cleaning up disk space or capturing the current system state.

![Nightingale Alarm Dashboard](doc/img/readme/active-events-en.png)

- Nightingale archives historical alarms and supports multi-dimensional query and statistics.  
- It supports flexible aggregation grouping, allowing a clear view of the distribution of alarms across the company.

![Nightingale Integration Center](doc/img/readme/integration-components-en.png)

- Nightingale has built-in metric descriptions, dashboards, and alerting rules for common operating systems, middleware, and databases, which are contributed by the community with varying quality.  
- It directly receives data via multiple protocols such as Remote Write, OpenTSDB, Datadog, and Falcon, integrates with various Agents.  
- It supports data sources like Prometheus, ElasticSearch, Loki, ClickHouse, MySQL, Postgres, allowing alerting based on data from these sources.  
- Nightingale can be easily embedded into internal enterprise systems (e.g. Grafana, CMDB), and even supports configuring menu visibility for these embedded systems.

![Nightingale dashboards](doc/img/readme/dashboard-en.png)

- Nightingale supports dashboard functionality, including common chart types, and comes with pre-built dashboards. The image above is a screenshot of one of these dashboards.  
- If you are already accustomed to Grafana, it is recommended to continue using Grafana for visualization, as Grafana has deeper expertise in this area.  
- For machine-related monitoring data collected by Categraf, it is advisable to use Nightingale's built-in dashboards for viewing. This is because Categraf's metric naming follows Telegraf's convention, which differs from that of Node Exporter.  
- Due to Nightingale's concept of business groups (where machines can belong to different groups), there may be scenarios where you only want to view machines within the current business group on the dashboard. Thus, Nightingale's dashboards can be linked with business groups for interactive filtering.

## 🌟 Stargazers over time

[![Stargazers over time](https://star-history.dera.page/svg?repos=ccfos/nightingale&type=Date)](https://star-history.dera.page/#ccfos/nightingale&Date)

## 🔥 Users

![User Logos](doc/img/readme/logos.png)

## 🤝 Community Co-Building

- ❇️ Please read the [Nightingale Open Source Project and Community Governance Draft](./doc/community-governance.md). We sincerely welcome every user, developer, company, and organization to use Nightingale, actively report bugs, submit feature requests, share best practices, and help build a professional and active open-source community.
- ❤️ Nightingale Contributors
<a href="https://github.com/ccfos/nightingale/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=ccfos/nightingale" />
</a>

## 📜 License
- [Apache License V2.0](https://github.com/ccfos/nightingale/blob/main/LICENSE)
