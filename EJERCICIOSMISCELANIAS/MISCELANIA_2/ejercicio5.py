#5. ¿Cuáles y cuántos son los números primos comprendidos entre 1 y 1000?

def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

def numeros_primos_entre_1_y_1000():
    primos = []
    for num in range(1, 1001):
        if es_primo(num):
            primos.append(num)
    return primos

# Llamamos a la función para obtener los números primos entre 1 y 1000
primos_comprendidos = numeros_primos_entre_1_y_1000()

# Imprimimos los números primos encontrados
print("Números primos entre 1 y 1000:")
print(primos_comprendidos)

# Imprimimos la cantidad de números primos encontrados
print("Cantidad de números primos entre 1 y 1000:", len(primos_comprendidos))
