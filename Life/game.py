import time
from GeneradorPatrones import *
from Comparador import Comparador
import os
from tablero import Tablero
from combination import *
import math


class Game(object):

    def __init__(self, mode, tablero, vidas=2):
        self.mode = mode
        self.tablero = tablero
        self.running = False
        self.vidas = vidas
        self.work = []

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
        def coordenar(ancho, coordenadas):
            def calccoord(ancho, coord):
                x = coord % ancho
                y = coord // ancho
                return (x,y)

            t = Tablero(ancho, ancho)
            for c in coordenadas:
                x,y = calccoord(ancho, c)
                t.tablero[x][y] = 1
            return t

        tam = len(self.tablero.tablero)

        self.clear()

        print("Combinaciones: ")
        print(math.factorial(tam)/math.factorial(tam-self.vidas))
        print("\n" + "Trabajando..." + "\n")

        for c in combinations(range(tam**2), self.vidas):
            t = coordenar(tam, c)
            comp = Comparador(1)
            comp.pushTablero(t.tablero)
            if comp.comparar(GeneradorPatrones.nextStep(t.tablero)) == 1:
                print(c)
                self.work.append(c)
        input("\n" + "Trabajo Completado")
        self.running = False






