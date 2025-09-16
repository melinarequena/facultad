from bandada import bandada

class bandadaEnI(bandada):
    def __init__(self, bandada):
        super().__init__(bandada)

    def atacar(self, vehiculo):
        self.bandada[0].ensuciar(vehiculo)
        self.bandada[len-1].ensuciar(vehiculo)
    
