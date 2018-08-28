import strip.ledconfig as ledconfig
from time import sleep

from neopixel import *

class Snake():
    def __init__(self):
        self.cells = None
        self.color = None
        self.direction = None
    def move():

    def add():

    def validate():

    
class Simulation():
     def __init__(self, strip):
        self.strip = strip
        self.state = None
        self.color = self.__getRandomColor()

    def update(self, state):
        newState = State()
        for position in range(ledconfig.LED_COUNT):

            isLiving = False
            actualCell = state.state[position]
            color = actualCell.color

            if actualCell.isLiving:
                isLiving = self.__dieMaybe(state, actualCell)
            else:
                isLiving = self.__resurection(state, actualCell)
            newCell = Cell(actualCell.x, actualCell.y, position, isLiving, color)
            newState.state.append(newCell)

        return newState

    def run(self):
        if self.state is None:
            self.state = self.__getRandomState()
        while(True):
            self.__draw()
            self.state = self.simulation.update(self.state)
            sleep(1)

    def __getRandomSnake(self):
        state = State()
        ledPosition = 0
        for x in range(11):
            for y in range(10):
                isLiving = randint(0, 1) == 1
                color = self.color
                cell = Cell(x, y, ledPosition, isLiving, color)
                state.state.append(cell)
                ledPosition += 1
        return state

    def __getRandomColor(self):
        return Color(randint(0, 255), randint(0, 255), randint(0, 255))

    def __draw(self):
        leds = []
        self.strip.resetLeds()
        for i in self.state.state:
            if i.isLiving:
                leds.append(i.ledPosition)
        self.strip.setLeds(leds, self.color)

	

       

class State():
    def __init__(self):
        self.state = []

class Cell():
    def __init__(self, x, y, ledPosition, isLiving, color):
        self.x = x
        self.y = y
        self.ledPosition = ledPosition
        self.isLiving = isLiving
        self.color = color




