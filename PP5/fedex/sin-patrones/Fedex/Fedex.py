class Fedex:
    def __init__(self):
        self.envios = []

    def addEnvio(self, envio):
        self.envios.append(envio)

    def internacionales(self):
        internacionales = []
        for envio in self.envios:
            if envio.isInternacional() == True:
                internacionales.append(envio)
        return internacionales
    
    def propicioAPerderse(self):
        pMin = 0 
        for envio in self.envios:
            if pMin < envio.pBruto():
                ePropicio = envio
        
        return ePropicio
    
    def renderInternacionales(self):
        i = 1
        for interacional in self.internacionales():
            print('Internacional ' + str(i) + ': ')
            i+=1
            interacional.getData()
