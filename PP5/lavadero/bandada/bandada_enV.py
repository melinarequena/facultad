from bandada.bandada import Bandada

class BandadaEnV(Bandada):
    def __init__(self, bandada):
        super().__init__(bandada)

    def atacar(self, vehiculo):
        for ave in self.bandada:
            ave.ensuciar(vehiculo)
    
