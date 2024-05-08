# Cálculo de interés compuesto

print("\n=========== Calcular Interés ===========\n")

# Inicializar variables
capital = -1
interes = 0
annos = 0

# Solicitar al usuario que ingrese valores válidos para capital, interés y años
while capital < 0 or interes <= 0 or interes >= 100 or annos <= 0:
    capital = float(input("Ingrese el Capital: "))
    interes = float(input("Ingrese el Interés: "))
    annos = int(input("Ingrese el Tiempo en Años: "))

# Calcular el capital final
for i in range(annos):
    capital *= (1 + (interes / 100))

# Imprimir el resultado
print("\nEl Capital en ese tiempo es de:", capital, "$")
