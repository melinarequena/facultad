class Banco:
    def __init__(self):
        self.clientes = []

    def addCliente(self, cuenta):
        self.clientes.append(cuenta)

    def consumir(self, numero, valor):
        for cliente in self.clientes:
            tarjeta = cliente.findTarjeta(numero)
        if tarjeta == False:
            raise ValueError('TARJETA NO ENCONTRADA')
        else:
            tarjeta.cobrar(valor)

    def findCuenta(self, dni):
        for cliente in self.clientes:
            if cliente.dni == dni:
                return cliente
        raise ValueError('CLIENTE NO ENCONTRADO')

    def consultar_saldo(self, dni):
        cuenta = self.findCuenta(dni)
        return cuenta.getMonto()
    
    def consultar_deuda(self, dni):
        cuenta = self.findCuenta(dni)
        return cuenta.getDeuda()
    
    def mejor_cliente(self):
        return max(self.clientes, key=lambda c: c.deuda)
        
