"""
Laberinto representa la clase principal del juego
"""


class Laberinto:

    def __init__(self):
        self.habitaciones = [];

    # Metodos

    # Se añade una habitación
    def agregarHabitacion(self, hab):
        self.habitaciones.append(hab)

    # Se entra a la primera habitacion de la lista de habitaciones del laberinto
    def entrar(self):
        hab = self.habitaciones[0]
        hab.entrar()
