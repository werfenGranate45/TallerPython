class Punto:
    x = 0.0
    y = 0.0
    
    def __init__(self,x,y) -> None:
        self.x = x
        self.y = y
    
    def setX(self,x):
        self.x = x
    
    def setY(self,y):
        self.y = y
    
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def imprimir(self):
        print(f"{self.x},{self.y}")
        return f"{self.x},{self.y}"
    
    