from Enfermedad.Enfermedad import Enfermedad

class EnfermedadAutoinmune(Enfermedad):
    def __init__(self, nom, cant):
        super().__init__(nom, cant)

    def destruirCelulas(self, persona):
        persona.disminuirCelulas(self.cantCelulas)

        
