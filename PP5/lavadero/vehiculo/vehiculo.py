from ciudad.ciudad import Ciudad
class Vehiculo:
    def __init__(self, nom, mod, ciudad):
        self.nivel = 0
        self.nombre = nom
        self.modelo = mod
        self.ubicacion = ciudad.nombre
        ciudad.autos.append(self)

    def getNivel(self):
        return self.nivel
    
    def irAlLavadero(self, lavadero):
        lavadero.lavar(self)

    def aumentarSuciedad(self, cantidad):
        self.nivel += cantidad

    def limpiar(self):
        self.nivel = 0

    def calcularTiempo(self):
        return self.nivel/5
    
    def encontrarLavadero(self):
        pass