from abc import ABC, abstractmethod

"""
ElementoMapa es la clase abstracta de los elementos del mapa.
"""


class ElementoMapa(ABC):

    @abstractmethod
    def entrar(self):
        pass

    def esHabitacion(self):
        return False

    def esBomba(self):
        return False

    def esPared(self):
        return False

    def esPuerta(self):
        return False
