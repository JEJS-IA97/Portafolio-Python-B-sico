import matplotlib.pyplot as plt

# Datos de ejemplo
tiempo = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
temperatura_caliente = [20, 21, 23, 25, 27, 28, 29, 30, 30, 30, 30]
temperatura_fria = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
temperatura_deseada = 25

# Crear la figura y el gráfico
fig, ax = plt.subplots()

# Agregar las curvas al gráfico
ax.plot(tiempo, temperatura_caliente, label='Agua caliente')
ax.plot(tiempo, temperatura_fria, label='Agua fría')

# Agregar una línea horizontal para la temperatura deseada
ax.axhline(y=temperatura_deseada, color='r', linestyle='--', label='Temperatura deseada')

# Configurar los ejes
ax.set_xlabel('Tiempo (segundos)')
ax.set_ylabel('Temperatura (°C)')
ax.set_ylim([0, 35])

# Agregar títulos y etiquetas
ax.set_title('Ajuste de temperatura en la ducha')
ax.legend()

# Mostrar el gráfico
plt.show()
