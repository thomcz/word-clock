import time 
import logging
from wordclock import WordClock
from countdown import Countdown
from stoppablethread import StoppableThread
import threading

from neopixel import *

from flask import Flask
from flask_ask import Ask, statement, convert_errors

app = Flask(__name__)
ask = Ask(app, '/')

logging.getLogger("flask_ask").setLevel(logging.DEBUG)
threads = []

@ask.intent('Wordclock')
def wordclock():
        clock = WordClock(Color(255,255,255))
        t = StoppableThread(clock.start, 10)
        t.start()
        threads.append(t)
        return statement('Uhr gestartet')

@ask.intent('Countdown')
def countdown():
        countdown = Countdown(Color(255,255,255))
        t = threading.Thread(target = countdown.start)
        t.start()
        return statement('Countdown gestartet')

@ask.intent('Stopp' )
def stop():
        for t in threads:
                t.stop()
                t.join()
        return statement("stopp")
                
if __name__ == '__main__':
        app.run()


