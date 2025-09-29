class Lugar:
    def __init__(self, ciudad, pais):
        self.ciudad = ciudad.upper()
        self.pais = pais.upper()

    def getPais(self):
        return self.pais
    
    def getCiudad(self):
        return self.ciudad
    