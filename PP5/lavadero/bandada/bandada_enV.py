from bandada import bandada

class bandadaEnV(bandada):
    def __init__(self, bandada):
        super().__init__(bandada)

    def atacar(self):
        for ave in self.bandada:
            ave.atacar()
    
