class Comparador(object):


    def __init__(self):
        self.tableros=[]
        self.n=2
    
    def pushTablero(self, tablero):
        self.tableros.insert(0,tablero)
        if len(self.tableros)>self.n:
            self.tableros.pop()

    def comparar(self,actual):
        for i, tab in enumerate(self.tableros):
            if actual==tab:
                self.pushTablero(actual)
                return i+1
        self.pushTablero(actual)
        return False
