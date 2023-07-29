#4. Determinar cuales y cuantos números perfectos hay entre 1 y 1000? 

# la funcio es_numero_perfecto(numero) sirve para verificar si un número dado es perfecto
def es_numero_perfecto(numero):
    # Inicializamos la suma de los divisores propios en 0
    suma_divisores = 0

    # Recorremos todos los posibles divisores del número
    for i in range(1, numero):
        if numero % i == 0:
            # Si encontramos un divisor, lo agregamos a la suma
            suma_divisores += i

    # Comparamos si la suma de los divisores propios es igual al número
    return suma_divisores == numero

#encontrar_numeros_perfectos(hasta) para encontrar todos los números perfectos hasta un límite dado.
def encontrar_numeros_perfectos(hasta):
    numeros_perfectos = []

    # Recorremos todos los números desde 1 hasta el límite "hasta"
    for num in range(1, hasta + 1):
        if es_numero_perfecto(num):
            # Si el número es perfecto, lo agregamos a la lista
            numeros_perfectos.append(num)

    return numeros_perfectos

limite = 1000
numeros_perfectos_encontrados = encontrar_numeros_perfectos(limite)

print("Los números perfectos entre 1 y 1000 son:")
print(numeros_perfectos_encontrados)
print("Cantidad de números perfectos:", len(numeros_perfectos_encontrados))