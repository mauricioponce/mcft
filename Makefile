# Names to identify images of this app
IMAGE_NAME='continuumio/anaconda3'
CONTAINER_NAME='my_anaconda'
CURRENT_DIR=$(shell pwd)

up:
	docker run -v ${CURRENT_DIR}:/mlt -it ${CONTAINER_NAME}

