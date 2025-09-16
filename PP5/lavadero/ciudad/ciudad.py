class ciudad:
    def __init__(self, nom):
        self.nombre = nom
        self.autos = []

    def llover(self, cantidad):
        for auto in self.autos:
            auto.nivel = auto.nivel + cantidad