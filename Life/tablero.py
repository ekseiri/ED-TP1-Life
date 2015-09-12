import random


class Tablero:

    def __init__(self, col, row, vivas):
        self.vivas = vivas
        self._col = col
        self._row = row
        self._tablero = [[None] * self._col for self._row in range(self._row)]

    def llenar(self):
        print (self.vivas, self._col, self._row)
        for i in range(self.vivas):
            posicion = (random.randint(0, self._row),
                        random.randint(0, self._col - 1))

            while (self.tablero[posicion[0]][posicion[1]] is not None):
                posicion = (random.randint(0, self._row),
                            random.randint(0, self._col - 1))
            else:
                self.tablero[posicion[0]][posicion[1]] = 1

    @property
    def tablero(self):
        return self._tablero

    @tablero.setter
    def tablero(self, t):
        self._tablero = t
