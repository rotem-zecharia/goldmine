# whitphx/streamlit-webrtc

Real-time video and audio processing on Streamlit

## tools

### [⚡️Showcase including following examples and more](https://github.com/whitphx/streamlit-webrtc-example): [🎈Online demo](https://share.streamlit.io/whitphx/streamlit-webrtc-example/main/app.py)

* Object detection
* OpenCV filter
* Uni-directional video streaming
* Audio processing

### [⚡️Real-time Speech-to-Text](https://github.com/whitphx/streamlit-stt-app): [🎈Online demo](https://share.streamlit.io/whitphx/streamlit-stt-app/main/app_deepspeech.py)

It converts your voice into text in real time.
This app is self-contained; it does not depend on any external API.

### [⚡️Real-time video style transfer](https://github.com/whitphx/style-transfer-web-app): [🎈Online demo](https://share.streamlit.io/whitphx/style-transfer-web-app/main/app.py)
It applies a wide variety of style transfer filters to real-time video streams.

### [⚡️Video chat](https://github.com/whitphx/streamlit-video-chat-example)
(Online demo not available)

You can create video chat apps with ~100 lines of Python code.

### [⚡️Tokyo 2020 Pictogram](https://github.com/whitphx/Tokyo2020-Pictogram-using-MediaPipe): [🎈Online demo](https://share.streamlit.io/whitphx/tokyo2020-pictogram-using-mediapipe/streamlit-app)
[MediaPipe](https://google.github.io/mediapipe/) is used for pose estimation.

## installation

```shell
$ pip install -U streamlit-webrtc
```

## Quick tutorial

See also [the sample pages, `pages/*.py`](https://github.com/whitphx/streamlit-webrtc/tree/main/pages), which contain a wide variety of usage.

See also ["Developing Web-Based Real-Time Video/Audio Processing Apps Quickly with Streamlit"](https://towardsdatascience.com/developing-web-based-real-time-video-audio-processing-apps-quickly-with-streamlit-7c7bcd0bc5a8).

---

Create `app.py` with the content below.
```py
from streamlit_webrtc import webrtc_streamer

webrtc_streamer(key="sample")
```
Unlike other Streamlit components, `webrtc_streamer()` requires the `key` argument as a unique identifier. Set an arbitrary string to it.

Then run it with Streamlit and open http://localhost:8501/.
```shell
$ streamlit run app.py
```

You see the app view, so click the "START" button.

Then, video and audio streaming starts. If asked for permissions to access the camera and microphone, allow it.
![Basic example of streamlit-webrtc](./docs/images/streamlit_webrtc_basic.gif)

### Media toggle controls

When the app sends local camera or microphone input, `webrtc_streamer()` shows camera and microphone toggle buttons next to the Start/Stop button. These controls let users turn their outgoing camera or microphone track on and off without stopping the WebRTC session.

Set `media_toggle_controls=False` to hide these toggle buttons.

```python
from streamlit_webrtc import webrtc_streamer

webrtc_streamer(key="example", media_toggle_controls=False)
```

When a user turns off the camera or microphone with these buttons, the WebRTC track stays active. As described in MDN's [`MediaStreamTrack.enabled` documentation](https://developer.mozilla.org/en-US/docs/Web/API/MediaStreamTrack/enabled), disabled audio tracks send silence, and disabled video tracks send black frames; the session does not stop or renegotiate.

Next, edit `app.py` as below and run it again.
```py
from streamlit_webrtc import webrtc_streamer
import av


def video_frame_callback(frame):
    img = frame.to_ndarray(format="bgr24")

    flipped = img[::-1,:,:]

    return av.VideoFrame.from_ndarray(flipped, format="bgr24")


webrtc_streamer(key="example", video_frame_callback=video_frame_callback)
```

Now the video is vertically flipped.
![Vertically flipping example](./docs/images/streamlit_webrtc_flipped.gif)

As an example above, you can edit the video frames by defining a callback that receives and returns a frame and passing it to the `video_frame_callback` argument (or `audio_frame_callback` for audio manipulation).
The input and output frames are the instance of [`av.VideoFrame`](https://pyav.org/docs/develop/api/video.html#av.video.frame.VideoFrame) (or [`av.AudioFrame`](https://pyav.org/docs/develop/api/audio.html#av.audio.frame.AudioFrame) when dealing with audio) of [`PyAV` library](https://pyav.org/).

You can inject any kinds of image (or audio) processing inside the callback.
See examples above for more applications.

### Pass parameters to the callback

You can also pass parameters to the callback.

In the example below, a boolean `flip` flag is used to turn on/off the image flipping.
```python
import streamlit as st
from streamlit_webrtc import webrtc_streamer
import av


flip = st.checkbox("Flip")


def video_frame_callback(frame):
    img = frame.to_ndarray(format="bgr24")

    flipped = img[::-1,:,:] if flip else img

    return av.VideoFrame.from_ndarray(flipped, format="bgr24")


webrtc_streamer(key="example", video_frame_callback=video_frame_callback)
```

### Pull values from the callback

Sometimes we want to read the values generated in the callback from the outer scope.

Note that the callback is executed in a forked thread running independently of the main script, so we have to take care of the following points and need some tricks for implementation like the example below (See also the section below for some limitations in the callback due to multi-threading).

* Thread-safety
  * Passing t

## limitations

The callbacks are executed in forked threads different from the main one, so there are some limitations:
* Streamlit methods (`st.*` such as `st.write()`) do not work inside the callbacks.
* Variables inside the callbacks cannot be directly referred to from the outside.
* The `global` keyword does not work expectedly in the callbacks.
* You have to care about thread-safety when accessing the same objects both from outside and inside the callbacks as stated in the section above.

## Cleanup on Stop (session lifecycle)

`webrtc_streamer()` accepts `on_video_ended` and `on_audio_ended` arguments — zero-argument callables that fire when the corresponding input media track ends (the user clicks "STOP", closes the page, or the connection drops). They are the recommended hook for tearing down per-session resources that the frame callbacks allocated, such as worker threads, model handles, file writers, queues, or `st.session_state` entries.

```python
import streamlit as st
from streamlit_webrtc import webrtc_streamer


def video_frame_callback(frame):
    # ... process the frame, possibly initializing per-session state on first call ...
    return frame


def on_video_ended():
    st.session_state.pop("my_session_resource", None)


webrtc_streamer(
    key="example",
    video_frame_callback=video_frame_callback,
    on_video_ended=on_video_ended,
)
```

These callbacks run on `aiortc`'s asyncio loop — not Streamlit's main thread — so the same caveats as the frame callbacks apply: `st.*` calls do not work inside them, and shared state must be mutated in a thread-safe way (e.g. with a `threading.Lock`, a `queue`, or a `threading.Event`).

When using the [class-based API](#class-based-callbacks), override `VideoProcessorBase.on_ended()` / `AudioProcessorBase.on_ended()` instead — they fire at the same lifecycle point.

## Source/sink track lifecycle

Factory helpers such as `create_video_source_track()`, `create_audio_source_track()`, `create_video_sink_track()`, `create_audio_sink_track()`, and `create_pcm_audio_source_track()` cache their returned objects in `st.session_state` by `key` so they survive Streamlit reruns. This is usually what you want: widget changes and reruns keep using the same media track.

By default, factory-created source and sink tracks are scoped to the active WebRTC session. When that session ends, for example when the user clicks STOP, closes the page, or the connection drops, the cached object is stopped and removed from `st.session_state`. The next WebRTC session with the same `key` gets a fresh object.

```python
from streamlit_webrtc import create_video_source_track

video_track = create_video_source_track(
    callback=video_source_callback,
    key="video-source",
)
```

To keep a factory-created object alive across multiple WebRTC sessions in the same Streamlit session, opt out with `lifecycle_scope="streamlit-session"`:

```python
video_track = create_video_source_track(
    callback=video_source_callback,
    key="video-source",
    lifecycle_scope="streamlit-session",
)
```

`lifecycle_scope` applies to source/sink factory helpers and `create_pcm_audio_source_track()`. It does not affect `webrtc_streamer()` itself, `create_process_track()`, or `create_mix_track()`, whose lifecycles are tied to input tracks or explicit mixer reuse.

## Class-based callbacks
The function-based callbacks (`video_frame_callback` / `audio_frame_callback`) shown above are the recommended API.

Until v0.37, the class-based callbacks (`video_processor_factory` / `audio_processor_factory` taking a `VideoProcessorBase` / `AudioProcessorBase` subclass) were the standard. They are still supported for backward compatibility — see the [old version of the README](https://github.com/whitphx/streamlit-webrtc/blob/v0.37.0/README.md#quick-tutorial) for that style — but new code should prefer the function-based callbacks. The class-based API is planned to be removed in a future major release (v1.0).

## Serving from remote host
When de

## configuration

To deploy the app to the cloud, we have to configure the *STUN* server via the `rtc_configuration` argument on `webrtc_streamer()` like below.

```python
webrtc_streamer(
    # ...
    rtc_configuration={  # Add this config
        "iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]
    }
    # ...
)
```

This configuration is necessary to establish the media streaming connection when the server is on a remote host.

:warning: You may need to set up a TURN server as well in some environments, **including Streamlit Community Cloud**. See also the next section.

`streamlit_webrtc` uses WebRTC for its video and audio streaming. It has to access a "STUN server" in the global network for the remote peers (precisely, peers over the NATs) to establish WebRTC connections.
As we don't see the details about STUN servers here, please google it if interested with keywords such as STUN, TURN, or NAT traversal, or read these articles ([1](https://towardsdatascience.com/developing-web-based-real-time-video-audio-processing-apps-quickly-with-streamlit-7c7bcd0bc5a8#1cec), [2](https://dev.to/whitphx/python-webrtc-basics-with-aiortc-48id), [3](https://www.3cx.com/pbx/what-is-a-stun-server/)).

The example above is configured to use `stun.l.google.com:19302`, which is a free STUN server provided by Google.

You can also use any other STUN servers.
For example, [one user reported](https://github.com/whitphx/streamlit-webrtc/issues/283#issuecomment-889753789) that the Google's STUN server had a huge delay when using from China network, and the problem was solved by changing the STUN server.

For those who know about the browser WebRTC API: The value of the rtc_configuration argument will be passed to the [`RTCPeerConnection`](https://developer.mozilla.org/en-US/docs/Web/API/RTCPeerConnection/RTCPeerConnection) constructor on the frontend.

### Configure the TURN server if necessary
Even if the STUN server is properly configured, media streaming may not work in some network environments, either from the server or from the client.
For example, if the server is hosted behind a proxy, or if the client is on an office network behind a firewall, the WebRTC packets may be blocked (**Streamlit Community Cloud is the case**). [This article](https://blog.addpipe.com/troubleshooting-webrtc-connection-issues/#steptwodiscoverystunandturn) summarizes the possible situations.

In such environments, [TURN server](https://webrtc.org/getting-started/turn-server) is required.

There are several options for setting up a TURN server:
* [Twilio Network Traversal Service](https://www.twilio.com/docs/stun-turn) (_recommended_) is a stable and easy-to-use solution. It's a paid service, but you can start with a free trial with a certain amount of credit.
  You can simply pass the `ice_servers` field of the [Network Traversal Service Tokens API](https://www.twilio.com/docs/api/2010-04-01/rest/token) response to the `iceServers` field of the `rtc_configuration` argument of `webrtc_streamer()`.
  ```python
  ## This sample code is from https://www.twilio.com/docs/stun-turn/api
  # Download the helper library from https://www.twilio.com/docs/python/install
  import os
  from twilio.rest import Client

  # Find your Account SID and Auth Token at twilio.com/console
  # and set the environment variables. See http://twil.io/secure
  account_sid = os.environ['TWILIO_ACCOUNT_SID']
  auth_token = os.environ['TWILIO_AUTH_TOKEN']
  client = Client(account_sid, auth_token)

  token = client.tokens.create()

  # Then, pass the ICE server information to webrtc_streamer().
  webrtc_streamer(
    # ...
    rtc_configuration={
        "iceServers": token.ice_servers
    }
    # ...
  )
  ```
  The [WebRTC sample app hosted on the Community Cloud](https://webrtc.streamlit.app/) uses this option. See [how it retrieves the ICE server information from the Twilio API](https://github.com/whitphx/streamlit-webrtc-example/blob/79ac65994a8c7f91475647d65e63b5040ea35863/sample_utils/turn.py) and 
