#Crear una lista de números racionales y utilizar un bucle for para encontrar el máximo de la lista.

from fractions import Fraction

# Crear una lista de números racionales
numeros_racionales = [Fraction(1, 2), Fraction(3, 4), Fraction(2, 5), Fraction(5, 6), Fraction(7, 8)]

# Inicializar una variable para almacenar el máximo
maximo = numeros_racionales[0]

# Usar un bucle for para encontrar el máximo
for numero in numeros_racionales:
    if numero > maximo:
        maximo = numero

# Imprimir el máximo
print("El número racional máximo es:", maximo)
