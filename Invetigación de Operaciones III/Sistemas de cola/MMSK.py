def calcular_rho(lambd, mu, s):
    return lambd / (s * mu)

def calcular_p0(lambd, mu, s, K):
    rho = calcular_rho(lambd, mu, s)
    if rho == 1:
        return 1 / (s + 1 - (s + 1) * (lambd / mu) ** s / factorial(s) / (1 - (lambd / mu) ** (K - s + 1)))
    else:
        suma_numerador = sum((lambd / mu) ** n / factorial(n) for n in range(s + 1))
        suma_denominador = sum((lambd / mu) ** n / factorial(n) for n in range(s, K + 1))
        return 1 / (1 + suma_numerador / factorial(s) / (1 - rho) + (lambd / mu) ** s / factorial(s) / (1 - rho) * suma_denominador)

def calcular_lq(p0, lambd, mu, s, K, rho):
    if rho == 1:
        return ((lambd / mu) ** s / factorial(s) / (1 - (lambd / mu) ** (K - s + 1))) * p0
    else:
        parte1 = (lambd / mu) ** (s + 1) / factorial(s) / (1 - rho)
        parte2 = (lambd / mu) ** s / factorial(s) / (1 - rho) * (1 - (lambd / mu) ** (K - s + 1)) / (1 - (lambd / mu) ** (K + 1))
        return parte1 * p0 + parte2

def calcular_l(lq, lambd, mu, K):
    return lq + lambd / mu * (1 - calcular_p0(lambd, mu, 1, K))

def calcular_costo_total(s, l):
    return 20 * s + 48 * l

def factorial(n):
    return 1 if n == 0 else n * factorial(n-1)

def main():
    while True:
        lambd = float(input("Ingrese la tasa media de llegada (λ): "))
        mu = float(input("Ingrese la tasa media de servicio (μ): "))
        s = int(input("Ingrese el número de servidores (s): "))
        K = int(input("Ingrese la capacidad del sistema (K): "))
        
        rho = calcular_rho(lambd, mu, s)
        print("ρ (ro):", rho)
        
        if rho >= 1:
            print("El sistema es inestable ya que ρ >= 1. No se pueden realizar cálculos para el sistema M/M/s/K.")
            continuar = input("¿Desea agregar otro valor para λ, μ, s o K? (s/n): ")
            if continuar.lower() != 's':
                break
        else:
            p0 = calcular_p0(lambd, mu, s, K)
            print("La probabilidad de que no haya clientes en el sistema es:", '{:.10f}'.format(p0))
            
            lq = calcular_lq(p0, lambd, mu, s, K, rho)
            print("La cantidad de clientes esperados en la cola es:", '{:.10f}'.format(lq))
            
            l = calcular_l(lq, lambd, mu, K)
            print("La cantidad de clientes esperados en el sistema es:", '{:.10f}'.format(l))
            
            costo_total = calcular_costo_total(s, l)
            print("El costo total es:", costo_total)
            
            respuesta = input("¿Desea calcular con otros valores de λ, μ, s o K? (s/n): ")
            if respuesta.lower() != 's':
                break

if __name__ == "__main__":
    main()
