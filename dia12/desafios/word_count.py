"""
Grupo1:
Felipe Arias
Najla Gatica
Lolett Llanquinao
Jimena Traipe
"""

#Desafío - Estructuras de datos y funciones (I)
#Actividad 2

#Exportamos el archivo de texto
with open("dia12/desafios/lorem_ipsum.txt", "r") as file: #la r es de read para la lectura del archivo
    texto = file.read()

#Cantidad de caracteres distintos
caracteres_distintos = len(set(texto)) 
#con set contamos caracteres o palabras únicas
#len nos da la cantidad total de los elementos únicos

#Cantidad de palabras distintas
palabras = texto.split(" ") #divide la cadena en una lista de palabras, usa el espacio en blanco como delimitador
palabras_distintas = len(set(palabras))

print("")

# Mostramos el texto y los resultados
print("Texto Lorem Ipsum:")
print(texto)
print("Cantidad de caracteres distintos:", caracteres_distintos)
print("Cantidad de palabras distintas:", palabras_distintas)