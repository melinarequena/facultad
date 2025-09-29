from gato import Gato
from perro import Perro

def main():
    mi_gato = Gato("Cati")
    tu_gato = Gato("Ross")
    print(type(mi_gato)) # Tipo de dato
    print(mi_gato) # Direccion de memoria
    mi_gato.saludar()
    tu_gato.saludar()

if __name__ == "__main__":
    main()