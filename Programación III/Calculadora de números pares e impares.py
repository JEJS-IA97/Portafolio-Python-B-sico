print("Calculadora de números pares e impares")

numero = int(input("Ingrese el número: "))

resto = numero % 2

if resto == 0:
    print("El número", numero ,"es par.")
elif resto == 1:
    print("El número", numero ,"es impar.")
