class GeneradorPatrones:

    def __init__(self):
        self.nada=0
                
    def vecinos(self,tablero,x,y):
        vivos=0
        for i in range(3):
            for j in range(3):
                if tablero.tablero[x-1+i][y-1+j]:
                    vivos=+1
        return vivos-1
                    
    def nextStep(self,tablero):
        for y in tablero.row:
            for x in tablero.col:
                if tablero.tablero[x][y]:
                    tablero.tablero[x][y] = self.vecinos(x,y)==2
                else:
                    tablero.tablero[x][y] = self.vecinos(x,y)==3
                
                
