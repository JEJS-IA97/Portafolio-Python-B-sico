# Cálculo de promedio, edad mayor y edad menor

print("\n============== Promedio de Edad ==============\n")

n = 0
edades = []

print("Ingrese 10 edades:\n")

# Solicitar al usuario que ingrese 10 edades
for i in range(1, 10+1):
    edad = int(input("Ingrese edad: "))
    edades.append(edad)
    n += edad

# Calcular el promedio de edades
promedio = n / 10

# Encontrar la edad mayor y la edad menor
mayor = max(edades)
menor = min(edades)

# Imprimir los resultados
print("El promedio de edad es:", promedio)
print("La edad menor es:", menor)
print("La edad mayor es:", mayor)
