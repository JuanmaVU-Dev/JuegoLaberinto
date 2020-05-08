from __future__ import annotations
from Orientacion import Orientacion


class Este(Orientacion):
    _UnicaInstacia = None

    @classmethod
    def default(cls) -> Este:
        if cls._UnicaInstacia is None:
            cls._UnicaInstacia = cls()
        return cls._UnicaInstacia

    def ponerElementoEnPosicion(self, unEM, unaHabitacion):
        unaHabitacion.este = unEM

    def recorrerDesde(self, lista, unContenedor):
        lista.append(unContenedor.este)
