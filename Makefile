# Names to identify images of this app
CURRENT_DIR=$(shell pwd)

up:
	docker run -v ${CURRENT_DIR}:/opt/notebooks -it -p 8888:8888 continuumio/anaconda3 /bin/bash -c "/opt/conda/bin/conda install jupyter -y --quiet  && /opt/conda/bin/jupyter notebook --notebook-dir=/opt/notebooks --ip='*' --port=8888 --no-browser --allow-root"
