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

- `> docker build -t connollyst/rpi-aws-iot-relay .`
- `> docker push connollyst/rpi-aws-iot-relay`

## Install Docker on Raspberry Pi

- `> sudo apt-get update && sudo apt-get upgrade && sudo reboot`
- `> curl -fsSL https://get.docker.com -o get-docker.sh && sudo sh get-docker.sh`

## Pull the Docker Image

- `> sudo docker pull connollyst/rpi-aws-iot-relay:latest`
- `> sudo docker run --privileged connollyst/rpi-aws-iot-relay`
- `> sudo docker run --device /dev/gpiomem connollyst/rpi-aws-iot-relay`

# Notes

## [Example PWM Code](https://www.waveshare.com/w/upload/8/81/Motor_Driver_HAT_User_Manual_EN.pdf):

```
pwm = PCA9685(0x40, debug=False)
pwm.setPWMFreq(50)
  …
  self.AIN1 = 1
  self.AIN2 = 2
    …
    pwm.setDutycycle(self.PWMA, speed)
      …
      print (“#1 forward”)
      pwm.setLevel(self.AIN1, 0)
      pwm.setLevel(self.AIN2, 1)
      …
    …
    print (“stopping”)
    pwm.setDutycycle(self.PWMA, 0)
  …
Motor = MotorDriver()
print("forward 2 s")
Motor.MotorRun(0, 'forward', 100)
Motor.MotorRun(1, 'forward', 100)
time.sleep(2)
```

## [Using WiringPi](https://www.instructables.com/Controlling-Any-Device-Using-a-Raspberry-Pi-and-a-/):

```
gpio readall
gpio read 0
gpio read 1
gpio mode 1 out
gpio write 1 0
gpio write 1 1
```

```
import RPi.GPIO as GPIO
import time

pin = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)
GPIO.output(pin, GPIO.HIGH)
time.sleep(1)
GPIO.output(pin, GPIO.LOW)
```

## [Options for Docker GPIO](https://blog.alexellis.io/gpio-on-swarm/)

- `> sudo docker run --privileged connollyst/rpi-aws-iot-relay`
- `> sudo docker run --device /dev/gpiomem connollyst/rpi-aws-iot-relay`