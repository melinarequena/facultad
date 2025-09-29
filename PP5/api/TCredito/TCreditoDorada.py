from TCredito.TCredito import TCredito

class TCreditoDorada(TCredito):
    def __init__(self, color, num):
        super().__init__(color, num)

    def cobrar(self, cuenta, valor):
        cuenta.aumentarDeuda(valor)
        