from abc import ABC, abstractmethod

class Lavadero(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def lavarAuto(vehiculo):
        pass

