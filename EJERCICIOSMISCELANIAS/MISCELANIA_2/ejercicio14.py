#14. Calcular todos los números de 3 cifras tales que la suma de los cubos de las 
#cifras es igual al valor del número.

#definirá una función sum_of_cubes_is_number(num) que determina si la suma de los
#cubos de las cifras de un número de 3 cifras num es igual al valor de ese número.
def sum_of_cubes_is_number(num):
    # Función auxiliar para calcular el cubo de un número
    def cube(n):
        return n ** 3

    # Extraemos las cifras del número
    digit1 = num // 100
    digit2 = (num // 10) % 10
    digit3 = num % 10

    # Calculamos la suma de los cubos de las cifras
    sum_of_cubes = cube(digit1) + cube(digit2) + cube(digit3)

    # Comprobamos si la suma es igual al número original
    return sum_of_cubes == num

# Lista para almacenar los números que cumplen con la condición
numbers_with_sum_of_cubes_equal = []

#iteramos sobre todos los números de 100 a 999 y almacenamos aquellos
# que cumplen con la condición en la lista numbers_with_sum_of_cubes_equal
for num in range(100, 1000):
    if sum_of_cubes_is_number(num):
        numbers_with_sum_of_cubes_equal.append(num)

# Imprimimos los números encontrados
print("Números de 3 cifras donde la suma de los cubos de las cifras es igual al valor del número:")
print(numbers_with_sum_of_cubes_equal)
