# fonoster/fonoster

🚀 The open-source alternative to Twilio.

## features

The most notable features of Fonoster are:

- [x] Multitenancy
- [x] Easy deployment of PBX functionalities
- [x] Programmable Voice Applications
- [x] NodeJS SDK
- [x] Support for Amazon Simple Storage Service (S3)
- [x] Secure API endpoints with Let's Encrypt
- [x] Authentication with OAuth2
- [X] Authentication with JWT 
- [x] Role-Based Access Control (RBAC)
- [x] Plugins-based Command-line Tool
- [x] Support for Google Speech APIs

## tools

A Voice Application is a server that controls a call's flow. A Voice Application can use any combination of the following verbs:

- `Answer` - Accepts an incoming call
- `Hangup` - Closes the call
- `Play`: Takes a URL with a media file and streams the sound back to the calling party
- `PlayDtmf` - Takes a DTMF sequence and plays it back to the calling party
- `Say` - Takes a text, synthesizes the text into audio, and streams back the result
- `Gather` - Waits for DTMF or speech events and returns back the result
- `SGather` - Returns a stream for future DTMF and speech results
- `Stream` - Creates a bidirectional stream to send and receive audio from a caller
- `Dial` - Passes the call to an Agent or a Number at the PSTN
- `Record` - It records the voice of the calling party and saves the audio on the Storage sub-system
- `Mute` - It tells the channel to stop sending media, effectively muting the channel
- `Unmute` - It tells the channel to allow media flow

Voice Application Example:

```typescript
const VoiceServer = require("@fonoster/voice").default;
const { 
  GatherSource, 
  VoiceRequest, 
  VoiceResponse 
} = require("@fonoster/voice");

new VoiceServer().listen(async (req: VoiceRequest, voice: VoiceResponse) => {
  const { ingressNumber, sessionRef, appRef } = req;

  await voice.answer();

  await voice.say("Hi there! What's your name?");

  const { speech: name } = await voice.gather({
    source: GatherSource.SPEECH
  });

  await voice.say("Nice to meet you " + name + "!");

  await voice.say("Please enter your 4 digit pin.");

  const { digits } = await voice.gather({
    maxDigits: 4,
    finishOnKey: "#"
  });

  await voice.say("Your pin is " + digits);

  await voice.hangup();
});

// Your app will live at tcp://127.0.0.1:50061 
// and you can easily publish it to the Internet with:
// ngrok tcp 50061
```

Everything in Fonoster is an API first, and initiating a call is no exception. You can use the SDK to start a call with a few lines of code.

Example of originating a call with the SDK:

```typescript
const SDK = require("@fonoster/sdk");

async function main(request) {
  const apiKey = "your-api-key";
  const apiSecret = "your-api-secret"
  const accessKeyId = "WO00000000000000000000000000000000";

  const client = new SDK.Client({ accessKeyId });
  await client.loginWithApiKey(apiKey, apiSecret);

  const calls = new SDK.Calls(client);
  const response = await calls.createCall(request);

  console.log(response); // successful response
}

const request = {
  from: "+18287854037",
  to: "+17853178070",
  appRef: "3e61ecb7-a1b6-4a93-84c3-4f1979165bca",
  // Optional metadata to be sent to the Voice Application
  metadata: {
    name: "John Doe",
    message: "Please call me back."
  }
};

main(request).catch(console.error);
```

## installation

To get started with Fonoster, use the following resources:

- [Deploying Fonoster with Docker](https://docs.fonoster.com/self-hosting)
- [Guide for Early Access User](https://docs.fonoster.com/quickstart)
- [Getting started with Fonoster](https://docs.fonoster.com/quickstart)
- [How we created an open-source alternative to Twilio and why it matters](https://dev.to/fonoster/how-we-created-an-open-source-alternative-to-twilio-and-why-it-matters-434g)

## Give a Star! ⭐

Please give it a star if you like this project or plan to use it. Thanks 🙏

## Bugs and Feedback

For bugs, questions, and discussions, please use the [Github Issues](https://github.com/fonoster/fonoster/issues)

## Contributing

For contributing, please see the following links:

 - [Contribution Documents](https://github.com/fonoster/fonoster/blob/main/CONTRIBUTING.md)
 - [Contributors](https://github.com/fonoster/fonoster/contributors)

<!-- readme: contributors -start -->
<table>
<tr>
    <td align="center" style="word-wrap: break-word; width: 150.0; height: 150.0">
        <a href=https://github.com/psanders>
            <img src=https://avatars.githubusercontent.com/u/539774?v=4 width="100;"  style="border-radius:50%;align-items:center;justify-content:center;overflow:hidden;padding-top:10px" alt=Pedro Sanders/>
            <br />
            <sub style="font-size:14px"><b>Pedro Sanders</b></sub>
        </a>
    </td>
    <td align="center" style="word-wrap: break-word; width: 150.0; height: 150.0">
        <a href=https://github.com/efraa>
            <img src=https://avatars.githubusercontent.com/u/40646537?v=4 width="100;"  style="border-radius:50%;align-items:center;justify-content:center;overflow:hidden;padding-top:10px" alt=Efrain Peralta/>
            <br />
            <sub style="font-size:14px"><b>Efrain Peralta</b></sub>
        </a>
    </td>
    <td align="center" style="word-wrap: break-word; width: 150.0; height: 150.0">
        <a href=https://github.com/angelbencosme>
            <img src=https://avatars.githubusercontent.com/u/6846866?v=4 width="100;"  style="border-radius:50%;align-items:center;justify-content:center;overflow:hidden;padding-top:10px" alt=Angel M. Bencosme/>
            <br />
            <sub style="font-size:14px"><b>Angel M. Bencosme</b></sub>
        </a>
    </td>
    <td align="center" style="word-wrap: break-word; width: 150.0; height: 150.0">
        <a href=https://github.com/whernandez>
            <img src=https://avatars.githubusercontent.com/u/37089069?v=4 width="100;"  style="border-radius:50%;align-items:center;justify-content:center;overflow:hidden;padding-top:10px" alt=Wandy Hernandez/>
            <br />
            <sub style="font-size:14px"><b>Wandy Hernandez</b></sub>
        </a>
    </td>
    <td align="center" style="word-wrap: break-word; width: 150.0; height: 150.0">
        <a href=https://github.com/obrucheoghene>
            <img src=https://avatars.githubusercontent.com/u/111436934?v=4 width="100;"  style="border-radius:50%;align-items:center;justify-content:center;overflow:hidden;padding-top:10px" alt=Obruche Wilfred  Oghenechohwo/>
            <br />
            <sub style="font-size:14px"><b>Obruche Wilfred  Oghenechohwo</b></sub>
        </a>
    </td>
    <td align="center" style="word-wrap: break-word; width: 150.0; height: 150.0">
        <a href=https://github.com/wardner>
            <img src=https://avatars.githubusercontent.com/u/51765669?v=4 width="100;"  style="border-radius:50%;align-items:center;justify-content:center;overflow:hidden;padding-top:10px" alt=Wardner Lara/>
            <br />
            <sub style="font-size:14px"><b>Wardner Lara</b></sub>
        </a>
    </td>
</tr>
<tr>
    <td align="center" style="word-wrap: break-word; width: 150.0; height: 150.0">
        <a href=https://github.com/rihernandez>
            <img src=https://avatars.githubusercontent.com/u/27718122?v=4 width="100;"  style="border-radius:50%;align-items:center;justify-content:center;overflow:hi
