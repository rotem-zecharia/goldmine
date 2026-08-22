# mangiucugna/json_repair

Repair malformed JSON from LLMs, APIs, logs, and user input in Python.

## tools

If you want copy-paste examples for real applications, see [examples/README.md](https://github.com/mangiucugna/json_repair/blob/main/examples/README.md):

- [repair_llm_output.py](https://github.com/mangiucugna/json_repair/blob/main/examples/repair_llm_output.py) repairs markdown-wrapped or prose-wrapped model output.
- [pydantic_schema.py](https://github.com/mangiucugna/json_repair/blob/main/examples/pydantic_schema.py) uses a Pydantic v2 model as schema guidance.
- [stream_stable.py](https://github.com/mangiucugna/json_repair/blob/main/examples/stream_stable.py) keeps partial JSON stable during streaming.
- [fastapi_app.py](https://github.com/mangiucugna/json_repair/blob/main/examples/fastapi_app.py) drops the repair step into a FastAPI endpoint.

### Use json_repair from CLI

Install the library for command-line with:
```
pipx install json-repair
```
to know all options available:
```
$ json_repair -h
usage: json_repair [-h] [-i] [-o TARGET] [--ensure_ascii] [--indent INDENT]
                   [--skip-json-loads] [--schema SCHEMA] [--schema-model MODEL]
                   [--strict] [--schema-repair-mode {standard,salvage}] [filename]

Repair and parse JSON files.

positional arguments:
  filename              The JSON file to repair (if omitted, reads from stdin)

options:
  -h, --help            show this help message and exit
  -i, --inline          Replace the file inline instead of returning the output to stdout
  -o TARGET, --output TARGET
                        If specified, the output will be written to TARGET filename instead of stdout
  --ensure_ascii        Pass ensure_ascii=True to json.dumps()
  --indent INDENT       Number of spaces for indentation (Default 2)
  --skip-json-loads     Skip initial json.loads validation
  --schema SCHEMA       Path to a JSON Schema file that guides repairs
  --schema-model MODEL  Pydantic v2 model in 'module:ClassName' form that guides repairs
  --strict              Raise on duplicate keys, missing separators, empty keys/values, and similar structural issues instead of repairing them
  --schema-repair-mode {standard,salvage}
                        Schema repair mode: standard (default) or salvage (best-effort array/object salvage)
```

## requirements

**Please pin this library only on the major version!**

We use TDD and strict semantic versioning, there will be frequent updates and no breaking changes in minor and patch versions.
To ensure that you only pin the major version of this library in your `requirements.txt`, specify the package name followed by the major version and a wildcard for minor and patch versions. For example:

    json_repair==0.*

In this example, any version that starts with `0.` will be acceptable, allowing for updates on minor and patch versions.

---
# How to cite
If you are using this library in your academic work (as I know many folks are) please find the BibTex here:

    @software{Baccianella_JSON_Repair_-_2025,
        author  = "Stefano {Baccianella}",
        month   = "feb",
        title   = "JSON Repair - A python module to repair invalid JSON, commonly used to parse the output of LLMs",
        url     = "https://github.com/mangiucugna/json_repair",
        version = "0.39.1",
        year    = 2025
    }

Thank you for citing my work and please send me a link to the paper if you can!

---

# How it works
This module will parse the JSON file following the BNF definition:

    <json> ::= <primitive> | <container>

    <primitive> ::= <number> | <string> | <boolean>
    ; Where:
    ; <number> is a valid real number expressed in one of a number of given formats
    ; <string> is a string of valid characters enclosed in quotes
    ; <boolean> is one of the literal strings 'true', 'false', or 'null' (unquoted)

    <container> ::= <object> | <array>
    <array> ::= '[' [ <json> *(', ' <json>) ] ']' ; A sequence of JSON values separated by commas
    <object> ::= '{' [ <member> *(', ' <member>) ] '}' ; A sequence of 'members'
    <member> ::= <string> ': ' <json> ; A pair consisting of a name, and a JSON value

If something is wrong (a missing parentheses or quotes for example) it will use a few simple heuristics to fix the JSON string:
- Add the missing parentheses if the parser believes that the array or object should be closed
- Quote strings or add missing single quotes
- Adjust whitespaces and remove line breaks

I am sure some corner cases will be missing, if you have examples please open an issue or even better push a PR

# Contributing
If you want to contribute, start with `CONTRIBUTING.md` and read the Code Wiki writeup for a tour of the codebase and key entry points: https://codewiki.google/github.com/mangiucugna/json_repair

# How to develop
Use `uv` to set up the dev environment and run tooling:

    uv sync --group dev
    uv run pre-commit run --all-files
    uv run pytest

Make sure that the Github Actions running after pushing a new commit don't fail as well.

# How to release
You will need owner access to this repository
- Edit `pyproject.toml` and update the version number appropriately using `semver` notation
- **Commit and push all changes to the repository before continuing or the next steps will fail**
- Run `python -m build`
- Create a new release in Github, making sure to tag all the issues solved and contributors. Create the new tag, same as the one in the build configuration
- Once the release is created, a new Github Actions workflow will start to publish on Pypi, make sure it didn't fail
