from wordclock import WordClock
from strip.ledstrip import LedStrip
from time import sleep

from neopixel import *

if __name__ == "__main__":
    wordclock = WordClock(LedStrip(), Color(255, 255, 255))
    while(True):
        wordclock.run()
        sleep(30)
