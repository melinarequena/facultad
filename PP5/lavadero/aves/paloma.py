from aves import Ave

class Paloma(Ave):
    def __init__(self, nom, pes):
        super().__init__(nom)           # llamamos al constructor de la superclass
        self.peso = pes

    def ensuciar(self, vehiculo):
        vehiculo.nivel = vehiculo.nivel + self.peso * 0.3
        self.peso = self.peso - self.peso * 0.3
    
    

    