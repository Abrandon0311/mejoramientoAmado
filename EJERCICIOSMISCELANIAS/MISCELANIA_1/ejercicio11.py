#11- Hallar el factorial de los numeros de una lista y guradarlos en otro lista.
#Utilice numeros entre 2 y 15 para llenar la lista

#define una función factorial(n) que calcula el factorial de un número dado utilizando una recursión simple
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

#la función calcular_factoriales(lista_numeros) toma una lista de números y devuelve una nueva
#lista con los factoriales de aquellos números que están entre 2 y 15 (inclusive).
def calcular_factoriales(lista_numeros):
    lista_factoriales = []
    for num in lista_numeros:
        if num >= 2 and num <= 15:
            lista_factoriales.append(factorial(num))
    return lista_factoriales

# Lista de números del 2 al 15
numeros = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# Calcular los factoriales y guardarlos en otra lista
factoriales = calcular_factoriales(numeros)

# Imprimir la lista de factoriales
print(factoriales)
