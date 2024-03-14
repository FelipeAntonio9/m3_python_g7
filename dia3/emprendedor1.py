precio = int(input("Ingrese Precio de Suscripción:\n"))
usuarios = int(input("Ingrese Número de Usuarios:\n"))
gastos_totales = int(input("Ingrese sus Gastos Totales:\n"))

resultado = precio * usuarios - gastos_totales

print(f"El resultado es: {resultado}")
