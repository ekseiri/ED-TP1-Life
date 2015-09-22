# coding: utf8
import time
from GeneradorPatrones import *
from Comparador import Comparador
from utils import Tools
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
        self.stills = 0
        self.combs = 0
        self.iter = 0
        self.combMatrix = []

    def run(self):
        if (self.mode == 1):
            self.normal()
        elif (self.mode == 2):
            self.still_life()

    def normal(self):
        Tools.clear()

        comparador = Comparador(2)

        while (self.running is True):
            print(self.tablero)
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
            Tools.clear()

    def still_life(self):
        def coordenar(ancho, coordenadas):
            pass

            t = Tablero(ancho, ancho)
            for c in coordenadas:
                x, y = Tools.calccoord(ancho, c)
                t.tablero[x][y] = 1
            return t

        tam = len(self.tablero.tablero)
        self.combs = math.factorial(
            tam**2) / (math.factorial(tam**2 - self.vidas) * math.factorial(self.vidas))
        Tools.clear()

        print("Combinaciones: " + repr(self.combs))
        print("\n" + "Trabajando..." + "\n")

        if len(self.combMatrix) == 0:
            self.combMatrix = list(combinations(range(tam**2), self.vidas))

        i = self.iter
        for c in range(i , len(self.combMatrix)):
            self.iter = self.iter + 1
            t = coordenar(tam, self.combMatrix[c])
            comp = Comparador(1)
            comp.pushTablero(t.tablero)
            if comp.comparar(GeneradorPatrones.nextStep(t.tablero)) == 1:
                self.stills += 1
                print(self.combMatrix[c])
                print("\n")
                print(t)
                self.work.append(self.combMatrix[c])
                print(
                    "\n" + "Progreso: %" + ("%.2f" % ((self.iter / self.combs) * 100)))
                # input("\n")
        print("\n" + "Trabajo Completado, presionar Enter " +
              "para volver al menu principal")
        input("Encontrados: " + repr(self.stills))
        self.running = False
