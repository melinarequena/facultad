class Bandada:
    def __init__(self, bandada: Bandada, aves):
        self.tipo = bandada
        self.bandada = aves

    def cambiarEstrategia(self, bandada: Bandada): # Comnuta el tipo de bandada
        self.tipo = bandada

    def atacarAuto(self, vehiculo):
        self.tipo.atacar(self, vehiculo)
