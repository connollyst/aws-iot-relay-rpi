# External module imports


# on = 10
# relayPin = 18
# GPIO.setmode(GPIO.BCM)
# GPIO.setup(relayPin, GPIO.OUT)
# GPIO.output(relayPin, GPIO.HIGH)
# time.sleep(on)
# GPIO.output(relayPin, GPIO.LOW)

from uuid import uuid4

from AwsIotCore import AwsIotCore

AWS_ENDPOINT = 'a12dev37b8fhwi-ats.iot.us-west-2.amazonaws.com'

writer = AwsIotCore(AWS_ENDPOINT)
writer.connect("tests-" + str(uuid4()))
writer.write('{"message":"Hello from Docker!"}')
writer.disconnect()
