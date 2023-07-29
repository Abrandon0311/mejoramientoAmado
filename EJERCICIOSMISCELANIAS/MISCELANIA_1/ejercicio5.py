#5.	Llenar un arreglo de n elementos con números generados con la función random. 
#Cada número siguiente debe ser mayor que el anterior, pero no puede exceder el 
#valor de la siguiente decena.

import random

# se define la función generar_numero_anterior(anterior) que toma el número anterior como
# argumento y genera un nuevo número aleatorio entre el valor anterior y la siguiente decena
def generar_numero_anterior(anterior):
    siguiente_decena = (anterior // 10 + 1) * 10
    return random.randint(anterior, siguiente_decena - 1)

# la función generar_arreglo(n) generará un arreglo de n elementos 
def generar_arreglo(n):
    arreglo = []
    anterior = random.randint(1, 9)  # Generamos el primer número aleatorio entre 1 y 9.
    arreglo.append(anterior)
    
    for _ in range(n - 1):
        nuevo_numero = generar_numero_anterior(anterior)
        arreglo.append(nuevo_numero)
        anterior = nuevo_numero
    
    return arreglo

# Ejemplo de uso:
n = 10
arreglo_resultante = generar_arreglo(n)
print(arreglo_resultante)
