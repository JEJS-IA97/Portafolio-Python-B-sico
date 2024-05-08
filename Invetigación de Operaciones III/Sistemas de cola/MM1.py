def calcular_rho(lambd, mu):
    return lambd / mu

def calcular_p0(lambd, mu, rho):
    return 1 - rho

def calcular_lq(rho):
    return (rho**2) / (1 - rho)

def calcular_l(lq, rho):
    return lq + rho

def calcular_costo_total(l, c):
    return l * c

def main():
    while True:
        lambd = float(input("Ingrese la tasa media de llegada (λ): "))
        mu = float(input("Ingrese la tasa media de servicio (μ): "))
        c = float(input("Ingrese el costo por unidad de tiempo del sistema (c): "))
        
        rho = calcular_rho(lambd, mu)
        print("ρ (ro):", rho)
        
        if rho >= 1:
            print("El sistema es inestable ya que ρ >= 1. No se pueden realizar cálculos para el sistema M/M/1.")
            continuar = input("¿Desea agregar otro valor para λ o μ? (s/n): ")
            if continuar.lower() != 's':
                break
        else:
            p0 = calcular_p0(lambd, mu, rho)
            print("La probabilidad de que no haya clientes en el sistema es:", '{:.10f}'.format(p0))
            
            lq = calcular_lq(rho)
            print("La cantidad de clientes esperados en la cola es:", '{:.10f}'.format(lq))
            
            l = calcular_l(lq, rho)
            print("La cantidad de clientes esperados en el sistema es:", '{:.10f}'.format(l))
            
            costo_total = calcular_costo_total(l, c)
            print("El costo total es:", costo_total)
            
            respuesta = input("¿Desea calcular con otros valores de λ, μ o c? (s/n): ")
            if respuesta.lower() != 's':
                break

if __name__ == "__main__":
    main()
