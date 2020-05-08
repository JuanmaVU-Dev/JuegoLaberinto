from __future__ import annotations
from Orientacion import Orientacion


class Oeste(Orientacion):
    _UnicaInstacia = None

    @classmethod
    def default(cls) -> Oeste:
        if cls._UnicaInstacia is None:
            cls._UnicaInstacia = cls()
        return cls._UnicaInstacia

    def ponerElementoEnPosicion(self,unEM,unaHabitacion):
        unaHabitacion.oeste = unEM

    def recorrerDesde(self, lista, unContenedor):
        lista.append(unContenedor.oeste)