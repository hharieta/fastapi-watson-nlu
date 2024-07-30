#!/usr/bin/env bash

docker build -t ibm-nlu .
docker run --rm -it -p 8000:8000 --name emotion ibm-nlu