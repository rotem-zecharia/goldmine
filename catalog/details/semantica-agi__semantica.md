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

# Every agent decision becomes a queryable, auditable knowledge node
decision_id = graph.record_decision(
    category="vendor_selection",
    scenario="Choose cloud provider for HIPAA workload",
    reasoning="AWS offers BAA, mature HIPAA tooling, and existing team expertise",
    outcome="selected_aws",
    confidence=0.93,
)

## tools

vs  = VectorStore(backend="faiss")
ctx = AgentContext(vector_store=vs, knowledge_graph=graph)
ctx.store("Alice approved the Acme renewal in Q1 2024", conversation_id="conv_001")
retrieved = ctx.retrieve("who approved the Acme contract?")
```

**Why graph over embeddings:** traversal finds connections embeddings miss (a person 3 hops from a contract); every node carries provenance so you can always ask *"where did this come from?"*; conflicts are flagged before they corrupt your knowledge base; point-in-time snapshots let you replay history without reprocessing.

---

## Recipe: Audit Trail for a Regulated Decision

One pattern built on the same Context Graph: record a causally-linked decision chain, attach provenance to every entity, and export a regulator-ready audit trail.

```python
from semantica.context import ContextGraph
from semantica.provenance import ProvenanceManager
from semantica.export import RDFExporter

graph = ContextGraph(advanced_analytics=True)
prov  = ProvenanceManager(storage_path="./audit.db")

# Record the decision chain
d1 = graph.record_decision(
    category="drug_interaction_check", scenario="Patient P-4821: warfarin + amiodarone co-prescribed",
    reasoning="Amiodarone potentiates warfarin's anticoagulant effect", outcome="flag_for_review", confidence=0.91,
)
d2 = graph.record_decision(
    category="dosage_adjustment", scenario="INR monitoring plan for P-4821",
    reasoning="Reduce warfarin dose per interaction severity; recheck INR in 5 days", outcome="dose_reduced_30pct", confidence=0.87,
)
# relationship_type must be one of CAUSED, INFLUENCED, or PRECEDENT_FOR
graph.add_causal_relationship(d1, d2, relationship_type="CAUSED")

# Track provenance for every entity
prov.track_entity("patient_P4821", source="ehr/medication_orders_2024.json",
                  metadata={"extractor": "NamedEntityRecognizer"})

# Export W3C PROV-O for regulator submission - to_kg_dict() is the official
# adapter that emits the {"entities": [...], "relationships": [...]} /
# source_id shape RDFExporter expects, so no manual field mapping is needed
kg = graph.to_kg_dict()
RDFExporter().export(kg, "audit_trail.ttl", format="turtle")
```

More recipes (GraphRAG pipelines, an AML rules engine, ontology-to-KG in one pass) are in **[More Recipes](#more-recipes)** below.

---

## Explore the Platform

Every module below is independently importable, with working code samples verified against the current source tree; use one or all of them.

| Module | What it does |
| --- | --- |
| [`semantica.ingest`](#semanticaingest-multi-source-ingestion) | Files, web, databases, APIs, streams, email, Git, Parquet, Databricks, Snowflake, SAP, MCP |
| [`semantica.semantic_extract`](#semanticasemantic_extract-ner-relations-events-triplets) | NER, relation extraction, event detection, triplet generation |
| [`semantica.kg`](#semanticakg-knowledge-graph-construction--analysis) | Graph construction, centrality, communities, link prediction |
| [`semantica.reasoning`](#semanticareasoning-forward-chaining-rete-datalog-sparql) | Forward chaining, Rete, Datalog, SPARQL, fully explainable |
| [`semantica.vector_store`](#semanticavector_store-hybrid--filtered-semantic-search) | FAISS, Qdrant, Weaviate, Milvus, Pinecone, PgVector, hybrid search |
| [`semantica.split`](#semanticasplit-graphrag-native-document-chunking) | Entity-aware, relation-aware, ontology-aware chunking for GraphRAG |
| [`semantica.provenance`](#semanticaprovenance-w3c-prov-o-lineage) | W3C PROV-O lineage on every fact |
| [`semantica.ontology`](#semanticaontology-owl-generation-shacl-validation) | OWL generation, SHACL validation, SKOS vocabularies |
| [`semantica.conflicts`](#semanticaconflicts-conflict-detection--resolution) | Detect and resolve conflicting facts across sources |
| [`semantica.deduplication`](#semanticadeduplication-entity-resolution-at-scale) | Entity resolution at scale |
| [`semantica.normalize`](#semanticanormalize-data-normalization--cleaning) | Text, enti
