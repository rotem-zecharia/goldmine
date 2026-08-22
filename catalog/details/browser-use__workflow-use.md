# browser-use/workflow-use

⚙️ Create and run workflows (RPA 2.0)

## tools

```bash
# Generate workflow from task description
python cli.py generate-workflow "Find GitHub stars for browser-use repo"

# List all workflows
python cli.py list-workflows

# Filter by generation mode
python cli.py list-workflows --generation-mode browser_use

# Run stored workflow
python cli.py run-stored-workflow <workflow-id> --prompt "Find stars for playwright repo"

# View workflow details
python cli.py workflow-info <workflow-id>

# Delete workflow
python cli.py delete-workflow <workflow-id>
```

### How It Works

1. **Describe**: Give a task in natural language
2. **Execute**: Browser-use completes the task once
3. **Generate**: Execution history → semantic workflow with parameters
4. **Store**: Save to database with metadata
5. **Reuse**: Run the workflow with different inputs, no AI needed

## configuration

```bash
# Custom models for generation
python cli.py generate-workflow "Your task" \
  --agent-model "gpt-4.1-mini" \
  --extraction-model "gpt-4.1-mini" \
  --workflow-model "gpt-4o"

# Use Browser-Use Cloud browser
python cli.py generate-workflow "Your task" --use-cloud

# Save to custom location
python cli.py generate-workflow "Your task" --output-file ./my-workflow.json

# Skip database storage
python cli.py generate-workflow "Your task" --no-save-to-storage
```

### Storage

Workflows stored at `workflows/storage/`:
- `metadata.json` - Searchable index of all workflows
- `workflows/<id>.workflow.json` - Individual workflow files

## installation

```bash
git clone https://github.com/browser-use/workflow-use
```

## Build the extension

```bash
cd extension && npm install && npm run build
```

## Setup workflow environment

```bash
cd .. && cd workflows
uv sync
source .venv/bin/activate # for mac / linux
playwright install chromium
cp .env.example .env # add your OPENAI_API_KEY to the .env file
```


## Run workflow as tool

```bash
python cli.py run-as-tool examples/example.workflow.json --prompt "fill the form with example data"
```

## Run workflow with predefined variables

```bash
python cli.py run-workflow examples/example.workflow.json
```

## Record your own workflow

```bash
python cli.py create-workflow
```

## features

- 🔁 **Record Once, Reuse Forever**: Record browser interactions once and replay them indefinitely.
- ⏳ **Show, don't prompt**: No need to spend hours prompting Browser Use to do the same thing over and over again.
- ⚙️ **Structured & Executable Workflows**: Converts recordings into deterministic, fast, and reliable workflows which automatically extract variables from forms.
- 🪄 **Human-like Interaction Understanding**: Intelligently filters noise from recordings to create meaningful workflows.
- 🔒 **Enterprise-Ready Foundation**: Built for future scalability with features like self-healing and workflow diffs.

## limitations

Show computer what it needs to do once, and it will do it over and over again without any human intervention.

## Workflows

- [ ] Nice way to use the `.json` files inside python code
- [ ] Improve LLM fallback when step fails (currently really bad)
- [ ] Self healing, if it fails automatically agent kicks in and updates the workflow file
- [ ] Better support for LLM steps
- [ ] Take output from previous steps and use it as input for next steps
- [ ] Expose workflows as MCP tools
- [ ] Use Browser Use to automatically create workflows from websites

## Developer experience

- [ ] Improve CLI
- [ ] Improve extension
- [ ] Step editor

## Agent

- [ ] Allow Browser Use to use the workflows as MCP tools
- [ ] Use workflows as website caching layer
