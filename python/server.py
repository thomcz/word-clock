from plugins.wordclock import WordClock
from plugins.countdown import Countdown
import subprocess as subprocess

from neopixel import *

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

executedProcess = None
brightness = 255
programPath = '/home/pi/word-clock/python/plugins/'
programStates = {
        0 : 'shutdown.py',
        1 : 'restart.py',
        2 : 'wordclock.py',
        3 : 'countdown.py'
        }
actualProgramState = 2
rgbColorTuple = (255, 255, 255)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/wordclock', methods=['GET', 'POST'])
def wordclock():
    global rgbColorTuple 
    if request.method == 'POST':
        rgbColorTuple = __hexToRGB(request.form['color'][1:])
        __wordclock()
        return redirect(url_for('index'))
    elif request.method == 'GET':
        return render_template('wordclock.html')

def __hexToRGB(color):
    return tuple(int(color[i : i + 2], 16) for i in (0, 2, 4)) 


@app.route('/countdown', methods=['GET', 'POST'])
def countdown():
    global rgbColorTuple
    if request.method == 'POST':
        rgbColorTuple = __hexToRGB(request.form['color'][1:])
        __countdown()
        return redirect(url_for('index'))
    elif request.method == 'GET':
        return render_template('countdown.html')

def __countdown():
    global actualProgramState

    actualProgramState = 3
    __runProgram()

@app.route('/brightness', methods=['POST'])
def setBrightness():
    global brightness

    brightness = 80
    __runProgram()

@app.route('/shutdown')
def shutdown():
    global actualProgramState

    actualProgramState = 0
    __runProgram()
    return 'shutdown startet'

@app.route('/restart', methods=['GET'])
def restart():
    global actualProgramState

    actualProgramState = 1
    __runProgram()
    return 'restart started'

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
    global actualProgramState

    actualProgramState = 2
    __runProgram()


def __runProgram():
    global executedProcess
    global brightness
    global acutalProgramState
    global rgbColorTuple

    print actualProgramState
    
    terminateRunningPlugin()
    executedProcess = subprocess.Popen(['python', 
        programPath + programStates[actualProgramState], 
        str(rgbColorTuple[0]), 
        str(rgbColorTuple[1]), 
        str(rgbColorTuple[2]), 
        str(brightness)])

if __name__ == '__main__':
    __wordclock()
    app.run(host = '0.0.0.0')
