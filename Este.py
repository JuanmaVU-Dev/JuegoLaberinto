from Orientacion import Orientacion


class Este(Orientacion):

    def ponerElementoEnPosicion(self,unEM,unaHabitacion):
        unaHabitacion.este = unEM

    def recorrerDesde(self, lista, unContenedor):
        lista.append(unContenedor.este)