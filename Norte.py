from __future__ import annotations
from Orientacion import Orientacion


class Norte(Orientacion):
    _UnicaInstacia = None

    @classmethod
    def default(cls) -> Norte:
        if cls._UnicaInstacia is None:
            cls._UnicaInstacia = cls()
        return cls._UnicaInstacia

    def ponerElementoEnPosicion(self,unEM,unaHabitacion):
        unaHabitacion.norte = unEM

    def recorrerDesde(self, lista, unContenedor):
        lista.append(unContenedor.norte)


