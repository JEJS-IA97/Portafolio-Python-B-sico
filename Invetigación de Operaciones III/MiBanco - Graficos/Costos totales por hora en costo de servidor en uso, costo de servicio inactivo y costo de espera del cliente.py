import matplotlib.pyplot as plt

# Datos
num_servidores = [2, 3, 4, 5]
costo_servidor_uso = [19.26, 19.26, 19.26, 19.26]  # Costo de servidor en uso por hora (S/.)
costo_servicio_inactivo = [2.96, 10.37, 17.78, 0]  # Costo de servicio inactivo por hora (S/.)
costo_espera_cliente = [237.07, 31.63, 7.73, 0]  # Costo de espera del cliente por hora (S/.)

# Gráfico de barras apiladas
plt.figure(figsize=(10, 6))
plt.bar(num_servidores, costo_servidor_uso, color='skyblue', label='Costo de Servidor en Uso')
plt.bar(num_servidores, costo_servicio_inactivo, color='orange', bottom=costo_servidor_uso, label='Costo de Servicio Inactivo')
plt.bar(num_servidores, costo_espera_cliente, color='green', bottom=[i+j for i,j in zip(costo_servidor_uso, costo_servicio_inactivo)], label='Costo de Espera del Cliente')
plt.xlabel('Número de Servidores')
plt.ylabel('Costo por Hora (S/.)')
plt.title('Desglose de Costos Totales por Hora')
plt.xticks(num_servidores)
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Guardar como PNG sin fondo
plt.savefig('grafico_costos.png', transparent=True)
plt.show()
