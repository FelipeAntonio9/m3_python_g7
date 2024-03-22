"""
while conicion:
    #codigo a ejecutar
    
"""
import getpass
"""
password = input("Ingrese su contraseña:\n")

while len(password) < 6:
    password = input(
        "Ingrese su contraseña con largo superior o igual a 6 caracteres:\n")

while password != "Hola Mundo":
    password = input(
        "no adivinaste la contraseña, Ingrese su contraseña nuevamente:\n")

print("Contraseña correcta")
# resto del programa
print("Fin del programa")
"""
# Iteracion
"""
i = 0
while i < 10:
    print(f"El valor de i es {i}")
    i += 1  # i = i + 1 incremento en 1

print(f"fuera del while, valor de i= {i}")
"""
"""
while True:
    print("acciones infinitas")
    if condicion:
    else:
        break # salir del bucle
"""
"""
saludo = "Hola"
saludo = saludo + " Mundo"
print(saludo)
saludo += "chao"
print(saludo)
"""
"""
numero_sumar = 1
i = 1
while i <= 100:
    print(i)
    numero_sumar += 1
    i += numero_sumar
print("Fin del programa")
"""

i = 1  # primer valor a sumar
suma = 0
while i <= 100:
    suma += i  # acumulamos para la suma
    i += 1  # incrementamos para sumar el siguiente valor

print(f"El resultado final es {suma}")
