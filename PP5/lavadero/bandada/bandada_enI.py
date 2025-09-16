from bandada import bandada

class bandadaEnI(bandada):
    def __init__(self, bandada):
        super().__init__(bandada)

    def atacar(self):
        self.bandada[0].atacar()
        self.bandada[len-1].atacar()
    
