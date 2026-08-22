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


## Main Function

A recording is generated either by the camera itself detecting motion, or by holding a given pin high (kept low by internal pulldown when released), eg by using an active high motion sensor such as a PIR (HC-SR501) or microwave radar (CWL-0516), or an I2C accelerometer (MPU6050), or a non motion detector such as a sound sensor (KY-037).
In addition a recording can be requested manually using the **Start Recording** button on the web page.

To play back a recording, select the file using **Playback & File Transfers** sidebar button to select the day folder then the required AVI file.
After selecting the AVI file, press **Start Playback** button to playback the recording. 
The **Start Stream** button shows a live video only feed from the camera. 

Recordings can then be uploaded to an FTP or HTTPS server or downloaded to the browser for playback on a media application, eg VLC.
To incorporate FTP or HTTPS server, set `#define INCLUDE_FTP_HFS` to `true`.

## Continuous Recording

A time lapse feature is available which can run in parallel with motion capture. 
Select **Time Lapse** button under **Motion Detect & Recording** sidebar button. Time Lapse configuration is under **Motion** button in **Edit Config** tab.
Time lapse files have the format **20200130_201015_VGA_15_60_T.avi**.

A continuous recording feature generates a sequence of files from power up, similar to dashcam recording style. Use **DashCam** slider in **Motion Detect & Recording** sidebar button to select a value representing the length in minutes of each file. Need to press **Save Settings** button then **Reboot ESP** to commence recording.
Select slider value 0 to switch off feature. Creates file names with format **20200130_201015_VGA_15_60_

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


## Configuration Web Page

More configuration details accessed via **Edit Config** tab, which displays further buttons:

**Network**:
* Default network interface is Wifi, but Ethernet can be used instead using boards with built in Ethernet, eg: [`CAMERA_MODEL_Waveshare_ESP32_S3_ETH`](https://www.waveshare.com/wiki/ESP32-S3-ETH), or by connecting an external W5500 Ethernet controller.
* Feature only available for ESP32S3 boards.
* All existing services automatically use the selected network interface after reboot.
* If Network interface in **Access Settings** side tab was previously set to Ethernet:
  * App runs in quiet mode (WiFi and BLE off).
  * First boot still prepares the SD `/data` folder and UI.
  * WiFi AP wizard is suppressed; access the device by its DHCP IP or mDNS `http(s)://<hostname>.local` if your network supports it.
  * PoE variants are supported at the hardware level; power delivery is handled by the board.
  * Contributed by [@RedCanti](https://github.com/RedCanti)
* If Network interface in **Access Settings** side tab was previously set to Eth+AP:
  * Wifi AP is available concurrently with Ethernet, but uses a separate network.
  * Do not open web pages on each network concurrently.
* To use an external W5500 Ethernet controller, after selecting Ethernet or Eth+AP, an additional tab **Ethernet** is present in the **Edit Config** tab for entering the SPI pins numbers used to connect to the W5500 Ethernet controller.

**Motion**: 
See [**Motion detection by Camera**](#motion-detection-by-camera) section.

**Peripherals** eg:
* Select if a PIR or radar sensor is to be used (which can also be used in parallel with camera motion detection).
* Control pan / tilt cradle for camera.
* Connect a PDM or I2S microphone and I2S amplifier.
* Connect a DS18B20 temperature sensor.
* Monitor voltage of battery supply on ADC pin.
* Wakeup on LDR after deep sleep at night.

To incorporate peripherals, set `#define INCLUDE_PERIPH` to `true`.

The **Peripherals** tab also enables further config tabs to be displayed:
* **Audio**: to configure microphones and amplifiers.
* **RC Config**: to configure hardware for remote control vehcles.
* **Servos**: to c
