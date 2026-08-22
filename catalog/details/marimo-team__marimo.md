# marimo-team/marimo

A reactive notebook for Python — run reproducible experiments, query with SQL, execute as a script, deploy as an app, and version with git. Stored as pure Python. All in a modern, AI-native editor.

## configuration

marimo guarantees your notebook code, outputs, and program state are consistent. This [solves many problems](https://docs.marimo.io/faq.html#faq-problems) associated with traditional notebooks like Jupyter.

**A reactive programming environment.**
Run a cell and marimo _reacts_ by automatically running the cells that
reference its variables, eliminating the error-prone task of manually
re-running cells. Delete a cell and marimo scrubs its variables from program
memory, eliminating hidden state.

<img src="https://raw.githubusercontent.com/marimo-team/marimo/main/docs/_static/reactive.gif" width="700px" />

<a name="expensive-notebooks"></a>

**Compatible with expensive notebooks.** marimo lets you [configure the runtime
to be
lazy](https://docs.marimo.io/guides/configuration/runtime_configuration.html),
marking affected cells as stale instead of automatically running them. This
gives you guarantees on program state while preventing accidental execution of
expensive cells.

**Synchronized UI elements.** Interact with [UI
elements](https://docs.marimo.io/guides/interactivity.html) like [sliders](https://docs.marimo.io/api/inputs/slider.html#slider),
[dropdowns](https://docs.marimo.io/api/inputs/dropdown.html), [dataframe
transformers](https://docs.marimo.io/api/inputs/dataframe.html), and [chat
interfaces](https://docs.marimo.io/api/inputs/chat.html), and the cells that
use them are automatically re-run with their latest values.

<img src="https://raw.githubusercontent.com/marimo-team/marimo/main/docs/_static/readme-ui.gif" width="700px" />

**Interactive dataframes.** [Page through, search, filter, and
sort](https://docs.marimo.io/guides/working_with_data/dataframes.html)
millions of rows blazingly fast, no code required.

<img src="https://raw.githubusercontent.com/marimo-team/marimo/main/docs/_static/docs-df.gif" width="700px" />

**Generate cells with data-aware AI.** Collaborate on marimo notebooks with
your favorite agent, such as Claude Code, Codex, or OpenCode, using [marimo
pair](https://docs.marimo.io/guides/generate_with_ai/marimo_pair/). Or,
generate code [in the marimo editor with an AI
assistant](https://docs.marimo.io/guides/editor_features/ai_completion/) that
is highly specialized for working with data, with context about your variables
in memory. Customize the system prompt, bring your own API keys, or use local
models.

<img src="https://raw.githubusercontent.com/marimo-team/marimo/main/docs/_static/readme-generate-with-ai.gif" width="700px" />

**Query data with SQL.** Build [SQL](https://docs.marimo.io/guides/working_with_data/sql.html) queries
that depend on Python values and execute them against dataframes, databases, lakehouses,
CSVs, Google Sheets, or anything else using our built-in SQL engine, which
returns the result as a Python dataframe.

<img src="https://raw.githubusercontent.com/marimo-team/marimo/main/docs/_static/readme-sql-cell.png" width="700px" />

Your notebooks are still pure Python, even if they use SQL.

**Dynamic markdown.** Use markdown parametrized by Python variables to tell
dynamic stories that depend on Python data.

**Built-in package management.** marimo has built-in support for all major
package managers, letting you [install packages on import](https://docs.marimo.io/guides/editor_features/package_management.html). marimo can even
[serialize package
requirements](https://docs.marimo.io/guides/package_management/inlining_dependencies/)
in notebook files, and auto install them in
isolated venv sandboxes.

**Deterministic execution order.** Notebooks are executed in a deterministic
order, based on variable references instead of cells' positions on the page.
Organize your notebooks to best fit the stories you'd like to tell.

**Performant runtime.** marimo runs only those cells that need to be run by
statically analyzing your code.

**Batteries-included.** marimo comes with GitHub Copilot, AI assistants, Ruff
code formatting, HTML export, fast code completion, a [VS Code
extension]

## installation

_The [marimo concepts
playlist](https://www.youtube.com/watch?v=3N6lInzq5MI&list=PLNJXGo8e1XT9jP7gPbRdm1XwloZVFvLEq)
on our [YouTube channel](https://www.youtube.com/@marimo-team) gives an
overview of many features._

**Installation.** In a terminal, run

```bash
pip install marimo  # or conda install -c conda-forge marimo
marimo tutorial intro
```

To install with additional dependencies that unlock SQL cells, AI completion, and more,
run

```bash
pip install "marimo[recommended]"
```

**Create notebooks.**

Create or edit notebooks with

```bash
marimo edit
```

**Run apps.** Run your notebook as a web app, with Python
code hidden and uneditable:

```bash
marimo run your_notebook.py
```

<img src="https://raw.githubusercontent.com/marimo-team/marimo/main/docs/_static/docs-model-comparison.gif" style="border-radius: 8px" width="450px" />

**Execute as scripts.** Execute a notebook as a script at the
command line:

```bash
python your_notebook.py
```

**Automatically convert Jupyter notebooks.** Automatically convert Jupyter
notebooks to marimo notebooks with the CLI

```bash
marimo convert your_notebook.ipynb > your_notebook.py
```

or use our [web interface](https://marimo.io/convert).

**Tutorials.**
List all tutorials:

```bash
marimo tutorial --help
```

**Share cloud-based notebooks.** Use
[molab](https://molab.marimo.io/notebooks), a cloud-based marimo notebook
service similar to Google Colab, to create and share notebook links.
