from ElementoMapa import ElementoMapa


class Bomba(ElementoMapa):

    def __init__(self):
        self.activa = False

    def entrar(self):
        if self.activa:
            print("La bomba ha explotado, has muerto")
        else:
            print("La bomba esta desactivada, no ha pasado nada")

    def esBomba(self):
        return True
