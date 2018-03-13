from time import sleep

import strip.states as states

from neopixel import *
 
class Countdown():

    def run(self):
       for hour in reversed(states.STUNDE):
            self.strip.resetLeds()
            self.strip.setLeds(hour, self.color)
            sleep(1)

    def __init__(self, color, strip):
        self.strip = srip
        self.color = color


