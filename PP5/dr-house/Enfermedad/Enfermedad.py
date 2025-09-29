class Enfermedad:
    def __init__(self, nom, cant):
        self.nombre = nom
        self.cantCelulas = cant

    def agravarEnfermedad(self, cant):
        self.cantCelulas += cant

    def atenuarEnfermedad(self, cant):
        self.cantCelulas = self.cantCelulas - cant * 15

    def atenuar(self, cant):
        self.cantCelulas -= cant

    def isCurada(self):
        return True if self.cantCelulas <= 0 else False
    
    def getCelulas(self):
        return self.cantCelulas
    
    
    
    