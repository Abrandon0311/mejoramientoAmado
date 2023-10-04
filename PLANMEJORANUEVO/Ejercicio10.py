#Usar una estructura de control if para verificar si un número racional es positivo, negativo o cero.

# Ingresar el numerador y el denominador de la fracción
numerador = int(input("Ingrese el numerador: "))
denominador = int(input("Ingrese el denominador: "))

# Calcular el valor decimal de la fracción
valor_decimal = numerador / denominador

# Usar una estructura de control if para verificar el signo
if valor_decimal > 0:
    print("La fracción es positiva.")
elif valor_decimal < 0:
    print("La fracción es negativa.")
else:
    print("La fracción es igual a cero.")
