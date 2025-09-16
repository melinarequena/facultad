class Ciudad:
    def __init__(self, nom):
        self.nombre = nom
        self.autos = []
        self.lavaderos = []

    def llover(self, cantidad):
        for auto in self.autos:
            auto.nivel = auto.nivel + cantidad

    def lavaderoBarato(self):
        ganador = self.lavaderos[0]
        for lavadero in self.lavaderos:
            if lavadero.costoPorMinuto < ganador.costoPorMinuto:
                ganador = lavadero
        return ganador