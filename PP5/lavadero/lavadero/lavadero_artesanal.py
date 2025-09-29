from lavadero.lavadero import Lavadero

class LavaderoArtesanal(Lavadero):
    def __init__(self, ciud, nom, personas, costoPM):
        super().__init__(ciud)
        self.nombre = nom
        self.cantPersonas = personas
        self.costoPorMinuto = costoPM
    
    def calcularCosto(self, vehiculo):
        return self.cantPersonas * vehiculo.calcularTiempo() * self.costoPorMinuto
    
    def lavarAuto(self, vehiculo):
        costo = self.calcularCosto(vehiculo)
        vehiculo.limpiar()
        return costo
        
