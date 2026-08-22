# awslabs/mcp

Open source MCP Servers for AWS

## features

MCP servers enhance the capabilities of foundation models (FMs) in several key ways:

- **Improved Output Quality**: By providing relevant information directly in the model's context, MCP servers significantly improve model responses for specialized domains like AWS services. This approach reduces hallucinations, provides more accurate technical details, enables more precise code generation, and ensures recommendations align with current AWS best practices and service capabilities.

- **Access to Latest Documentation**: FMs may not have knowledge of recent releases, APIs, or SDKs. MCP servers bridge this gap by pulling in up-to-date documentation, ensuring your AI assistant always works with the latest AWS capabilities.

- **Workflow Automation**: MCP servers convert common workflows into tools that foundation models can use directly. Whether it's CDK, Terraform, or other AWS-specific workflows, these tools enable AI assistants to perform complex tasks with greater accuracy and efficiency.

- **Specialized Domain Knowledge**: MCP servers provide deep, contextual knowledge about AWS services that might not be fully represented in foundation models' training data, enabling more accurate and helpful responses for cloud development tasks.

## installation

Get started quickly with one-click installation buttons for popular MCP clients. Click the buttons below to install servers directly in Cursor or VS Code:

### 🚀 Getting Started with AWS

For AWS interactions, we recommend starting with:

| Server Name                                                                                                 | Description | Install |
|-------------------------------------------------------------------------------------------------------------|-------------|---------|
| [AWS MCP Server (in preview)](https://docs.aws.amazon.com/aws-mcp/latest/userguide/what-is-mcp-server.html) | Start here for secure, auditable AWS interactions! This remote, managed MCP server is hosted by AWS and combines comprehensive AWS API support with access to the latest AWS documentation, API references, What's New posts, and Getting Started information. Features pre-built Agent SOPs that follow AWS best practices, helping agents complete complex multi-step AWS tasks reliably. Built with safety and control in mind: syntactically validated API calls, IAM-based permissions with zero credential exposure, and complete CloudTrail audit logging. Access all AWS services for managing infrastructure, exploring resources, and executing AWS operations with full transparency and traceability. [Read more](https://docs.aws.amazon.com/aws-mcp/latest/userguide/what-is-mcp-server.html) | [![Install](https://img.shields.io/badge/Install-Kiro-9046FF?style=flat-square&logo=kiro)](https://kiro.dev/launch/mcp/add?name=aws-mcp&config=%7B%22command%22%3A%22uvx%22%2C%22args%22%3A%5B%22mcp-proxy-for-aws%40latest%22%2C%22https%3A//aws-mcp.us-east-1.api.aws/mcp%22%5D%7D) <br/>[![Install](https://img.shields.io/badge/Install-Cursor-blue?style=flat-square&logo=cursor)](https://cursor.com/en-US/install-mcp?name=aws-mcp&config=eyJjb21tYW5kIjoidXZ4IG1jcC1wcm94eS1mb3ItYXdzQGxhdGVzdCBodHRwczovL2F3cy1tY3AudXMtZWFzdC0xLmFwaS5hd3MvbWNwIn0%3D) <br/>[![Install on VS Code](https://img.shields.io/badge/Install-VS_Code-FF9900?style=flat-square&logo=visualstudiocode&logoColor=white)](<https://insiders.vscode.dev/redirect/mcp/install?name=AWS%20MCP%20Server&config=%7B%22command%22%3A%22uvx%22%2C%22args%22%3A%5B%22mcp-proxy-for-aws%40latest%22%2C%22https%3A%2F%2Faws-mcp.us-east-1.api.aws%2Fmcp%22%5D%7D>) |

### Browse by What You're Building

#### 📚 Real-time access to official AWS documentation

| Server Name | Description | Install |
|-------------|-------------|---------|
| [AWS Knowledge MCP Server](src/aws-knowledge-mcp-server) | A remote, fully-managed MCP server hosted by AWS that provides access to the latest AWS docs, API references, What's New Posts, Getting Started information, Builder Center, Blog posts, Architectural references, and Well-Architected guidance. | [![Install](https://img.shields.io/badge/Install-Kiro-9046FF?style=flat-square&logo=kiro)](https://kiro.dev/launch/mcp/add?name=aws-knowledge-mcp&config=%7B%22url%22%3A%22https%3A//knowledge-mcp.global.api.aws%22%7D) <br/>[![Install](https://img.shields.io/badge/Install-Cursor-blue?style=flat-square&logo=cursor)](https://cursor.com/en/install-mcp?name=aws-knowledge-mcp&config=eyJ1cmwiOiJodHRwczovL2tub3dsZWRnZS1tY3AuZ2xvYmFsLmFwaS5hd3MifQ==) <br/>[![Install on VS Code](https://img.shields.io/badge/Install-VS_Code-FF9900?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=aws-knowledge-mcp&config=%7B%22type%22%3A%22http%22%2C%22url%22%3A%22https%3A%2F%2Fknowledge-mcp.global.api.aws%22%7D) |
| [AWS Documentation MCP Server](src/aws-documentation-mcp-server) | Get latest AWS docs and API references | [![Install](https://img.shields.io/badge/Install-Kiro-9046FF?style=flat-square&logo=kiro)](https://kiro.dev/launch/mcp/add?name=awslabs.aws-documentation-mcp-server&config=%7B%22command%22%3A%22uvx%22%2C%22args%22%3A%5B%22awslabs.aws-documentation-mcp-server%40latest%22%5D%2C%22env%22%3A%7B%22FASTMCP_LOG_LEVEL%22%3A%22ERROR%22%2C%22AWS_DOCUMENTATION

## tools

Accelerate development with code analysis, documentation, and testing utilities.

| Server Name | Description | Install |
|-------------|-------------|---------|
| [AWS IAM MCP Server](src/iam-mcp-server) | Comprehensive IAM user, role, group, and policy management with security best practices | [![Install](https://img.shields.io/badge/Install-Kiro-9046FF?style=flat-square&logo=kiro)](https://kiro.dev/launch/mcp/add?name=awslabs.iam-mcp-server&config=%7B%22command%22%3A%22uvx%22%2C%22args%22%3A%5B%22awslabs.iam-mcp-server%40latest%22%5D%2C%22env%22%3A%7B%22AWS_PROFILE%22%3A%22your-aws-profile%22%2C%22AWS_REGION%22%3A%22us-east-1%22%2C%22FASTMCP_LOG_LEVEL%22%3A%22ERROR%22%7D%7D) <br/>[![Install](https://img.shields.io/badge/Install-Cursor-blue?style=flat-square&logo=cursor)](https://cursor.com/en/install-mcp?name=awslabs.iam-mcp-server&config=eyJjb21tYW5kIjoidXZ4IiwiYXJncyI6WyJhd3NsYWJzLmlhbS1tY3Atc2VydmVyQGxhdGVzdCJdLCJlbnYiOnsiQVdTX1BST0ZJTEUiOiJ5b3VyLWF3cy1wcm9maWxlIiwiQVdTX1JFR0lPTiI6InVzLWVhc3QtMSIsIkZBU1RNQ1BfTE9HX0xFVkVMIjoiRVJST1IifX0%3D) <br/>[![Install on VS Code](https://img.shields.io/badge/Install-VS_Code-FF9900?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=AWS%20IAM%20MCP%20Server&config=%7B%22command%22%3A%22uvx%22%2C%22args%22%3A%5B%22awslabs.iam-mcp-server%40latest%22%5D%2C%22env%22%3A%7B%22AWS_PROFILE%22%3A%22your-aws-profile%22%2C%22AWS_REGION%22%3A%22us-east-1%22%2C%22FASTMCP_LOG_LEVEL%22%3A%22ERROR%22%7D%7D) |
| [AWS Security Agent MCP Server](src/security-agent-mcp-server) | Automated security scanning, penetration testing, and remediation using AWS Security Agent | |
| [OpenAPI MCP Server](src/openapi-mcp-server) | Dynamic API integration through OpenAPI specifications | [![Install](https://img.shields.io/badge/Install-Kiro-9046FF?style=flat-square&logo=kiro)](https://kiro.dev/launch/mcp/add?name=awslabs.openapi-mcp-server&config=%7B%22command%22%3A%22uvx%22%2C%22args%22%3A%5B%22awslabs.openapi-mcp-server%40latest%22%5D%2C%22env%22%3A%7B%22API_NAME%22%3A%22your-api-name%22%2C%22API_BASE_URL%22%3A%22https%3A//api.example.com%22%2C%22API_SPEC_URL%22%3A%22https%3A//api.example.com/openapi.json%22%2C%22LOG_LEVEL%22%3A%22ERROR%22%2C%22ENABLE_PROMETHEUS%22%3A%22false%22%2C%22ENABLE_OPERATION_PROMPTS%22%3A%22true%22%2C%22UVICORN_TIMEOUT_GRACEFUL_SHUTDOWN%22%3A%225.0%22%2C%22UVICORN_GRACEFUL_SHUTDOWN%22%3A%22true%22%7D%7D) <br/>[![Install](https://img.shields.io/badge/Install-Cursor-blue?style=flat-square&logo=cursor)](https://cursor.com/en/install-mcp?name=awslabs.openapi-mcp-server&config=eyJjb21tYW5kIjoidXZ4IGF3c2xhYnMub3BlbmFwaS1tY3Atc2VydmVyQGxhdGVzdCIsImVudiI6eyJBUElfTkFNRSI6InlvdXItYXBpLW5hbWUiLCJBUElfQkFTRV9VUkwiOiJodHRwczovL2FwaS5leGFtcGxlLmNvbSIsIkFQSV9TUEVDX1VSTCI6Imh0dHBzOi8vYXBpLmV4YW1wbGUuY29tL29wZW5hcGkuanNvbiIsIkxPR19MRVZFTCI6IkVSUk9SIiwiRU5BQkxFX1BST01FVEhFVVMiOiJmYWxzZSIsIkVOQUJMRV9PUEVSQVRJT05fUFJPTVBUUyI6InRydWUiLCJVVklDT1JOX1RJTUVPVVRfR1JBQ0VGVUxfU0hVVERPV04iOiI1LjAiLCJVVklDT1JOX0dSQUNFRlVMX1NIVVRET1dOIjoidHJ1ZSJ9LCJkaXNhYmxlZCI6ZmFsc2UsImF1dG9BcHByb3ZlIjpbXX0%3D) <br/>[![Install on VS Code](https://img.shields.io/badge/Install-VS_Code-FF9900?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=OpenAPI%20MCP%20Server&config=%7B%22command%22%3A%22uvx%22%2C%22args%22%3A%5B%22awslabs.openapi-mcp-server%40latest%22%5D%2C%22env%22%3A%7B%22API_NAME%22%3A%22your-api-name%22%2C%22API_BASE_URL%22%3A%22https%3A%2F%2Fapi.example.com%22%2C%22API_SPEC_URL%22%3A%22https%3A%2F%2Fapi.example.com%2Fopenapi.json%22%2C%22LOG_LEVEL%22%3A%22ERROR%22%2C%22ENABLE_PROMETHEUS%22%3A%22false%22%2C%22ENABLE_OPERATION_PROMPTS%22%3A%22true%22%2C%22UVICORN_TIMEOUT_GRACEFUL_SHUTDOWN%22%3A%225.0%22%2C%22UVICORN_GRACEFUL_SHUTDOWN%22%3A%22true%22%7D%2C%22disabled%22%3Afalse%2C%22autoApprove%22%3A%5B%5D%7D) |


### 📡 Integration & Messaging

Connect systems with messaging, workflows, and location services
