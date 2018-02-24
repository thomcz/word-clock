import time 
import datetime
import logging
from wordclock import WordClock

from neopixel import *

from flask import Flask
from flask_ask import Ask, statement, convert_errors

app = Flask(__name__)
ask = Ask(app, '/')

logging.getLogger("flask_ask").setLevel(logging.DEBUG)

@ask.intent('Wordclock')
def wordclock():
	clock = WordClock(Color(255,255,255))
	clock.start()
	now = datetime.datetime.now()
        print(now)


if __name__ == '__main__':
	app.run()
