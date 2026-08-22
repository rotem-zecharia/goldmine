# Arindam200/awesome-ai-apps

A collection of projects showcasing RAG, agents, workflows, and other AI use cases

## requirements

- **Python 3.10+** (Python 3.11+ recommended for newer projects)
- **Git** for cloning the repository
- **Package Manager**: `pip` or `uv` (recommended for faster installs)
- **API Keys**: Most projects require API keys (see individual project READMEs)

## installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/Arindam200/awesome-ai-apps.git
   cd awesome-ai-apps
   ```

2. **Choose a project** and navigate to its directory

   ```bash
   cd starter_ai_agents/agno_starter  # Example: Start with Agno starter
   ```

3. **Set up environment variables**

   ```bash
   cp .env.example .env  # Copy example environment file
   # Edit .env with your API keys
   ```

4. **Install dependencies**

   ```bash
   # Using pip
   pip install -r requirements.txt

   # OR using uv (recommended - faster)
   uv sync
   # or
   uv pip install -e .
   ```

5. **Run the project**

   ```bash
   python main.py
   # or for Streamlit apps
   streamlit run app.py
   ```
