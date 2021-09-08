#!/usr/bin/python


import time
from enum import Enum

from .GPIO import GPIO


class Relay:
    class State(Enum):
        ON = 1
        OFF = 0

    def __init__(self, pin, initial: State, gpio=None, logger=None):
        self._logger = logger
        self._gpio = gpio or GPIO()
        self._gpio.set_mode_bcm()
        self._gpio.set_pin_out(pin)
        self._pin = pin
        self._state = None
        self.state = initial

    @property
    def pin(self):
        return self._pin

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, state: State):
        if not hasattr(self, '_state'):
            self._state = None
        self._logger.info('Setting state to {}'.format(state))
        if state == Relay.State.ON:
            if self._state != Relay.State.ON:
                self._state = state
                self._gpio.output_high(self.pin)
        elif state == Relay.State.OFF:
            if self._state != Relay.State.OFF:
                self._state = state
                self._gpio.output_low(self.pin)
        else:
            raise TypeError('Unsupported relay state: {} (current={})'.format(state, self._state))

    def on(self):
        self.state = Relay.State.ON

    def off(self):
        self.state = Relay.State.OFF

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
