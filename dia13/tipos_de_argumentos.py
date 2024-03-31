precios = {'Notebook': 700000, # SE CREA UN DICCIONARIO CON ELEMENTOS Y SE GUARDA EN VARIABLE precios
'Teclado': 25000,
'Mouse': 12000,
'Monitor': 250000,
'Escritorio': 135000,
'Tarjeta de Video': 1500000}

def filtrar(diccionario, umbral): # SE CREA MÉTODO filtrar CON PARÁMETOS (diccionario, umbral)
    filtro = {k:v for k,v in diccionario.items() if v > umbral} #PYTHON COMPREHENSION GUARDADO EN VARIABLE filtro
    return filtro
filtrar(precios, 12000) # AL MÉTODO SE LE ASIGNA COMO ARGUMENTO LA VARIABLE precios EN EL PARÁMETRO DICCIONARIO Y AL 12000 COMO ARGUMENTO AL PARÁMETRO umbral

# *args
def funcion_tuplas(*parametros):  # EN EL PARÁMETRO PUEDE SER CUALQUIER NOMBRE ESO SI, CON EL ASTERISCO AL PRINCIPIO
    print(parametros) # (1, [2, 3], 'hola', {'clave': [4]})
    return parametros
output = funcion_tuplas(1,[2,3],'hola',{'clave':[4]})
print(type(output))# <class 'tuple'>

# EN RESUMEN CON *ARGS PUEDES PASAR ELEMENTOS INDETERMINADOS QUE SE PUEDEN TRABAJAR INTERNAMENTE COMO UNA TUPLA

# **kwargs
def funcion_dicc(**parametros): # EN EL PARÁMETRO PUEDE SER CUALQUIER NOMBRE ESO SI, CON EL ASTERISCO AL PRINCIPIO
    print(parametros) # {'valor': 1, 'texto': 'hola', 'lista_nombres': [4, 5, 6, 7]}
    return parametros
output = funcion_dicc(valor = 1, texto = 'hola', lista_nombres = [4,5,6,7])
print(type(output))# <class 'dict'>

# EN RESUMEN ON *KWARGS PUEDES PASAR ARGUMENTOS ESPECIFICADOS POR NOMBRES PARA TRABAJAR CON DICCIONARIO