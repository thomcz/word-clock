 
class LedUtil():

    
    def __getRandomCell(self):
        x = randint(0, 10)
        y = randint(0, 9)
        color = self.__getRandomColor()
        ledPos = ledPosition.ledPosition[(foodPositionX, foodPositionY)]
        return Cell(foodPositionX, foodPositionY, ledPos, color)

