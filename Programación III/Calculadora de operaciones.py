print("Calculadora")
print("Ingrese el tipo de operación que desea ejecutar.")
print("1. Suma\n2. Resta\n3. Multiplicación\n4. División\n5. División Entera\n6. Exponente\n7. Módulo")

operacion = int(input("Ingrese el número correspondiente a la operación: "))

if operacion in range(1, 8):
    if operacion == 1:
        print("Ha elegido Suma\n")
        numero = int(input("Ingrese el primer número que desea sumar: "))
        numero += int(input("Ingrese el segundo número que desea sumar: "))
        print("El resultado de la suma es:", numero)

    elif operacion == 2:
        print("Ha elegido Resta\n")
        numero = int(input("Ingrese el primer número que desea restar: "))
        numero -= int(input("Ingrese el segundo número que desea restar: "))
        print("El resultado de la resta es:", numero)

    elif operacion == 3:
        print("Ha elegido Multiplicación\n")
        numero = int(input("Ingrese el primer número que desea multiplicar: "))
        numero *= int(input("Ingrese el segundo número que desea multiplicar: "))
        print("El resultado de la multiplicación es:", numero)

    elif operacion == 4:
        print("Ha elegido División\n")
        numero = float(input("Ingrese el primer número que desea dividir: "))
        divisor = float(input("Ingrese el segundo número que desea dividir: "))
        if divisor != 0:
            print("El resultado de la división es:", round(numero / divisor, 2))
        else:
            print("¡No se puede dividir entre cero!")

    elif operacion == 5:
        print("Ha elegido División Entera\n")
        numero = int(input("Ingrese el primer número que desea dividir: "))
        divisor = int(input("Ingrese el segundo número que desea dividir: "))
        if divisor != 0:
            print("El resultado de la división entera es:", numero // divisor)
        else:
            print("¡No se puede dividir entre cero!")

    elif operacion == 6:
        print("Ha elegido Exponente\n")
        base = int(input("Ingrese la base: "))
        exponente = int(input("Ingrese el exponente: "))
        print("El resultado exponencial es:", base ** exponente)

    elif operacion == 7:
        print("Ha elegido Módulo\n")
        numero = int(input("Ingrese el primer número: "))
        divisor = int(input("Ingrese el segundo número: "))
        if divisor != 0:
            print("El resultado del módulo es:", numero % divisor)
        else:
            print("¡No se puede calcular el módulo entre cero!")
else:
    print("La operación no existe.")
