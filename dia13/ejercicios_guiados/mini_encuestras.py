"""preguntas = ['Enunciado Pregunta 1','Enunciado Pregunta 2','Enunciado Pregunta 3']

respuestas = []

# Hacer preguntas
print(preguntas[0])
print('Opciones: ')
print('1). De acuerdo')
print('2). En desacuerdo')
print('3). No me interesa')
respuestas.append(input('> '))

print(preguntas[1])
print('Opciones: ')
print('1). De acuerdo')
print('2). En desacuerdo')
print('3). No me interesa')
respuestas.append(input('> '))

print(preguntas[2])
print('Opciones: ')
print('1). De acuerdo')
print('2). En desacuerdo')
print('3). No me interesa')
respuestas.append(input('> '))

print(f'La respuesta a la pregunta 1 fue {respuestas[0]}')
print(f'La respuesta a la pregunta 2 fue {respuestas[1]}')
print(f'La respuesta a la pregunta 3 fue {respuestas[2]}')
print('Muchas gracias por responder la encuesta')
"""

# PRINCIPIO DE DRY APLICADO
def imprimir_menu():
    print('Opciones: ')
    print('1). De acuerdo')
    print('2). En desacuerdo')
    print('3). No me interesa')
preguntas = ['Enunciado Pregunta 1', 'Enunciado Pregunta 2','Enunciado Pregunta 3']
respuestas = []
# Hacer preguntas
for p in preguntas:
    print(p)
    imprimir_menu()
    respuestas.append(input('> '))
    
print(f'La respuesta a la pregunta 1 fue {respuestas[0]}')
print(f'La respuesta a la pregunta 2 fue {respuestas[1]}')
print(f'La respuesta a la pregunta 3 fue {respuestas[2]}')
print('Muchas gracias por responder la encuesta')