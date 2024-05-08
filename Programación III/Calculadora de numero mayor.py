print("Calculadora de mayores")

uno = int(input("Ingrese el primer número: "))
dos = int(input("Ingrese el segundo número: "))
tres = int(input("Ingrese el tercer número: "))

if uno == dos or uno == tres or dos == tres:
    print("No ingrese números repetidos.")
elif uno > dos and uno > tres:
    print(uno, "es el mayor.")
elif dos > tres:
    print(dos, "es el mayor.")
else:
    print(tres, "es el mayor.")
    

