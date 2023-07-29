#4.	Llenar un arreglo de n elementos con números generados con la función random. No puede 
#haber números repetidos. Si intenta ingresar al arreglo un número que ya existe, imprimirlo
#para anunciar que ese número ya está en el arreglo.

import random

def generar_numero(min_val, max_val):
    return random.randint(min_val, max_val)

def verificar_repetido(arreglo, numero):
    return numero in arreglo

def llenar_arreglo(n, min_val, max_val):
    arreglo = []
    while len(arreglo) < n:
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
