import time
from LEDConfiguration import LEDConfiguration
from WordClockStates import WordClockStates

from neopixel import *
 
class Countdown():
	def _setClock(self, ledList):
		for led in ledList:
                	self.strip.setPixelColor(led, self.color)
	        self.strip.show()

	def _resetLeds(self):
		for led in range(self.strip.numPixels()):
			self.strip.setPixelColor(led, 0)
		self.strip.show()

	def _countdown(self):
		wordState = WordClockStates()
                for hour in reversed(wordState.STUNDE):
                        self._resetLeds()
                        self._setClock(hour)
                        time.sleep(1)

	def start(self):
		self._countdown()

	def __init__(self, color):
		self.color = color
		ledConfig = LEDConfiguration()
		self.strip = Adafruit_NeoPixel(ledConfig.LED_COUNT, ledConfig.LED_PIN, ledConfig.LED_FREQ_HZ, ledConfig.LED_DMA, ledConfig.LED_INVERT, ledConfig.LED_BRIGHTNESS, ledConfig.LED_CHANNEL, ledConfig.LED_STRIP)
                self.strip.begin()

if __name__ == '__main__':
        Countdown(Color(255,255,255)).start()


