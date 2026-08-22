# semantica-agi/semantica

Graph-Native Infrastructure for Context and Accountable AI Systems

## features

| | Vector DB + RAG | Plain LLM Memory | **Semantica** |
| --- | --- | --- | --- |
| **Recall method** | Embedding similarity | Token window | Graph traversal + semantic search |
| **Decision history** | Not stored | Not stored | First-class queryable objects |
| **Provenance** | None | None | W3C PROV-O, source-linked |
| **Reasoning** | None | Black box | Forward chain, Rete, Datalog, SPARQL |
| **Conflict detection** | Silent overwrite | Silent overwrite | Detected, flagged, resolved |
| **Time travel** | No | No | Point-in-time graph snapshots |
| **Compliance export** | None | None | PROV-O, SHACL, OWL, RDF |
| **Policy enforcement** | None | None | Built-in rule engine + SHACL |
| **Entity resolution** | No | No | Blocking + semantic deduplication |
| **Multi-agent context** | Separate per agent | Separate per agent | Single shared intelligence layer |

Semantica complements your existing stack rather than replacing it. Keep your LLM, vector store, and agent framework exactly as they are; Semantica adds the decision records, causal reasoning, provenance, ontology governance, conflict detection, and audit trails on top. The reasoning engines, KG construction, and provenance layer are fully deterministic; no LLM is required to use them.

---

## installation

```bash
pip install semantica
```

```python
from semantica.context import ContextGraph

graph = ContextGraph(advanced_analytics=True)

## configuration

```

<div align="center">

If Semantica solves a real problem for you, a star helps others find it.

**[⭐ Star on GitHub](https://github.com/semantica-agi/semantica)** &nbsp;·&nbsp; **[Join Discord](https://discord.gg/sV34vps5hH)**

</div>

---

## tools

vs  = VectorStore(backend="faiss")
ctx = AgentContext(vector_store=vs, knowledge_graph=graph)
ctx.store("Alice approved the Acme renewal in Q1 2024", conversation_id="conv_001")
retrieved = ctx.retrieve("who approved the Acme contract?")
```

**Why graph over embeddings:** traversal finds connections embeddings miss (a person 3 hops from a contract); every node carries provenance so you can always ask *"where did this come from?"*; conflicts are flagged before they corrupt your knowledge base; point-in-time snapshots let you replay history without reprocessing.

---
