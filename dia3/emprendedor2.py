precio_normal = int(input("Ingrese Precio de Suscripción Normal:\n"))
usuario_normal = int(input("Ingrese Número de Usuario Normal:\n"))
gastos_totales = int(input("Ingrese sus Gastos Totales:\n"))

resultado_normal = precio_normal * usuario_normal - gastos_totales

print(f"Su resultado normal es: {resultado_normal}")


precio_normal = int(input("Ingrese Precio de Suscripción Premium:\n"))
usuario_premium = int(input("Ingrese Número de Usuario Premium:\n"))
gastos_totales = int(input("Ingrese sus Gastos Totales:\n"))

precio_premium = precio_normal * 1.5
resultado_premium = precio_premium * usuario_premium - gastos_totales
print(f"El resultado premium es: {resultado_premium}")
