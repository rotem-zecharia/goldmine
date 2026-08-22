# HumanSignal/label-studio

Label Studio is a multi-type data labeling and annotation tool with standardized output format

## installation

Official Label Studio docker image is [here](https://hub.docker.com/r/heartexlabs/label-studio) and it can be downloaded with `docker pull`. 
Run Label Studio in a Docker container and access it at `http://localhost:8080`.


```bash
docker pull heartexlabs/label-studio:latest
docker run -it -p 8080:8080 -v $(pwd)/mydata:/label-studio/data heartexlabs/label-studio:latest
```
You can find all the generated assets, including SQLite3 database storage `label_studio.sqlite3` and uploaded files, in the `./mydata` directory.

#### Override default Docker install
You can override the default launch command by appending the new arguments:
```bash
docker run -it -p 8080:8080 -v $(pwd)/mydata:/label-studio/data heartexlabs/label-studio:latest label-studio --log-level DEBUG
```

#### Build a local image with Docker
If you want to build a local image, run:
```bash
docker build -t heartexlabs/label-studio:latest .
```

## configuration

poetry new my-label-studio
cd my-label-studio
poetry add label-studio

## tools

You can use Label Studio as an independent part of your machine learning workflow or integrate the frontend or backend into your existing tools.
