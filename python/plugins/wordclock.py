import datetime
from strip.ledstrip import LedStrip
from strip.states import WordclockStates
from neopixel import *

import logging
from time import sleep
import sys

class WordClock:
    logging.basicConfig(filename='wordclock.log', format='%(asctime)s %(message)s')

    def __init__(self, strip, color):
        self.actualLeds = []
        self.strip = strip
        self.color = color
    
    def run(self):
        now = datetime.datetime.now()
        
        logging.info('time was set')

	newLeds = self.__calculateTime(now.minute, now.hour)
        self.__setTime(newLeds)
        
    def __setTime(self, newLeds):    
        if (self.actualLeds != newLeds):
            self.strip.resetLeds()
            self.strip.setLeds(newLeds, self.color)
            self.actualLeds = newLeds

        
    def __calculateTime(self, minute, hour):   
        minute = minute / 5
        hour = hour % 12 + (1 if minute > 4 else 0)

        wordState = WordclockStates.getInstance()
        return wordState.getPrefix() + \
            wordState.getMinute()[minute] + \
            wordState.getHour()[hour] + \
            (wordState.getPostfix() if(minute == 0) else [])
           
if __name__ == "__main__":
    if len(sys.argv) != 5:
        print "invalid number of arguments"
    LedStrip.getInstance().setBrightness(int(sys.argv[4]))
    wordclock = WordClock(LedStrip.getInstance(), Color(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])))
    while(True):
        wordclock.run()
        sleep(30)















