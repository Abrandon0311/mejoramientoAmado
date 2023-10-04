#Simplificar un número racional:

import math
from Ejercicio1 import NumeroRacional

def simplificar_racional(racional):
    gcd = math.gcd(racional.numerador, racional.denominador)
    numerador_simplificado = racional.numerador // gcd
    denominador_simplificado = racional.denominador // gcd
    return NumeroRacional(numerador_simplificado, denominador_simplificado)

# Ejemplo de uso
racional = NumeroRacional(6, 8)
racional_simplificado = simplificar_racional(racional)
print(racional_simplificado)
