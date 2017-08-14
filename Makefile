# Names to identify images of this app
IMAGE_NAME='continuumio/anaconda3'
CURRENT_DIR=$(shell pwd)

up:
	docker run -d -v ${CURRENT_DIR}:/opt/ -t ${IMAGE_NAME} /bin/bash

