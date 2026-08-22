# iOfficeAI/OfficeCLI

OfficeCLI is the first and best Office suite purpose-built for AI agents to read, edit, and automate Word, Excel, and PowerPoint files. Free, open-source, single binary, no Office installation require

## installation

curl -fsSL https://raw.githubusercontent.com/iOfficeAI/OfficeCLI/main/install.sh | bash

## features

What used to take 50 lines of Python and 3 separate libraries:

```python
from pptx import Presentation
from pptx.util import Inches, Pt
prs = Presentation()
slide = prs.slides.add_slide(prs.slide_layouts[0])
title = slide.shapes.title
title.text = "Q4 Report"

## tools

officecli batch deck.pptx --commands '[{"op":"set","path":"/slide[1]/shape[1]","props":{"text":"Hi"}}]'
