import json
import time
from uuid import uuid4

from aws.AwsIotCore import AwsIotCore
from gpio.Relay import Relay

AWS_ENDPOINT = 'a12dev37b8fhwi-ats.iot.us-west-2.amazonaws.com'

relay = Relay()
relay_on_duration = 30
writer = AwsIotCore(AWS_ENDPOINT)
writer.connect("tests-" + str(uuid4()))

message = {
    "address": relay.pin,
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

relay.turn_on()
time.sleep(relay_on_duration)
relay.turn_off()

message['reading'] = {
    "value": "OFF",
    "timestamp": time.time()
}
writer.write('atlas', json.dumps(message, indent=4, default=str))

writer.disconnect()
