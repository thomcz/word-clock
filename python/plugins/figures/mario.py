from rpi_ws281x import *

class Mario:
    hat = [(2, 9), (3, 9), (4, 9), (5, 9), (6, 9),
            (1, 8), (2, 8), (3, 8), (4, 8), (5, 8), (6, 8), (7, 8), (8, 8), (9, 8)]
    face = [(4, 7), (5, 7), (7, 7), 
            (1, 6), (3, 6), (4, 6), (5, 6), (7, 6), (8, 6), (9, 6), 
            (1, 5), (4, 5), (5, 5), (6, 5), (8, 5), (9, 5), (10, 5),
            (2, 4), (3, 4), (4, 4), (5, 4),
            (2, 3), (3, 3), (4, 3), (5, 3), (6, 3), (7, 3)]
    hair = [(1, 7), (2, 7), (3, 7),
            (0, 6), (2, 6),
            (0, 5), (2, 5), (3, 5), 
            (1, 4)]
    moustache = [(7, 5),
            (6, 4), (7, 4), (8, 4), (9, 4)]
    trousers = [(3, 2), (6, 2),
            (3, 1), (6, 1),
            (3, 0), (4, 0), (5, 0), (6, 0)]
    shirt = [(1, 2), (2, 2), (4, 2), (5, 2), (7, 2), (8, 2),
            (0, 1), (1, 1), (2, 1), (4, 1), (5, 1), (7, 1), (8, 1), (9, 1),
            (0, 0), (1, 0), (2, 0), (7, 0), (8, 0), (9, 0), (10, 0)]
    background = [(0, 9), (1, 9), (7, 9), (8, 9), (9, 9), (10, 9),
            (0, 8), (10, 8),
            (0, 7), (8, 7), (9, 7), (10, 7), 
            (10, 6), 
            (0, 4), (10, 4),
            (0, 3), (1, 3), (8, 3), (9, 3), (10, 3), 
            (0, 2), (9, 2), (10, 2), 
            (10, 1)]
    
    
    mario = [(hat, Color(255, 0, 0)),
            (face, Color(255, 222, 173)),
            (hair, Color(160, 82, 45)),
            (moustache, Color(160, 82, 45)),
            (trousers, Color(0, 0, 255)),
            (shirt, Color(255, 0, 0))]

    def getFigure(self):
        return self.mario


