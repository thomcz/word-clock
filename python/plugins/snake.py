import strip.ledconfig as ledconfig
import strip.ledposition as ledPosition
from time import sleep
from random import randint
from rpi_ws281x import *

class Snake():
    def __init__(self, cells, color):
        print(cells[0].ledPosition)
        self.cells = cells
        self.color = color
        self.direction = None
    def move(self, direction):
        head = self.cells[0]
        newHead = self.__getNewHead(head, direction)
        self.cells.insert(0, newHead)
        #[newHead] + self.cells
        print("newPos")
        print(newHead.ledPosition)
        print(len(self.cells))
        del self.cells[-1]
        
    def __getNewHead(self, head, direction):
        newX = head.x
        newY = head.y
        newLedPosition = head.ledPosition
        if (direction == Direction().NORTH):
            newY += 1
        if (direction == Direction().EAST):
            newX += 1
        if (direction == Direction().SOUTH):
            newY -= 1
        if (direction == Direction().WEST):
            newX -= 1
    
        newX %= 11
        newY %= 10
        newLedPosition = ledPosition.ledPosition[(newX, newY)]
        return Cell(newX, newY, newLedPosition, head.color)

class Simulation():
    def __init__(self, strip):
        self.strip = strip
        self.state = None
        self.color = self.__getRandomColor()

    def __update(self):

        snake = self.state.snake
        food = self.state.food

        snake.move(self.__getDirectionOfFood(snake, food))
        
        self.__checkIfFoodEaten(snake, food)

        return State(snake, food)

    def run(self):
        self.state = State(self.__getRandomSnake(), self.__getRandomCell())

        print(self.state.snake.cells[0].ledPosition)
        while(True):
            self.__draw()
            self.state = self.__update()
            sleep(1)


    def __checkIfFoodEaten(self, snake, food):
        hasEaten = False

        return hasEaten


    def __getDirectionOfFood(self, snake, food):
        head = snake.cells[0]
        direction = Direction()
        if head.x == food.x:
            if head.y < food.y:
                return direction.EAST
            else:
                return direction.WEST
        elif head.y == food.y:
            if head.x < food.x:
                return direction.NORTH
            else:
                return direction.SOUTH
        elif head.x < food.x:
            return direction.NORTH
       
        return 3

    def __getRandomSnake(self):
        cells = []
        head = self.__getRandomCell()
        cells.append(head)
        print(head.ledPosition)
        
        return Snake([head], head.color)

    
    def __getRandomCell(self):
        foodPositionX = randint(0, 10)
        foodPositionY = randint(0, 9)
        color = self.__getRandomColor()
        ledPos = ledPosition.ledPosition[(foodPositionX, foodPositionY)]
        return Cell(foodPositionX, foodPositionY, ledPos, color)

    def __getRandomColor(self):
        return Color(randint(0, 255), randint(0, 255), randint(0, 255))

    def __draw(self):
        leds = []
        self.strip.resetLeds()
        food = self.state.food
        self.strip.setLed(food.ledPosition, food.color)
        for cell in self.state.snake.cells:
            leds.append(cell.ledPosition)
    
        self.strip.setLeds(leds, self.state.snake.color)

	

class Direction():
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3


class State():
    def __init__(self, snake, food):
        self.snake = snake
        self.food = food
        self.dead = False

class Cell():
    def __init__(self, x, y, ledPosition, color):
        self.x = x
        self.y = y
        self.ledPosition = ledPosition
        self.color = color




