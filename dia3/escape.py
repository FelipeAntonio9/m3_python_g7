# import math
from math import sqrt

# paso 1
# capturar y almacenar dato ingresado por el usuario
radio = input("Ingrese el radio en Kilómetros:\n")
# 6371 -> "6371"

# paso 2
# transformar string a numero
radio = float(radio)  # la funcion float(), transforma un string a float
# radio = float("6371") -> radio = 6371

# paso 3
# transformar kilometros a metros (multiplicar por 1000)
radio = radio * 1000  # radio = 6371 * 1000 -> radio = 6371000

# paso 1 para g
constante_gravitacional = input("Ingrese la constante gravitacional: ")
# 9.8 -> "9.8"
# paso 2
# transformar string a numero(float)
constante_gravitacional = float(constante_gravitacional)
# constante_gravitacional = float("9.8") -> constante_grativacional = 9.8

# calculo formula V𝑒 = √2𝑔r
multiplicacion = 2 * constante_gravitacional * radio

velocidad_escape = sqrt(multiplicacion)

print(f"La velocidad de Escape es {round(velocidad_escape, 1)} [m/s]")
