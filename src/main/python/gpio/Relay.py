#!/usr/bin/python
import time
from enum import Enum

from .GPIO import GPIO


class Relay:
    class State(Enum):
        ON = 1
        OFF = 0

    def __init__(self, pin, initial: State, gpio=None):
        self.gpio = gpio or GPIO()
        self.gpio.set_mode_bcm()
        self.gpio.set_pin_out(pin)
        self._pin = pin
        self.state = initial

    @property
    def pin(self):
        return self._pin

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, state: State):
        print('Setting state to {}'.format(state))
        if state == Relay.State.ON:
            self._state = state
            self.gpio.output_high(self.pin)
        elif state == Relay.State.OFF:
            self._state = state
            self.gpio.output_low(self.pin)
        else:
            raise TypeError('Unsupported relay state: {}'.format(state))

    def to_json(self):
        return {
            "address": self.pin,
            "addressType": "GPIO",
            "module": "Relay",
            "version": "0.2",
            "reading": {
                "value": self.state,
                "timestamp": time.time()
            }
        }
