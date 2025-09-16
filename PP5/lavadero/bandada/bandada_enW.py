from bandada.bandada import Bandada

class BandadaEnW(Bandada):
    def __init__(self, bandada):
        super().__init__(bandada)

    def atacar(self, vehiculo):
        for ave in self.bandada:
            ave.ensuciar(vehiculo)
        for ave in self.bandada:
            ave.ensuciar(vehiculo)
