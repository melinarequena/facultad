from lavadero.lavadero import Lavadero

class LavaderoArtesanal(Lavadero):
    def __init__(self, ciud, nom, personas, costoPM):
        super().__init__(ciud)
        self.nombre = nom
        self.cantPersonas = personas
        self.costoPorMinuto = costoPM

    def calcularTiempo(self, vehiculo):
        return vehiculo.nivel/5
    
    def calcularCosto(self, vehiculo):
        return self.cantPersonas * self.calcularTiempo(vehiculo) * self.costoPorMinuto
    
    def lavarAuto(self, vehiculo):
        costo = self.calcularCosto(vehiculo)
        vehiculo.nivel = 0
        return costo
        
