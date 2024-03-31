#imprimir_menu() AQUI NO FUNCIONARÁ

def imprimir_menu():
    print('Opciones: ')
    print('1). De acuerdo') # PUEDES MODIFICAR EL CÓDIGO Y EL CAMBIO ES PARA TODAS LAS INVOCACIONES (SE LE AGREGÓ UN PUNTO)
    print('2). En desacuerdo')
    print('3). No me interesa')
    
# SI USTED NO INVOCA LA FUNCIÓN, ES UN CÓDIGO MUERTO QUE NO HACE NADA
# PARA LLAMARLA SE LLAMA POR EL NOMBRE imprimir_menu()
# LLAMADO O INVOCACIÓN
#imprimir_menu()
# SE EJECUTA EL LA FUNCIÓN CUANDO SE HAYA DEFINIDO EL CÓDIGO PRIMERO

# SE PUEDE EJECUTAR CUANTAS VECES SE QUIERA
#imprimir_menu()
#imprimir_menu()
#imprimir_menu()
# ES OBLIGATORIO PONER PARENTESIS LUEGO DEL NOMBRE PARA QUE SE INTERPRETE COMO FUNCIÓN

# SE PUEDE CREAR UNA FUNCIÓN PARA IMPRIMIR RESPUESTAS
def imprimir_respuestas():
    """print(f'La respuesta a la pregunta 1 fue {respuestas[0]}')
    print(f'La respuesta a la pregunta 2 fue {respuestas[1]}')
    print(f'La respuesta a la pregunta 3 fue {respuestas[2]}')
    """
    """for i in range(len(respuestas)):#[0,1,2] len()=3 
        print(f'La respuesta a la pregunta {i+1} fue {respuestas[i]}')
    """
    for posicion, respuesta in enumerate(respuestas):#[0,1,2] len()=3
        print(f'La respuesta a la pregunta {posicion+1} fue {respuesta}')
    
        

preguntas = ['Enunciado Pregunta 1', 'Enunciado Pregunta 2','Enunciado Pregunta 3','Enunciado Pregunta 4']
respuestas = []
# Hacer preguntas 
for pregunta in preguntas:
    print(pregunta)
    #llamado o invocacion
    imprimir_menu()
    respuestas.append(input('> '))
    print("")
    
print("")
imprimir_respuestas()
