from __future__ import annotations
from Orientacion import Orientacion


class Sur(Orientacion):
    _UnicaInstacia = None

    @classmethod
    def default(cls) -> Sur:
        if cls._UnicaInstacia is None:
            cls._UnicaInstacia = cls()
        return cls._UnicaInstacia

    def ponerElementoEnPosicion(self,unEM,unaHabitacion):
        unaHabitacion.sur = unEM

    def recorrerDesde(self, lista, unContenedor):
        lista.append(unContenedor.sur)