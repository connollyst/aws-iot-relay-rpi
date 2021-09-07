import RPi.GPIO as GPIO

class Relay:

    def __init__(self):
        self._pin = 18
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self._pin, GPIO.OUT)

    @property
    def pin(self):
        return self._pin

    def turn_on(self):
        GPIO.output(self._pin, GPIO.HIGH)

    def turn_off(self):
        GPIO.output(self._pin, GPIO.LOW)