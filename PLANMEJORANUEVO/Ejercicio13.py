#Utilizar una tupla para almacenar una fracción y su representación decimal.

# Definir una función para calcular la representación decimal de una fracción
def decimal_representation(fraction):
    numerator, denominator = fraction
    result = numerator / denominator
    return result

# Crear una tupla que almacene la fracción y su representación decimal
fraction = (3, 4)  # Por ejemplo, 3/4
decimal_value = decimal_representation(fraction)

# Imprimir la tupla
print(f"Fracción: {fraction[0]}/{fraction[1]}")
print(f"Representación Decimal: {decimal_value}")
