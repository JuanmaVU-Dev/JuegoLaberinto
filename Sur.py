from Orientacion import Orientacion


class Sur(Orientacion):

    def ponerElementoEnPosicion(self,unEM,unaHabitacion):
        unaHabitacion.sur = unEM

    def recorrerDesde(self, lista, unContenedor):
        lista.append(unContenedor.sur)