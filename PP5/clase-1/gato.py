class Gato:
    def __init__(self, nombre): # Funcion inicializadora
        # Magic Methods --> __metodos__ que funcionan como sobrecargas
        self.nombre = Gato._validar_nombre(nombre)

    # Convecion: los miembros que comienzan con _ son "privados"
    @staticmethod
    def _validar_nombre(nombre): # Al ser estatico no necesito usar self
        if not isinstance(nombre, str):
            raise TypeError("Debe ser una cadena")
        if not nombre:
            raise ValueError("No debe ser vacio")
        return nombre

    def saludar(self):
        print(f"{self.nombre} dice miau")