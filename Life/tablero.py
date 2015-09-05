import random

class Tablero:

    def __init__(self, col, row, vivas):
        self.vivas = vivas
        self.col = col
        self.row = row
        self.tablero = [[None] * self.col for self.row in range(self.row) ]

    def llenar(self):
        print (self.vivas, self.col, self.row)
        for i in range(self.vivas):
            posicion = (random.randint(0,self.row),random.randint(0,self.col - 1))

            while (self.tablero[posicion[0]][posicion[1]] is not None):
                posicion = (random.randint(0,self.row),random.randint(0,self.col - 1))
            else:
                self.tablero[posicion[0]][posicion[1]] = 1

