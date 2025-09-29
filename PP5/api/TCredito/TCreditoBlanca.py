from TCredito.TCredito import TCredito

class TCreditoBlanca(TCredito):
    def __init__(self, color, num):
        super().__init__(color, num)
        self.tope = 10000
        
    def validarTope(self, valor):
        return True if self.tope > valor else False # Raise Value Error

    def cobrar(self, cuenta, valor):
        if self.validarTope(valor):
            cuenta.aumentarDeuda(valor)