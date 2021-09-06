# External module imports
import time

import RPi.GPIO as GPIO

on = 10
# off = 30

relayPin = 18  # Broadcom pin 23 (P1 pin 16)

GPIO.setmode(GPIO.BCM)  # Broadcom pin-numbering scheme
GPIO.setup(relayPin, GPIO.OUT)  # LED pin set as output

GPIO.output(relayPin, GPIO.HIGH)
time.sleep(on)
GPIO.output(relayPin, GPIO.LOW)
# time.sleep(off)
