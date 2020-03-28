from Puerta import Puerta
from Pared import Pared
from Habitacion import Habitacion
from Laberinto import Laberinto
from Bomba import Bomba


# Juego es la clase principal de la solución

class Juego:
    def __init__(self):
        self.laberinto = None

    # Métodos de fabricación

    def fabricaPuerta(self):
        return Puerta()

    def fabricarPuerta(self, hab1, hab2):
        pt = self.fabricaPuerta()
        pt.hab1 = hab1
        pt.hab2 = hab2
        return pt

    def fabricarPared(self):
        return Pared()

    def fabricarBomba(self):
        return Bomba()

    def fabricarHabitacion(self, num):
        hab = Habitacion()
        hab.num = num
        return hab;

    def fabricarLaberinto(self):
        return Laberinto()

    def fabricarLaberinto2HabFM(self):
        print("Juego del laberinto con 2 habitaciones")
        lab = self.fabricarLaberinto()
        hab1 = self.fabricarHabitacion(1)
        hab2 = self.fabricarHabitacion(2)
        puerta = self.fabricarPuerta(hab1, hab2)

        hab1.norte = self.fabricarPared()
        hab1.este = self.fabricarPared()
        hab1.oeste = self.fabricarPared()
        hab1.sur = puerta

        hab2.norte = puerta
        hab2.este = self.fabricarPared()
        hab2.oeste = self.fabricarPared()
        hab2.sur = self.fabricarPared()

        lab.agregarHabitacion(hab1)
        lab.agregarHabitacion(hab2)

        self.laberinto = lab

    def fabricarLaberinto2Hab2Bomb(self):
        print("Juego del laberinto con dos habitaciones y dos bombas")
        lab = self.fabricarLaberinto()
        hab1 = self.fabricarHabitacion(1)
        hab2 = self.fabricarHabitacion(2)
        puerta = self.fabricarPuerta(hab1, hab2)

        hab1.norte = self.fabricarBomba()
        hab1.este = self.fabricarPared()
        hab1.oeste = self.fabricarPared()
        hab1.sur = puerta

        hab2.norte = puerta
        hab2.este = self.fabricarPared()
        hab2.oeste = self.fabricarPared()
        hab2.sur = self.fabricarBomba()

        lab.agregarHabitacion(hab1)
        lab.agregarHabitacion(hab2)

        self.laberinto = lab
