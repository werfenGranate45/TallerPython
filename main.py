from Modelos.Cafe import Cafe
from Modelos.Punto3D import Punto3D
from Modelos.Punto import Punto
from Modelos.FiguraGeometica import Circulo,Cuadrado

objCafe = Cafe("Americano","Leche y cafe","Grande","500ml","32.05")

del objCafe

punto = Punto(2,2)
punto3D = Punto3D(2.0,2.0,-5.5)

#print("Imprimir desde punto: ")
#punto.imprimir()
#print("Desde punto 3D: ")
#punto3D.imprimir()

#cir = Circulo(4.5)
#cua = Cuadrado(5.0)

#print(cir.area())
#print(cua.area())
#print(cir.perimietro())
#print(cua.perimietro())


try:
    x = 10
    if x >= 10:
        raise 
except ZeroDivisionError as vari:
    print(vari)
    