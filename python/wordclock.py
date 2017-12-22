import time 
import datetime

from LEDConfiguration import LEDConfiguration
from WordClockStates import WordClockStates

from neopixel import *

color = Color(255, 255, 255)

def _setClock(strip, color, ledList):
        for led in ledList:
                strip.setPixelColor(led, color)
        strip.show()

def _resetLeds(strip):
	for led in range(strip.numPixels()):
		strip.setPixelColor(led, 0)
	strip.show()

def _timeLoop(strip, wordState):
	while True:
  	       	now = datetime.datetime.now()
               	print(now)
               	minute = now.minute
               	hour = now.hour

               	leds = []
		_resetLeds(strip)
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

                _setClock(strip, color, leds)
                time.sleep(30)

def _initLed():
	# Create NeoPixel object with appropriate configuration.
        ledConfig = LEDConfiguration()
        strip = Adafruit_NeoPixel(ledConfig.LED_COUNT, ledConfig.LED_PIN, ledConfig.LED_FREQ_HZ, ledConfig.LED_DMA, ledConfig.LED_INVERT, ledConfig.LED_BRIGHTNESS, ledConfig.LED_CHANNEL, ledConfig.LED_STRIP)
        # Intialize the library (must be called once before other functions).
        strip.begin()
	return strip

def _main():
	strip =	_initLed()
        wordState = WordClockStates()

        try:
                _timeLoop(strip, wordState)
        finally:
                _resetLeds(strip)

if __name__ == '__main__':
        _main()
