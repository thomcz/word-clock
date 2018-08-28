from random import randint
import strip.ledconfig as ledconfig
from time import sleep

from neopixel import *

class GameOfLife():
    def __init__(self, strip):
        self.strip = strip
        self.state = None
        self.color = self.__getRandomColor()

    def run(self):
        if self.state is None:
            self.state = self.__getRandomState()
        while(True):
            self.__draw()
            self.state = self.__update(self.state)

            sleep(1)

    def __getRandomState(self):
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

    def __update(self, state):
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
	
    def __dieMaybe(self, state, cell):
        neighbours =  self.__countLivingNeighbours(state, cell)
        return neighbours == 2 or neighbours == 3

    def __resurection(self, state, cell):
        return self.__countLivingNeighbours(state, cell) == 3
		
    def __countLivingNeighbours(self, state, cell):
        livingNeighbours = 0
        for i in range(ledconfig.LED_COUNT):
            actualCell = state.state[i]
            if actualCell.x == cell.x + 1 and actualCell.y == cell.y - 1 and actualCell.isLiving:
                livingNeighbours += 1
            elif actualCell.x == cell.x and actualCell.y == cell.y - 1 and actualCell.isLiving:
                livingNeighbours += 1
            elif actualCell.x == cell.x - 1 and actualCell.y == cell.y - 1 and actualCell.isLiving:
                livingNeighbours += 1
            elif actualCell.x == cell.x + 1 and actualCell.y == cell.y and actualCell.isLiving:
                livingNeighbours += 1
            elif actualCell.x == cell.x - 1 and actualCell.y == cell.y and actualCell.isLiving:
                livingNeighbours += 1
            elif actualCell.x == cell.x - 1 and actualCell.y == cell.y + 1 and actualCell.isLiving:
                livingNeighbours += 1
            elif actualCell.x == cell.x and actualCell.y == cell.y + 1 and actualCell.isLiving:
                livingNeighbours += 1
            elif actualCell.x == cell.x + 1 and actualCell.y == cell.y + 1 and actualCell.isLiving:
                livingNeighbours += 1

        return livingNeighbours

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



