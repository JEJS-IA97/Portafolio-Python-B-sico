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
    while True:
        lambd = float(input("Ingrese la tasa media de llegada (λ): "))
        mu = float(input("Ingrese la tasa media de servicio (μ): "))
        s = int(input("Ingrese el número de servidores (s): "))
        
        rho = calcular_rho(lambd, mu, s)
        print("ρ (ro):", rho)
        
        if rho > 1:
            print("No se puede proceder a calcular la probabilidad con el valor de s ingresado.")
            continuar = input("¿Desea agregar otro valor a s? (s/n): ")
            if continuar.lower() != 's':
                break
        else:
            p0 = calcular_p0(lambd, mu, s, rho)
            print("La probabilidad de que no hayan clientes en la cola es:", '{:.10f}'.format(p0))
            
            lq = calcular_lq(p0, lambd, mu, s, rho)
            print("La cantidad de clientes esperados en la cola es:", '{:.10f}'.format(lq))
            
            l = calcular_l(lq, lambd, mu)
            print("Por lo tanto La cantidad de clientes esperados en el sistema es:", '{:.10f}'.format(l))
            
            costo_total = calcular_costo_total(s, l)
            print("El costo total es:", costo_total)
            
            respuesta = input("¿Desea calcular con otra cantidad de servidores? (s/n): ")
            if respuesta.lower() != 's':
                break

if __name__ == "__main__":
    main()


