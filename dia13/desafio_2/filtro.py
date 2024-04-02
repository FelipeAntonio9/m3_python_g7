from sys import argv

precios = {'Notebook': 700000,
'Teclado': 25000,
'Mouse': 12000,
'Monitor': 250000,
'Escritorio': 135000,
'Tarjeta de Video': 1500000}

umbral = int(argv[1])

def filtrar (precios, umbral, mayor_que = True):
    if mayor_que:
        filtro = [producto for producto in precios if precios[producto] > umbral]
        print(f"Los productos mayores al umbral son: {', '.join(filtro)}")
    else:
        filtro = [producto for producto in precios if precios[producto] < umbral]
        print(f"Los productos menores al umbral son: {', '.join(filtro)}")
    
#python dia13/desafio_2/filtro.py 30000
if len(argv) == 2:
    filtrar(precios,umbral)
else:
    #python dia13/desafio_2/filtro.py 30000 menor/mayor
    if argv[2].lower() == "mayor":
        filtrar(precios,umbral)
    elif argv[2].lower() == "menor":
        filtrar(precios,umbral, False)
    else:
        print("Lo sentimos, no es una operación válida")
