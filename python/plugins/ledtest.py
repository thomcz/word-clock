from time import sleep

import strip.states as states

from neopixel import *

class LedTest():

    def run(self):
       for led in range(110):
            self.strip.resetLeds()
            self.strip.setLed(led, self.color)
            sleep(0.5)

    def __init__(self, color, strip):
        self.strip = strip
        self.color = color

