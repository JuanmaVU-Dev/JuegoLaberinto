from ElementoMapa import ElementoMapa

"""
Decorator define la interfaz común para los objetos decoradores.
"""


class Decorator(ElementoMapa):

    def __init__(self):
        self.componente = None

    def entrar(self):
        raise Exception("Entrar no implementado")



