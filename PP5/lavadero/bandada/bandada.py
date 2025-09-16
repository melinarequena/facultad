from abc import ABC, abstractmethod

class bandada(ABC): # Abstract class
    def __init__(self, aves):
        # Lista de aves
        self.bandada = aves
        
    @abstractmethod
    def atacar(self):
        pass # Obliga a las hijas a implementarla