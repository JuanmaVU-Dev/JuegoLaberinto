import time
"""
Modo define el comportamiento del bicho.
"""


class Modo:

    def actua(self, unBicho):
        """Template Method"""
        self.mover(unBicho)
        self.atacar(unBicho)
        self.dormir(unBicho)

    def esGeneroso(self):
        return False

    def esPerezoso(self):
        return False

    def esAgresivo(self):
        return False

    def mover(self, unBicho):
        """El bicho se mueve"""
        orientacion = unBicho.posicion.obtenerOrientacionAleatoria()
        orientacion.entrarAlguien(unBicho)

    def atacar(self, unBicho):
        unBicho.atacar()

    def dormir(self, unBicho):
        print(str(unBicho)+" duerme....zzzzzz")
        time.sleep(3)