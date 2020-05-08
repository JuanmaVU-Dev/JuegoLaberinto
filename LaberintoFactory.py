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

"""
Implementación patrón Abstract Factory.
"""


class LaberintoFactory:
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
        return Sur().default()

    def fabricarEste(self):
        return Este().default()

    def fabricarNorte(self):
        return Norte().default()

    def fabricarOeste(self):
        return Oeste().default()

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
