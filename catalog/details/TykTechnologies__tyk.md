# TykTechnologies/tyk

Tyk Open Source API Gateway written in Go, supporting REST, GraphQL, TCP and gRPC protocols

## tools

**Tyk Gateway** is the cloud-native, open source, enterprise-ready API Gateway supporting REST, GraphQL, TCP and gRPC protocols.

Built from the ground up, as the [fastest API Gateway](https://tyk.io/performance-benchmarks/) on the planet since 2014.

_Tyk Gateway_ is provided ‘Batteries-included’, with no feature lockout. Enabling your organization to rate limit, auth, gather analytics, apply microservice patterns [and more](#open-source-api-gateway-features) with ease.

Tyk runs natively on _Kubernetes_, if you prefer, thanks to the _[Tyk Kubernetes Operator](https://github.com/TykTechnologies/tyk-operator)_

<table>
  <tr>
   <td>
     <center>
        <a href="https://tyk.io/docs/deployment-and-operations/tyk-open-source-api-gateway/quick-start"> <img src="https://raw.githubusercontent.com/TykTechnologies/tyk-docs/master/tyk-docs/assets/img/logos/tyk-logo-opensource.svg" width="30%"></a>
     </center>
     </br>Everything you need to manage APIs. Follow the simple Get Started guide below 👇
   </td>
   <td>
     <center>
       <a href="https://tyk.io/docs/tyk-self-managed/install"> <img src="https://raw.githubusercontent.com/TykTechnologies/tyk-docs/master/tyk-docs/assets/img/logos/tyk-logo-selfmanaged.png" width="25%"></a>
     </center>
     </br>The Enterprise API Management platform: Management Control Plane, Dashboard GUI & Developer Portal.
     </br><a href="https://tyk.io/api-lifecycle-management/">Install Tyk Self Managed</a>
   </td>
   <td>
     <center>
       <a href="https://tyk.io/docs/tyk-cloud"> <img src="https://raw.githubusercontent.com/TykTechnologies/tyk-docs/master/tyk-docs/assets/img/logos/tyk-logo-cloud.png" width="20%"></a>
     </center>
     </br>The Enterprise API Management platform SaaS: Management Control Plane, Dashboard GUI & Developer Portal.
     </br><a href="https://tyk.io/docs/deployment-and-operations/tyk-cloud-platform/quick-start">Deploy Tyk Cloud </a>
   </td>
  </tr>
</table>

---

## Get Started

We’ll install Tyk, add auth, analytics, quotas and rate limiting to your API in under 5 minutes.

We recommend [Tyk Gateway Docker](https://github.com/TykTechnologies/tyk-gateway-docker#start-up-the-deployment) as the quickest way to get started now. Later, you can move to one of our other [supported distributions](https://tyk.io/docs/apim/open-source/installation/) if you prefer.

#### Step 1 - Clone the docker-compose repository
```console
git clone https://github.com/TykTechnologies/tyk-gateway-docker
```

#### Step 2 - Change to the new directory
```console
cd tyk-gateway-docker
```

#### Step 3 - Deploy Tyk Gateway and Redis
```console
docker-compose up
```

You can run this in detach mode using the `-d` flag: `docker-compose up -d`

**Congratulations, you’re done!**

Your Tyk Gateway is now configured and ready to use. Confirm this by checking against the ‘hello’ endpoint:
```console
curl localhost:8080/hello
```
Output:
```json
{"status": "pass", "version": "v3.2.1", "description": "Tyk GW"}
```

Next, visit [adding your first API](https://tyk.io/docs/getting-started/create-api/) to Tyk and follow the Open Source instructions.

---

Other Installations are available:

1. [Docker](https://tyk.io/docs/tyk-oss/ce-docker/)
2. [Kubernetes-Native ](https://github.com/TykTechnologies/tyk-oss-k8s-deployment)
3. [Kubernetes-Helm](https://github.com/TykTechnologies/tyk-helm-chart#install-tyk-community-edition)
4. [Ansible](https://tyk.io/docs/tyk-oss/ce-ansible/)
5. [Red Hat](https://tyk.io/docs/tyk-oss/ce-redhat/)
6. [Ubuntu](https://tyk.io/docs/tyk-oss/ce-ubuntu/)
7. [CentOS](https://tyk.io/docs/tyk-oss/ce-centos/)
8. [Compile Tyk from Source](#compiling-tyk-gateway)

## features

Use any protocol: REST, SOAP, [GraphQL](https://tyk.io/docs/tyk-apis/tyk-gateway-api/api-definition-objects/graphql/), [gRPC](https://tyk.io/docs/key-concepts/grpc-proxy/), and [TCP](https://tyk.io/docs/key-concepts/tcp-proxy/).

Industry Standard Authentication: [OIDC](https://tyk.io/docs/advanced-configuration/integrate/api-auth-mode/open-id-connect/#setting-up-oidc), [JWT,](https://tyk.io/docs/tyk-apis/tyk-gateway-api/api-definition-objects/jwt/) [bearer Tokens](https://tyk.io/docs/basic-config-and-security/security/authentication-authorization/bearer-tokens/), [Basic Auth](https://tyk.io/docs/tyk-apis/tyk-dashboard-api/basic-authentication/), Client Certificates and more.

[Open API Standards:](https://tyk.io/docs/getting-started/using-oas-definitions/import-an-oas-api/) Import your Swagger and OpenAPI Documents (OAS 2.X and OAS 3.0.1) to scaffold APIs in Tyk.

[Ultra performant](https://tyk.io/performance-tuning-your-tyk-api-gateway/): Low latency, and thousands of rps with just a single CPU, horizontally and vertically scalable.

[Content mediation](https://tyk.io/docs/advanced-configuration/transform-traffic/): Transform all the things, from request or response headers to converting between SOAP and GraphQL.

[Extensible Plugin Architecture](https://tyk.io/docs/plugins/): Customize Tyk’s middleware chain by writing plugins in your language of choice - from Python to Javascript to Go, or any language which supports gRPC.

[Rate Limiting](https://tyk.io/docs/basic-config-and-security/control-limit-traffic/rate-limiting/#setting-rate-limits-in-the-tyk-community-edition-gateway-ce) & Quotas: Protect your upstreams from becoming overloaded and/or apply limits for each consumer.

[API Versioning](https://tyk.io/docs/tyk-apis/tyk-gateway-api/api-definition-objects/versioning-endpoint/) - API Versions can be easily set and sunset (deprecated) at a specific time and date.

[Granular Access Control](https://tyk.io/docs/security/security-policies/secure-apis-method-path/) - Grant access to one or more APIs on a per version and operation basis.

[Blocklist](https://tyk.io/docs/advanced-configuration/transform-traffic/endpoint-designer/#blocklist)/[Allowlist](https://tyk.io/docs/advanced-configuration/transform-traffic/endpoint-designer/#allowlist)/[Ignore](https://tyk.io/docs/advanced-configuration/transform-traffic/endpoint-designer/#ignore) endpoint access - Enforce strict security models on a version-by-version basis to your access points.

Analytics logging - Record detailed usage data on who is using your APIs (raw data only)

[CORS](https://tyk.io/docs/tyk-apis/tyk-gateway-api/api-definition-objects/cors/) - Enable CORS for certain APIs so users can make browser-based requests

[Webhooks](https://tyk.io/docs/basic-config-and-security/report-monitor-trigger-events/webhooks/) - Trigger webhooks against events such as Quota Violations and Authentication failures

[IP AllowListing](https://tyk.io/docs/tyk-apis/tyk-gateway-api/api-definition-objects/ip-whitelisting/) - Block access to non-trusted IP addresses for more secure interactions

[Hitless reloads](https://tyk.io/docs/tyk-configuration-reference/hot-restart-tyk-gateway-process/) - Tyk configurations can be altered dynamically and the service restarted without affecting any active request

[Kubernetes native](https://tyk.io/docs/tyk-oss/ce-helm-chart/) declarative API: using Open Source [Tyk Operator](https://github.com/TykTechnologies/tyk-operator) (more info in OSS section)
![OpenSourceAPIGateway-Diagram](https://github.com/TykTechnologies/tyk/assets/8012032/7466be3f-fb81-4a95-88ac-3b09254c815d)

Tyk Technologies uses the same API Gateway for all it’s applications. Protecting, securing, and processing APIs for thousands of organizations and businesses around the world. Ideal for Open Banking, building software in the clouds as well as exposing APIs to teams, partners & consumers.


## Tyk OSS Integrations

Tyk Technologies maintains other Open Source Software which can be
