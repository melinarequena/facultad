from aves.ave import Ave

class Paloma(Ave):
    def __init__(self, nom, pes):
        super().__init__(nom)           # llamamos al constructor de la superclass
        self.peso = pes

    def ensuciar(self, vehiculo):
        cant = self.peso * 0.3
        vehiculo.aumentarSuciedad(cant)
        self.peso -= self.peso * 0.3
        print(f"{self.nombre}: He ensuciado al vehiculo")
    
    

    