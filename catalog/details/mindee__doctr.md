# mindee/doctr

docTR (Document Text Recognition) - a seamless, high-performing & accessible library for OCR-related tasks powered by Deep Learning. Ongoing development and maintenance by t2k.

## installation

webpage_doc = DocumentFile.from_url("https://www.yoursite.com")
# Multiple page images
multi_img_doc = DocumentFile.from_images(["path/to/page1.jpg", "path/to/page2.jpg"])
```

### Putting it together

Let's use the default pretrained model for an example:

```python
from doctr.io import DocumentFile
from doctr.models import ocr_predictor

model = ocr_predictor(pretrained=True)
# PDF
doc = DocumentFile.from_pdf("path/to/your/doc.pdf")
# Analyze
result = model(doc)
```

### Detecting the document layout

You can additionally run a layout detection model as part of the pipeline by passing `detect_layout=True`. The detected regions (e.g. `Title`, `Text`, `Table`, `Page-header`, `Page-footer`) are attached to every page and rendered by `.show()`:

```python
from doctr.io import DocumentFile
from doctr.models import ocr_predictor

model = ocr_predictor(pretrained=True, detect_layout=True)
doc = DocumentFile.from_images("path/to/your/doc.jpg")
result = model(doc)

# Access the detected layout regions of the first page
for region in result.pages[0].layout:
    print(region.type, region.confidence, region.geometry)
```

### Dealing with rotated documents

Should you use docTR on documents that include rotated pages, or pages with multiple box orientations,
you have multiple options to handle it:

- If you only use straight document pages with straight words (horizontal, same reading direction),
consider passing `assume_straight_pages=True` to the ocr_predictor. It will directly fit straight boxes
on your page and return straight boxes, which makes it the fastest option.

- If you want the predictor to output straight boxes (no matter the orientation of your pages, the final localizations
will be converted to straight boxes), you need to pass `export_as_straight_boxes=True` in the predictor. Otherwise, if `assume_straight_pages=False`, it will return rotated bounding boxes (potentially with an angle of 0°).

If both options are set to False, the predictor will always fit and return rotated boxes.

To interpret your model's predictions, you can visualize them interactively as follows:

```python
# Display the result (requires matplotlib & mplcursors to be installed)
result.show()
```

![Visualization sample](https://github.com/mindee/doctr/raw/main/docs/images/doctr_example_script.gif)

Or even rebuild the original document from its predictions:

```python
import matplotlib.pyplot as plt

synthetic_pages = result.synthesize()
plt.imshow(synthetic_pages[0])
plt.axis("off")
plt.show()
```

![Synthesis sample](https://github.com/mindee/doctr/raw/main/docs/images/synthesized_sample.png)

The `ocr_predictor` returns a `Document` object with a nested structure (with `Page`, `Block`, `Line`, `Word`, `Artefact`).
To get a better understanding of our document model, check our [documentation](https://mindee.github.io/doctr/modules/io.html#document-structure):

You can also export them as a nested dict, more appropriate for JSON format:

```python
json_output = result.export()
```

### Use the KIE predictor

The KIE predictor is a more flexible predictor compared to OCR as your detection model can detect multiple classes in a document. For example, you can have a detection model to detect just dates and addresses in a document.

The KIE predictor makes it possible to use detector with multiple classes with a recognition model and to have the whole pipeline already setup for you.

```python
from doctr.io import DocumentFile
from doctr.models import kie_predictor

# Model
model = kie_predictor(det_arch="db_resnet50", reco_arch="crnn_vgg16_bn", pretrained=True)
# PDF
doc = DocumentFile.from_pdf("path/to/your/doc.pdf")
# Analyze
result = model(doc)

predictions = result.pages[0].predictions
for class_name in predictions.keys():
    list_predictions = predictions[class_name]
    for prediction in list_predictions:
        print(f"Prediction for {class_name}: {prediction}")
```

The KIE predictor results per page are in a dictionary format with each key

## requirements

Python 3.11 (or higher) and [pip](https://pip.pypa.io/en/stable/) are required to install docTR.

### Latest release

You can then install the latest release of the package using [pypi](https://pypi.org/project/python-doctr/) as follows:

```shell
pip install python-doctr
```

We try to keep extra dependencies to a minimum. You can install specific builds as follows:

```shell
# standard build
pip install python-doctr

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

### Example notebooks

Looking for more illustrations of docTR features? You might want to check the [Jupyter notebooks](https://github.com/mindee/doctr/tree/main/notebooks) designed to give you a broader overview.


## Citation

If you wish to cite this project, feel free to use this [BibTeX](http://www.bibtex.org/) reference:

```bibtex
@misc{doctr2021,
    title={docTR: Document Text Recognition},
    author={Mindee},
    year={2021},
    publisher = {GitHub},
    howpublished = {\url{https://github.com/mindee/doctr}}
}
```

## Custom Development and Support

[t2k GmbH](https://www.text2knowledge.de/de) offers professional services around docTR : whether you are building a product or contributing to the open-source project.

### For organizations

Interested in docTR and want to develop, implement, or ship your own solution? t2k can help with:

- **Custom OCR development** : individual detection, recognition, and pipeline work built on docTR
- **Project implementation** : turning your ideas into production-ready docTR integrations
- **Technical consulting** : architecture, deployment, and integration guidance
- **Ongoing development** : feature extensions and implementation support tailored to your use case
- **Workshops & advisory** : verbal consulting, hands-on sessions, and recommendations for working with docTR

Contact [info@text2knowledge.de](mailto:info@text2knowledge.de) or visit our [home page](https://www.text2knowledge.de) to discuss your project.

## Contributing

If you scrolled down to this section, you most likely appreciate open source. Do you feel like extending the range of our supported characters? Or perhaps submitting a paper implementation? Or contributing in any other way?

You're in luck, we compiled a short guide (cf. [`CONTRIBUTING`](https://mindee.github.io/doctr/contributing/contributing.html)) for you to easily do so!

## License

Distributed under the Apache 2.0 License. See [`LICENSE`](https://github.com/mindee/doctr?tab=Apache-2.0-1-ov-file#readme) for more information.
