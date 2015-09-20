class GeneradorPatrones(object):

    def __init__(self):
        pass

    @staticmethod
    def vecinos(tablero, fila, columna):
        if fila == 0:
            rangoFilai = 0
        else:
            rangoFilai = fila - 1

        if columna == 0:
            rangoColumnai = 0
        else:
            rangoColumnai = columna - 1

        if (fila + 1) == len(tablero):
            rangoFilaf = fila
        else:
            rangoFilaf = fila + 1

        if (columna + 1) == len(tablero[0]):
            rangoColumnaf = columna
        else:
            rangoColumnaf = columna + 1

        vivos = 0
        '''print("Probando", fila, columna)'''
        for i in range(rangoFilai, rangoFilaf + 1):
            for j in range(rangoColumnai, rangoColumnaf + 1):
                '''print(i, j)'''
                '''print("estado", tablero[i][j])'''
                if tablero[i][j] == 1:
                    vivos = vivos + 1
        if tablero[fila][columna] == 1:
            '''print("vivos", vivos - 1)'''
            return vivos - 1
        '''print("vivos", vivos)'''
        return vivos

    @staticmethod
    def nextStep(tablero):
        # print(tablero)
        modificado = [list(row) for row in tablero]

        for fila in range(len(tablero)):
            for columna in range(len(tablero[0])):
                vecinos = GeneradorPatrones.vecinos(tablero, fila, columna)
                if tablero[fila][columna] == 1:
                    if vecinos == 2 or vecinos == 3:
                        modificado[fila][columna] = 1
                    else:
                        modificado[fila][columna] = 0
                else:
                    if vecinos == 3:
                        modificado[fila][columna] = 1
                    else:
                        modificado[fila][columna] = 0
        # print(tablero)
        # print(modificado)
        return modificado
