# deniscerri/ytdlnis

Full-featured audio/video downloader for Android using yt-dlp

## features

- Download audio/video files from more than <a href="https://github.com/yt-dlp/yt-dlp/blob/master/supportedsites.md">1000 websites</a>
- Process playlists
	- Edit every playlist item separately just like in a normal download item
	- Select a common format for all items and/or select multiple audio formats in case you are downloading them as a video
	- Select a download path for all items
	- Select a filename template for all items
	- Batch update download type to audio/video/custom command in one click
- Queue downloads and schedule them by date and time
	- You can also schedule multiple items at the same time
- Download multiple items at the same time
- Use custom commands and templates or use yt-dlp with the built-in terminal
	- You can backup and restore templates so you can share them with your buddies
- Supports cookies. Log in with your accounts and download private/unavailable videos, unlock premium formats etc.
- Cut videos based on timestamps and video chapters (experimental yt-dlp feature)
	- You can make unlimited cuts
- Remove SponsorBlock elements from downloaded items
	- Embed them as a chapters in your video 
- Embed subtitles/metadata/chapters etc
- Modify metadata such as title and author
- Split item into separate files depending on its chapters
- Select different download formats
- Bottom card right from the share menu, no need to open the app 
	- You can create a txt file and fill it with links/playlists/search queries separate by a new line and the app will process them
- Search or insert a link from the app
	- You can stack searches so you can process them at the same time
- Log downloads in case of problems
- Re-download cancelled or failed downloads
	- You can use gestures to swipe left to redownload and right to delete
	- You can long click the redownload button in the details sheet to show the download card for more functionality
- Incognito mode when you don't want to save a download history or logs
- Quick download mode
	- Download immediately without having to wait for data to process. Turn off the bottom card and it will instantly start
- Open / share downloaded files right from the finished notification
- Most yt-dlp features are implemented, suggestions are welcome
- Material You interface
- Theming options
- Backup and restore features
- MVVM architecture with WorkManager

## 🧩 Plugin Support

YTDLnis orchestrates plugins so users can freely upgrade and downgrade components such as:
- Python
- JS Runtimes (NodeJS, Deno)
- FFmpeg
- Aria2c

You can install ytdlnis packages from this repository [ytdlnis-packages](https://github.com/deniscerri/ytdlnis-packages/) or through the updating section in the application.
<br>For more information refer to the repo's README.

## 📲 Screenshots

<div>
<img src="fastlane/metadata/android/en-US/images/phoneScreenshots/01.png" width="30%" />
<img src="fastlane/metadata/android/en-US/images/phoneScreenshots/02.png" width="30%" />
<img src="fastlane/metadata/android/en-US/images/phoneScreenshots/03.png" width="30%" />
<img src="fastlane/metadata/android/en-US/images/phoneScreenshots/04.png" width="30%" />
<img src="fastlane/metadata/android/en-US/images/phoneScreenshots/05.png" width="30%" />
<img src="fastlane/metadata/android/en-US/images/phoneScreenshots/06.png" width="30%" />
<img src="fastlane/metadata/android/en-US/images/phoneScreenshots/07.png" width="30%" />
<img src="fastlane/metadata/android/en-US/images/phoneScreenshots/08.png" width="30%" />
<img src="fastlane/metadata/android/en-US/images/phoneScreenshots/09.png" width="30%" />
<img src="fastlane/metadata/android/en-US/images/phoneScreenshots/10.png" width="30%" />
<img src="fastlane/metadata/android/en-US/images/phoneScreenshots/11.png" width="30%" />
<img src="fastlane/metadata/android/en-US/images/phoneScreenshots/12.png" width="30%" />
<img src="fastlane/metadata/android/en-US/images/phoneScreenshots/13.png" width="90%" />
</div>

## 💬 Contact

Join our [Discord](https://discord.gg/WW3KYWxAPm) or 
