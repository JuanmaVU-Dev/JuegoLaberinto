from Pared import Pared

"""
ParedBomba es una pared que tiene una bomba y explota cuando está activa.
"""


class ParedBomba(Pared):
    def __init__(self):
        self.activa = False

    def entrar(self):
        if self.activa:
            print("La bomba ha explotado, has muerto")
        else:
            print("La bomba esta desactivada, no ha pasado nada")
