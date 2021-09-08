#!/usr/bin/python
import json
import time
from uuid import uuid4

from aws.AwsIotCore import AwsIotCore
from gpio.Relay import Relay

AWS_ENDPOINT = 'a12dev37b8fhwi-ats.iot.us-west-2.amazonaws.com'

relay = Relay(pin=18, initial=Relay.State.OFF)
relay_on_duration = 3
writer = AwsIotCore(AWS_ENDPOINT)
writer.connect("tests-" + str(uuid4()))
writer.write('atlas', json.dumps(relay.to_json(), indent=4, default=str))
relay.on()
time.sleep(relay_on_duration)
relay.off()
writer.write('atlas', json.dumps(relay.to_json(), indent=4, default=str))
writer.disconnect()
