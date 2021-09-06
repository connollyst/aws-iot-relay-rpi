FROM balenalib/raspberry-pi-debian-python:latest

MAINTAINER Sean Connolly <connolly.st@gmail.com>

RUN apt-get update && \
    apt-get install -y \
    build-essential \
    gcc \
    --no-install-recommends && \
    rm -rf /var/lib/apt/lists/*
RUN pip install wheel
COPY requirements.txt /
RUN pip install -r requirements.txt

COPY main.py /
CMD [ "python", "./main.py" ]