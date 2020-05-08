from abc import ABC
from ElementoMapa import ElementoMapa
from Este import Este
from Norte import Norte
from Oeste import Oeste
from Sur import Sur
import random


class Contenedor(ElementoMapa, ABC):
    def __init__(self):
        self.num = None
        self.hijos = []
        self.orientaciones = []
        self.agregarOrientaciones()

    def esArmario(self):
        return False

    def esHabitacion(self):
        return False

    def agregarOrientaciones(self):
        self.orientaciones = [Norte().default(), Sur().default(), Este().default(), Oeste().default()]

    def ponerEnOrientacionUnElemento(self, orientacion, unEM):
        orientacion.ponerElementoEnPosicion(unEM, self)

    def agregarHijo(self, unEM):
        unEM.padre = self
        self.hijos.append(unEM)

    def recorrer(self, lista):
        for hijo in self.hijos:
            lista.append(hijo)
            hijo.recorrer(lista)

        for orientacion in self.orientaciones:
            orientacion.recorrerDesde(lista, self)

    def obtenerOrientacionAleatoria(self):
        return self.orientaciones[random.randint(0, len(self.orientaciones) - 1)]

    def obtenerPuertaAleatoria(self):
        lista = []
        self.recorrer(lista)
        listaPuertas = []
        for each in lista:
            if each.esPuerta():
                listaPuertas.append(each)
        return listaPuertas[random.randint(0, len(listaPuertas) - 1)]




