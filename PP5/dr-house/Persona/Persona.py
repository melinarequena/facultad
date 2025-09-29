class Persona:
    def __init__(self, nom, cant, temp):
        self.nombre = nom
        self.cantCelulas = cant
        self.enfermedades = []
        self.temperatura = temp

    def enfermarse(self, enfermedad):
        self.enfermedades.append(enfermedad)

    def tomarMedicacion(self, cant):
        for enfermedad in self.enfermedades:
            print('Tomando medicacion para: ')
            print(enfermedad.nombre)
            print('Celulas antes:')
            print(enfermedad.cantCelulas)
            enfermedad.atenuarEnfermedad(cant)
            print('Celulas despues:')
            print(enfermedad.cantCelulas)
            if enfermedad.isCurada():
                self.enfermedades.remove(enfermedad)

    def isSana(self):
        return True if self.enfermedades.__len__() == 0 else False
    
    def getCelulas(self):
        return self.cantCelulas
    
    def disminuirCelulas(self, cant):
        self.cantCelulas -= cant

    def aumentarTemperatura(self, cant):
        self.temperatura += cant

    