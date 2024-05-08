import matplotlib.pyplot as plt

# Datos
num_servidores = [2, 3, 4, 5]
costo_total_hora = [259.30, 61.27, 44.78, 0]  # Costo total por hora para cada número de servidores (S/.)

# Gráfico de barras
plt.figure(figsize=(8, 6))
plt.bar(num_servidores, costo_total_hora, color='orange')
plt.xlabel('Número de Servidores')
plt.ylabel('Costo Total por Hora (S/.)')
plt.title('Costo Total por Hora con Diferentes Números de Servidores')
plt.xticks(num_servidores)
plt.ylim(0, max(costo_total_hora) * 1.1)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Guardar como PNG sin fondo
plt.savefig('grafico_costo_total.png', transparent=True)
plt.show()
