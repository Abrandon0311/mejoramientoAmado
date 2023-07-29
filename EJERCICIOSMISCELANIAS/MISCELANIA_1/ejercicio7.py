#7-Cuantos y cuales son primos

#La función es_primo() se encarga de verificar si un número es primo
def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

# primos_en_rango() encuentra y enumera los números primos dentro de un rango específico
def primos_en_rango(inicio, fin):
    primos = []
    for num in range(inicio, fin + 1):
        if es_primo(num):
            primos.append(num)
    return primos

# Ejemplo de uso
inicio_rango = 1
fin_rango = 50
lista_primos = primos_en_rango(inicio_rango, fin_rango)
cantidad_primos = len(lista_primos)

print(f"En el rango del {inicio_rango} al {fin_rango} hay {cantidad_primos} números primos:")
print(lista_primos)
