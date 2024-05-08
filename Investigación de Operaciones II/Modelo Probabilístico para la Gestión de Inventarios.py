import numpy 
import math
import scipy.integrate as spi
import matplotlib.pyplot as plt

texto = "============ MODELO PROBABILISTICO ==============="
titulo = texto.title()
print(titulo)


D= int (input("Ingrese la Demanda esperada por unidad de tiempo (D): "))
K= int (input("Ingree el costo de preparacion por pedido(K): "))
H= float(input ("Ingrese el costo de almacenamiento (H): "))
P= int (input("Ingrese el costo por faltante (P): "))
a= float(input("Ingrese el valor de a: "))
b= float(input("Ingrese el valor de b: "))


#Calcular el valor de la función y la Esperanza 
f = 1 / (b - a)
E= (b+a)/2
def integrand(x, R):
    return (x - R) * f

ytech=math.sqrt((2*D*(K+(P*E)))/H)
ycurv= (P*D)/H

print(" La funcion es : ", f)
print(" La esperanza es : ", E)



if( ycurv>ytech):
    print("Existen soluciones únicas para Yi* y Ri*, tal que : ")
# Inicializamos RO y el contador de iteraciones
    RO = 0
    iteraciones = 0


# Calculamos la primera iteración
    yi = math.sqrt((2 * K * D) / H)
    Ri = 100 - (yi / 50)
    S= 0

# Si Ri no es aproximadamente igual a RO, continuamos con iteraciones adicionales
    while abs(Ri - RO)>0.000001:
        iteraciones += 1
    
    # Guardamos el valor anterior de Ri y calculamos los nuevos valores de yi y Ri
        RO = Ri
        S, error = spi.quad(integrand, RO, b, args=RO)
        yi = math.sqrt((2 * D * (K + (P * S)))/H)
        Ri = b - (H*(b-a)* yi)/ ( P*D)

# Imprimimos los valores de Ri y Yi y el número de iteraciones realizadas
    print(f"Se requirieron {iteraciones} iteraciones.")
    print(f"El valor de R{iteraciones} es: {Ri: .6f}")
    print(f"El valor de y{iteraciones} es: {yi: .6f}")
    print(f"El valor de s{iteraciones} es: {S: .6f}")

    print (f"Esto quiere decir que la politica Òptima de Inventario indica pedir {yi:.4f} unidades, siempre que el nivel de existencia baje a {Ri:.4f} unidades ")

else:
        print("No existe solución para éste problema")

    # Agregar gráficos para representar la política de inventario óptima
    Q = D * yi
    TC = (K * D / Q) + (H * Q / 2) + (P * D * S)
    Qs = np.linspace(Q / 10, Q * 2, 100)
    TCs = (K * D / Qs) + (H * Qs / 2) + (P * D * S)
    plt.plot(Qs, TCs, label="Curva de costo total")
    plt.axvline(x=Q, color="r", linestyle="--", label="Q*")
    plt.xlabel("Cantidad de pedido")
    plt.ylabel("Costo total")
    plt.legend()
    plt.show()

    plt.plot(Qs, H * Qs / 2, label="Curva de costo de almacenamiento")
    plt.xlabel("Cantidad de pedido")
    plt.ylabel("Costo de almacenamiento")
    plt.legend()
    plt.show()

    plt.plot(Qs, P * D * S * np.ones_like(Qs), label="Curva de costo por faltante")
    plt.xlabel("Cantidad de pedido")
    plt.ylabel("Costode faltante")
    plt.legend()
    plt.show()

