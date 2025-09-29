class TDebito:
    def __init__(self, num, monto, cuenta):
        self.numero = num
        self.monto = monto
        self.cuenta = cuenta

    def validarSaldo(self, valor):
        if self.monto > valor:
            return True
        else:
            raise ValueError('SALDO INSUFICIENTE') 
    
    def validarIVA(valor):
        return valor * 0.79 if valor > 3000 else valor
    
    def cobrar(self, valor):
        monto = self.validarIVA(valor)
        if self.validarSaldo(monto):
            self.cuenta.gastarMonto(monto)

