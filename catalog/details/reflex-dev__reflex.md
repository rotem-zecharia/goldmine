# reflex-dev/reflex

🕸️ Web apps in pure Python 🐍

## installation

**Important:** We strongly recommend using a virtual environment to ensure the `reflex` command is available in your PATH.

## 🥳 Create your first app

Create a project, add Reflex, and start the development server with [uv](https://docs.astral.sh/uv/):

```shell
mkdir my_app_name
cd my_app_name
uv init

uv add reflex
uv run reflex init
uv run reflex run
```

You should see your app running at http://localhost:3000.

Now you can modify the source code in `my_app_name/my_app_name.py`. Reflex has fast refreshes so you can see your changes instantly when you save your code.

## 🫧 Example App

Build an image generation app in Python with Reflex: define the UI, manage state in a class, and call an image model from an event handler.

<div align="center">
<video src="https://github.com/user-attachments/assets/aaff28ad-8b3c-43bf-967e-439ee34c8a87" width="900" controls muted poster="https://raw.githubusercontent.com/reflex-dev/reflex/main/docs/images/reflex-image-generation-app.png">
  <a href="https://web.reflex-assets.dev/video/reflex-dalle-video-2x.mp4">
    <img src="https://raw.githubusercontent.com/reflex-dev/reflex/main/docs/images/reflex-image-generation-app.png" alt="Preview of an image generation app built with Reflex" width="900">
  </a>
</video>
</div>

```python
import reflex as rx
import openai

client = openai.AsyncOpenAI()


class State(rx.State):
    prompt: str = ""
    image_url: str = ""
    processing: bool = False

    @rx.event
    def set_prompt(self, value: str):
        self.prompt = value

    @rx.event
    async def generate(self):
        self.processing = True
        yield
        response = await client.images.generate(
            model="gpt-image-1.5",
            prompt=self.prompt,
        )
        self.image_url = f"data:image/png;base64,{response.data[0].b64_json}"
        self.processing = False


def index():
    return rx.vstack(
        rx.heading("Image Generator"),
        rx.input(placeholder="Enter a prompt...", on_change=State.set_prompt),
        rx.button("Generate", on_click=State.generate, loading=State.processing),
        rx.image(src=State.image_url),
    )


app = rx.App()
app.add_page(index, title="Reflex:Image Generation")
```

## All Thanks To Our Contributors:

<a href="https://github.com/reflex-dev/reflex/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=reflex-dev/reflex" />
</a>
