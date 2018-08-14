import datetime

import strip.states as wordState
from neopixel import *


class WordClock:

    def __init__(self, strip, color):
        self.actualLeds = []
        self.strip = strip
        self.color = color
    
    def run(self):
        now = datetime.datetime.now()
	print(now)

        minute = now.minute
    	hour = now.hour
	newLeds = self.__calculateTime(minute, hour)
        self.__setTime(newLeds)
        
    def __setTime(self, newLeds):    
        if (self.actualLeds != newLeds):
            self.strip.resetLeds()
            self.strip.setLeds(newLeds, self.color)
            self.actualLeds = newLeds

        
    def __calculateTime(self, minute, hour):   
        hour = hour % 12
        if (hour > 0  and minute < 30):
            hour = hour - 1
        
        if (minute < 5):
            return wordState.ES_IST + wordState.STUNDE[hour] + wordState.UHR
	elif (minute < 10):
            return wordState.ES_IST + wordState.FUENF_NACH + wordState.STUNDE[hour]
        elif (minute < 15):
            return  wordState.ES_IST + wordState.ZEHN_NACH + wordState.STUNDE[hour]
	elif (minute < 20):
    	    return wordState.ES_IST + wordState.VIERTEL_NACH + wordState.STUNDE[hour]
      	elif (minute < 25):
            return wordState.ES_IST + wordState.ZWANZIG_NACH + wordState.STUNDE[hour]
	elif (minute < 30):
    	    return wordState.ES_IST + wordState.FUENF_VOR_HALB + wordState.STUNDE[hour]
    	elif (minute < 35):
            return wordState.ES_IST + wordState.HALB + wordState.STUNDE[hour]
        elif (minute < 40):
    	    return wordState.ES_IST + wordState.FUENF_NACH_HALB + wordState.STUNDE[hour]
        elif (minute < 45):
            return wordState.ES_IST + wordState.ZWANZIG_VOR + wordState.STUNDE[hour]
        elif (minute < 50):
            return wordState.ES_IST + wordState.VIERTEL_VOR + wordState.STUNDE[hour]
        elif (minute < 55):
            return wordState.ES_IST + wordState.ZEHN_VOR + wordState.STUNDE[hour]
        elif (minute < 60):
            return wordState.ES_IST + wordState.FUENF_VOR + wordState.STUNDE[hour]







