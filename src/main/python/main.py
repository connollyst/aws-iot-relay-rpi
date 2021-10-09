#!/usr/bin/python
from App import App

SECONDS = 1
MINUTES = 60 * SECONDS
HOURS = 60 * MINUTES

if __name__ == '__main__':
    pin = 18
    duration = 30 * SECONDS
    frequency = 5 * MINUTES
    App(pin, duration, frequency).start()
