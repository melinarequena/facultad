class CuentaBancaria:
    def __init__(self, doc, monto, limite, tDebito):
        self.dni = doc
        self.limite = limite
        self.tDebito = tDebito
        self.tCredito = []
        self.deuda = 0
        self.monto = monto


    def addCredito(self, tarjeta):
        self.tCredito.append(tarjeta)

    def aumentarDeuda(self, valor):
        deuda += valor

    def gastarMonto(self, valor):
        self.monto -= valor
    
    def findTarjeta(self, numero):
        if self.tDebito.numero == numero:
            return self.tDebito
        for tarjeta in self.tCredito:
            if tarjeta.numero == numero:
                return tarjeta
        return False
    
    def getMonto(self):
        return self.monto
    
    def getDeuda(self):
        return self.deuda
                
        
