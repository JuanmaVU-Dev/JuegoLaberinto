from abc import ABC,abstractmethod

"""
Orientacion define el interfaz de las orientaciones.
"""


class Orientacion(ABC):

    @abstractmethod
    def ponerElementoEnPosicion(self,unEM,unaHabitacion):
        pass