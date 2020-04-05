from ElementoMapa import ElementoMapa

"""
Habitacion es un elemento del mapa que tiene lados.
"""


class Habitacion(ElementoMapa):
    def __init__(self):
        self.num = None
        self.norte = None
        self.sur = None
        self.este = None
        self.oeste = None

    # Metodos
    def entrar(self):
        print("Estás en la habitación: ", self.num)

    def esHabitacion(self):
        return True

    def ponerEnOrientacionUnElemento(self, orientacion, unEM):
        orientacion.ponerElementoEnPosicion(unEM, self)
