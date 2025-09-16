from bandada import bandada

class bandadaEnW(bandada):
    def __init__(self, bandada):
        super().__init__(bandada)

    def atacar(self):
        for ave in self.bandada:
            ave.atacar()
        for ave in self.bandada:
            ave.atacar()
    pass
