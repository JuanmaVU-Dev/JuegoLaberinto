from ElementoMapa import ElementoMapa

"""
Puerta es un EM que une dos habitaciones.
"""


class Puerta(ElementoMapa):
    def __init__(self):
        self.abierta = False
        self.hab1 = None
        self.hab2 = None

    def entrar(self):
        if self.abierta:
            print("La puerta esta abierta.")
        else:
            print("La puerta esta cerrada.")

    def entrarAlguien(self, alguien):
            if self.abierta:
                if alguien.posicion == self.hab1:
                    self.hab2.entrarAlguien(alguien)
                else:
                    self.hab1.entrarAlguien(alguien)
            else:
                print("La puerta esta cerrada.")

    def abrir(self):
        if self.abierta:
            "La puerta ya esta abierta"
        else:
            print("Puerta abierta")
            self.abierta = True

    def cerrar(self):
        if not self.abierta:
            "La puerta ya esta cerrada"
        else:
            print("Puerta cerrada")
            self.abierta = False

    def esPuerta(self):
        return True
