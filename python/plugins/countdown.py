from time import sleep
from strip.ledstrip import LedStrip
from strip.states import WordclockStates

import sys

from rpi_ws281x import *
 
class Countdown():

    def run(self):
        for hour in reversed(WordclockStates.getInstance().getHour()):
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
    countdown.run()
