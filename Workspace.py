from Juego import Juego
from JuegoBombas import JuegoBombas
from LaberintoFactory import LaberintoFactory


# --------------------------------|
# Código para probar el laberinto |
# --------------------------------|

# Codigo de prueba práctica 1

"""
juego = Juego()
juego.fabricarLaberinto2HabFM()
juego.laberinto.entrar()
juego.laberinto.habitaciones[1].entrar()
juego.laberinto.habitaciones[1].sur.entrar()

print()
juego.fabricarLaberinto2HabFM()
juego.laberinto.entrar()
juego.laberinto.habitaciones[0].norte.entrar()
juego.laberinto.habitaciones[1].entrar()

print()

print("¿Es h2 una habitación?", juego.laberinto.habitaciones[1].esHabitacion())
print("¿Es bomba el norte de h1?", juego.laberinto.habitaciones[0].norte.esBomba())
print("¿Es pared el este de h2?", juego.laberinto.habitaciones[1].este.esPared())
print("¿Es puerta el norte de h2?", juego.laberinto.habitaciones[1].norte.esPuerta())

print()

juego.laberinto.habitaciones[0].norte.activa = True
juego.laberinto.habitaciones[0].norte.entrar()
"""

# Codigo de prueba práctica 2

"""
juego = Juego()
juego.fabricarLaberinto4HabFM()
juego.laberinto.entrar()

juego.laberinto.habitaciones[1].entrar()
juego.laberinto.habitaciones[2].entrar()
juego.laberinto.habitaciones[3].entrar()

juego.laberinto.habitaciones[1].sur.entrar()

print("¿Es Bicho perezoso?", juego.bichos[0].esPerezoso())
print("¿Es Bicho agresivo?", juego.bichos[1].esAgresivo())
print("¿Es Bicho perezoso?", juego.bichos[2].esPerezoso())
print("¿Es Bicho agresivo?", juego.bichos[3].esAgresivo())"""

# Codigo de prueba práctica 3 (Patrón Composite)

"""juego = Juego()
juego.fabricarLaberinto4HabArm()
juego.laberinto.entrar()
juego.laberinto.habitaciones[0].hijos[0].entrar()
print("¿Es el hijo 0 de la habitacion un armario?", juego.laberinto.habitaciones[0].hijos[0].esArmario())
print("¿Es el hijo 1 de la habitacion una bomba?", juego.laberinto.habitaciones[0].hijos[1].esBomba())"""

# Codigo de prueba práctica 4 (Iterator y Template Method)

"""juego = Juego()
juego.fabricarLaberinto4HabArm()
juego.abrirPuertas()
juego.lanzarHilosBichos()
juego.cerrarPuertas()
juego.terminarHilosBichos()"""

# Código de prueba práctica 5 (AbstractFactory y Singleton)

juego = Juego()
unaFactoria = LaberintoFactory()
juego.fabricarLaberinto4HabArmAF(unaFactoria)
juego.abrirPuertas()
orientaciones = []


def funciona():

    if id(or1) == id(or2) == id(or3) == id(or4):
        print("Singleton funciona, todas las variables contienen la misma instancia")
    else:
        print("Singleton ha fallado, las variable no tienen la misma instancia")


or1 = juego.laberinto.habitaciones[0].orientaciones[0]
or2 = juego.laberinto.habitaciones[1].orientaciones[0]
or3 = juego.laberinto.habitaciones[2].orientaciones[0]
or4 = juego.laberinto.habitaciones[3].orientaciones[0]

funciona()

or1 = juego.laberinto.habitaciones[0].orientaciones[1]
or2 = juego.laberinto.habitaciones[1].orientaciones[1]
or3 = juego.laberinto.habitaciones[2].orientaciones[1]
or4 = juego.laberinto.habitaciones[3].orientaciones[1]

funciona()

or1 = juego.laberinto.habitaciones[0].orientaciones[2]
or2 = juego.laberinto.habitaciones[1].orientaciones[2]
or3 = juego.laberinto.habitaciones[2].orientaciones[2]
or4 = juego.laberinto.habitaciones[3].orientaciones[2]

funciona()

or1 = juego.laberinto.habitaciones[0].orientaciones[3]
or2 = juego.laberinto.habitaciones[1].orientaciones[3]
or3 = juego.laberinto.habitaciones[2].orientaciones[3]
or4 = juego.laberinto.habitaciones[3].orientaciones[3]

funciona()












