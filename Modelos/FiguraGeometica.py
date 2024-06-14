from abc import ABC,abstractmethod
import math

class FiguraGeometrica(ABC):

    @abstractmethod
    def area(self): pass
    
    @abstractmethod
    def perimietro(self): pass

class Circulo(FiguraGeometrica):
    radio = 0.0
    
    def __init__(self,rad):
        self.radio = rad
    
    def area(self):
        return (self.radio*self.radio)*math.pi
    
    def perimietro(self):
        return (self.radio*2.0)*math.pi

class Cuadrado(FiguraGeometrica):
    lado = 0.0
    
    def __init__(self,lado) -> None:
        self.lado = lado
    
    def area(self):
        return self.lado*self.lado
    
    def perimietro(self):
        return 4.0*self.lado