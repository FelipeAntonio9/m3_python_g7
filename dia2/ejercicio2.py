# division de enteros, resulta un float
print(10/20)
print(10 + 2.5)
print(10 - 3.5)
print(10 * 3.5)

# STRING -> cadena de caracteres
nombre = 'isra'
edad = 44
print('a123124 _-!."!!%&')
print(edad)  # imprimir el contenido de la variable
print("tu edad es")
numero = 100
# duplicacion
print(type(edad))
print(3*edad)  # edad edad edad
print(3*edad)  # 444444

print(type(numero))  # <class 'int'>
print(3*numero)  # 300

# metodo count() y len()
print("21.384.060-6".count("."))  # 2
print(len("13.955.160-5"))  # 12
# print(len(123456789))#TypeError: object of type 'int' has no len()

# metodo upper()mayuscula y lower()minuscula
print("KaKaRoTo".upper())  # KAKAROTO
print("KaKaRoTo".lower())  # kakaroto
print("KaKaRoTo ".title())  # Kakaroto

# join -> unir elementos separados
print(", ".join(["a", "b", "c"]))

# Tipo de Datos
entero = 7
decimal = 9.5
cadena = " esto es una cadena"
booleanos = True

print(type(entero))  # <class 'int'>
print(type(decimal))  # <class 'float'>
print(type(cadena))  # <class 'str'>
print(type(booleanos))  # <class 'bool'>

numero2 = 200
numero2 = numero2 + 100  # numero2 = 200 + 100

texto = "asd"
texto = texto + "qwe"  # texto = "asdqwe"

# precision de datos
promedio = (4+6+7)/3
print(f"el promedio es {promedio}")

print(f"resulta de la division {promedio:.4f}")
print(f"resulta de la division {round(promedio, 3)}")

# Ingreso de datos (INPUT)
nombre = input("Ingrese su nombre:\n")
edad = input("Ingrese su edad:\n")

print(f"Tu nombre es {nombre}")
print(f"Tu edad es {edad}")
print(type(edad))  # <class 'str'>

input("ingresa tu apellido")
