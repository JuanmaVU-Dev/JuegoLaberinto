from Contenedor import Contenedor

"""
Habitacion es un elemento del mapa que tiene lados.
"""


class Habitacion(Contenedor):
    def __init__(self):
        super().__init__()
        self.lados = []

    # Metodos
    def entrar(self):
        print("Estás en la habitación: ", self.num)

    def esHabitacion(self):
        return True