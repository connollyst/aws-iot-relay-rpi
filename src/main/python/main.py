#!/usr/bin/python
import json
import sys
import time
from uuid import uuid4

from Logger import get_logger
from aws.AwsIotCore import AwsIotCore
from gpio.Relay import Relay

sys.path.append("..")

AWS_ENDPOINT = 'a12dev37b8fhwi-ats.iot.us-west-2.amazonaws.com'

logger = get_logger(__name__)

relay = Relay(pin=18, initial=Relay.State.OFF, logger=logger)
relay_on_duration = 1
writer = AwsIotCore(AWS_ENDPOINT, logger=logger)
writer.connect("tests-" + str(uuid4()))
writer.write('atlas', json.dumps(relay.to_json(), indent=4, default=str))
relay.on()
time.sleep(relay_on_duration)
relay.off()
writer.write('atlas', json.dumps(relay.to_json(), indent=4, default=str))
writer.disconnect()
