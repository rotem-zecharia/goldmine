# s60sc/ESP32-CAM_MJPEG2SD

ESP32 Camera motion capture application to record JPEGs to SD card as AVI files and stream to browser as MJPEG. If a microphone is installed then a WAV file is also created. Files can be uploaded via 

## installation

Download github files into the Arduino IDE sketch folder, removing `-master` from the application folder name.
Compile with at least arduino-esp32 core v3.1.1 which contains network fixes and frame selection changes.
Select the required ESP-CAM board by uncommenting ONE only of the `#define CAMERA_MODEL_*` in `ESP32-CAM_MJPEG2SD.h` unless using the one of the defaults:
* ESP32 Cam board - `CAMERA_MODEL_AI_THINKER`
* Freenove ESP32S3 Cam board - `CAMERA_MODEL_FREENOVE_ESP32S3_CAM`  

Optional features are not included by default. To include a feature, in `ESP32-CAM_MJPEG2SD.h` set relevant `#define INCLUDE_*` to `true`. 

Select the ESP32 or ESP32S3 Dev Module board and compile with PSRAM enabled and the following Partition scheme:
* ESP32 - `Minimal SPIFFS (...)`
* ESP32S3 - `8M with spiffs (...)` or `16MB(3MB APP...)`

**NOTE:**
* **If you get compilation errors you need to update your `arduino-esp32` core library in the IDE to latest v3.x
using [Boards Manager](https://github.com/s60sc/ESP32-CAM_MJPEG2SD/issues/61#issuecomment-1034928567)**
* **If you get error: `Startup Failure: Check SD card inserted`, or `Camera init error 0x105` it is usually a [camera board selection](https://github.com/s60sc/ESP32-CAM_MJPEG2SD/issues/219#issuecomment-1627785417) issue**
* **If you get warning: `Crash loop detected, check log`, it is usually an inadequate power supply.**


On first installation, the application will start in wifi AP mode - connect to SSID: **ESP-CAM_MJPEG_...**, to allow router to be selected and router password entered via the web page on `192.168.4.1`. The configuration data file (except passwords) is automatically created, and the application web pages automatically downloaded from GitHub to the SD card **/data** folder when an internet connection is available.

Subsequent updates to the application, or to the **/data** folder files, can be made using the **OTA Upload** tab. The **/data** folder can also be reloaded from GitHub using the **Reload /data** button on the **Edit Config** tab, or by using a WebDAV client.

An alternative installation process by [@ldijkman](https://github.com/ldijkman) is described [here](https://youtu.be/YLLGBM3i2aQ).

Browser functions only fully tested on Chrome.

## configuration

The operation of the application can be modified dynamically as below, by using the main web page, which should mostly be self explanatory.

Connections:
* The Wifi/Ethernet choice, Time zone, FTP/HTTPS, SMTP, and authentication parameters can be defined in **Access Settings** sidebar button. 
  - for **Time Zone** use dropdown, or paste in values from second column [here](https://raw.githubusercontent.com/nayarsystems/posix_tz_db/master/zones.csv)
* To make the changes persistent, press the **Save** button
    * For network changes, ESP must be rebooted.
* mdns name services in order to use `http://[Host Name]` instead of ip address.

To change the recording parameters:
* `Resolution` is the pixel size of each frame
* `Frame Rate` is the required frames per second
* `Quality` is the level of JPEG compression which affects image size.

SD storage management:
* Folders or files within folders can be deleted by selecting the required file or folder from the drop down list then pressing the **Delete** button and confirming.
* Folders or files within folders can be uploaded to a remote server via FTP / HTTPS by selecting the required file or folder from the drop down list then pressing the **File Upload** button. Can be uploaded in AVI format.
* Download selected AVI file from SD card to browser using **Download** button.
* Delete, or upload and delete oldest folder when card free space is running out.  

View application log via web page, displayed using **Show Log** tab:
  * Select log type for display:
    * RTC RAM: Cyclic 7KB log saved in RTC RAM (default)
    * Websocket: log is dynamically output via websocket
    * SD card: Unlimited size log saved to SD card
  * Use slider to enable SD logging, but can slow recording rate
  * Use buttons to refresh or clear selected log
