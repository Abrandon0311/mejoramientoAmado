#2. Determinar si un numero es o no es primo

#la función es_primo(numero) toma un número como argumento y retorna True si el número es primo,
#y False en caso contrario. 
def es_primo(numero):
    if numero <= 1:
        return False

    # Comprobamos si el número es divisible por algún número desde 2 hasta la raíz cuadrada de dicho número
    # Si encontramos un divisor, el número no es primo
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False

    # Si el bucle termina sin encontrar ningún divisor, el número es primo
    return True

# Pedimos al usuario que ingrese un número
numero_ingresado = int(input("Ingresa un número: "))

# Llamamos a la función es_primo() y mostramos el resultado
if es_primo(numero_ingresado):
    print(f"{numero_ingresado} es un número primo.")
else:
    print(f"{numero_ingresado} no es un número primo.")