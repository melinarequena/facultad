class vehiculo:
    def __init__(self, nom, mod, ubi):
        self.nivel = 0
        self.nombre = nom
        self.modelo = mod
        self.ubicacion = ubi


    def getNivel(self):
        return self.nivel
    
    def irAlLavadero(self, lavadero):
        lavadero.lavar(self)