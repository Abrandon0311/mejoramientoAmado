#Multiplicación de dos números racionales:

from Ejercicio1 import NumeroRacional
def multiplicacion_racionales(racional1, racional2):
    numerador = racional1.numerador * racional2.numerador
    denominador = racional1.denominador * racional2.denominador
    return NumeroRacional(numerador, denominador)

# Ejemplo de uso
racional1 = NumeroRacional(2, 5)
racional2 = NumeroRacional(3, 7)
resultado = multiplicacion_racionales(racional1, racional2)
print(resultado)
