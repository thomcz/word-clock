from rpi_ws281x import *

class Heart:
    heart = [(2, 9), (3, 9), (7, 9), (8, 9), 
            (1, 8), (4, 8), (6, 8), (9, 8),
            (0, 7), (5, 7), (10, 7), 
            (0, 6), (10, 6), 
            (0, 5), (10, 5), 
            (1, 4), (9, 4), 
            (2, 3), (8, 3),
            (3, 2), (7, 2),
            (4, 1), (6, 1), 
            (5, 0)]
    
    heartFigure = [(heart, Color(255, 0, 0))]

    def getFigure(self):
        return self.heartFigure


