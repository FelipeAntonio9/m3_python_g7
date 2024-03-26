# Adicto a redes

minutos_usados = [120, 50, 600, 30, 90, 10, 200, 0, 500]
clasificacion = ['mal' if tiempo >= 90 else 'bien' for tiempo in minutos_usados]
print(clasificacion)
