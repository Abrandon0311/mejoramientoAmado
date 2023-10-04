#Calcular la suma de una lista de números racionales utilizando un bucle for.

# Definir la lista de números racionales
from fractions import Fraction

numeros_racionales = [Fraction(1, 2), Fraction(2, 3), Fraction(3, 4)]

# Inicializar una variable para almacenar la suma
suma = Fraction(0, 1)

# Iterar a través de la lista y sumar los números racionales
for numero in numeros_racionales:
    suma += numero

# Imprimir el resultado
print("La suma de los números racionales es:", suma)
