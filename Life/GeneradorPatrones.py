class GeneradorPatrones(object):

    def __init__(self):
        pass

    @staticmethod
    def vecinos(tablero,x,y):
        vivos=0
        for i in range(3):
            for j in range(3):
                try:
                    if tablero[x-1+i][y-1+j]==1:
                        vivos=+1
                except Exception:
                    pass
        print(x,y)
        if tablero[x][y]==1:
            return vivos-1
        return vivos

    @staticmethod
    def nextStep(tablero):
        modificado = list(tablero)
        for y in range(len(tablero)):
            for x in range(len(tablero[y])):
                vecinos = self.vecinos(tablero,x,y)
                if tablero[x][y]==1:
                    if vecinos==2 or vecinos==3:
                        modificado[x][y] = 1
                    else:
                        modificado[x][y] = 0
                else:
                    if vecinos==3:
                        modificado[x][y] = 1 
                    else:
                        modificado[x][y] = 0
        return modificado
                
