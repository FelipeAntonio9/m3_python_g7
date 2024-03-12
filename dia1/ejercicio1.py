# esto es un comentario de una linea
"""
comentario 
de mas de
una linea
"""
print("texto a imprimir por consola")
print(2+2)
print(12-2)
print(2*2)
# print(2/0)  # ZeroDivisionError: divison by zero
print(20/10)  # el resultado siempre sera un float

numero = 23
print(numero)

# Limitantes
# No esta permitido la suma de letras y numeros
# print("texto"+12)  # TypeError: can only concatenate str (not "int") to str
print("texto", 12)
# concatenar = "texto"+12
print("texto"+"34")

# INTERPOLACION
nombre = "Mijail"
print(f"el numero es {nombre} \n y tu edad es {numero}")
print("Tu nombre es"+nombre)
# string.format
print("tu nombre es {} y tu edad es {}".format(nombre, numero))
# formato con %: %s para string y %d para numeros
print("Tu nombre es %s y tu edad es %d" % (nombre, numero))
# metodo con cadena
apellido = "palma loren"
print(apellido.title())
