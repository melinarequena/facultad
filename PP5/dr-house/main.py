from Enfermedad.EnfermedadInfecciosa import EnfermedadInfecciosa
from Enfermedad.EnfermedadAutoinmune import EnfermedadAutoinmune
from Enfermedad.Enfermedad import Enfermedad

from Persona.Persona import Persona

lupus = EnfermedadAutoinmune('Lupus', 10000)
malaria = EnfermedadInfecciosa('Malaria', 5000)
persona1 = Persona('Lelo', 3000000, 36)

print(persona1.getCelulas()) # 3000000
print(persona1.isSana()) # True

# 1
persona1.enfermarse(lupus)
persona1.enfermarse(malaria)

print(persona1.isSana()) # False


lupus.destruirCelulas(persona1)
malaria.atacarPersona(persona1)

# 2
lupus.atenuar(500)
malaria.atenuar(5000)
print(persona1.isSana()) # False

# 3
while persona1.isSana() == False:
    persona1.tomarMedicacion(300)
    print('Tomando medicacion')
    print(persona1.isSana())

print(persona1.isSana())



