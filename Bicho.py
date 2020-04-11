"""
Bicho es el enemigo básico de nuestro juego.
"""


class Bicho:
    def __init__(self):
        self.modo = None
        self.posicion = None

    def actua(self):
        self.modo.actua(self)

    def esGeneroso(self):
        return self.modo.esGeneroso()

    def esAgresivo(self):
        return self.modo.esAgresivo()

    def esPerezoso(self):
        return self.modo.esPerezoso()
