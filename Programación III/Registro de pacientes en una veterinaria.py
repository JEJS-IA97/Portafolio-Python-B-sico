# Registro de pacientes en una veterinaria

print("\n============== Veterinaria ==============\n")

print("Este mes fueron atendidos 30 pacientes\n")

total_pacientes = 10
suma_edades_perros = 0
cantidad_perros = 0
suma_edades_gatos = 0
cantidad_gatos = 0

for i in range(1, total_pacientes + 1):
    tipo = int(input("Ingrese el tipo de mascota (1. Perro, 2. Gato): "))
    edad = int(input("Ingrese la edad de la mascota: "))
    
    if tipo == 1:
        suma_edades_perros += edad
        cantidad_perros += 1
    else:
        suma_edades_gatos += edad
        cantidad_gatos += 1

print("\nLa cantidad de pacientes caninos atendidos fue de:", cantidad_perros)
print("El promedio de edad de los pacientes caninos es de:", suma_edades_perros / cantidad_perros)
print("La cantidad de pacientes felinos atendidos fue de:", cantidad_gatos)
print("El promedio de edad de los pacientes felinos es de:", suma_edades_gatos / cantidad_gatos)
