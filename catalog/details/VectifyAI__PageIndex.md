# VectifyAI/PageIndex

📑 PageIndex: Document Index for Vectorless, Reasoning-based RAG

## installation

```bash
pip install -U pageindex
```


```python
import os
from pageindex import PageIndexClient

os.environ["OPENAI_API_KEY"] = "your-openai-key"

client = PageIndexClient(                     
    index_model="gpt-5.6-luna",               # model to build the tree index
    chat_model="gpt-5.6-sol",                 # model to search the tree
)
doc_id = client.submit_document("report.pdf")["doc_id"]

answer = client.chat("What was the 2023 operating margin, and where is it stated?",
                     doc_id=doc_id)
print(answer)
```

## tools

</summary>

<br>
