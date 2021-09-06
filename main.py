import json
import time
from uuid import uuid4

import RPi.GPIO as GPIO

from AwsIotCore import AwsIotCore

AWS_ENDPOINT = 'a12dev37b8fhwi-ats.iot.us-west-2.amazonaws.com'

on = 10
relayPin = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(relayPin, GPIO.OUT)

writer = AwsIotCore(AWS_ENDPOINT)
writer.connect("tests-" + str(uuid4()))

message = {
    "address": relayPin,
    "addressType": "GPIO",
    "name": "",
    "module": "Relay",
    "version": "0.1",
    "reading": {}
}
message['reading'] = {
    "value": "ON",
    "timestamp": time.time()
}
writer.write('atlas', json.dumps(message, indent=4, default=str))
GPIO.output(relayPin, GPIO.HIGH)
time.sleep(on)
GPIO.output(relayPin, GPIO.LOW)
message['reading'] = {
    "value": "OFF",
    "timestamp": time.time()
}
writer.write('atlas', json.dumps(message, indent=4, default=str))

writer.disconnect()
