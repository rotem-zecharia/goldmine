# microsoft/kernel-memory

Research project. A Memory solution for users, teams, and applications.

## tools

The example show the default documents ingestion pipeline:

1. Extract text: automatically recognize the file format and extract the information
2. Partition the text in small chunks, ready for search and RAG prompts
3. Extract embeddings using any LLM embedding generator
4. Save embeddings into a vector index such as
   [Azure AI Search](https://learn.microsoft.com/azure/search/vector-search-overview),
   [Qdrant](https://qdrant.tech/) or other DBs.

The example shows how to **safeguard private information** specifying who owns each document, and
how to **organize data** for search and faceted navigation, using **Tags**.

## C#

> ```csharp
> #r "nuget: Microsoft.KernelMemory.WebClient"
>
> var memory = new MemoryWebClient("http://127.0.0.1:9001"); // <== URL of KM web service
>
> // Import a file
> await memory.ImportDocumentAsync("meeting-transcript.docx");
>
> // Import a file specifying Document ID and Tags
> await memory.ImportDocumentAsync("business-plan.docx",
>     new Document("doc01")
>         .AddTag("user", "devis@contoso.com")
>         .AddTag("collection", "business")
>         .AddTag("collection", "plans")
>         .AddTag("fiscalYear", "2025"));
> ```

## Python

> ```python
> import requests
>
> # Files to import
> files = {
>           "file1": ("business-plan.docx", open("business-plan.docx", "rb")),
>         }
>
> # Tags to apply, used by queries to filter memory
> data = { "documentId": "doc01",
>          "tags": [ "user:devis@contoso.com",
>                    "collection:business",
>                    "collection:plans",
>                    "fiscalYear:2025" ]
>        }
>
> response = requests.post("http://127.0.0.1:9001/upload", files=files, data=data)
> ```




Direct Data Ingestion using embedded Serverless .NET component
==============================================================

> ```csharp
> var memory = new KernelMemoryBuilder()
>     .WithOpenAIDefaults(Environment.GetEnvironmentVariable("OPENAI_API_KEY"))
>     .Build<MemoryServerless>();
>
> // Import a file
> await memory.ImportDocumentAsync("meeting-transcript.docx");
>
> // Import a file specifying Document ID and Tags
> await memory.ImportDocumentAsync("business-plan.docx",
>     new Document("doc01")
>         .AddTag("collection", "business")
>         .AddTag("collection", "plans")
>         .AddTag("fiscalYear", "2025"));
> ```




Memory retrieval and RAG
========================

Asking questions, running RAG prompts, and filtering by user and other criteria is simple, with
answers including citations and all the information needed to verify their accuracy, pointing to
which documents ground the response.

## C#

> ### Asking questions:
> Questions can be asked targeting the entire memory set, or a subset using filters,
> e.g. to implement security filters.
> ```csharp
> var answer1 = await memory.AskAsync("How many people attended the meeting?");
>
> var answer2 = await memory.AskAsync("what's the project timeline?",
>                                     filter: MemoryFilters.ByTag("user", "devis@contoso.com"));
> ```

> ### Token usage:
> When generating answers with LLMs, the result includes a token usage report.
> ```csharp
> foreach (var report in tokenUsage)
> {
>     Console.WriteLine($"{report.ServiceType}: {report.ModelName} ({report.ModelType})");
>     Console.WriteLine($"- Input : {report.ServiceTokensIn}");
>     Console.WriteLine($"- Output: {report.ServiceTokensOut}");
> }
> ```
> #### Output:
> > Azure OpenAI: gpt-4o (TextGeneration)
> > - Input : 24356 tokens
> > - Output: 103 tokens

![km-stream-token-usage](https://github.com/user-attachments/assets/71abf161-106c-47cc-af06-66f810314687)

> ### Data lineage, citations, referencing sources:
>
> ```csharp
> await memory.ImportFileAsync("NASA-news.pdf");
>
> var answer = await memory.AskAsync("Any news from NASA about Orion?");
>
> Console.WriteLine(answer.Result + "/n");
>
> foreach (var x in answer.RelevantSources)
> {
>     Console.WriteLine($"  * {x.So
