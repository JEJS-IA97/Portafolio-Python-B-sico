# Calculadora de promedio

print("========== Calculadora de Promedio ==========\n")

# Solicitar al usuario que ingrese las notas de los exámenes
nota1 = float(input("Ingrese la nota obtenida en el primer examen: "))
nota2 = float(input("Ingrese la nota obtenida en el segundo examen: "))
nota3 = float(input("Ingrese la nota obtenida en el tercer examen: "))
nota4 = float(input("Ingrese la nota obtenida en el cuarto examen: "))

# Calcular la suma de las notas y el promedio
suma_notas = nota1 + nota2 + nota3 + nota4
promedio = suma_notas / 4

# Imprimir el promedio
print("El promedio es:", promedio)

# Imprimir un mensaje indicando si el estudiante aprobó o reprobó
if promedio >= 10:
    print("¡Felicidades, has aprobado!")
else:
    print("Lo siento, has reprobado.")
