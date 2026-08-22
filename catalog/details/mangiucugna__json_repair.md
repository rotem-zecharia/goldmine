# mangiucugna/json_repair

Repair malformed JSON from LLMs, APIs, logs, and user input in Python.

## tools

If you want copy-paste examples for real applications, see [examples/README.md](https://github.com/mangiucugna/json_repair/blob/main/examples/README.md):

- [repair_llm_output.py](https://github.com/mangiucugna/json_repair/blob/main/examples/repair_llm_output.py) repairs markdown-wrapped or prose-wrapped model output.
- [pydantic_schema.py](https://github.com/mangiucugna/json_repair/blob/main/examples/pydantic_schema.py) uses a Pydantic v2 model as schema guidance.
- [stream_stable.py](https://github.com/mangiucugna/json_repair/blob/main/examples/stream_stable.py) keeps partial JSON stable during streaming.
- [fastapi_app.py](https://github.com/mangiucugna/json_repair/blob/main/examples/fastapi_app.py) drops the repair step into a FastAPI endpoint.

## requirements

**Please pin this library only on the major version!**

We use TDD and strict semantic versioning, there will be frequent updates and no breaking changes in minor and patch versions.
To ensure that you only pin the major version of this library in your `requirements.txt`, specify the package name followed by the major version and a wildcard for minor and patch versions. For example:

    json_repair==0.*

In this example, any version that starts with `0.` will be acceptable, allowing for updates on minor and patch versions.

---
