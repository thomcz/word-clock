from plugins.wordclock import WordClock
from plugins.countdown import Countdown
#from plugins.gameoflife import GameOfLife
#from plugins.ledsoff import LedsOff
#from plugins.ledtest import LedTest
from strip.ledstrip import LedStrip
#from tools.stoppablethread import StoppableThread
#import threading
import subprocess as subprocess

from neopixel import *

from flask import Flask, render_template

app = Flask(__name__)

ledStrip = LedStrip()

executedProcess = None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/wordclock')
def wordclock():
    return render_template('wordclock.html')

@app.route('/countdown')
def countdown():
    return render_template('countdown.html')
#    global executedProcess
#    terminateRunningPlugin()
 #   executedProcess = subprocess.Popen(['python', 'countdown_runner.py'])
  #  return 'countdown started'

#@app.route('/brightness')
#def brightness():
#    global executedProcess
#    terminateRunningPlugin()
#    LedStrip.getInstance().setBrightness(40)
#    __wordclock()
#    return 'brightness set'


@app.route('/shutdown')
def shutdown():
    global executedProcess
    terminateRunningPlugin()
    executedProcess = subprocess.Popen(['python', 'shutdown.py'])
    return 'shutdown'

def terminateRunningPlugin():
    global executedProcess
    print(executedProcess)
    if executedProcess != None:
        subprocess.Popen.terminate(executedProcess)

#@ask.intent('GOL')
#def gameOfLife():
#    gol = GameOfLife(ledStrip)
#    __run(gol.run, 1, True)
#    return statement(render_template('gol_start'))

#@ask.intent('LedsOff')
#def ledsOff():
#    off = LedsOff(ledStrip)
#    __run(off.run, 0, False)
#    return statement(render_template('lights_off'))


#@ask.intent('Stopp')
#def stop():
#    for thread in threads:
#        thread.stop()
#        thread.join()
#    return statement("")

#def __run(func, waitingTime, loop):
#    stop()
#    thread = StoppableThread(func, waitingTime, loop)
#    thread.start()
#    threads.append(thread)

def __wordclock():
    global executedProcess

    terminateRunningPlugin()
    executedProcess = subprocess.Popen(['python', 'wordclock.py', '123', '123', '123', '123'])
    return 'wordclock started'

#def __ledtest():
#    test = LedTest(Color(255,255,255), ledStrip)
#    __run(test.run, 0, False)


if __name__ == '__main__':
    __wordclock()
    app.run(host = '0.0.0.0')
