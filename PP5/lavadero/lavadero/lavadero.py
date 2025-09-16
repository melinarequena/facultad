from abc import ABC, abstractmethod

class Lavadero(ABC):
    def __init__(self, ciudad):
        ciudad.lavaderos.append(self)

    @abstractmethod
    def lavarAuto(vehiculo):
        pass

