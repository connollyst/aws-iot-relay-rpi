# aws-iot-relay-rpi

AWS IoT connected relay automation for Raspberry Pi

## Installation

### Install the OS:

- Open Raspberry Pi Imager
- Select OS Lite & burn
- Eject & reinsert SD card
- Write empty file called `ssh` to the root of the `boot` partition.
- Write a text file called `wpa_supplicant.conf` with:

```
country=US
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
network={
  ssid="YOUR_NETWORK_NAME"
  psk="YOUR_PASSWORD"
  key_mgmt=WPA-PSK
}
```

### Set up the relay

...

### Set up AWS IoT:

https://docs.aws.amazon.com/iot/latest/developerguide/interactive-demo.html
https://docs.aws.amazon.com/iot/latest/developerguide/connecting-to-existing-device.html

- `> sudo apt-get update`
- `> sudo apt-get upgrade`
- `> sudo apt-get install cmake`
- `> sudo apt-get install libssl-dev`
- `> sudo apt-get install git`
- `> sudo apt install python3`
- `> sudo apt install python3-pip`
- `> python3 -m pip install awsiotsdk`
- `> git clone https://github.com/aws/aws-iot-device-sdk-python-v2.git`
- `> mkdir certs`
  ```
  % scp *.key pi@192.168.1.192:~/certs
  % scp *.pem pi@192.168.1.192:~/certs
  % scp *.crt pi@192.168.1.192:~/certs
  ```
- `> python3 pubsub.py --topic topic_1 --root-ca ~/certs/Amazon-root-CA-1.pem --cert ~/certs/device.pem.crt --key ~/certs/private.pem.key --endpoint a12dev37b8fhwi-ats.iot.us-west-2.amazonaws.com`

https://docs.aws.amazon.com/iot/latest/developerguide/iot-moisture-raspi-setup.html

# Docker

## Build & Push the Docker Image

- `> docker build -t connollyst/iot .`
- `> docker run connollyst/iot`
- `> docker push connollyst/iot`

## Install & Pull the Docker Image on Raspberry Pi

- `> sudo apt-get update`
- `> sudo apt-get upgrade`
- `> curl -fsSL https://get.docker.com -o get-docker.sh`
- `> sudo sh get-docker.sh`
- `> sudo docker login`
- `> sudo docker pull connollyst/iot:latest`
- `> sudo docker run connollyst/iot`