from Orientacion import Orientacion


class Oeste(Orientacion):

    def ponerElementoEnPosicion(self,unEM,unaHabitacion):
        unaHabitacion.oeste = unEM

    def recorrerDesde(self, lista, unContenedor):
        lista.append(unContenedor.oeste)