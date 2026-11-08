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

## Sample Console Application

![sample-project](img/sample.gif)

---

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
- Parallel saving of all chunks directly into one file (no extra file per chunk).
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
- Lightweight, fast codebase. The only dependency is `Microsoft.Extensions.Logging.Abstractions`.
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
};
```

#### Complex Configuration

> **Note**: Only include the options you need in your application.

```csharp
var downloadOpt = new DownloadConfiguration()
{
    // size of each read from the network (1 byte to 1MB),
    // the default value is 1024 bytes
    BufferBlockSize = 10240, // 10KB
    // file parts to download, the default value is 1
    ChunkCount = 8,             
    // download speed limited to MaximumBytesPerSecond, 
    // the default value is zero, which means unlimited
    MaximumBytesPerSecond = 1024*1024*2, // 2MB/s
    // the maximum number of retries for each chunk,
    // the default value is int.MaxValue (retry forever)
    MaxTryAgainOnFailure = 5,    
    // release memory buffer after each MaximumMemoryBufferBytes 
    MaximumMemoryBufferBytes = 1024 * 1024 * 50, // 50MB
    // download parts of the file in parallel or not. 
    // The default value is false
    ParallelDownload = true,
    // number of parallel downloads. 
    // The default value is the same as the chunk count
    ParallelCount = 4,    
    // timeout (millisecond) per stream block reader, 
    // the default value is 5000 (minimum 100)
    BlockTimeout = 5000,
    // timeout (millisecond) per HttpClient request, 
    // default value is 100 seconds
    HttpClientTimeout = 100 * 1000,
    // set true if you want to download just a specific 
    // range of bytes of a large file
    RangeDownload = false,
    // floor offset of download range of a large file
    RangeLow = 0,
    // ceiling offset of download range of a large file
    RangeHigh = 0, 
    // clear package chunks data when download completed 
    // with failure, default value is false
    ClearPackageOnCompletionWithFailure = true, 
    // the minimum size of file to chunking or download a
    // file in multiple parts, the default value is 512
    MinimumSizeOfChunking = 102400, // 100KB
    // the minimum size of a single chunk, 
    // default value is 0 equal unlimited
    MinimumChunkSize = 10240, // 10KB
    // Get on-demand downloaded data with 
    // ReceivedBytes on the downloadProgressChanged event.
    // Live streaming uses one chunk, and it can not be
    // changed while a download runs (see Step 3)
    EnableLiveStreaming = false,
    // How to handle an existing filename when 
    // starting to download?
    FileExistPolicy = FileExistPolicy.Delete,
    // When enabled, the Downloader appends package 
    // metadata to the end of the .download file. 
    // On the next download attempt, 
    // if metadata is found in an existing .download file,
    // the download resumes automatically.
    EnableAutoResumeDownload = true,
    // A temporary extension appended to 
    // the real filename while downloading.
    // e.g., "file.zip" becomes "file.zip.download" 
    // during download. The Downloader always uses this
    // extension regardless of EnableAutoResumeDownload.
    // When the download completes, 
    // the file is renamed back to its final name.
    DownloadFileExtension = ".download",
    // config and customize request headers
    RequestConfiguration = 
    {        
        Accept = "*/*",
        CookieContainer = cookies,
        // your custom headers. Note: the default list is ["Accept-Encoding: identity"];
        // if you ask for gzip/br here, also set AutomaticDecompression,
        // or the compressed bytes are saved as the file.
        Headers = ["Accept-Encoding: identity", "X-Custom-Header: value"],
        KeepAlive = true, 
        ProtocolVersion = HttpVersion.Version11,
        // your custom user agent or 
        // your_app_name/app_version.
        UserAgent = "Mozilla/5.0",
        // without a Proxy the system proxy is used;
        // new WebProxy() (no address) means no proxy 

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

[Pause and Resume quickly](https://github.com/bezzad/Downloader/blob/master/src/Downloader.Test/UnitTests/DownloadBuilderTest.cs#L268):

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

## Using a Custom HttpClient or HttpMessageHandler

Some scenarios require using a custom `HttpClient` or `HttpMessageHandler` — for example, to reuse the connection pool from `IHttpClientFactory`, add HTTP caching via a `DelegatingHandler`, or apply custom authentication logic.

The Downloader provides two delegate properties on `DownloadConfiguration` for this purpose:

### Option 1: Provide a fully custom `HttpClient`

Use `CustomHttpClientFactory` when you want **full control** over the `HttpClient` instance. The Downloader will skip all internal handler and header configuration and use the returned client directly.

```csharp
var downloadOpt = new DownloadConfiguration()
{
    ChunkCount = 8,
    ParallelDownload = true,
    CustomHttpClientFactory = () => {
        // Example: use IHttpClientFactory
        return httpClientFactory.CreateClient("MyDownloader");
    }
};

var downloader = new DownloadService(downloadOpt);
await downloader.DownloadFileTaskAsync(url, filePath);
```

### Option 2: Provide a custom `HttpMessageHandler`

Use `CustomHttpMessageHandlerFactory` when you want to customize only the handler (e.g., for caching or custom SSL), while letting the Downloader still configure default request headers and timeout on the `HttpClient`.

```csharp
var downloadOpt = new DownloadConfiguration()
{
    ChunkCount = 8,
    ParallelDownload = true,
    CustomHttpMessageHandlerFactory = () => {
        return new SocketsHttpHandler {
            MaxConnectionsPerServer = 500,
            PooledConnectionLifetime = TimeSpan.FromMinutes(10)
        };
    }
};

var downloader = new DownloadService(downloadOpt);
await downloader.DownloadFileTaskAsync(url, filePath);
```

### Using the fluent builder API

Both options are also available through the `DownloadBuilder`:

```csharp
// With a custom HttpClient
await DownloadBuilder.New()
    .WithUrl(url)
    .WithDirectory(@"C:\temp")
    .WithHttpClient(() => httpClientFactory.CreateClient("MyDownloader"))
    .Build()
    .StartAsync();

// With a custom HttpMessageHandler
await DownloadBuilder.New()
    .WithUrl(url)
    .WithDirectory(@"C:\temp")
    .WithHttpMessageHandler(() => new SocketsHttpHandler {
        MaxConnectionsPerServer = 500,
        PooledConnectionLifetime = TimeSpan.FromMinutes(10)
    })
    .Build()
    .StartAsync();
```

> **Note:** If both `CustomHttpClientFactory` and `Cu

## requirements

- [.NET 8.0 SDK](https://dotnet.microsoft.com/download/dotnet/8.0) or later.
- A supported platform (Windows, Linux, or macOS).

---

### Build Instructions

#### 1. Clone the Repository

```bash
git clone https://github.com/bezzad/downloader.git
cd downloader
```

#### 2. Build the Native AOT Executable

Run the following command to compile the project for your target platform:

Windows (x64):

```bash
dotnet publish src/Downloader/Downloader.csproj -r win-x64 -f net8.0 -c Release
```

Linux (x64):

```bash
dotnet publish src/Downloader/Downloader.csproj -r linux-x64 -f net8.0 -c Release
```

macOS (x64):

```bash
dotnet publish src/Downloader/Downloader.csproj -r osx-x64 -f net8.0 -c Release
```

#### 3. Find the Output

The output will be located in:

```bash
src/Downloader/bin/Release/net8.0/<RUNTIME_IDENTIFIER>/publish/
```

Example for Windows:

```bash
src/Downloader/bin/Release/net8.0/win-x64/publish/
```

# Instructions for Contributing

Contributions are welcome — feel free to make changes and open a [**Pull Request**](http://help.github.com/pull-requests/) against the `develop` branch.
You can use either the latest version of Visual Studio or Visual Studio Code and .NET CLI for Windows, Mac and Linux.

For GitHub workflow, check out our Git workflow below this paragraph. We are following the excellent GitHub Flow process, and would like to make sure you have all the information needed to be a world-class contributor!

## Git Workflow

The general process for working with Downloader is:

1. [Fork](http://help.github.com/forking/) on GitHub
2. Make sure your line endings are correctly configured and fix your line endings!
3. Clone your fork locally
4. Configure the upstream repo (`git remote add upstream https://github.com/bezzad/downloader.git`)
5. Switch to the latest development branch (`git checkout develop`)
6. Create a local branch from that (`git checkout -b myBranch`).
7. Work on your feature
8. Rebase if required
9. Push the branch up to GitHub (`git push origin myBranch`)
10. Send a Pull Request on GitHub - the PR should target (have as a base branch) the `develop` branch rather than `master`.

We accept pull requests from the community. But you should **never** work on a clone of `master`, and you should **never** send a pull request from `master` - always from a branch. Please be sure to branch from the head of the `develop` branch (rather than `master`) when developing contributions.

## You can run tests with the Docker Compose file with the following command
>
> `docker compose -p downloader up`

(Older Docker installs use `docker-compose` instead.)

## Or with docker file
>
> `docker build -f ./dockerfile -t downloader-linux .`
> `docker run --name downloader-linux-container -d downloader-linux --env=ASPNETCORE_ENVIRONMENT=Development .`

## Or run the following command to call docker directly
>
> `docker run --rm -v ${pwd}:/app --env=ASPNETCORE_ENVIRONMENT=Development -w /app/src mcr.microsoft.com/dotnet/sdk:10.0 dotnet test -p:TargetFrameworks=net10.0 --logger:trx`

------------------------------------------------------

# Support the Project

I've spent a lot of time creating this project.

If you like my work, please give it a ⭐ — thanks! ❤️

Want to support the project? 

You can make a donation in any of the following ways:

[![Donate using Liberapay](https://liberapay.com/assets/widgets/donate.svg)](https://liberapay.com/bezzad/donate)

![donate tether (BSC)](https://img.shields.io/badge/Tether%20(BEP20)-0xFF6B6524BA90Fb7b0C5d5bE1D71903CBF0f8198a-green.svg)

------------------------------------------------------

# License

Licensed under the terms of the [MIT License](https://raw.githubusercontent.com/bezzad/Downloader/master/LICENSE)

[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2Fbezzad%2FDownloader.svg?type=large)](https://app.fossa.com/projects/git%2Bgithub.com%2Fbezzad%2FDownloader?ref=badge_large)

# Contributors

Thanks go to these wonderful people (List made with
