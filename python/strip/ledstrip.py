from ledconfig import LEDConfiguration

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
    	ledConfig = LEDConfiguration()
	self.strip = Adafruit_NeoPixel(ledConfig.LED_COUNT, ledConfig.LED_PIN, ledConfig.LED_FREQ_HZ, ledConfig.LED_DMA, ledConfig.LED_INVERT, ledConfig.LED_BRIGHTNESS, ledConfig.LED_CHANNEL, ledConfig.LED_STRIP)
        self.strip.begin()


