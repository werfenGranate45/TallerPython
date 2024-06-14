from Modelos.Punto import Punto

class Punto3D(Punto):
    z = 0.0
    
    def __init__(self, x, y, z) -> None:
        super().__init__(x, y)
        self.z = z
    
    def setZ(self,z):
        self.z = z
    
    def getZ(self): return self.z
    
    def imprimir(self):
        print(f"{super().imprimir()},{self.z}")
    
    def imprimirPunto3D(self):
        print(f"{self.x},{self.y},{self.z}")
        
    