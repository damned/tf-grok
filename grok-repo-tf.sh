#!/bin/bash
mkdir -p repos
cd repos
git clone --depth 1 https://github.com/nhsconnect/prm-repo-nems-event-processor.git
cd prm-repo-nems-event-processor/terraform
ls -l *.tf
cp ../../../grok-tf.py .
docker build -f ../../../Dockerfile --tag grok-prm-repo-nems-event-processor .
docker run --rm -it grok-prm-repo-nems-event-processor python grok-tf.py