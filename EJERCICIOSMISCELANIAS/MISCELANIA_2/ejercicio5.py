#5. ¿Cuáles y cuántos son los números primos comprendidos entre 1 y 1000?

#se define la función es_primo() que verifica si un número es primo o no
def es_primo(numero):
    if numero <= 1:
        return False
    #utilizando un bucle for para comprobar si el número es divisible por algún otro número menor que él
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

#la función numeros_primos_entre_1_y_1000() recorre todos los números entre 1 y 1000, y si 
#un número es primo, lo agrega a la lista primos.
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
