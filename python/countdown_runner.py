from plugins.countdown import Countdown
from strip.ledstrip import LedStrip
from time import sleep

from neopixel import *

if __name__ == "__main__":
    Countdown(Color(200, 43, 157), LedStrip()).run()
