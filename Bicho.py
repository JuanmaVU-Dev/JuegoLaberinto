"""
Bicho es el enemigo básico de nuestro juego.
"""


class Bicho:
    def __init__(self):
        self.modo = None
        self.posicion = None

    def actua(self):
        self.modo.actua(self)
