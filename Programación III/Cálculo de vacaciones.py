print("Reporte Vacaciones")

nombre = input("Ingrese el nombre del empleado: ")
codigo = int(input("Ingrese el código del departamento: "))
antiguedad = float(input("Ingrese la cantidad de años trabajados: "))

if codigo == 1:
    if 1 <= antiguedad < 2:
        print("El empleado", nombre ,"tiene derecho a 6 días de vacaciones.")
    elif 2 <= antiguedad <= 6:
        print("El empleado", nombre ,"tiene derecho a 14 días de vacaciones.")
    else:
        print("El empleado", nombre ,"tiene derecho a 20 días de vacaciones.")

elif codigo == 2:
    if 1 <= antiguedad < 2:
        print("El empleado", nombre ,"tiene derecho a 7 días de vacaciones.")
    elif 2 <= antiguedad <= 6:
        print("El empleado", nombre ,"tiene derecho a 15 días de vacaciones.")
    else:
        print("El empleado", nombre ,"tiene derecho a 22 días de vacaciones.")

elif codigo == 3:
    if 1 <= antiguedad < 2:
       print("El empleado", nombre ,"tiene derecho a 10 días de vacaciones.")
    elif 2 <= antiguedad <= 6:
        print("El empleado", nombre ,"tiene derecho a 20 días de vacaciones.")
    else:
        print("El empleado", nombre ,"tiene derecho a 30 días de vacaciones.")
else:
    print("El código no ha sido asignado a un departamento, ingrese un código válido.")
