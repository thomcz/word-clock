from random import randint
import strip.ledconfig as ledconfig

from neopixel import *

class GameOfLife():
    def __init__(self, strip):
        self.strip = strip
        self.state = None
        self.simulation = Simulation()
    
    def run(self):
        if self.state is None:
            self.state = self.__getRandomState()
        self.__draw()
        self.state = self.simulation.update(self.state)

    def __getRandomState(self):
        state = State()
        for position in range(ledconfig.LED_COUNT):
            isLiving = randint(0, 1) == 1
            color = self.__getRandomColor()
            cell = Cell(position, isLiving, color)
            state.state.append(cell)
        return state

    def __getRandomColor(self):
        return Color(255, 255, 255)
    
    def __draw(self):
        leds = []
        for i in range(self.state.state):
            if self.state.state[i].isLiving:
                leds.append(i)
        self.strip.setLeds(leds, Color(255, 255, 255))



        

class Simulation():
    def __init__(self):
        self.state = None

    def update(self, state):
        newState = State()
        for position in range(ledconfig.LED_COUNT):
            
            isLiving = False
            #color = state[position].color
            color = Color(255, 255, 255)

            if state.isLiving:
                isLiving = self__dieMaybe(state, position)
            else:
                isLiving = self.__resurection(state, position)
            cell = Cell(position, isLiving, color)
            newState.state.append(cell)

        return newState

    def __dieMaybe(self, state, position):
        return False

    def __isLiving(self, state, position):
        return False


class Draw():
    def draw(state):
        leds = []
        for i in range(state.state):
            if state.state[i].isLiving:
                leds.append(i)
        strip.setLeds(leds, Color(255, 255, 255))
    


class State():
    def __init__(self):
        self.state = []

class Cell():
    def __init__(self, position, isLiving, color):
        self.position = position
        self.isLiving = isLiving
        self.color = color
