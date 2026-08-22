# whitphx/streamlit-webrtc

Real-time video and audio processing on Streamlit

## tools

* Object detection
* OpenCV filter
* Uni-directional video streaming
* Audio processing

## installation

```shell
$ pip install -U streamlit-webrtc
```

## limitations

The callbacks are executed in forked threads different from the main one, so there are some limitations:
* Streamlit methods (`st.*` such as `st.write()`) do not work inside the callbacks.
* Variables inside the callbacks cannot be directly referred to from the outside.
* The `global` keyword does not work expectedly in the callbacks.
* You have to care about thread-safety when accessing the same objects both from outside and inside the callbacks as stated in the section above.

## configuration

To deploy the app to the cloud, we have to configure the *STUN* server via the `rtc_configuration` argument on `webrtc_streamer()` like below.

```python
webrtc_streamer(
    # ...
    rtc_configuration={  # Add this config
        "iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]
    }
    # ...
