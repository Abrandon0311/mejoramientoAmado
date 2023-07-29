#1. Determinar los divisores de un  número introducido por teclado 

#La función obtener_divisores(numero) toma un número como argumento y devuelve una lista
#de sus divisores.
def obtener_divisores(numero):
    divisores = []
    for i in range(1, numero + 1):
        if numero % i == 0:
            divisores.append(i)
    return divisores

#En el bloque try, solicitamos al usuario que introduzca un número entero y lo convertimos
#a un entero usando int(input()).
try:
    numero = int(input("Introduce un número entero: "))
    if numero <= 0:
        print("Por favor, introduce un número entero positivo.")
    else:
        lista_divisores = obtener_divisores(numero)
        print("Los divisores de", numero, "son:", lista_divisores)
except ValueError:
    print("Error: Debes introducir un número entero válido.")

#Si el número es positivo, llamamos a la función obtener_divisores(numero) para obtener 
#una lista de divisores y la almacenamos en lista_divisores.