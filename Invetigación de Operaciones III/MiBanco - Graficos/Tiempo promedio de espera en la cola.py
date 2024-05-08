import matplotlib.pyplot as plt

# Datos
tiempo_espera = [5.39, 1.41, 0.25]  # Tiempo promedio de espera en la cola para cada hora (minutos)
hora_inicio = [3, 4, 5]  # Hora de inicio de cada intervalo de tiempo (3 pm, 4 pm, 5 pm)

# Gráfico de líneas
plt.figure(figsize=(8, 6))
plt.plot(hora_inicio, tiempo_espera, marker='o', color='green', linestyle='-')
plt.xlabel('Hora de Inicio')
plt.ylabel('Tiempo Promedio de Espera en la Cola (min)')
plt.title('Tiempo Promedio de Espera en la Cola de 3 pm a 6 pm')
plt.xticks(hora_inicio)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Guardar como PNG sin fondo
plt.savefig('grafico_tiempo_espera.png', transparent=True)
plt.show()
