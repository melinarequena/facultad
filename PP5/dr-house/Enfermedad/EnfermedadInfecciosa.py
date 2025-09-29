from Enfermedad.Enfermedad import Enfermedad
class EnfermedadInfecciosa(Enfermedad):
    def __init__(self, nom, cant):
        super().__init__(nom, cant)

    def atacarPersona (self, persona):
        persona.aumentarTemperatura(self.cantCelulas)

    def reproducirse (self):
        self.cantCelulas = self.cantCelulas*2

