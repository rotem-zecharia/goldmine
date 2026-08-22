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

## configuration

```

<div align="center">

If Semantica solves a real problem for you, a star helps others find it.

**[⭐ Star on GitHub](https://github.com/semantica-agi/semantica)** &nbsp;·&nbsp; **[Join Discord](https://discord.gg/sV34vps5hH)**

</div>

---

## Architecture

Semantica is a real end-to-end pipeline, not a single library with a marketing name. Every stage below is a shipping module, independently importable:

```
Sources → Ingest → Parse → Normalize → Split → Extract → Conflict Detection → Deduplication
   → Knowledge Graph → [ Ontology · Reasoning · Provenance · Decisions ] → Enriched KG
   → Vector Store + Polyglot Graph Store (RDF & LPG) → Export / Visualize / REST · MCP · CLI
```

- **Ingest:** files, web, databases, enterprise data platforms (Databricks, Snowflake), cloud (Google Drive, Elasticsearch), streams (Kafka, Kinesis), Git, email, MCP
- **Parse → Normalize → Split:** document parsing, text/entity/date normalization, GraphRAG-native entity-aware chunking
- **Extract → Conflict Detection → Deduplication:** NER, relations, events, triplets; conflicting facts flagged and resolved before they merge
- **Knowledge Graph:** `GraphBuilder` constructs the graph; bi-temporal facts and full graph analytics (centrality, communities, link prediction) run on top of it
- **Ontology · Reasoning · Provenance · Decisions:** the intelligence layer sitting on the KG, with SHACL/OWL governance, Rete/Datalog/SPARQL inference, W3C PROV-O lineage, and first-class decision records
- **Storage:** polyglot by design, with RDF triple stores (embedded Oxigraph, Blazegraph, Apache Jena, Eclipse RDF4J), Labeled Property Graphs (Neo4j, FalkorDB, Apache AGE, AWS Neptune), and vector stores, all swappable without touching your code
- **Outputs:** export (RDF, OWL, Parquet, Cypher, JSON-LD), interactive visualization, and access via REST API, MCP server, or CLI

**→ [Full Mermaid diagrams for the pipeline and the decision intelligence lifecycle](ARCHITECTURE.md)**

---

## Decision Intelligence

Decision Intelligence turns every AI choice from an ephemeral inference into a permanent, auditable, queryable record. It answers *"what did your AI decide, why, and what happened next?"*: the question regulators and enterprise risk teams ask with increasing urgency.

In Semantica, a decision is not a log line. It is a first-class graph node with a full lifecycle. In regulated domains, every AI decision must be traceable to a source and defensible to an auditor: `record_decision()` creates a permanent, structured record exportable as W3C PROV-O, the format most compliance frameworks accept for regulator submission.

```
record_decision()             → stored as a graph node with full structured context
add_causal_relationship()     → linked to upstream causes and downstream effects
find_similar_decisions()      → semantic precedent search across all past decisions
trace_decision_chain()        → full causal ancestry back to root causes
analyze_decision_impact()     → downstream influence map - everything this decision affected
check_decision_rules()        → policy compliance gate against configurable rule sets
export / audit trail          → W3C PROV-O, CSV, or JSON for regulator submission
```

```python
from semantica.context import ContextGraph

graph = ContextGraph(advanced_analytics=True)

# Record decisions with full structured context
app_id = graph.record_decision(
    category="credit_application",
    scenario="Personal loan, $85k income, 31% DTI, 3yr employment",
    reasoning="Income meets threshold; employment stable; no adverse credit events",
    outcome="proceed_to_underwriting",
    confidence=0.88,
    metadata={"applicant_id": "A-7291"},
)
uw_id = graph.record_decision(
    category="loan_underwriting",
    scenario="Underwriting review for A-7291",
    reasoning="DTI within policy; clean 36-month credit history",
    outcome="approved",
    confidence=0.94,
)
rate_id = graph.record_decision(
    category="interest_rate",
    scenario=

## tools

vs  = VectorStore(backend="faiss")
ctx = AgentContext(vector_store=vs, knowledge_graph=graph)
ctx.store("Alice approved the Acme renewal in Q1 2024", conversation_id="conv_001")
retrieved = ctx.retrieve("who approved the Acme contract?")
```

**Why graph over embeddings:** traversal finds connections embeddings miss (a person 3 hops from a contract); every node carries provenance so you can always ask *"where did this come from?"*; conflicts are flagged before they corrupt your knowledge base; point-in-time snapshots let you replay history without reprocessing.

---

## Recipe: Audit Trail for a Regulated Decision

The flagship pattern: record a causally-linked decision chain, attach provenance to every entity, and export a regulator-ready audit trail.

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
| [`semantica.ingest`](#semanticaingest-multi-source-ingestion) | Files, web, databases, APIs, streams, email, Git, Parquet, Databricks, Snowflake, MCP |
| [`semantica.semantic_extract`](#semanticasemantic_extract-ner-relations-events-triplets) | NER, relation extraction, event detection, triplet generation |
| [`semantica.kg`](#semanticakg-knowledge-graph-construction--analysis) | Graph construction, centrality, communities, link prediction |
| [`semantica.reasoning`](#semanticareasoning-forward-chaining-rete-datalog-sparql) | Forward chaining, Rete, Datalog, SPARQL, fully explainable |
| [`semantica.vector_store`](#semanticavector_store-hybrid--filtered-semantic-search) | FAISS, Qdrant, Weaviate, Milvus, Pinecone, PgVector, hybrid search |
| [`semantica.split`](#semanticasplit-graphrag-native-document-chunking) | Entity-aware, relation-aware, ontology-aware chunking for GraphRAG |
| [`semantica.provenance`](#semanticaprovenance-w3c-prov-o-lineage) | W3C PROV-O lineage on every fact |
| [`semantica.ontology`](#semanticaontology-owl-generation-shacl-validation) | OWL generation, SHACL validation, SKOS vocabularies |
| [`semantica.conflicts`](#semanticaconflicts-conflict-detection--resolution) | Detect and resolve conflicting facts across sources |
| [`semantica.deduplication`](#semanticadeduplication-entity-resolution-at-scale) | Entity resolution at scale |
| [`semantica.normalize`](#semanticanormalize-data-normalization--cleaning) | Text, entity, date, and number normali
