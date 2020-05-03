"""
Bicho es el enemigo básico de nuestro juego.
"""


class Bicho:
    def __init__(self):
        self.modo = None
        self.posicion = None
        self.vivo = True

    def __str__(self):
        return "Un Bicho modo "+str(self.modo)

    def actua(self):
        self.modo.actua(self)

    def esGeneroso(self):
        return self.modo.esGeneroso()

    def esAgresivo(self):
        return self.modo.esAgresivo()

    def esPerezoso(self):
        return self.modo.esPerezoso()

    def obtenerPuertaAleatoria(self):
        return self.posicion.obtenerPuertaAleatoria()

    def atacar(self):
        print(str(self)+" ataca.")

    def matar(self):
        self.vivo = False

