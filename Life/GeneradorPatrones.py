class GeneradorPatrones(object):

    def __init__(self):
        pass

    @staticmethod
    def vecinos(tablero,fila,columna):
        if fila == 0:
            rangoFilai = 0
        else:
            rangoFilai = fila-1

        if columna == 0:
            rangoColumnai = 0
        else:
            rangoColumnai = columna-1

        if (fila + 1) > len(tablero):
            rangoFilaf = fila
        else:
            rangoFilaf = fila + 1

        if (columna + 1) > len(tablero[0]):
            rangoColumnaf = columna
        else:
            rangoColumnaf = columna + 1

        vivos=0
        for i in range(rangoFilai,rangoFilaf):
            for j in range(rangoColumnai,rangoColumnaf):
                if tablero[i][j]==1:
                    vivos=+1
                
        if tablero[fila][columna]==1:
            return vivos-1
        return vivos

    @staticmethod
    def nextStep(tablero):
        modificado = list(tablero)

        for fila in range(len(tablero)):
            for columna in range(len(tablero[0])):
                vecinos = GeneradorPatrones.vecinos(tablero,fila,columna)
                if tablero[fila][columna]==1:
                    if vecinos==2 or vecinos==3:
                        modificado[fila][columna] = 1
                    else:
                        modificado[fila][columna] = 0
                else:
                    if vecinos==3:
                        modificado[fila][columna] = 1 
                    else:
                        modificado[fila][columna] = 0
        return modificado
                
