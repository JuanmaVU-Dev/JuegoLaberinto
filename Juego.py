from Agresivo import Agresivo
from Armario import Armario
from Bicho import Bicho
from Bomba import Bomba
from Este import Este
from Generoso import Generoso
from Habitacion import Habitacion
from Laberinto import Laberinto
from Norte import Norte
from Oeste import Oeste
from Pared import Pared
from Perezoso import Perezoso
from Puerta import Puerta
from Sur import Sur


# Juego es la clase principal de la solución

class Juego:
    def __init__(self):
        self.laberinto = None
        self.bichos = []

    # Metodos

    # Se añade un bicho
    def agregarBicho(self,bicho):
        self.bichos.append(bicho)

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
        return hab

    def fabricarArmario(self):
        return Armario()

    def fabricarArmarioEn(self, unContenedor):
        armario = self.fabricarArmario()
        puerta = self.fabricarPuerta(armario, unContenedor)
        armario.ponerEnOrientacionUnElemento(self.fabricarNorte(), self.fabricarPared())
        armario.ponerEnOrientacionUnElemento(self.fabricarOeste(), self.fabricarPared())
        armario.ponerEnOrientacionUnElemento(self.fabricarEste(), self.fabricarPared())
        armario.ponerEnOrientacionUnElemento(self.fabricarSur(), puerta)

        armario.num = len(unContenedor.hijos) + 1

        unContenedor.agregarHijo(armario)

    def fabricarLaberinto(self):
        return Laberinto()

    def fabricarSur(self):
        return Sur()

    def fabricarEste(self):
        return Este()

    def fabricarNorte(self):
        return Norte()

    def fabricarOeste(self):
        return Oeste()

    def fabricarModoAgresivo(self):
        return Agresivo()

    def fabricarModoPerezoso(self):
        return Perezoso()

    def fabricarModoGeneroso(self):
        return Generoso()

    def fabricarBichoAgresivoEn(self, hab):
        bicho = Bicho()
        bicho.modo = self.fabricarModoAgresivo()
        bicho.posicion = hab
        return bicho

    def fabricarBichoPerezosoEn(self, hab):
        bicho = Bicho()
        bicho.posicion = hab
        bicho.modo = self.fabricarModoPerezoso()
        return bicho

    def fabricarBichoGenerosoEn(self, hab):
        bicho = Bicho()
        bicho.posicion = hab
        bicho.modo = self.fabricarModoGeneroso()
        return bicho

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

    """
    Laberinto de 4 habitaciones y 4 bichos (2 perezosos y 2 agresivos)
    """

    def fabricarLaberinto4HabFM(self):
        print("Juego del laberinto con 4 habitaciones")
        lab = self.fabricarLaberinto()
        hab1 = self.fabricarHabitacion(1)
        hab2 = self.fabricarHabitacion(2)
        hab3 = self.fabricarHabitacion(3)
        hab4 = self.fabricarHabitacion(4)

        pt12 = self.fabricarPuerta(hab1, hab2)
        pt13 = self.fabricarPuerta(hab1, hab3)
        pt34 = self.fabricarPuerta(hab3, hab4)
        pt24 = self.fabricarPuerta(hab2, hab4)

        hab1.ponerEnOrientacionUnElemento(self.fabricarNorte(), self.fabricarPared())
        hab1.ponerEnOrientacionUnElemento(self.fabricarEste(), pt13)
        hab1.ponerEnOrientacionUnElemento(self.fabricarOeste(), self.fabricarPared())
        hab1.ponerEnOrientacionUnElemento(self.fabricarSur(), pt12)

        hab2.ponerEnOrientacionUnElemento(self.fabricarNorte(), pt12)
        hab2.ponerEnOrientacionUnElemento(self.fabricarEste(), pt24)
        hab2.ponerEnOrientacionUnElemento(self.fabricarOeste(), self.fabricarPared())
        hab2.ponerEnOrientacionUnElemento(self.fabricarSur(), self.fabricarPared())

        hab3.ponerEnOrientacionUnElemento(self.fabricarNorte(), self.fabricarPared())
        hab3.ponerEnOrientacionUnElemento(self.fabricarEste(), self.fabricarPared())
        hab3.ponerEnOrientacionUnElemento(self.fabricarOeste(), pt13)
        hab3.ponerEnOrientacionUnElemento(self.fabricarSur(), pt34)

        hab4.ponerEnOrientacionUnElemento(self.fabricarNorte(), pt34)
        hab4.ponerEnOrientacionUnElemento(self.fabricarEste(), self.fabricarPared())
        hab4.ponerEnOrientacionUnElemento(self.fabricarOeste(), pt24)
        hab4.ponerEnOrientacionUnElemento(self.fabricarSur(), self.fabricarPared())

        lab.agregarHabitacion(hab1)
        lab.agregarHabitacion(hab2)
        lab.agregarHabitacion(hab3)
        lab.agregarHabitacion(hab4)

        self.agregarBicho(self.fabricarBichoPerezosoEn(hab2))
        self.agregarBicho(self.fabricarBichoAgresivoEn(hab1))
        self.agregarBicho(self.fabricarBichoPerezosoEn(hab4))
        self.agregarBicho(self.fabricarBichoAgresivoEn(hab3))

        self.laberinto = lab

    def fabricarLaberinto4HabArm(self):
        print("Juego del laberinto con 4 habitaciones y 4 armarios")
        lab = self.fabricarLaberinto()
        hab1 = self.fabricarHabitacion(1)
        hab2 = self.fabricarHabitacion(2)
        hab3 = self.fabricarHabitacion(3)
        hab4 = self.fabricarHabitacion(4)

        pt12 = self.fabricarPuerta(hab1, hab2)
        pt13 = self.fabricarPuerta(hab1, hab3)
        pt34 = self.fabricarPuerta(hab3, hab4)
        pt24 = self.fabricarPuerta(hab2, hab4)

        hab1.ponerEnOrientacionUnElemento(self.fabricarNorte(), self.fabricarPared())
        hab1.ponerEnOrientacionUnElemento(self.fabricarEste(), pt13)
        hab1.ponerEnOrientacionUnElemento(self.fabricarOeste(), self.fabricarPared())
        hab1.ponerEnOrientacionUnElemento(self.fabricarSur(), pt12)

        self.fabricarArmarioEn(hab1)

        hab2.ponerEnOrientacionUnElemento(self.fabricarNorte(), pt12)
        hab2.ponerEnOrientacionUnElemento(self.fabricarEste(), pt24)
        hab2.ponerEnOrientacionUnElemento(self.fabricarOeste(), self.fabricarPared())
        hab2.ponerEnOrientacionUnElemento(self.fabricarSur(), self.fabricarPared())

        self.fabricarArmarioEn(hab2)

        hab3.ponerEnOrientacionUnElemento(self.fabricarNorte(), self.fabricarPared())
        hab3.ponerEnOrientacionUnElemento(self.fabricarEste(), self.fabricarPared())
        hab3.ponerEnOrientacionUnElemento(self.fabricarOeste(), pt13)
        hab3.ponerEnOrientacionUnElemento(self.fabricarSur(), pt34)

        self.fabricarArmarioEn(hab3)

        hab4.ponerEnOrientacionUnElemento(self.fabricarNorte(), pt34)
        hab4.ponerEnOrientacionUnElemento(self.fabricarEste(), self.fabricarPared())
        hab4.ponerEnOrientacionUnElemento(self.fabricarOeste(), pt24)
        hab4.ponerEnOrientacionUnElemento(self.fabricarSur(), self.fabricarPared())

        self.fabricarArmarioEn(hab4)

        hab1.agregarHijo(self.fabricarBomba())
        hab2.agregarHijo(self.fabricarBomba())
        hab3.agregarHijo(self.fabricarBomba())
        hab4.agregarHijo(self.fabricarBomba())

        lab.agregarHabitacion(hab1)
        lab.agregarHabitacion(hab2)
        lab.agregarHabitacion(hab3)
        lab.agregarHabitacion(hab4)

        self.agregarBicho(self.fabricarBichoPerezosoEn(hab2))
        self.agregarBicho(self.fabricarBichoAgresivoEn(hab1))
        self.agregarBicho(self.fabricarBichoPerezosoEn(hab4))
        self.agregarBicho(self.fabricarBichoAgresivoEn(hab3))

        self.laberinto = lab

