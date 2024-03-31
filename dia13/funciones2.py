PI=3.14 #CONSTANTE
IVA=19 #CONSTANTE

suma=4 #variable global

def sumar(numero1,numero2):
    #variable local
    #global suma -> CON ESTO SE PUEDE USAR LA VARIABLE GLOBAL DENTRO Y SERÁ SOBREESCRITO POR LA VARIABLE DE ABAJO
    suma = numero1 + numero2              # NO ES NECESARIO HACER ESTAR OPERATORIA
    return numero1 + numero2# return 33   # CUANDO CON RETURN PUEDE HACERSE Y ASÍ AHORRARSE CÓDIGO GUARDANDOLA EN UNA VARIABLE

#llamado a la función
sumar(14,15)

#imprimir el valor de retorno
print(sumar(15,16))# print(31) -> 31 en consola

#capturar el valor de retorno
valor_retorno = sumar(16,17) # LLAMAMOS EL MÉTODO "SUMAR" QUE AL SUMAR DA 33 Y ESE VALOR LO GUARDAMOS EN LA VARIABLE valor_retorno
print(valor_retorno) #LA IMPRIMIMOS 33

print(suma) #imprimiendo variable global


# MÚLTIPLES RETORNOS

def cuadrado_cubo(base): # SE CREA MÉTODO LLAMADO cuadrado_cubo CON PARÁMETRO (base)
    cuadrado = base**2   # LA BASE INGRESADA SE ELEVA A 2 Y SE GUARDA EN VARIABLE cuadrado
    cubo = base**3       # LA BASE INGRESADA SE ELEVA A 3 Y SE GUARDA EN VARIABLE cubo
    return cuadrado, cubo# RETURN cuadrado Y cubo

print(cuadrado_cubo(2))  # IMPRIME EL MÉTODO AGINANDOLE COMO PARÁMETRO 2
# IMPRIMIRÁ: (4,8)

valor_cuadrado, valor_cubo =  cuadrado_cubo(2) # SE PUEDEN DECLARAR 2 VARIABLES GRACIAS AL RETURN Y GUARDAR EL RESULTADO DE LOS MÉTODOS EN ELLOS
print(valor_cuadrado)
print(valor_cubo)
