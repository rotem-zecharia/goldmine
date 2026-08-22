# Kong/kong

🦍 The API and AI Gateway

## installation

If you prefer to use a cloud-hosted Kong, you can [sign up for a free trial of Kong Konnect](https://konghq.com/products/kong-konnect/register?utm_medium=Referral&utm_source=Github&utm_campaign=kong-gateway&utm_content=konnect-promo-in-gateway&utm_term=get-started) and get started in minutes. If not, you can follow the instructions below to get started with Kong on your own infrastructure.

Let’s test drive Kong by adding authentication to an API in under 5 minutes.

We suggest using the docker-compose distribution via the instructions below, but there is also a [docker installation](https://docs.konghq.com/gateway/latest/install/docker/#install-kong-gateway-in-db-less-mode) procedure if you’d prefer to run the Kong Gateway in DB-less mode.

Whether you’re running in the cloud, on bare metal, or using containers, you can find every supported distribution on our [official installation](https://konghq.com/install/#kong-community) page.

1) To start, clone the Docker repository and navigate to the compose folder.
```cmd
  $ git clone https://github.com/Kong/docker-kong
  $ cd docker-kong/compose/
```

2) Start the Gateway stack using:
```cmd
  $ KONG_DATABASE=postgres docker-compose --profile database up
```

The Gateway is now available on the following ports on localhost:

- `:8000` - send traffic to your service via Kong
- `:8001` - configure Kong using Admin API or via [decK](https://github.com/kong/deck)
- `:8002` - access Kong's management Web UI ([Kong Manager](https://github.com/Kong/kong-manager)) on [localhost:8002](http://localhost:8002)

Next, follow the [quick start guide](https://docs.konghq.com/gateway-oss/latest/getting-started/configuring-a-service/
) to tour the Gateway features.

## features

By centralizing common API, AI and MCP functionality across all your organization's services, Kong Gateway creates more freedom for engineering teams to focus on the challenges that matter most.

The top Kong features include:

- Advanced routing, load balancing, health checking - all configurable via a RESTful admin API or declarative configuration.
- Authentication and authorization for APIs using methods like JWT, basic auth, OAuth, ACLs and more.
- Universal LLM API to route across multiple providers like OpenAI, Anthropic, GCP Gemini, AWS Bedrock, Azure AI, Databricks, Mistral, Huggingface and more.
- MCP traffic governance, MCP security and MCP observability in addition to MCP autogeneration from any RESTful API.
- 60+ AI features like AI observability, semantic security and caching, semantic routing and more.
- Proxy, SSL/TLS termination, and connectivity support for L4 or L7 traffic.
- Plugins for enforcing traffic controls, rate limiting, req/res transformations, logging, monitoring and including a plugin developer hub.
- Sophisticated deployment models like Declarative Databaseless Deployment and Hybrid Deployment (control plane/data plane separation) without any vendor lock-in.
- Native [ingress controller](https://github.com/Kong/kubernetes-ingress-controller) support for serving Kubernetes.

[![][kong-benefits]][kong-url]
