from abc import ABC, abstractmethod

class Bandada(ABC): # Abstract class
    def __init__(self, aves):
        # Lista de aves
        self.bandada = aves
        
    @abstractmethod
    def atacar(self, vehiculo):
        pass # Obliga a las hijas a implementarla