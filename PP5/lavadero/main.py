from bandada.bandada_enV import bandadaEnV;
from aves.ave import Ave;
from aves.paloma import paloma;
from aves.gaviota import gaviota;
from vehiculo.vehiculo import vehiculo
from lavadero.lavadero_artesanal import lavaderoArtesanal
from ciudad.ciudad import ciudad;




def main():
    gav1 = gaviota('Gaviota Pepe', 2)
    gav2 = gaviota('Gaviota Marie', 3)
    paloma = Ave('Paloma Carlos')
    cotorra = Ave('Cotorra Lucia')
    loro1 = Ave('Loro Pablo')
    loro2 = Ave('Loro Felipe')

    buenosAires = ciudad('Buenos Aires')

    bandada = bandadaEnV([gav1, gav2, paloma, cotorra, loro1, loro2])

    auto = vehiculo('Mi Auto', 'C4', buenosAires)

    SmallLav = lavaderoArtesanal('SmallLav', 3, 20)

    