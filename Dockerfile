FROM balenalib/raspberry-pi-debian:latest

MAINTAINER Sean Connolly <connolly.st@gmail.com>

RUN sudo apt-get update && \
    sudo apt-get install -y \
    cmake \
    python3-dev \
    python3-pip \
    --no-install-recommends && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt /
RUN python3 -m pip install -r requirements.txt

COPY main.py /
COPY AwsIotCore.py /
COPY certs/ /certs/
CMD [ "python3", "./main.py" ]