from Modo import Modo
import time
"""
Agresivo es un comportamiento de Bicho.
"""


class Agresivo(Modo):

    def __str__(self):
        return "Agresivo"

    def esAgresivo(self):
        return True

    def dormir(self, unBicho):
        print(str(unBicho)+" duerme....zzzzzz")
        time.sleep(2)

    def mover(self, unBicho):
        puerta = unBicho.obtenerPuertaAleatoria()
        puerta.entrarAlguien(unBicho)
