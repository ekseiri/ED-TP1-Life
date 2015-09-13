class GeneradorPatrones(object):

    def __init__(self):
        self.nada=0

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
    
        if tablero[x][y]==1:
            return vivos-1
        return vivos

    @staticmethod
    def nextStep(tablero):
        for y in range(len(tablero)):
            for x in range(len(tablero[y])):
                if tablero[x][y]==1:
                    if self.vecinos(x,y)==2:
                        tablero[x][y] = 1
                    else:
                        tablero[x][y] = 0
                else:
                    if self.vecinos(x,y)==3:
                        tablero[x][y] = 1 
                    else:
                        tablero[x][y] = 0
                
                
