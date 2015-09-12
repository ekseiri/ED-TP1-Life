class Comparador:


    def __init__(self):
        self.tableros=[]
        self.n=2
    
    def pushTablero(self, tablero):
        self.tableros.append(tablero)
        if len(self.tableros)>self.n:
            self.tableros.pop()

    def comparar(self,actual):
        i=0
        for tab in self.tableros:
            i=+1
            if actual==tab:
                self.pushTablero(actual)
                self.tableros.pop()
                return i
        self.pushTablero(actual)
        self.tableros.pop()
        return False
