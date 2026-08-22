# mindee/doctr

docTR (Document Text Recognition) - a seamless, high-performing & accessible library for OCR-related tasks powered by Deep Learning. Ongoing development and maintenance by t2k.

## installation

webpage_doc = DocumentFile.from_url("https://www.yoursite.com")

## requirements

Python 3.11 (or higher) and [pip](https://pip.pypa.io/en/stable/) are required to install docTR.

## tools

Looking to integrate docTR into your API? Here is a template to get you started with a fully working API using the wonderful [FastAPI](https://github.com/tiangolo/fastapi) framework.

#### Deploy your API locally

Specific dependencies are required to run the API template, which you can install as follows:

```shell
cd api/
pip install poetry
make lock
pip install -r requirements.txt
```

You can now run your API locally:

```shell
uvicorn --reload --workers 1 --host 0.0.0.0 --port=8002 --app-dir api/ app.main:app
```

Alternatively, you can run the same server on a docker container if you prefer using:

```shell
PORT=8002 docker-compose up -d --build
```

#### What you have deployed

Your API should now be running locally on your port 8002. Access your automatically-built documentation at [http://localhost:8002/redoc](http://localhost:8002/redoc) and enjoy your three functional routes ("/detection", "/recognition", "/ocr", "/kie"). Here is an example with Python to send a request to the OCR route:

```python
import requests

params = {"det_arch": "db_resnet50", "reco_arch": "crnn_vgg16_bn"}

with open("/path/to/your/doc.jpg", "rb") as f:
    files = [  # application/pdf, image/jpeg, image/png supported
        ("files", ("doc.jpg", f.read(), "image/jpeg")),
    ]
print(requests.post("http://localhost:8080/ocr", params=params, files=files).json())
```
