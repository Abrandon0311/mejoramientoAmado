#4.	Llenar un arreglo de n elementos con números generados con la función random. No puede 
#haber números repetidos. Si intenta ingresar al arreglo un número que ya existe, imprimirlo
#para anunciar que ese número ya está en el arreglo.

import random

def generar_numero(min_val, max_val): #La función generar_numero toma un valor mínimo y máximo como argumentos.
    return random.randint(min_val, max_val) #devuelve un número aleatorio entre esos valores utilizando la función random.randint.

#La función verificar_repetido toma un arreglo y un número como argumentos y devuelve True
#si el número ya existe en el arreglo, o False en caso contrario.
def verificar_repetido(arreglo, numero): 
    return numero in arreglo

#La función llenar_arreglo toma la cantidad de elementos n, el valor mínimo min_val 
#y el valor máximo max_val como argumentos.
def llenar_arreglo(n, min_val, max_val):
    arreglo = []
    while len(arreglo) < n: #se crea  un bucle while para generar números aleatorios y llenar el arreglo hasta que alcance la cantidad de elementos n
        numero = generar_numero(min_val, max_val)
        if verificar_repetido(arreglo, numero):
            print(f"El número {numero} ya está en el arreglo.")
        else:
            arreglo.append(numero)
    return arreglo

# Datos para el llenado del arreglo
n = 10  # Cantidad de elementos en el arreglo
min_val = 1  # Valor mínimo para los números aleatorios
max_val = 100  # Valor máximo para los números aleatorios

# Llenar el arreglo
arreglo_resultado = llenar_arreglo(n, min_val, max_val)
print("Arreglo generado:", arreglo_resultado)
