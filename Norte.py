from Orientacion import Orientacion


class Norte(Orientacion):

    def ponerElementoEnPosicion(self,unEM,unaHabitacion):
        unaHabitacion.norte = unEM

    def recorrerDesde(self, lista, unContenedor):
            lista.append(unContenedor.norte)