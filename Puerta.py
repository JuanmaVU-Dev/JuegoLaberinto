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

    def esPuerta(self):
        return True
