from strip.ledstrip import LedStrip
from figures.mario import Mario
from figures.heart import Heart
from figures.melon import Melon
from neopixel import *
import strip.ledposition as ledPosition
import sys

class Figures:
    figures = {"mario": Mario().getFigure(),
                "heart": Heart().getFigure(),
		"melon": Melon().getFigure()}
 
    def __init__(self, strip, figure):
        self.actualLeds = []
        self.strip = strip
        self.figure = figure

    def run(self):
        self.draw(self.figures[self.figure])

    def draw(self, figure):
        for item in figure:
            color = item[1]
            leds = list(map(lambda (x, y): ledPosition.ledPosition[(x, y)], item[0]))
            print leds
            print color
            self.strip.setLeds(leds, color)

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print "invalid number of arguments"
    LedStrip.getInstance().setBrightness(int(sys.argv[2]))
    figures = Figures(LedStrip.getInstance(), sys.argv[1])
    figures.run()
