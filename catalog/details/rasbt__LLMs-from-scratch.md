# rasbt/LLMs-from-scratch

Implement a ChatGPT-like LLM in PyTorch from scratch, step by step

## requirements

The most important prerequisite is a strong foundation in Python programming.
With this knowledge, you will be well prepared to explore the fascinating world of LLMs
and understand the concepts and code examples presented in this book.

If you have some experience with deep neural networks, you may find certain concepts more familiar, as LLMs are built upon these architectures.

This book uses PyTorch to implement the code from scratch without using any external LLM libraries. While proficiency in PyTorch is not a prerequisite, familiarity with PyTorch basics is certainly useful. If you are new to PyTorch, Appendix A provides a concise introduction to PyTorch. Alternatively, you may find my book, [PyTorch in One Hour: From Tensors to Training Neural Networks on Multiple GPUs](https://sebastianraschka.com/teaching/pytorch-1h/), helpful for learning about the essentials.



<br>
&nbsp;

## Hardware Requirements

The code in the main chapters of this book is designed to run on conventional laptops within a reasonable timeframe and does not require specialized hardware. This approach ensures that a wide audience can engage with the material. Additionally, the code automatically utilizes GPUs if they are available. (Please see the [setup](https://github.com/rasbt/LLMs-from-scratch/blob/main/setup/README.md) doc for additional recommendations.)


&nbsp;
## Video Course

[A 17-hour and 15-minute companion video course](https://www.manning.com/livevideo/master-and-build-large-language-models) where I code through each chapter of the book. The course is organized into chapters and sections that mirror the book's structure so that it can be used as a standalone alternative to the book or complementary code-along resource.

<a href="https://www.manning.com/livevideo/master-and-build-large-language-models"><img src="https://sebastianraschka.com/images/LLMs-from-scratch-images/video-screenshot.webp?123" width="350px"></a>


&nbsp;


## Companion Book / Sequel

[*Build A Reasoning Model (From Scratch)*](https://mng.bz/lZ5B), while a standalone book, can be considered as a sequel to *Build A Large Language Model (From Scratch)*.

It starts with a pretrained model and implements different reasoning approaches, including inference-time scaling, reinforcement learning, and distillation, to improve the model's reasoning capabilities.

Similar to *Build A Large Language Model (From Scratch)*, [*Build A Reasoning Model (From Scratch)*](https://mng.bz/lZ5B) takes a hands-on approach implementing these methods from scratch.

<a href="https://mng.bz/lZ5B"><img src="https://sebastianraschka.com/images/reasoning-from-scratch-images/cover.webp?123" width="120px"></a>

- Amazon link (TBD)
- [Manning link](https://mng.bz/lZ5B)
- [GitHub repository](https://github.com/rasbt/reasoning-from-scratch)

<br>

&nbsp;
## Exercises

Each chapter of the book includes several exercises. The solutions are summarized in Appendix C, and the corresponding code notebooks are available in the main chapter folders of this repository (for example,  [./ch02/01_main-chapter-code/exercise-solutions.ipynb](./ch02/01_main-chapter-code/exercise-solutions.ipynb).

In addition to the code exercises, you can download a free 170-page PDF titled  [Test Yourself On Build a Large Language Model (From Scratch)](https://www.manning.com/books/test-yourself-on-build-a-large-language-model-from-scratch) from the Manning website. It contains approximately 30 quiz questions and solutions per chapter to help you test your understanding.

<a href="https://www.manning.com/books/test-yourself-on-build-a-large-language-model-from-scratch"><img src="https://sebastianraschka.com/images/LLMs-from-scratch-images/test-yourself-cover.jpg?123" width="150px"></a>

&nbsp;
## Bonus Material

Several folders contain optional materials as a bonus for interested readers:
- **Setup**
  - [Python Setup Tips](setup/01_optional-python-setup-preferences)
  - [Installing Python Packages and Libraries Used in This Boo
