import logging
from plugins.wordclock import WordClock
from plugins.countdown import Countdown
from plugins.gameoflife import GameOfLife
from plugins.ledsoff import LedsOff
from strip.ledstrip import LedStrip
from tools.stoppablethread import StoppableThread
import threading

from neopixel import *

from flask import Flask, render_template

from flask_ask import Ask, statement, convert_errors

app = Flask(__name__)
ask = Ask(app, '/')

ledStrip = LedStrip()

logging.getLogger("flask_ask").setLevel(logging.DEBUG)
threads = []

@ask.intent('Wordclock')
def wordclock():
    __wordclock()
    return statement(render_template('wordclock_start'))

@ask.intent('Countdown')
def countdown():
    countdown = Countdown(Color(255,255,255), ledStrip)
    __run(countdown.run, 0, False)
    return statement(render_template('countdown_start'))

@ask.intent('GOL')
def gameOfLife():
    gol = GameOfLife(ledStrip)
    __run(gol.run, 1, True)
    return statement(render_template('gol_start'))

@ask.intent('LedsOff')
def ledsOff():
    off = LedsOff(ledStrip)
    __run(off.run, 0, False)
    return statement(render_template('lights_off'))


@ask.intent('Stopp')
def stop():
    for thread in threads:
        thread.stop()
        thread.join()
    return statement("")

def __run(func, waitingTime, loop):
    stop()
    thread = StoppableThread(func, waitingTime, loop)
    thread.start()
    threads.append(thread)

def __wordclock():
    clock = WordClock(Color(255,255,255), ledStrip)
    __run(clock.run, 10, True)

if __name__ == '__main__':
    __wordclock()
    app.run()
