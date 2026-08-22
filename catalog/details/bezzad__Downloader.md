# bezzad/Downloader

Fast, cross-platform and reliable multipart downloader with asynchronous progress events for .NET applications.

## installation

```bash
dotnet add package Downloader
```

```csharp
await DownloadBuilder
    .New()
    .WithUrl(@"https://host.com/test-file.zip")
    .WithDirectory(@"C:\temp")
    .Build()
    .StartAsync();
```

## features

- Simple interface for download requests.
- Asynchronous, non-blocking file downloads.
- Supports all file types (e.g., images, videos, PDFs, APKs).
- Cross-platform support for files of any size.
- Real-time progress updates for each download chunk.
- Downloads files in multiple parts (parallel download).
- Resilient to client-side and server-side errors.
- Configurable `ChunkCount` to control download segmentation.
- Supports both in-memory and on-disk multipart downloads.
- Parallel saving of chunks directly into the final file (no temporary files).
- Always downloads to a temporary file (configurable extension, default `.download`), then renames to the final name on completion.
- Always pre-allocates file size before download begins.
- Resume downloads manually by saving and restoring the `DownloadPackage` object.
- Automatic resume: when enabled, download metadata is embedded inside the `.download` file — no extra files or manual serialization needed.
- Provides real-time speed and progress data.
- Asynchronous pause and resume functionality.
- Download files with dynamic speed limits.
- Supports downloading to memory streams (without saving to disk).
- Supports large file downloads and live-streaming (e.g., music playback during download).
- Download a specific byte range from a large file.
- Resolve a remote file's name, size, and range support **without downloading it** (`RemoteFileResolver`).
- Lightweight, fast codebase with no external dependencies.
- Manage RAM usage during downloads.
- Supports custom `HttpClient` or `HttpMessageHandler` injection for advanced scenarios (e.g., `IHttpClientFactory`, HTTP caching, custom delegating handlers).

---

## configuration

#### Simple Configuration

```csharp
var downloadOpt = new DownloadConfiguration()
{
    // Number of file parts, default is 1
    ChunkCount = 8, 
    // Download parts in parallel (default is false)
    ParallelDownload = true

## tools

For easy and fluent use of the downloader, you can use the `DownloadBuilder` class. Consider the following examples:

Simple usage:

```csharp
await DownloadBuilder
    .New()
    .WithUrl(@"https://host.com/test-file.zip")
    .WithDirectory(@"C:\temp")
    .Build()
    .StartAsync();
```

Complex usage:

```csharp
IDownload download = DownloadBuilder
    .New()
    .WithUrl(@"https://host.com/test-file.zip")
    .WithDirectory(@"C:\temp")
    .WithFileName("test-file.zip")
    .WithConfiguration(new DownloadConfiguration())
    .Build();

download.DownloadProgressChanged += DownloadProgressChanged;
download.DownloadFileCompleted += DownloadFileCompleted;
download.DownloadStarted += DownloadStarted;
download.ChunkDownloadProgressChanged += ChunkDownloadProgressChanged;

await download.StartAsync();

download.Stop(); // cancel current download
```

Resume the existing download package:

```csharp
await DownloadBuilder.New().Build(package).StartAsync();
```

Resume the existing download package with a new configuration:

```csharp
await DownloadBuilder.New().Build(package, config).StartAsync();
```

[Pause and Resume quickly](https://github.com/bezzad/Downloader/blob/master/src/Downloader.Test/UnitTests/DownloadBuilderTest.cs#L110):

```csharp
var download = DownloadBuilder
    .New()
    .WithUrl(url)
    .WithFileLocation(path)
    .Build();

download.DownloadProgressChanged += (_, _) => {
    // pause current download quickly
    download.Pause();  
    // continue current download quickly
    download.Resume(); 
};

await download.StartAsync().ConfigureAwait(false);
```

---

## requirements

- [.NET 8.0 SDK](https://dotnet.microsoft.com/download/dotnet/8.0) or later.
- A supported platform (Windows, Linux, or macOS).

---
