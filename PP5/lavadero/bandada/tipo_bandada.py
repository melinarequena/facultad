from abc import ABC, abstractmethod

class TipoBandada(ABC): # Abstract class
    def __init__(self):
        # # Lista de aves
        # self.bandada = aves
        
    @abstractmethod
    def atacar(self, vehiculo):
        pass # Obliga a las hijas a implementarla