from wordclock import WordClock
from plugins.countdown import Countdown
from plugins.gameoflife import GameOfLife

from strip.ledstrip import LedStrip
from time import sleep

from neopixel import *

if __name__ == "__main__":
    print('started')
#    GameOfLife(LedStrip()).run()
#    Countdown(Color(200, 43, 157), LedStrip()).run()
     wordclock = WordClock(LedStrip(), Color(255, 255, 255))
     while(True):
         wordclock.run()
         sleep(30)
