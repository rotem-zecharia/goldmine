# gildas-lormeau/SingleFile

Web Extension for saving a faithful copy of a complete web page in a single HTML file

## installation

SingleFile can be installed from the store of:

- Firefox: https://addons.mozilla.org/firefox/addon/single-file
- Firefox for Android:
  https://addons.mozilla.org/android/addon/single-file
- Chrome:
  https://chromewebstore.google.com/detail/singlefile/mpiodijhokgodhhofbcjdecpffjipkle
- Safari (macOS and iOS): https://apps.apple.com/us/app/singlefile-for-safari/id6444322545
- Microsoft Edge:
  https://microsoftedge.microsoft.com/addons/detail/efnbkdcfmcmnhlkaijjjmhjjgladedno

You can also download the zip file
(https://github.com/gildas-lormeau/SingleFile/archive/master.zip) of the project
and install it manually by unzipping it somewhere on your disk and following
these instructions:

- Firefox: https://extensionworkshop.com/documentation/develop/temporary-installation-in-firefox
- Chrome and Microsoft Edge: https://github.com/gildas-lormeau/SingleFile-MV3
- Safari: https://github.com/gildas-lormeau/SingleFile-Safari-Extension
  
## Getting started

- Click on the SingleFile button in the extension toolbar to save the page.
- You can click again on the button to cancel the action when processing a page.

## Additional notes

- Open the context menu by right-clicking the SingleFile button in the extension
  toolbar or on the webpage. It allows you to save:
  - the current tab,
  - the selected content,
  - the selected frame.
- You can also process multiple tabs in one click and save:
  - the selected tabs,
  - the unpinned tabs,
  - all the tabs.
- Select "Annotate and save the page..." in the context menu to:
  - highlight text,
  - add notes,
  - remove content.
- The context menu also allows you to activate the auto-save of:
  - the current tab,
  - the unpinned tabs,
  - all the tabs.
- With auto-save active, pages are automatically saved every time after being
  loaded (or before being unloaded if not).
- Right-click on the SingleFile button and select "Manage extension" (Firefox) /
  "Options" (Chrome) to open the options page.
- Enable the option "Destination > save to Google Drive" or "Destination >
  upload to GitHub" to upload pages to Google Drive or GitHub respectively.
- Enable the option "Misc. > add proof of existence" to prove the existence of
  saved pages by linking the SHA256 of the pages into the blockchain.
- You can use the customizable shortkey Ctrl+Shift+Y to save the current tab or
  the selected tabs. Go to about:addons and select "Manage extension shortcuts"
  in the cogwheel menu to change it in Firefox. Go to
  chrome://extensions/shortcuts to change it in Chrome.
- The default save folder is the download folder configured in your browser, cf.
  about:addons in Firefox and chrome://settings in Chrome.
- See the extension help in the options page for more detailed information about
  the options and technical notes.

## FAQ

See https://github.com/gildas-lormeau/SingleFile/blob/master/faq.md

## Release notes

See https://addons.mozilla.org/firefox/addon/single-file/versions/

## limitations

See https://github.com/gildas-lormeau/SingleFile/blob/master/known-issues.md

## Command Line Interface (SingleFile CLI)

You can save web pages to HTML from the command line interface. See here for
more info: https://github.com/gildas-lormeau/single-file-cli.

## Integration with user scripts

You can execute a user script just before (and after) SingleFile saves a page.
For more info, see
https://github.com/gildas-lormeau/SingleFile/wiki/How-to-execute-a-user-script-before-a-page-is-saved.

## File format comparison

|   	                                                                          |        HTML        | Self-extracting ZIP | MHTML | Webarchive (Safari) | HTML+folder |
| ---                                	                                          |       :---:        |        :---:        | :---: |         :---:       |    :---:    |
| Pages are saved as a single file                                              | ✓ 	               | ✓ 	                 | ✓     | ✓                   |             |
| HTML and styles are minified                                                  | ✓                  | ✓ 	                 |       |    	               |             |
| Unused HTML and styles are removed from files                                 | ✓                  | ✓ 	                 |       |                     |   	         |
| Binary resources are not encoded in base 64                                   |                    | ✓ 	                 |       | ✓                   | ✓ 	         |
| Files are compressed                                                          |                    | ✓ 	                 |       |                     |   	         |
| Files can be viewed without installing any extension                          | ✓                  | ✓¹                  | ✓²    | ✓³                  | ✓           |
| Files can be viewed without running JavaScript                                | ✓                  |         	           | ✓     | ✓                   | ✓ 	         |
| Files can be unzipped to extract page resources                               |                    | ✓ 	                 |       |                     | n/a         |
| Files contains the text of the page (plain or formatted) which can be indexed | ✓ 	               | ✓⁴                  | ✓     | ✓ 	                 | ✓ 	         |

Footnotes:

¹ When using the "universal" self-extracting file format

² Only in Chromium-based browsers, and Internet Explorer

³ Only in Safari

⁴ An option must be enabled in the extension

## Projects using/compatible with SingleFile

- ArchiveBox - Open-source self-hosted web archiving:
  https://github.com/ArchiveBox/ArchiveBox
- htmls-to-datasette - Tool to index HTML files into a Sqlite database:
  https://github.com/pjamar/htmls-to-datasette
- Karakeep - Self-hostable bookmark-everything app with a touch of AI: 
  https://karakeep.app
- KOReader - Document viewer primarily aimed at e-ink readers:
  https://github.com/koreader/koreader
- linkding - Bookmark manager that you can host yourself. It's designed be to
  be minimal, fast, and easy to set up using Docker:
  https://github.com/sissbruecker/linkding
- Linkwarden - Self-hosted collaborative bookmark manager to collect, read, 
  annotate, and fully preserve what matters, all in one place:
  https://github.com/linkwarden/linkwarden
- obsidian-html-plugin - Plugin for reading HTML pages in Obsidian:
  https://github.com/nuthrash/obsidian-html-plugin
- Org-Dex.el - Emacs package designed to enhance Org-mode by integrating 
  SingleFile CLI: https://github.com/nitincodery/org-dex.el
- Petal Cite Web Importer - Browser extension to save PDFs and capture web pages
  in Petal Cite: https://github.com/ks-collab/cite-extension
- Pocket Search Engine - Semantic search app for Android that works entirely 
  offline: https://play.google.com/store/apps/details?id=com.pocketsearchengin
