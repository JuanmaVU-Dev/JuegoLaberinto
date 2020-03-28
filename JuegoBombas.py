from Juego import Juego
from ParedBomba import ParedBomba


class JuegoBombas(Juego):

    def fabricarPared(self):
        return ParedBomba();
