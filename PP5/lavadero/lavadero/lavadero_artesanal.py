from lavadero import lavadero

class lavaderoArtesanal(lavadero):
    def __init__(self, nom, personas, costoPM):
        super().__init__()
        self.nombre = nom
        self.cantPersonas = personas
        self.costoPorMinuto = costoPM

    def calcularTiempo(self, vehiculo):
        return vehiculo.nivel/5
    
    def calcularCosto(self, vehiculo):
        return self.cantPersonas * self.calcularTiempo(vehiculo) * self.costoPorMinuto
    
    def lavarAuto(self, vehiculo):
        vehiculo.nivel = 0
        return self.calcularCosto(self, vehiculo)
        
