class Ave:
    def __init__(self, nom):
        self.nombre = nom

    def ensuciar(self, vehiculo):
        vehiculo.nivel = vehiculo.nivel + 10
        print(f"{self.nombre}: He ensuciado al vehiculo")