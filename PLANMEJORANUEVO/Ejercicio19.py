#Utilizar una función map para simplificar una lista de números racionales.

from fractions import Fraction

# Definir una lista de números racionales
numeros_racionales = [Fraction(4, 8), Fraction(3, 6), Fraction(5, 10)]

# Utilizar map para simplificar la lista
simplificados = list(map(Fraction, numeros_racionales))

# Imprimir la lista simplificada
print(simplificados)
