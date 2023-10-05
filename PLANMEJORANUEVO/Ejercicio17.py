#Crear una función que genere una lista de números racionales aleatorios.

import fractions
import random

def generar_racionales_aleatorios(n, limite):
    racionales_aleatorios = []

    for _ in range(n):
        numerador = random.randint(1, limite)
        denominador = random.randint(1, limite)
        racional = fractions.Fraction(numerador, denominador)
        racionales_aleatorios.append(racional)

    return racionales_aleatorios

# Ejemplo de uso:
lista_racionales = generar_racionales_aleatorios(5, 10)
print(lista_racionales)
