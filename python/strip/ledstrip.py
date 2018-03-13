import ledconfig

from neopixel import *

class LedStrip():
    def setLeds(self, ledList, color):
        for led in ledList:
            self.strip.setPixelColor(led, color)
	    self.strip.show()

    def resetLeds(self):
	for led in range(self.strip.numPixels()):
	    self.strip.setPixelColor(led, 0)
    	self.strip.show()

    def __init__(self):
    	self.strip = Adafruit_NeoPixel(ledconfig.LED_COUNT, ledconfig.LED_PIN, ledconfig.LED_FREQ_HZ, ledconfig.LED_DMA, ledconfig.LED_INVERT, ledconfig.LED_BRIGHTNESS, ledconfig.LED_CHANNEL, ledconfig.LED_STRIP)
        self.strip.begin()


