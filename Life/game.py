import time
from GeneradorPatrones import *
from Comparador import Comparador
import os


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

    def clear(self):
        if ('win32' not in str.lower(os.sys.platform)):
            print('')
            os.system('clear')
        else:
            print('')
            os.system('cls')

    def normal(self):
        self.clear()

        comparador = Comparador(2)

        while (self.running is True):
            print (self.tablero)
            time.sleep(0.2)
            c = comparador.comparar(self.tablero.tablero)

            if (c is not False):
                if (c == 2):
                    input('Oscilador Nivel 2 encontrado, presionar Enter ' +
                          'para terminar')
                    self.running = False

                elif (c == 1):
                    input('Vida Estatica encontrada, presionar Enter ' +
                          'para terminar')
                    self.running = False
            else:
                self.tablero.tablero = GeneradorPatrones.nextStep(
                                       self.tablero.tablero)
            self.clear()

    def still_life(self):
        input('Still Life Game Loop')
        print (self.tablero)
