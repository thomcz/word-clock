import datetime

from WordClockStates import WordClockStates
from ledstrip import LedStrip

from neopixel import *


class WordClock:
    def run(self):
    	wordState = WordClockStates()
    	now = datetime.datetime.now()
	print(now)
        minute = now.minute
    	hour = now.hour

	leds = []
	self.strip.resetLeds()
        if (minute < 5):
            leds = wordState.ES_IST + wordState.STUNDE[hour%12] + wordState.UHR
	elif (minute < 10):
            leds =  wordState.ES_IST + wordState.FUENF_NACH + wordState.STUNDE[hour%12]
        elif (minute < 15):
            leds =  wordState.ES_IST + wordState.ZEHN_NACH + wordState.STUNDE[hour%12]
	elif (minute < 20):
    	    leds = wordState.ES_IST + wordState.VIERTEL_NACH + wordState.STUNDE[hour%12]
      	elif (minute < 25):
            leds = wordState.ES_IST + wordState.ZWANZIG_NACH + wordState.STUNDE[hour%12]
	elif (minute < 30):
    	    leds = wordState.ES_IST + wordState.FUENF_VOR_HALB + wordState.STUNDE[hour%12]
    	elif (minute < 35):
            leds = wordState.ES_IST + wordState.HALB + wordState.STUNDE[(hour+1)%12]
        elif (minute < 40):
    	    leds = wordState.ES_IST + wordState.FUENF_NACH_HALB + wordState.STUNDE[(hour+1)%12]
        elif (minute < 45):
            leds = wordState.ES_IST + wordState.ZWANZIG_VOR + wordState.STUNDE[(hour+1)%12]
        elif (minute < 50):
            leds = wordState.ES_IST + wordState.VIERTEL_VOR + wordState.STUNDE[(hour+1)%12]
        elif (minute < 55):
            leds = wordState.ES_IST + wordState.ZEHN_VOR + wordState.STUNDE[(hour+1)%12]
        elif (minute < 60):
            leds = wordState.ES_IST + wordState.FUENF_VOR + wordState.STUNDE[(hour+1)%12]

        self.strip.setLeds(leds, self.color)
	    

    def __init__(self, color):
        self.strip = LedStrip()
        self.color = color

if __name__ == '__main__':
    WordClock(Color(255,255,255)).start()
