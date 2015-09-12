class GeneradorPatrones:

    def __init__(self):
        self.nada=0

    @staticmethod
    def vecinos(tablero,x,y):
        vivos=0
        for i in range(3):
            for j in range(3):
                if tablero[x-1+i][y-1+j]:
                    vivos=+1
        return vivos-1

    @staticmethod
    def nextStep(tablero):
        for y in range(len(tablero)):
            for x in range(len(tablero[y])):
                if tablero[x][y]:
                    tablero[x][y] = self.vecinos(x,y)==2
                else:
                    tablero[x][y] = self.vecinos(x,y)==3
                
                
