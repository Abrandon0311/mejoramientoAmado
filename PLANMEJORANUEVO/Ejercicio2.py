#Suma de dos números racionales:

from Ejercicio1 import NumeroRacional

def suma_racionales(racional1, racional2):
    numerador = (racional1.numerador * racional2.denominador) + (racional2.numerador * racional1.denominador)
    denominador = racional1.denominador * racional2.denominador
    return NumeroRacional(numerador, denominador)

# Ejemplo de uso
racional1 = NumeroRacional(1, 4)
racional2 = NumeroRacional(1, 6)
resultado = suma_racionales(racional1, racional2)
print(resultado)
