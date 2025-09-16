from aves.ave import Ave

class Gaviota(Ave):
    def __init__(self, nom, cantPez):
        super().__init__(nom)
        self.cantPecesComidos = cantPez

    def ensuciar(self, vehiculo):
        vehiculo.nivel = vehiculo.nivel + self.cantPecesComidos * 3
        print(f"{self.nombre}: He ensuciado al vehiculo")