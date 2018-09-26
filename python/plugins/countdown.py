from time import sleep

import states
import sys

from neopixel import *
 
class Countdown():

    def run(self):
        for hour in reversed(states.STUNDE):
            self.strip.resetLeds()
            self.strip.setLeds(hour, self.color)
            sleep(1)

    def __init__(self, strip, color):
        self.strip = strip
        self.color = color

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print "invalid number of arguments"
    LedStrip.getInstance().setBrightness(int(sys.argv[4]))
    countdown = Countdown(LedStrip.getInstance(), Color(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])))
    tountdown.run()
