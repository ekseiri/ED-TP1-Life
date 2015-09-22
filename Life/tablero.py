# coding: utf8
import random
import os
from utils import *


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
        while True:
            Tools.clear()
            print(self)
            try:

                key = int(input("\n" + "Ingrese la celda a cambiar, " +
                                "CTRL+C para iniciar" + "\n"))

                # if ((key > 0) and (key <= (self._col * self._row))):
                x, y = Tools.calccoord(self._col, key)
                if self.tablero[x][y] == 1:
                    self.tablero[x][y] = 0
                else:
                    self.tablero[x][y] = 1

            except KeyboardInterrupt:
                break
            except ValueError:
                print("Error: Debe ingresar un entero")
                input("")
            except IndexError:
                print("Error: Numero de celda invalido " +
                      "(0:" + repr(self._col ** 2 - 1) + ")")
                input("")

    @property
    def tablero(self):
        return self._tablero

    @tablero.setter
    def tablero(self, t):
        self._tablero = t

    def __repr__(self):
        header = [i for i in range(0, self._col)]
        headString = ''.join(['{:2}'.format(item) for item in header])

        if ('win32' not in str.lower(os.sys.platform)):
            CEROS = '\033[95m'
            UNOS = '\033[93m'
            TERM = '\033[0m'
            BOLD = '\033[1m'

            headString = BOLD + '  ' + headString + TERM + '\n'

            tabString = '\n'.join(
                [BOLD + '{:2}'.format(i) + TERM + ''.join(
                    ['{:2}'.format(item)
                     .replace('0', CEROS + '-' + TERM).replace
                     ('1', UNOS + '*' + TERM) for item in row])
                    for i, row in enumerate(self._tablero)])

        else:
            headString = '  ' + headString + '\n'

            tabString = '\n'.join(
                ['{:2}'.format(i) + ''.join(
                    ['{:2}'.format(item)
                     .replace('0', '-').replace
                     ('1', '*') for item in row])
                    for i, row in enumerate(self._tablero)])

        return headString + tabString
