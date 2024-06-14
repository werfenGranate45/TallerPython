#Nombre de las clases en UpperCamelCase
#Atriutos de la clase en Python en Snake_Case
class Cafe: 
    estilo = ""
    ingrediente = ""
    tamaño = ""
    capacidad = 0.0
    temperatura = True
    
    def __init__(self, estilo, ingrediente, tamaño, capacidad, temperatura) -> None:
        self.estilo = estilo
        self.ingrediente = ingrediente
        self.tamaño = tamaño
        self.capacidad = capacidad
        self.temperatura = temperatura
    
    def setEstilo(self, est: str):
        if(len(est) > 0): return True
        else: return False
    
    def getEstilo(self): return self.estilo
    
    def quemar(self):    pass
    
    def despertar(self): pass
    
    def __del__(self):
        print("Se destruyó")
    
    def toString(self): 
        cadena = "Estilo: "+str(self.estilo)
        cadena  += "Ingrediente: "+str(self.ingrediente)
        cadena += " Tamaño: "+str(self.tamaño)
        cadena += " Capacidad: "+str(self.capacidad)
        cadena += " Temperatura: "+str(self.temperatura) 
        return cadena