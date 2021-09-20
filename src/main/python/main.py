#!/usr/bin/python
from App import App

SECONDS = 1
MINUTES = 60 * SECONDS
HOURS = 60 * MINUTES

if __name__ == '__main__':
    pin = 18
    frequency = 2 * MINUTES
    duration = 30 * SECONDS
    App(pin, frequency, duration).start()
