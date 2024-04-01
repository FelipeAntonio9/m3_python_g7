precios = {'Notebook': 700000,
'Teclado': 25000,
'Mouse': 12000,
'Monitor': 250000,
'Escritorio': 135000,
'Tarjeta de Video': 1500000}

def filtrar(diccionario, umbral):
    filtro = {k:v for k,v in diccionario.items() if v > umbral}
    return filtro

filtrado = filtrar(precios, 30000)

resultado = ', '.join(filtrado)

print("")

print(f"Los productos mayores al umbral son: {resultado}")
