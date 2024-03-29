"""
CICLO FOR
for variable in iterable:
"""
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in range(10):  # el valor 10 no será considerado
    print(i)
print("")
# [4,5,6,7,8,9]
for i in range(4, 10, 1):
    print(i)
""" for en javascript
for (let index = 4; index < 10; index++) {
    console.log(index);
}
"""
print("")
# Lista
numeros = [2, "4", True, 3, "5", [2, 5, 8], {"clave": "valor"}]
for numero in numeros:
    print(numero)
print("")
# String-> son similares a las listas
print("")
texto = "Hola Mundo"
for caracter in texto:
    print(caracter)
print("")

# Diccionario, se compone de elementos(clave:valor)
datos_personales = {
    "Nombre": "Israel",
    "Apellido": "Palma",
    "Edad": 44,
}
# imprime las claves
for clave in datos_personales:
    print(clave)
print("")

# imprime los valores
for clave in datos_personales:
    print(datos_personales[clave])

print("")
# imprime clave, valor
for clave, valor in datos_personales.items():
    print(f"clave: {clave} - valor: {valor}")

print("")
for par in datos_personales.items():
    print(par)

print("")
for clave in datos_personales.keys():
    print(valor)

print("")
for valor in datos_personales.values():
    print(valor)

# ENUMERATE
print("")
for posicion, caracter in enumerate(texto):
    print(f"la posicion {posicion} del caracter {caracter}")

print("")
for posicion, numero in enumerate(numeros):
    print(f"la posicion {posicion} del numero {numero}")

print("")

prefijo = ['La', 'El', 'La', 'El', 'Los']
frutas = ['manzana', 'platano', 'frutilla', 'tomate']
colores = ['verde', 'amarillo', 'roja', 'rojo']
for p, fruta, color in zip(prefijo, frutas, colores):
    print(f'{p} {fruta} es de color {color}')

print("")

# BREAK
numeros = [2, "4", True, 3, "5", [2, 5, 8], {"clave": valor}]
for numero in numeros:
    print(numero)
    if numero == 3:
        break

print("fuera del for")
