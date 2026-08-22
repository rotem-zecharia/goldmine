# alibaba/MNN

MNN: A blazing-fast, lightweight inference engine battle-tested by Alibaba, powering high-performance on-device LLMs and Edge AI.

## tools

Base on MNN (Tensor compute engine), we provided a series of tools for inference, train and general computation.

- MNN-Converter: Convert other models to MNN models for inference, such as Tensorflow(lite), Caffe, ONNX, Torchscripts. And do graph optimization to reduce computation.
- MNN-Compress: Compress model to reduce size and increase performance / speed
- MNN-Express: Support model with controlflow, use MNN's OP to do general-purpose computing.
- MNN-CV: An OpenCV-like library, but based on MNN and then much more lightweight.
- MNN-Train: Support train MNN model.
