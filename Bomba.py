from Decorator import Decorator


class Bomba(Decorator):

    def __init__(self):
        self.activa = False

    def entrar(self):
        if self.activa:
            print("La bomba ha explotado, has muerto")
        else:
            self.componente.entrar()

    def esBomba(self):
        return True
