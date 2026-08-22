# keploy/keploy

Open-source platform for creating safe, isolated production sandboxes for API, integration, and E2E testing.

## tools

Keploy uses existing recordings, Swagger/OpenAPI Schema to find: boundary values, missing/extra fields, wrong types, out‑of‑order sequences, retries/timeouts. 

This helps expand API Schema, Statement, and Branch Coverage. 

👉 [Read the docs on coverage](https://app.keploy.io/)

<img src="https://keploy-devrel.s3.us-west-2.amazonaws.com/ai+test+case+generation+that+works.png" width="100%" alt="ai test gen for api statement schema and branch coverage"/>

## features

- 🌐 **CI/CD Integration:** Run tests with mocks anywhere you like—locally on the CLI, in your CI pipeline (Jenkins, Github Actions..) , or even across a Kubernetes cluster. [Read more](https://keploy.io/docs/running-keploy/api-testing-cicd/)

- 🎭 **Multi-Purpose Mocks**: You can also use Keploy-generated Mocks, as server Tests!

- 📊 **Reporting:** Unified reports for API, integration, unit, and e2e coverage with insights directly in your CI or PRs.
- 🖥️ **Console:** A developer-friendly console to view, manage, and debug recorded tests and mocks.
- ⏱️ **Time Freezing:** Deterministically replay tests by freezing system time during execution. [Read more](https://keploy.io/docs/keploy-cloud/time-freezing/)
- 📚 **Mock Registry:** Centralized registry to manage, reuse, and version mocks across teams and environments. [Read more](https://keploy.io/docs/keploy-cloud/mock-registry/)

---

## installation

### 1. Install Keploy Agent

```bash
curl --silent -O -L https://keploy.io/install.sh && source install.sh
```

### 2. Record Test Cases

Start your app under Keploy to convert real API calls into tests and mocks.

```bash
keploy record -c "CMD_TO_RUN_APP"
```

Example for Python:

```bash
keploy record -c "python main.py"
```

### 3. Run Tests

Run tests offline without external dependencies.

```bash
keploy test -c "CMD_TO_RUN_APP" --delay 10
```

## Resources
### - 📘 [Installation](https://keploy.io/docs/server/installation/)
### - 🏁 [QuickStarts](https://keploy.io/docs/quickstart/quickstart-filter/)


---


## Languages &amp; Frameworks (Any stack)

Because Keploy intercepts at the **network layer (eBPF)**, it works with **any language, framework, or runtime**—no SDK required. 
> Note: Some of the dependencies are not open-source by nature because their protocols and parsings are not open-sourced. It's not supported in Keploy enterprise. 

<p align="center">

<!-- Languages -->
<img src="https://img.shields.io/badge/Go-00ADD8?logo=go&amp;logoColor=white" />
<img src="https://img.shields.io/badge/Java-ED8B00?logo=openjdk&amp;logoColor=white" />
<img src="https://img.shields.io/badge/Node.js-43853D?logo=node.js&amp;logoColor=white" />
<img src="https://img.shields.io/badge/Python-3776AB?logo=python&amp;logoColor=white" />
<img src="https://img.shields.io/badge/Rust-000000?logo=rust&amp;logoColor=white" />
<img src="https://img.shields.io/badge/C%23-239120?logo=csharp&amp;logoColor=white" />
<img src="https://img.shields.io/badge/C/C++-00599C?logo=cplusplus&amp;logoColor=white" />
<img src="https://img.shields.io/badge/TypeScript-3178C6?logo=typescript&amp;logoColor=white" />
<img src="https://img.shields.io/badge/Scala-DC322F?logo=scala&amp;logoColor=white" />
<img src="https://img.shields.io/badge/Kotlin-7F52FF?logo=kotlin&amp;logoColor=white" />
<img src="https://img.shields.io/badge/Swift-FA7343?logo=swift&amp;logoColor=white" />
<img src="https://img.shields.io/badge/Dart-0175C2?logo=dart&amp;logoColor=white" />
<img src="https://img.shields.io/badge/PHP-777BB4?logo=php&amp;logoColor=white" />
<img src="https://img.shields.io/badge/Ruby-CC342D?logo=ruby&amp;logoColor=white" />
<img src="https://img.shields.io/badge/Elixir-4B275F?logo=elixir&amp;logoColor=white" />
<img src="https://img.shields.io/badge/.NET-512BD4?logo=dotnet&amp;logoColor=white" />

<!-- Protocols &amp; infra commonly virtualized -->
<img src="https://img.shields.io/badge/gRPC-5E35B1?logo=grpc&amp;logoColor=white" />
<img src="https://img.shields.io/badge/GraphQL-E10098?logo=graphql&amp;logoColor=white" />
<img src="https://img.shields.io/badge/HTTP%2FREST-0A84FF?logo=httpie&amp;logoColor=white" />
<img src="https://img.shields.io/badge/Kafka-231F20?logo=apachekafka&amp;logoColor=white" />
<img src="https://img.shields.io/badge/RabbitMQ-FF6600?logo=rabbitmq&amp;logoColor=white" />
<img src="https://img.shields.io/badge/PostgreSQL-4169E1?logo=postgresql&amp;logoColor=white" />
<img src="https://img.shields.io/badge/MySQL-4479A1?logo=mysql&amp;logoColor=white" />
<img src="https://img.shields.io/badge/MongoDB-47A248?logo=mongodb&amp;logoColor=white" />
<img src="https://img.shields.io/badge/Redis-DC382D?logo=redis&amp;logoColor=white" />
</p>

---

## Questions? 

### Book a Live Demo / Enterprise Support

Want a guided walkthrough, dedicated support, or help planning enterprise rollout?

<p>
  <a href="https://calendar.app.google/4ZKd1nz9A5wLuP4W7">
    <img src="https://img.shields.io/badge/Request%20a%20Demo-Email-2ea44f?logo=gmail" />
  </a>
  &nbsp;
  <a href="https://join.slack.com/t/keploy/shared_invite/zt-3zcnuqfgl-WYK1NMhslVHsCtNcA1ULwA">
    <img src="https://img.shields.io/badge/Chat%20with%20Us-Slack-4A154B?logo=slack&amp;logoColor=white" />
  </a>
  <!-- Optional: replace with your scheduling link (Cal.com/Calendly) -->
  <!-- <a href="https://cal.com/keploy/demo"><img src="https://img.shields.io/badge/Book%20via%20Calendar-Cal.com-111111" />
