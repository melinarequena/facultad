from bandada.tipo_bandada import TipoBandada

class BandadaEnW(TipoBandada):
    def __init__(self):
        super().__init__()

    def atacar(bandada, vehiculo):
        for ave in bandada.bandada:
            ave.ensuciar(vehiculo)
        for ave in bandada.bandada:
            ave.ensuciar(vehiculo)
