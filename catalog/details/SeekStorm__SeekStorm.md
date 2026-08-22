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

## Benchmarks

### Lexical Search

<img src="assets/search_benchmark_game1.png" width="800" alt="Benchmark">
<br>
<br>
<img src="assets/search_benchmark_game2.png" width="800" alt="Benchmark">
<br>
<br>
<img src="assets/search_benchmark_game3.png" width="800" alt="Benchmark">
<br>
<br>
<img src="assets/ranking.jpg" width="800" alt="Ranking">

*the who: vanilla BM25 ranking vs. SeekStorm proximity ranking*<br><br>

**Methodology**  
Comparing different open-source search engine libraries (BM25 lexical search) using the open-source **search_benchmark_game** developed by [Tantivy](https://github.com/quickwit-oss/search-benchmark-game/) and [Jason Wolfe](https://github.com/jason-wolfe/search-index-benchmark-game).

**Benefits**
+ using a proven open-source benchmark used by other search libraries for comparability
+ adapters written mostly by search library authors themselves for maximum authenticity and faithfulness
+ results can be replicated by everybody on their own infrastructure
+ detailed results per query, per query type and per result type to investigate optimization potential

**Detailed benchmark results**
https://seekstorm.github.io/search-benchmark-game/

**Benchmark code repository**
https://github.com/SeekStorm/search-benchmark-game/

See our **blog posts** for more detailed information: [SeekStorm is now Open Source](https://seekstorm.com/blog/sneak-peek-seekstorm-rust/) and [SeekStorm gets Faceted search, Geo proximity search, Result sorting](https://seekstorm.com/blog/faceted_search-geo-proximity-search/)

### Vector search

<img src="assets/vector_search_benchmark.png" width="800" alt="Benchmark">
<br>
<br>

#### [SIFT1M dataset](http://corpus-texmex.irisa.fr/) 1 million vectors, 128 dimensions, f32 precision, Euclidean  
- 8-bit Scalar Quantization, nprobe=16 -> recall@10=95%, average latency=188 microseconds  
- 8-bit Scalar Quantization, nprobe=33 -> recall@10=99%, average latency=302 microseconds  

<br>

#### [GIST1M dataset](http://corpus-texmex.irisa.fr/) 1 million vectors, 960 dimensions, f32 precision, Euclidean  
- 8-bit Scalar Quantization, nprobe=38 -> recall@10=95%, average latency=3,198 microseconds  
- 8-bit Scalar Quantization, nprobe=80 -> recall@10=98%, average latency=5,737 microseconds  


[Benchmark code](#vector-search-sift1m-dataset)

### Benchmark vector search vs. lexical search (Wikipedia)

There are benchmarks of vector search engines, and benchmarks of lexical search engines.  
But seeing the latency of lexical search and vector search stacked up against each other might offer some unique insigh

## tools

### Lexical search

Add required crates to your project
```text
cargo add seekstorm
cargo add tokio
cargo add serde_json
```

Use an asynchronous Rust runtime
```rust
use std::error::Error;
#[tokio::main]
async fn main() -> Result<(), Box<dyn Error + Send + Sync>> {

  // your SeekStorm code here

   Ok(())
}
```

create schema (from JSON)
```rust
use seekstorm::index::SchemaField;

let schema_json = r#"
[{"field":"title","field_type":"Text","store":false,"index_lexical":false,"dictionary_source":true,"completion_source":true},
{"field":"body","field_type":"Text","store":true,"index_lexical":true},
{"field":"url","field_type":"Text","store":false,"index_lexical":false}]"#;
let schema:Vec<SchemaField>=serde_json::from_str(schema_json).unwrap();
```

create schema (from SchemaField)
```rust
use seekstorm::index::{SchemaField,FieldType};

let schema= vec![
    SchemaField::new("title".to_owned(), false, false,false, FieldType::Text, false,false, 1.0,true,true),
    SchemaField::new("body".to_owned(),true,true,false,FieldType::Text,false,true,1.0,false,false),
    SchemaField::new("url".to_owned(), false, false,false, FieldType::Text,false,false,1.0,false,false),
];
```

create index
```rust ,no_run
# tokio_test::block_on(async {

use std::path::Path;
use seekstorm::index::{IndexMetaObject, Clustering, LexicalSimilarity,TokenizerType,StopwordType,FrequentwordType,AccessType,StemmerType,NgramSet,SchemaField,FieldType,SpellingCorrection,QueryCompletion,DocumentCompression,create_index};
use seekstorm::vector::Inference;
use seekstorm::vector_similarity::VectorSimilarity;

let index_path=Path::new("C:/index/");

let schema= vec![
    SchemaField::new("title".to_owned(), false, false,false, FieldType::Text, false,false, 1.0,true,true),
    SchemaField::new("body".to_owned(),true,true,false,FieldType::Text,false,true,1.0,false,false),
    SchemaField::new("url".to_owned(), false, false, false,FieldType::Text,false,false,1.0,false,false),
];

let meta = IndexMetaObject {
    id: 0,
    name: "test_index".into(),
    lexical_similarity: LexicalSimilarity::Bm25f,
    tokenizer: TokenizerType::UnicodeAlphanumeric,
    stemmer: StemmerType::None,
    stop_words: StopwordType::None,
    frequent_words: FrequentwordType::English,
    ngram_indexing: NgramSet::NgramFF as u8,
    document_compression: DocumentCompression::Snappy,
    access_type: AccessType::Mmap,
    spelling_correction: Some(SpellingCorrection { max_dictionary_edit_distance: 1, term_length_threshold: Some([2,8].into()),count_threshold: 20,max_dictionary_entries:500_000 }),
    query_completion: Some(QueryCompletion{max_completion_entries:10_000_000}),
    clustering: Clustering::None,
    inference: Inference::None,
};

let segment_number_bits1=11;
let index_arc=create_index(index_path,meta,&schema,&Vec::new(),segment_number_bits1,false,None).await.unwrap();

# });
```

open index (alternatively to create index)
```rust ,no_run
# tokio_test::block_on(async {

use std::path::Path;
use seekstorm::index::open_index;

let index_path=Path::new("C:/index/");
let mut index_arc=open_index(index_path).await.unwrap(); 

# });
```

index documents (from JSON)
```rust ,no_run
# tokio_test::block_on(async {

use std::path::Path;
use seekstorm::index::{open_index, IndexDocuments};

let index_path=Path::new("C:/index/");
let mut index_arc=open_index(index_path).await.unwrap(); 

let documents_json = r#"
[{"title":"title1 test","body":"body1","url":"url1"},
{"title":"title2","body":"body2 test","url":"url2"},
{"title":"title3 test","body":"body3 test","url":"url3"}]"#;
let documents_vec=serde_json::from_str(documents_json).unwrap();

index_arc.index_documents(documents_vec).await; 

# });
```

index document (from Document)
```rust ,no_run
# tokio_test::block_on(async {

use seekstorm::index::{FileType, Document, IndexDocument, open_index};
use std::path::Path;
use serde_json::Value;

let index_path=Path::new("C:/index/");
let mut index_arc=open_index(index_path).await.unwrap(); 

let docume

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
}
```
create index
```rust ,no_run
# tokio_test::block_on(async {

use std::path::Path;
use std::sync::{Arc, RwLock};
use seekstorm::index::{IndexMetaObject, Clustering,LexicalSimilarity,TokenizerType,StopwordType,FrequentwordType,AccessType,StemmerType,NgramSet,DocumentCompression,create_index};
use seekstorm::vector::Inference;
use seekstorm::vector_similarity::VectorSimilarity;

let index_path=Path::new("C:/index/");//x

let schema_json = r#"
[{"field":"title","field_type":"Text","store":false,"index_lexical":false},
{"field":"body","field_type":"Text","store":true,"index_lexical":true},
{"field":"url","field_type":"Text","store":true,"index_lexical":false},
{"field":"town","field_type":"String16","store":false,"index_lexical":false,"facet":true}]"#;
let schema=serde_json::from_str(schema_json).unwrap();

let meta = IndexMetaObject {
    id: 0,
    name: "test_index".into(),
    lexical_similarity: LexicalSimilarity::Bm25f,
    tokenizer: TokenizerType::AsciiAlphabetic,
    stemmer: StemmerType::None,
    stop_words: StopwordType::None,
    frequent_words: FrequentwordType::English,
    ngram_indexing: NgramSet::NgramFF as u8,
    document_compression: DocumentCompression::Snappy,
    access_type: AccessType::Mmap,
    spelling_correction: None,
    query_completion: None,
    clustering: Clustering::None,
    inference: Inference::None,
};

let synonyms=Vec::new();

let segment_number_bits1=11;
let index_arc=create_index(index_path,meta,&schema,&synonyms,segment_number_bits1,false,None).await.unwrap();

# });
```

index documents
```rust ,no_run
# tokio_test::block_on(async {

use std::path::Path;
use seekstorm::index::{IndexDocuments,open_index};
use seekstorm::commit::Commit;

let index_path=Path::new("C:/index/");
let index_arc=open_index(index_path).await.unwrap();

let documents_json = r#"
[{"title":"title1 test","body":"body1","url":"url1","town":"Berlin"},
{"title":"title2","body":"body2 test","url":"url2","town":"Warsaw"},
{"title":"title3 test","body":"body3 test","url":"url3","town":"New York"}]"#;
let documents_vec=serde_json::from_str(documents_json).unwrap();

index_arc.index_documents(documents_vec).await; 

// ### commit documents

index_arc.commit().await;

# });
```

search index
```rust ,no_run
# tokio_test::block_on(async {

use std::path::Path;
use seekstorm::index::{IndexDocuments,open_index};
use seekstorm::search::{Search,SearchMode,QueryType,ResultType,QueryFacet,QueryRewriting};
use seekstorm::highlighter::{Highlight,highlighter};
use std::collections::HashSet;

let index_path=Path::new("C:/index/");
let index_arc=open_index(index_path).await.unwrap();
let query="test".to_string();
let query_vector=None;
let search_mode=SearchMode::Lexical;
let enable_empty_query=false;
let offset=0;
let length=10;
let query_type=QueryType::Intersection; 
let result_type=ResultType::TopkCount;
let include_uncommitted=false;
let field_filter=Vec::new();
let query_facets = vec![QueryFacet::String16 {field: "age".to_string(),prefix: "".to_string(),length:u16::MAX}];
let facet_filter=Vec::new();
//let facet_filter = vec![FacetFilter::String { field: "town".to_string(),filter: vec!["Berlin".to_string()],}];
let result

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
