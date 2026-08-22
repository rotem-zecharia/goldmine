# SeekStorm/SeekStorm

SeekStorm: vector & lexical search - in-process library & multi-tenancy server, in Rust.

## features

**Twin-core native vector & keyword search**  
[Two separate, first-class, native index architectures](ARCHITECTURE.md#architecture) for **vector search** and **keyword search** under one roof.  
A query planner with 8 dedicated QueryModes and FusionTypes automatically decide how to combine the results for maximum query understanding.

**Performance**  
Lower latency, higher throughput, lower cost & energy consumption, esp. for multi-field and concurrent queries.  
Low tail latencies ensure a smooth user experience and prevent loss of customers and revenue.  
While some rely on proprietary hardware accelerators (FPGA/ASIC) or clusters to improve performance,  
SeekStorm achieves a similar boost algorithmically on a single commodity server.

**Consistency**  
No unpredictable query latency during and after large-volume indexing as SeekStorm doesn't require resource-intensive segment merges.  
Stable latencies - no cold start costs due to just-in-time compilation, no unpredictable garbage collection delays.  

**Scaling**  
Maintains low latency, high throughput, and low RAM consumption even for billion-scale indices.  
Unlimited field number, field length & index size.

**Relevance**  
Term proximity ranking provides more relevant results compared to BM25.

**Real-time**  
True real-time search, as opposed to NRT: every indexed document is immediately searchable, even before and during commit.

## installation

Facets are defined in 3 different places:
1. The facet fields are defined in the schema at create_index.
2. The facet field values are set in index_document at index time.
3. The query_facets/facet_filter parameters are specified at query time.  
   Facets are then returned in the search result object.

A minimal working example of faceted indexing & search requires just 60 lines of code. But to puzzle it all together from the documentation alone might be tedious. This is why we provide a quick start example here:

Add required crates to your project
```text
cargo add seekstorm
cargo add tokio
cargo add serde_json
```

Use an asynchronous Rust runtime
```rust ,no_run
use std::error::Error;
#[tokio::main]
async fn main() -> Result<(), Box<dyn Error + Send + Sync>> {

  // your SeekStorm code here

   Ok(())

## limitations

The following new features are planned to be implemented.  
Are you missing something? Let us know via issue or discussions.

**Improvements**

* Relevancy benchmarks: BeIR, MS MARCO

**New features**

* ✅ Native vector search
* ✅ TurboQuant (TQ) for vector search
* Late Interaction Multimodal Retrieval
* Geocoding, reverse geocoding, GeoJSON
* Model Context Protocol (MCP) server and CLI for Retrieval Augmented Generation (RAG) and agentic search.
* **Split of storage and compute**
  * Use S3 object storage as index backend
  * Use Distributed Key-Value store as index backend
* Elasticity: automatic spawning and winding down of shards in the cloud depending on index size and load.
* Distributed search cluster (currently PoC)
* More tokenizer types (Japanese, Korean)
* WebAssembly (Wasm)
* Wrapper/bindings in JavaScript, Python, Java, C#, C, Go for the SeekStorm Rust library
* Client libraries/SDK for the SeekStorm server REST API
  * ✅ Rust
  * ✅ Python
  * ✅ C#
  * ✅ Java 
  * TypeScript
  * Go
  * C
* Improved SIMD support
  - ✅ lexical search: 
	- ✅ x86_64 (Intel, AMD)
	  - ✅ AVX2
	  - AVX512
	  - AVX10
	- ✅ AArch64 (Apple Silicon, AWS Graviton)
	  - ✅ NEON 
	  - SVE/SVE2 
	- GPU (NVIDIA)
  - ✅ vector search: 
	- ✅ x86_64 (Intel, AMD)
	  - ✅ AVX2
	  - AVX512
	  - AVX10
	- ✅ AArch64 (Apple Silicon, AWS Graviton)
	  - ✅ NEON 
	  - SVE/SVE2 
	- GPU (NVIDIA)
