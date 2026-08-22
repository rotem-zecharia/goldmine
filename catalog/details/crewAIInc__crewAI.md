# crewAIInc/crewAI

Framework for orchestrating role-playing, autonomous AI agents. By fostering collaborative intelligence, CrewAI empowers agents to work together seamlessly, tackling complex tasks.

## features

- **Tracing & Observability**: Monitor and track your AI agents and workflows in real-time, including metrics, logs, and traces.
- **Unified Control Plane**: A centralized platform for managing, monitoring, and scaling your AI agents and workflows.
- **Seamless Integrations**: Easily connect with existing enterprise systems, data sources, and cloud infrastructure.
- **Advanced Security**: Built-in robust security and compliance measures ensuring safe deployment and management.
- **Actionable Insights**: Real-time analytics and reporting to optimize performance and decision-making.
- **24/7 Support**: Dedicated enterprise support to ensure uninterrupted operation and quick resolution of issues.
- **On-premise and Cloud Deployment Options**: Deploy CrewAI AMP on-premise or in the cloud, depending on your security and compliance requirements.

CrewAI AMP is designed for enterprises seeking a powerful, reliable solution to transform complex business processes into efficient,
intelligent automations.

## installation

Setup and run your first CrewAI agents by following this tutorial.

[![CrewAI Getting Started Tutorial](https://img.youtube.com/vi/-kSOTtYzgEw/hqdefault.jpg)](https://www.youtube.com/watch?v=-kSOTtYzgEw "CrewAI Getting Started Tutorial")

## requirements

If you encounter issues during installation or usage, here are some common solutions:

#### Common Issues

1. **ModuleNotFoundError: No module named 'tiktoken'**

   - Install tiktoken explicitly: `uv pip install 'crewai[embeddings]'`
   - If using embedchain or other tools: `uv pip install 'crewai[tools]'`

2. **Failed building wheel for tiktoken**

   - Ensure Rust compiler is installed (see installation steps above)
   - For Windows: Verify Visual C++ Build Tools are installed
   - Try upgrading pip: `uv pip install --upgrade pip`
   - If issues persist, use a pre-built wheel: `uv pip install tiktoken --prefer-binary`

## configuration

To create a new CrewAI project, run the following CLI (Command Line Interface) command:

```shell
crewai create crew <project_name>
```

This command creates a new project folder with the following structure:

```
my_project/
├── .gitignore
├── pyproject.toml
├── README.md
├── .env
└── src/
    └── my_project/
        ├── __init__.py
        ├── main.py
        ├── crew.py
        ├── tools/
        │   ├── custom_tool.py
        │   └── __init__.py
        └── config/
            ├── agents.yaml
            └── tasks.yaml
```

You can now start developing your crew by editing the files in the `src/my_project` folder. The `main.py` file is the entry point of the project, the `crew.py` file is where you define your crew, the `agents.yaml` file is where you define your agents, and the `tasks.yaml` file is where you define your tasks.

#### To customize your project, you can:

- Modify `src/my_project/config/agents.yaml` to define your agents.
- Modify `src/my_project/config/tasks.yaml` to define your tasks.
- Modify `src/my_project/crew.py` to add your own logic, tools, and specific arguments.
- Modify `src/my_project/main.py` to add custom inputs for your agents and tasks.
- Add your environment variables into the `.env` file.

#### Example of a simple crew with a sequential process:

Instantiate your crew:

```shell
crewai create crew latest-ai-development
```

Modify the files as needed to fit your use case:

**agents.yaml**

```yaml

## tools

You can test different real life examples of AI crews in the [CrewAI-examples repo](https://github.com/crewAIInc/crewAI-examples?tab=readme-ov-file):

- [Landing Page Generator](https://github.com/crewAIInc/crewAI-examples/tree/main/crews/landing_page_generator)
- [Having Human input on the execution](https://docs.crewai.com/en/learn/human-input-on-execution)
- [Trip Planner](https://github.com/crewAIInc/crewAI-examples/tree/main/crews/trip_planner)
- [Stock Analysis](https://github.com/crewAIInc/crewAI-examples/tree/main/crews/stock_analysis)
