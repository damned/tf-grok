FROM python:slim

RUN pip install python-hcl2

RUN mkdir -p /work
WORKDIR /work
COPY . .
RUN ls -la *

