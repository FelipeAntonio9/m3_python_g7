def sumar(x,y):
    """imprimir la suma de dos numeros

    Args:
        x (float): primer numero
        y (float): segundo numero
    """
    print(f"El resultado de la suma es  {x+y}")
    
    
# LO QUE ESTÉ BAJO ESTA VALIDACIóN SE VA A GATILLAR ÚNICA Y EXCLUSIVAMENTE CUANDO SE EJECUTE EL ARCHIVO
# Y PARA QUÉ HACEMOS ESTO? PARA PROBAR NUESTRO CÓDIGO
if __name__ == "__main__":
    print("Probando el metodo sumar")
    sumar(4,6)
    sumar(1,2)