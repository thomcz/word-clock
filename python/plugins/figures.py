from strip.ledstrip import LedStrip
from neopixel import *
import strip.ledposition as ledPosition
import sys

class Figures:
    
    def __init__(self, strip, color):
        self.actualLeds = []
        self.strip = strip
        self.color = color

    def run(self):
        self.draw(Mario().getFigure())

    def draw(self, figure):
        for item in figure:
            color = item[1]
            leds = list(map(lambda (x, y): ledPosition.ledPosition[(x, y)], item[0]))
            print leds
            print color
            self.strip.setLeds(leds, color)

class Mario:
    hat = [(2, 9), (3, 9), (4, 9), (5, 9), (6, 9), (7, 9),
            (0, 8), (1, 8), (2, 8), (3, 8), (4, 8), (5, 8), (6, 8), (7, 8), (8, 8)]
    face = [(2, 7), (4, 7), (6, 7), 
            (2, 6), (4, 6), (6, 6), (8, 6),
            (5, 5), (6, 5), (7, 5), (8, 5),
            (7, 4),
            (6, 3), (7, 3), (8, 3)]
    hair = [(7, 7), (8, 7), (9, 7),
            (7, 6), (9, 6),
            (9, 5), 
            (8, 4), (9, 4)]
    nose = [(1, 5), (2, 5), (3, 5), (4, 5),
            (1, 4), (2, 4), (3, 4), (4, 4)]
    moustache = [(0, 4), (5, 4), (6, 4),
            (1, 3), (2, 3), (3, 3), (4, 3), (5, 3)]
    trousers = [(2, 2), (6, 2),
            (3, 1), (4, 1), (5, 1), (7, 1),
            (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0)]
    shirt = [(3, 2), (4, 2), (5, 2), (7, 2), (8, 2),
            (1, 1), (8, 1), (9, 1)]
    buckle = [(2, 1), (6, 1)]
    hands = [(1, 0), (8, 0), (9, 0)]
    
    
    mario = [(hat, Color(255, 0, 0)),
            (face, Color(255, 153, 204)),
            (hair, Color(153, 102, 0)),
            (nose, Color(255, 153, 204)),
            (moustache, Color(255, 153, 0)),
            (trousers, Color(0, 0, 255)),
            (shirt, Color(255, 0, 0)),
            (buckle, Color(255, 255, 0)), 
            (hands, Color(255, 153, 204))]

    def getFigure(self):
        return self.mario

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print "invalid number of arguments"
    LedStrip.getInstance().setBrightness(int(sys.argv[4]))
    figures = Figures(LedStrip.getInstance(), Color(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])))
    figures.run()
