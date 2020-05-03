from Contenedor import Contenedor


class Armario(Contenedor):

    def __init__(self):
        super().__init__()
        self.num = None
        self.norte = None
        self.sur = None
        self.este = None
        self.oeste = None

        # Metodos
    def entrar(self):
        print("Estás en el armario: ", self.num)

    def entrarAlguien(self, alguien):
        print("Estás en el armario: ", self.num)
        alguien.posicion = self

    def esArmario(self):
        return True
