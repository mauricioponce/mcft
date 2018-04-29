FROM continuumio/anaconda

COPY notebooks /opt/notebooks
COPY docker/conf/requirements.txt /tmp

RUN /opt/conda/bin/conda install jupyter -y --quiet

#install ta-lib using https://mrjbq7.github.io/ta-lib/install.html
COPY docker/lib/ta-lib-0.4.0-src.tar.gz /tmp

RUN apt-get install -y build-essential && \
    cd /tmp && \
    tar xfz ta-lib-0.4.0-src.tar.gz && \
    cd ta-lib && \
    ./configure --prefix=/usr && \
    make && \
    make install && \
    cd /tmp && \
    rm -rf ta-lib*

RUN apt-get upgrade -y && \
	apt-get update -y && \
	pip install -r /tmp/requirements.txt && \
    apt-get clean && \
    apt-get autoremove

WORKDIR /opt/notebooks

CMD /opt/conda/bin/jupyter notebook --notebook-dir=/opt/notebooks --ip='*' --port=8888 --no-browser --allow-root --NotebookApp.iopub_data_rate_limit=10000000000
