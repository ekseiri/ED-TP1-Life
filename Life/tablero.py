# coding: utf8
import random
import os


class Tablero (object):

    def __init__(self, col, row):
        self._col = col
        self._row = row
        self._tablero = [[0] * self._col for self._row in range(self._row)]

    def fill(self, vivas):
        for i in range(vivas):
            posicion = (random.randint(0, self._row),
                        random.randint(0, self._col - 1))

            while (self._tablero[posicion[0]][posicion[1]] is not 0):
                posicion = (random.randint(0, self._row),
                            random.randint(0, self._col - 1))
            else:
                self._tablero[posicion[0]][posicion[1]] = 1

    def manual_fill(self):
        pass

    @property
    def tablero(self):
        return self._tablero

    @tablero.setter
    def tablero(self, t):
        self._tablero = t

    def __repr__(self):
        if ('win32' not in str.lower(os.sys.platform)):
            CEROS = '\033[95m'
            UNOS = '\033[93m'
            TERM = '\033[0m'
            return '\n'.join(
                   [''.join(
                    ['{:2}'.format(item)
                     .replace('0', CEROS + '-' + TERM).replace
                     ('1', UNOS + '*' + TERM) for item in row])
                    for row in self._tablero])
        else:
            return '\n'.join(
                   [''.join(
                    ['{:2}'.format(item)
                     .replace('0', '-').replace
                     ('1', '*') for item in row])
                    for row in self._tablero])
