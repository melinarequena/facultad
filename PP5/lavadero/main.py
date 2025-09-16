from bandada.bandada_enV import BandadaEnV
from bandada.bandada_enW import BandadaEnW
from aves.ave import Ave
from aves.paloma import Paloma
from aves.gaviota import Gaviota
from vehiculo.vehiculo import Vehiculo
from lavadero.lavadero_artesanal import LavaderoArtesanal
from ciudad.ciudad import Ciudad


def main():
    gav1 = Gaviota('Gaviota Pepe', 2)
    gav2 = Gaviota('Gaviota Marie', 3)
    paloma = Paloma('Paloma Carlos', 20)
    cotorra = Ave('Cotorra Lucia')
    loro1 = Ave('Loro Pablo')
    loro2 = Ave('Loro Felipe')

    buenosAires = Ciudad('Buenos Aires')

    # Deberia poder cambiar el tipo de bandada sin necesidad de instaniar una nueva clase
    bandadaV = BandadaEnV([gav1, gav2, paloma, cotorra, loro1, loro2])
    bandadaW = BandadaEnW([gav1, gav2, paloma, cotorra, loro1, loro2])

    auto = Vehiculo('Mi Auto', 'C4', buenosAires)

    SmallLav = LavaderoArtesanal(buenosAires,'SmallLav', 3, 20)

    # print(auto.getNivel())
    # buenosAires.llover(100)
    # print(auto.getNivel())
    # print(SmallLav.lavarAuto(auto))

    # Agregar a tests
    paloma.ensuciar(auto)
    bandadaV.atacar(auto)
    buenosAires.llover(100)
    print(auto.getNivel())
    print(SmallLav.lavarAuto(auto)) # La regla del costo esta mal
    print(auto.getNivel())

    bandadaW.atacar(auto)

    lavaderoBarato = buenosAires.lavaderoBarato()
    lavaderoBarato.lavarAuto(auto)




main()

