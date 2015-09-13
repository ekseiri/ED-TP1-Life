from tablero import Tablero


class Game(object):

    def __init__(self, mode, tablero):
        self.mode = mode
        self.tablero = tablero
        self.running = False

    def run(self):
        if (self.mode == 1):
            self.normal()
        elif (self.mode == 2):
            self.still_life()

    def normal(self):
        print (self.tablero.tablero)
        input('Normal Game Loop')

    def still_life(self):
        print (self.tablero.tablero)
        input('Still Life Game Loop')
