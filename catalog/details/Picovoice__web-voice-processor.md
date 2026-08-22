# Picovoice/web-voice-processor

A library for real-time voice processing in web browsers

## features

- '\_picovoice' : whether all Picovoice requirements are met
- 'AudioWorklet' (not currently used; intended for the future)
- 'isSecureContext' (required for microphone permission for non-localhost)
- 'mediaDevices' (basis for microphone enumeration / access)
- 'WebAssembly' (required for all Picovoice engines)
- 'webKitGetUserMedia' (legacy predecessor to getUserMedia)
- 'Worker' (required for resampler and for all engine processing)

## installation

```console
npm install @picovoice/web-voice-processor
```

(or)

```console
yarn add @picovoice/web-voice-processor
```

## configuration

To update the audio settings in `WebVoiceProcessor`, use the `setOptions` function:

```javascript
// Override default options
let options = {
  frameLength: 512,
  outputSampleRate: 16000,
  deviceId: null,
  filterOrder: 50,
};

WebVoiceProcessor.setOptions(options);
```
