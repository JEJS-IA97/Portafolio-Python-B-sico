import matplotlib.pyplot as plt

# Datos
num_servidores = [2, 3, 4, 5]
utilizacion_sistema = [86.67, 65.00, 52.00, 0]  # Utilización para cada número de servidores (%)

# Gráfico de barras
plt.figure(figsize=(8, 6))
plt.bar(num_servidores, utilizacion_sistema, color='skyblue')
plt.xlabel('Número de Servidores')
plt.ylabel('Utilización del Sistema (%)')
plt.title('Utilización del Sistema con Diferentes Números de Servidores')
plt.xticks(num_servidores)
plt.ylim(0, 100)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Guardar como PNG sin fondo
plt.savefig('grafico_utilizacion_sistema.png', transparent=True)
plt.show()
