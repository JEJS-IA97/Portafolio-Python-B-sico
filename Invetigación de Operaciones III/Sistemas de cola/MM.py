def calcular_rho(lambd, mu, s):
    return lambd / (s * mu)

def calcular_p0(lambd, mu, s, rho):
    suma = sum(((lambd / mu) ** n) / factorial(n) for n in range(s))
    suma += ((lambd / mu) ** s) / factorial(s) * (1 / (1 - rho))
    return 1 / suma

def calcular_lq(p0, lambd, mu, s, rho):
    return (p0 * ((lambd / mu) ** s) * rho) / (factorial(s) * (1 - rho) ** 2)

def calcular_l(lq, lambd, mu):
    return lq + lambd / mu

def calcular_costo_total(s, l):
    return 20 * s + 48 * l

def factorial(n):
    return 1 if n == 0 else n * factorial(n-1)

def main():
    resultados = []  # Lista para almacenar los resultados para cada configuración de servidores

    while True:
        lambd = float(input("Ingrese la tasa media de llegada (λ): "))
        mu = float(input("Ingrese la tasa media de servicio (μ): "))
        servidores = [int(input(f"Ingrese el número de servidores para el caso {i + 1}: ")) for i in range(5)]
        
        for s in servidores:
            rho = calcular_rho(lambd, mu, s)
            print(f"\nResultados para {s} servidor(es):")
            print("ρ (ro):", rho)
            
            if rho > 1:
                print("No se puede proceder a calcular la probabilidad con el valor de s ingresado.")
                continue
            
            p0 = calcular_p0(lambd, mu, s, rho)
            print("La probabilidad de que no hayan clientes en la cola es:", '{:.10f}'.format(p0))
            
            lq = calcular_lq(p0, lambd, mu, s, rho)
            print("La cantidad de clientes esperados en la cola es:", '{:.10f}'.format(lq))
            
            l = calcular_l(lq, lambd, mu)
            print("La cantidad de clientes esperados en el sistema es:", '{:.10f}'.format(l))
            
            costo_total = calcular_costo_total(s, l)
            print("El costo total es:", costo_total)
            
            resultados.append({
                "Servidores": s,
                "Rho": rho,
                "Probabilidad sin clientes en la cola": p0,
                "Clientes esperados en la cola": lq,
                "Clientes esperados en el sistema": l,
                "Costo total": costo_total
            })

        respuesta = input("\n¿Desea ingresar otros valores para λ y μ? (s/n): ")
        if respuesta.lower() != 's':
            break

    print("\nResultados para cada configuración de servidores:")
    for resultado in resultados:
        print(f"\nResultados para {resultado['Servidores']} servidor(es):")
        print("ρ (ro):", resultado['Rho'])
        print("La probabilidad de que no hayan clientes en la cola es:", '{:.10f}'.format(resultado['Probabilidad sin clientes en la cola']))
        print("La cantidad de clientes esperados en la cola es:", '{:.10f}'.format(resultado['Clientes esperados en la cola']))
        print("La cantidad de clientes esperados en el sistema es:", '{:.10f}'.format(resultado['Clientes esperados en el sistema']))
        print("El costo total es:", resultado['Costo total'])

if __name__ == "__main__":
    main()
