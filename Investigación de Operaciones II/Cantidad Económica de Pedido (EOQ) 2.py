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
    tiempo_espera = float(input("Ingrese el tiempo de espera de reabastecimiento: "))

    # Cálculo del EOQ y costo total
    y_opt = calcular_eoq(demanda_anual, costo_pedido, costo_mantenimiento)
    costo_total = calcular_costo_total(y_opt, demanda_anual, costo_pedido, costo_mantenimiento)
    duracion_ciclo = y_opt / demanda_anual

    if tiempo_espera < duracion_ciclo:
        n = round(tiempo_espera / duracion_ciclo, 0)
        tiempo_espera_efectivo = tiempo_espera - (n * duracion_ciclo)
    else:
        tiempo_espera_efectivo = tiempo_espera - duracion_ciclo

    punto_reorden = tiempo_espera_efectivo * demanda_anual

    # Resultados
    print("Cantidad Económica de Pedido (EOQ):", y_opt)
    print("Costo Total Anual (CTA):", costo_total)
    print("Duración del ciclo (Lo):", duracion_ciclo)
    print("Punto óptimo de Reorden:", punto_reorden, "unidades")

if __name__ == "__main__":
    main()
