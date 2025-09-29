class Envio:
    def __init__(self, origen, destino, peso, base, categorias):
        self.origen = origen
        self.destino = destino
        self.peso = peso
        self.pBase = base
        self.categorias = categorias
        self.impuestos = []

    # Recargos

    def checkCategory(self):
        if self.categorias.count('tecnologia') >= 1:
            return True
        else: return False
            
    def checkSobrepeso(self):
        if self.peso > 1000:
            return True
        else: return False

    def addRecargos(self):
        recargos = []
        if self.checkCategory():
            recargos.append(self.pBase * 0.10)

        if self.checkSobrepeso():
            recargos.append(80)

        return recargos

    # Peso Neto

    def pNeto(self):
        pRecargos = 0
        for recargo in self.addRecargos():
            pRecargos += recargo
        pNeto = self.pBase + pRecargos
        return pNeto
        
        
    # Impuestos

    def isInternacional(self):
        return True if self.origen.getPais() != self.destino.getPais() else False
    
    def isMunicipal(self):
        return True if not self.isInternacional() and self.origen.getCiudad() == self.destino.getCiudad() else False

    def calcularImpuestos(self):
        self.impuestos = []
        pNeto = self.pNeto()
        self.impuestos.append(pNeto * 0.20)

        if self.categorias.__len__() > 3:
            self.impuestos.append(pNeto * 0.01)
        
        if self.isInternacional():
            self.impuestos.append(pNeto * 0.50)

        # if self.pBase % 2 == 0:
        #     self.impuestos.append(pNeto * 0.10)

        if self.isMunicipal():
            self.impuestos.append(pNeto * 0.05)
        
        total = 0
        for impuesto in self.impuestos:
            total += impuesto

        return total
    
    def pBruto(self):
        return self.pNeto() + self.calcularImpuestos()
    
    def getData(self):
        print(self.destino.getCiudad() + " --> " + self.origen.getCiudad() + " Precio Base: " + str(self.pBase) + " Precio Bruto: " + str(self.pBruto()) + " Precio Neto: " + str(self.pNeto()) + '\n' + 'Categoria: ')
        for categoria in self.categorias:
            print(categoria)


