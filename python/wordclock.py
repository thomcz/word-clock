import datetime

import strip.states as wordState
from neopixel import *

import logging

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

        return wordState.ES_IST + \
            wordState.MINUTE[minute] + \
            wordState.STUNDE[hour] + \
            (wordState.UHR if(minute == 0) else [])
           

















