# AWS IoT: Raspberry Pi Relay

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

# Docker

## Install Docker on Raspberry Pi

- `> sudo apt-get update && sudo apt-get upgrade && sudo reboot`
- `> curl -sSL https://get.docker.com | sh`
- `> sudo groupadd docker`
- `> sudo usermod -aG docker ${USER}`

## Build & Push the Docker Image

- `> docker build -t connollyst/rpi-aws-iot-relay . && docker run connollyst/rpi-aws-iot-relay`
- `> docker build -t connollyst/rpi-aws-iot-relay . && docker push connollyst/rpi-aws-iot-relay`

- `> docker build -t connollyst/rpi-aws-iot-relay:latest -t connollyst/rpi-aws-iot-relay:vX.Y.Z .`
- `> docker push connollyst/rpi-aws-iot-relay:latest && docker push connollyst/rpi-aws-iot-relay:vX.Y.Z`

## Pull the Docker Image

- `> docker pull connollyst/rpi-aws-iot-relay:latest`
- `> docker run --restart=on-failure --privileged connollyst/rpi-aws-iot-relay:vX.Y.Z &`
- `> docker run --device /dev/gpiomem connollyst/rpi-aws-iot-relay`

# Notes

## [Example PCA9685 Code](https://www.waveshare.com/w/upload/8/81/Motor_Driver_HAT_User_Manual_EN.pdf):

## [Using WiringPi](https://www.instructables.com/Controlling-Any-Device-Using-a-Raspberry-Pi-and-a-/):

```
gpio readall
gpio read 0
gpio read 1
gpio mode 1 out
gpio write 1 0
gpio write 1 1
```

## [Options for Docker GPIO](https://blog.alexellis.io/gpio-on-swarm/)

- `> sudo docker run --privileged connollyst/rpi-aws-iot-relay`
- `> sudo docker run --device /dev/gpiomem connollyst/rpi-aws-iot-relay`