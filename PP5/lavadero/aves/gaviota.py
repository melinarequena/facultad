from aves import Ave

class gaviota(Ave):
    def __init__(self, nom, cantPez):
        super().__init__(nom)
        self.cantPecesComidos = cantPez

    def ensuciar(self, vehiculo):
        vehiculo.nivel = vehiculo.nivel + self.cantPecesComidos * 3