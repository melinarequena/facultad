from Envio.Envio import Envio
from Lugar.Lugar import Lugar
from Fedex.Fedex import Fedex

fedex = Fedex()

california = Lugar('California', 'Estados Unidos')
miami = Lugar('Miami', 'Estados Unidos')
bsas = Lugar('buenos aires', 'argentina')
utrecht = Lugar('Utretch', 'Paises Bajos')

envio1 = Envio(california, miami, 5000, 1500, ['Libros'])

envio2 = Envio(bsas, utrecht, 2000, 220, ['musica', 'arte', 'tecnologia'])

fedex.addEnvio(envio1)
fedex.addEnvio(envio2)

# 1
print('Punto 1')
fedex.renderInternacionales()
# 2
print('Punto 2')
print(envio1.pNeto())
print(envio1.pBruto())

# 3
print('Punto 3')
print(envio2.pNeto())
print(envio2.pBruto())

# 4
print('Punto 4')
print(fedex.propicioAPerderse().getData())


