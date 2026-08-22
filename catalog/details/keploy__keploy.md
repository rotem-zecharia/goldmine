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

```bash
curl --silent -O -L https://keploy.io/install.sh && source install.sh
```
