def calcular_costo_acumulado():
    print("Cálculo del costo acumulado de inversión")
    print("")

    inversion_inicial = float(input("Ingrese la inversión inicial: "))
    años = int(input("Ingrese la cantidad de años: "))

    costo_funcionamiento = []
    valor_salvamento = []

    # Recopilación de datos de costos de funcionamiento y valores de salvamento para cada año
    for i in range(años):
        cf = float(input(f"Ingrese el costo de funcionamiento para el año {i + 1}: "))
        costo_funcionamiento.append(cf)
        vs = float(input(f"Ingrese el valor de salvamento para el año {i + 1}: "))
        valor_salvamento.append(vs)

    # Verificación de la tasa de interés
    tasa_interes = float(input("Ingrese la tasa de interés: ")) if input("¿Posee una tasa de interés? (S/N): ").upper() == "S" else 0

    # Cálculos e impresión de resultados para cada año
    for i in range(años):
        ci = inversion_inicial - valor_salvamento[i]
        sumacf = sum(costo_funcionamiento[:i + 1])
        cpi = ci / (i + 1)
        cpf = cpi / (i + 1)
        cpt = cpi + cpf

        print()
        print(f"Para el año {i + 1}:")
        print(f"Costo de Inversión = {ci:.0f}")
        print(f"Sumatoria Costo de Funcionamiento = {sumacf:.0f}")
        print(f"Costo Promedio de Inversión = {cpi:.0f}")
        print(f"Costo Promedio de Funcionamiento = {cpf:.0f}")
        print(f"Costo Promedio Total = {cpt:.0f}")

        if tasa_interes > 0:
            print(f"Valor Presente = {costo_funcionamiento[i] / ((1 + tasa_interes) ** (i + 1)):.2f}")
            print(f"Costo de Inversión = {inversion_inicial - costo_funcionamiento[i] / ((1 + tasa_interes) ** (i + 1)):.2f}")

        print()

calcular_costo_acumulado()

