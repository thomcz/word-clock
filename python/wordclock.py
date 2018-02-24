import time 
import datetime

from LEDConfiguration import LEDConfiguration
from WordClockStates import WordClockStates

from neopixel import *


class WordClock:
	def _setClock(self, ledList):
		for led in ledList:
                	self.strip.setPixelColor(led, self.color)
	        self.strip.show()

	def _resetLeds(self):
		for led in range(self.strip.numPixels()):
			self.strip.setPixelColor(led, 0)
		self.strip.show()

	def _timeLoop(self):
		wordState = WordClockStates()
		while True:
  	       		now = datetime.datetime.now()
	               	print(now)
        	       	minute = now.minute
               		hour = now.hour

	               	leds = []
			self._resetLeds()
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

                	self._setClock(leds)
	                time.sleep(30)

	def _initLed():
		# Create NeoPixel object with appropriate configuration.
	        ledConfig = LEDConfiguration()
        	strip = Adafruit_NeoPixel(ledConfig.LED_COUNT, ledConfig.LED_PIN, ledConfig.LED_FREQ_HZ, ledConfig.LED_DMA, ledConfig.LED_INVERT, ledConfig.LED_BRIGHTNESS, ledConfig.LED_CHANNEL, ledConfig.LED_STRIP)
	        # Intialize the library (must be called once before other functions).
        	strip.begin()
		return strip

	def start(self):
		self.strip.begin()
		self._timeLoop()

	def __init__(self, color):
		self.color = color
		ledConfig = LEDConfiguration()
		self.strip = Adafruit_NeoPixel(ledConfig.LED_COUNT, ledConfig.LED_PIN, ledConfig.LED_FREQ_HZ, ledConfig.LED_DMA, ledConfig.LED_INVERT, ledConfig.LED_BRIGHTNESS, ledConfig.LED_CHANNEL, ledConfig.LED_STRIP)
