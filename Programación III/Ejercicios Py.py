# Ejercicio 1: Multiplicar dos números sin usar el operador *
print("Ejercicio 1: Multiplicar dos números sin usar el operador *\n")
a =  4
b = 8
resultado = 0

for x in range(a):
    resultado += b

print(resultado)

# Ejercicio 2: Ingresar nombre y apellido e imprimir al revés
print("\n")
print("Ejercicio 2: Ingresar nombre y apellido e imprimir al revés\n")
nombre = ' Jose'
apellido = ' Jimenez'

cadena = nombre + '  ' + apellido
print(cadena[::-1])

# Ejercicio 3a: Escribir una función que encuentre el elemento menor de una lista
print('\n')
print("Ejercicio 3a: Escribir una función que encuentre el elemento menor de una lista\n")
lista =  [1,  -2,  3,  -4,  5]
menor = min(lista)
print(menor)

# Ejercicio 3b: Escribir una función que encuentre el elemento menor de una lista (otra forma)
print('\n')
print("Ejercicio 3b: Escribir una función que encuentre el elemento menor de una lista (otra forma)\n")
menor2 = ' init'
for x in lista:
    if menor2 == ' init':
          menor2 = x
    else:
        menor2 = x if x < menor2 else menor2
print(' menor' ,menor2)

# Ejercicio 4: Escribir una función que devuelva el volumen de una esfera por su radio
print('\n')
print("Ejercicio 4: Escribir una función que devuelva el volumen de una esfera por su radio\n")
def calcularVolumen(r):
    return 4/3 * 3.14 * r ** 3
resultado = calcularVolumen(6)
print(resultado)

# Ejercicio 5: Escribir una función que indique si el usuario es mayor de edad
print('\n')
print("Ejercicio 5: Escribir una función que indique si el usuario es mayor de edad\n")
def mayor(usuario):
    return usuario.edad > 17
class Usuario:
    def __init__(self,edad):
        self.edad = edad

usuario = Usuario(16)
usuario2 = Usuario(21)

resultado1 = mayor(usuario)
resultado2 = mayor(usuario2)

print(resultado1, resultado2)

# Ejercicio 6: Escribir una función que indique si un número es par o impar
print('\n')
print("Ejercicio 6: Escribir una función que indique si un número es par o impar\n")
def par(n):
    return n % 2 ==0
resultado = par(10)
print(resultado)

# Ejercicio 7: Imprimir cuántas vocales tiene una palabra
print('\n')
print("Ejercicio 7: Imprimir cuántas vocales tiene una palabra\n")
palabra = 'Chanchito'
vocales = 0
for x in palabra:
    y = x.lower()
    vocales += 1  if y == 'a' or y  == 'e' or y  == 'i' or y == 'o' or y == 'u' else 0
print(vocales)

# Ejercicio 8: Escribir una aplicación que reciba una cantidad infinita de números y devuelva su suma
print('\n')
print("Ejercicio 8: Escribir una aplicación que reciba una cantidad infinita de números y devuelva su suma\n")
lista=[]
print('Ingrese numeros y para salir escriba "basta"')
while True:
    valor = input('Ingrese Valor:  ')
    if valor =='basta':
        break
    else:
        try:
            valor = int(valor)
            lista.append(valor)
        except:
            print('Dato incorrecto')
            exit()

resultado = 0
for x in lista:
    resultado += x
print(resultado)

# Ejercicio 9: Escribir una función que reciba nombre y apellido y los agregue a un archivo
print('\n')
print("Ejercicio 9: Escribir una función que reciba nombre y apellido y los agregue a un archivo\n")
def agrega(nom, apell):
    c = open('nombre.txt','a')
    c.write(nom + ' ' + apell + '\n')
    c.close()
agrega('Jose', 'Jimenez')
