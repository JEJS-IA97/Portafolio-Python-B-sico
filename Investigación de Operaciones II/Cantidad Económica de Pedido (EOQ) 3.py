import math
import matplotlib.pyplot as plt

def calcular_eoq(demanda_anual, costo_pedido, costo_mantenimiento):
    # Cálculo del EOQ
    eoq = math.sqrt((2 * demanda_anual * costo_pedido) / costo_mantenimiento)
    return eoq

def calcular_costo_total(eoq, demanda_anual, costo_pedido, costo_mantenimiento):
    # Cálculo del costo total
    costo_total = (costo_pedido * demanda_anual) / eoq + (eoq * costo_mantenimiento) / 2
    return costo_total

# Entrada de datos
while True:
    try:
        demanda_anual = float(input("Ingrese la demanda anual: "))
        costo_pedido = float(input("Ingrese el costo de pedido: "))
        costo_mantenimiento = float(input("Ingrese el costo de mantenimiento unitario: "))
        if demanda_anual <= 0 or costo_pedido <= 0 or costo_mantenimiento <= 0:
            print("Error: los valores ingresados deben ser mayores a cero.")
        else:
            break
    except ValueError:
        print("Error: se deben ingresar valores numéricos.")

# Cálculo del EOQ y costo total
eoq = calcular_eoq(demanda_anual, costo_pedido, costo_mantenimiento)
costo_total = calcular_costo_total(eoq, demanda_anual, costo_pedido, costo_mantenimiento)

# Creación de la gráfica de costo contra cantidad de unidades ordenadas
q = range(1, int(demanda_anual) + 1)
costos = [calcular_costo_total(qi, demanda_anual, costo_pedido, costo_mantenimiento) for qi in q]

plt.plot(q, costos)
plt.title("Curva de costo total")
plt.xlabel("Cantidad de unidades ordenadas")
plt.ylabel("Costo total")
plt.show()

# Resultados
print("Cantidad Económica de Pedido (EOQ):", round(eoq, 2))
print("Costo Total Anual (CTA):", round(costo_total, 2))
