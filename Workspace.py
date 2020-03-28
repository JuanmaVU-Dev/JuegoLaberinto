from Juego import Juego
from JuegoBombas import JuegoBombas

# --------------------------------|
# Código para probar el laberinto |
# --------------------------------|

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
