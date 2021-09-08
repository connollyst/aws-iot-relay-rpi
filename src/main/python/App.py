import json
import time
from uuid import uuid4

from Logger import get_logger
from aws.AwsIotCore import AwsIotCore
from gpio.Relay import Relay


class App:
    LOGGER = get_logger(__name__)

    AWS_ENDPOINT = 'a12dev37b8fhwi-ats.iot.us-west-2.amazonaws.com'
    AWS_IOT_MQTT_TOPIC = 'iot/devices/readings'
    AWS_CLIENT_ID = "iot-relay-" + str(uuid4())
    RELAY_DURATION = 30

    def run(self):
        relay = Relay(pin=18, initial=Relay.State.OFF, logger=self.LOGGER)
        writer = AwsIotCore(self.AWS_ENDPOINT, logger=self.LOGGER)
        writer.connect(self.AWS_CLIENT_ID)
        writer.write(self.AWS_IOT_MQTT_TOPIC, json.dumps(relay.to_json(), indent=4, default=str))
        relay.on()
        time.sleep(self.RELAY_DURATION)
        relay.off()
        writer.write(self.AWS_IOT_MQTT_TOPIC, json.dumps(relay.to_json(), indent=4, default=str))
        writer.disconnect()
