import ledconfig

from neopixel import *

class LedStrip():
    __instance = None

    @staticmethod
    def getInstance():
        if LedStrip.__instance == None:
            LedStrip()
        return LedStrip.__instance
    
    def setBrightness(self, brightness):
        self.strip.setBrightness(brightness)
        self.strip.show()
    
    def setLeds(self, ledList, color):
        for led in ledList:
            self.strip.setPixelColor(led, color)
	self.strip.show()

    def setLed(self, led, color):
        self.strip.setPixelColor(led, color)

    def resetLeds(self):
	for led in range(self.strip.numPixels()):
	    self.strip.setPixelColor(led, 0)
    	self.strip.show()

    def __init__(self):

        if LedStrip.__instance != None:
            raise Exception("this class is singelton")
        else:
            self.strip = Adafruit_NeoPixel(ledconfig.LED_COUNT, ledconfig.LED_PIN, ledconfig.LED_FREQ_HZ, ledconfig.LED_DMA, ledconfig.LED_INVERT, ledconfig.LED_BRIGHTNESS, ledconfig.LED_CHANNEL, ledconfig.LED_STRIP)
            self.strip.begin()
            
            LedStrip.__instance = self

