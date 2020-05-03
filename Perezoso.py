from Modo import Modo
import time
"""
Agresivo es un comportamiento de Bicho.
"""


class Perezoso(Modo):

    def __str__(self):
        return "Perezoso"

    def esPerezoso(self):
        return True

    def mover(self, unBicho):
        """El bicho se mueve"""
        print("Los perezosos no se mueven")

    def atacar(self, unBicho):
        unBicho.atacar()

    def dormir(self, unBicho):
        print(str(unBicho)+" duerme....zzzzzz")
        time.sleep(5)
