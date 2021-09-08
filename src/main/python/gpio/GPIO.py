try:
    import RPi.GPIO as IO
except ModuleNotFoundError:
    import Mock.GPIO as IO


class GPIO:

    def __init__(self):
        print('hi')

    def set_mode_bcm(self):
        IO.setmode(IO.BCM)

    def setmode(self, mode):
        IO.setmode(mode)

    def set_pin_out(self, pin):
        IO.setup(pin, IO.OUT)

    def setup(self, pin, mode):
        IO.setup(pin, mode)

    def output_high(self, pin):
        IO.output(pin, IO.HIGH)

    def output_low(self, pin):
        IO.output(pin, IO.LOW)