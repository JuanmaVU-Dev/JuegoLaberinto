from abc import ABC
from ElementoMapa import ElementoMapa
from Este import Este
from Norte import Norte
from Oeste import Oeste
from Sur import Sur


class Contenedor(ElementoMapa, ABC):
    def __init__(self):
        self.hijos = []
        self.orientaciones = []
        self.agregarOrientaciones()

    def esArmario(self):
        return False

    def agregarOrientaciones(self):
        self.orientaciones = [Norte(), Sur(), Este(), Oeste()]

    def ponerEnOrientacionUnElemento(self, orientacion, unEM):
        orientacion.ponerElementoEnPosicion(unEM, self)

    def agregarHijo(self, unEM):
        unEM.padre = self
        self.hijos.append(unEM)
