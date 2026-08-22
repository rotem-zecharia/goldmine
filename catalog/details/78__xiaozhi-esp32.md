# 78/xiaozhi-esp32

An MCP-based chatbot / 一个基于MCP的聊天机器人

## features

- Wi-Fi, wired Ethernet, USB RNDIS, and ML307/EC801E or NT26 Cat.1 4G networking; supported boards can switch between Wi-Fi and 4G
- Offline voice wake-up with [ESP-SR](https://github.com/espressif/esp-sr), including customizable wake words
- Two communication transports: [WebSocket](docs/websocket.md) and [MQTT + UDP](docs/mqtt-udp.md)
- Opus audio streaming with conventional streaming ASR + LLM + TTS pipelines and Realtime end-to-end voice models; AEC-capable hardware supports realtime full-duplex interaction
- Speaker recognition, identifies the current speaker [3D Speaker](https://github.com/modelscope/3D-Speaker)
- OLED / LCD displays with emoji and rich expression support, plus camera vision input on supported boards
- Battery display and power management
- 39 interface languages, with localized voice prompts where available and English fallback
- ESP32, ESP32-C3, ESP32-C5, ESP32-C6, ESP32-S3, and ESP32-P4 chip platforms
- Wi-Fi provisioning through hotspot or BluFi
- Device-side MCP for device control (Speaker, LED, Servo, GPIO, etc.)
- Cloud-side MCP to extend large model capabilities (smart home control, PC desktop operation, knowledge search, email, etc.)
- Customizable wake words, fonts, emojis, and chat backgrounds with online web-based editing ([Custom Assets Generator](https://github.com/78/xiaozhi-assets-generator))

## configuration

- Cursor or VSCode
- Install the ESP-IDF plugin. [ESP-IDF v6.0.2](https://github.com/espressif/esp-idf/releases/tag/v6.0.2) is preferred; use a stable v6.0 or later release. ESP-IDF v5.5.2 is retained only for legacy board compatibility
- Linux is better than Windows for faster compilation and fewer driver issues
- This project uses Google C++ code style, please ensure compliance when submitting code
