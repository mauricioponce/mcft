FROM continuumio/anaconda3

ADD . /mlt

WORKDIR /mlt

RUN pip install -r requirements.txt

ENTRYPOINT /bin/bash

