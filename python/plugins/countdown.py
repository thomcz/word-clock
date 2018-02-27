from time import sleep

from strip.states import WordClockStates
from strip.ledstrip import LedStrip

from neopixel import *
 
class Countdown():

    def run(self):
       wordState = WordClockStates()
       for hour in reversed(wordState.STUNDE):
            self.strip.resetLeds()
            self.strip.setLeds(hour, self.color)
            sleep(1)

    def __init__(self, color):
        self.strip = LedStrip()
        self.color = color
            
if __name__ == '__main__':
        Countdown(Color(255,255,255)).start()


