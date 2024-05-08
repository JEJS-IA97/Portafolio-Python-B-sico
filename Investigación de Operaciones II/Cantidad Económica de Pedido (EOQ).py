import math

def calcular_eoq(demanda_anual, costo_pedido, costo_mantenimiento):
    # Cálculo del EOQ
    eoq = math.sqrt((2 * demanda_anual * costo_pedido) / costo_mantenimiento)
    return eoq

def calcular_costo_total(eoq, demanda_anual, costo_pedido, costo_mantenimiento):
    # Cálculo del costo total
    costo_total = (costo_pedido * demanda_anual) / eoq + (eoq * costo_mantenimiento) / 2
    return costo_total

def main():
    # Entrada de datos
    demanda_anual = float(input("Ingrese la demanda anual: "))
    costo_pedido = float(input("Ingrese el costo de pedido: "))
    costo_mantenimiento = float(input("Ingrese el costo de mantenimiento unitario: "))

    # Cálculo del EOQ y costo total
    eoq = calcular_eoq(demanda_anual, costo_pedido, costo_mantenimiento)
    costo_total = calcular_costo_total(eoq, demanda_anual, costo_pedido, costo_mantenimiento)

    # Resultados
    print("Cantidad Económica de Pedido (EOQ):", eoq)
    print("Costo Total Anual (CTA):", costo_total)

if __name__ == "__main__":
    main()
