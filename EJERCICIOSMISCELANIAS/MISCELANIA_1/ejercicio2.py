#2.	Llenar dos arreglos de n elementos con números generados con la función random. Compararlos y decir:
#a.	Cuál de los dos tiene la suma más alta
#b.	Cuál de los dos tiene el número mayor
#c.	Cuál de los dos tiene el número menor
#d.	Cuál es el promedio conjunto (uniendo los dos arreglos)
#e.	Sacar el promedio de cada uno y decir si está por encima o por debajo del arreglo conjunto
#f.	Cuál de los dos tiene mayor cantidad de pares
#g.	Cuál de los dos tiene mayor cantidad de impares

import random

def generar_arreglo(n):
    return [random.randint(1, 100) for _ in range(n)]

def suma_mas_alta(arreglo1, arreglo2):
    return max(sum(arreglo1), sum(arreglo2))

def numero_mayor(arreglo1, arreglo2):
    return max(max(arreglo1), max(arreglo2))

def numero_menor(arreglo1, arreglo2):
    return min(min(arreglo1), min(arreglo2))

def promedio_conjunto(arreglo1, arreglo2):
    conjunto = arreglo1 + arreglo2
    return sum(conjunto) / len(conjunto)

def promedio_individual(arreglo):
    return sum(arreglo) / len(arreglo)

def comparar_promedio_conjunto(arreglo1, arreglo2):
    promedio_arreglos = (promedio_individual(arreglo1) + promedio_individual(arreglo2)) / 2
    promedio_conjunto_val = promedio_conjunto(arreglo1, arreglo2)

    if promedio_conjunto_val > promedio_arreglos:
        return "El promedio conjunto está por encima del arreglo conjunto."
    elif promedio_conjunto_val < promedio_arreglos:
        return "El promedio conjunto está por debajo del arreglo conjunto."
    else:
        return "El promedio conjunto es igual al promedio de los arreglos individuales."

def contar_pares_impares(arreglo):
    pares = sum(1 for num in arreglo if num % 2 == 0)
    impares = sum(1 for num in arreglo if num % 2 != 0)
    return pares, impares

# Tamaño de los arreglos
n = 10

# Generar los arreglos
arreglo1 = generar_arreglo(n)
arreglo2 = generar_arreglo(n)

# Comparaciones
print("Arreglo 1:", arreglo1)
print("Arreglo 2:", arreglo2)

print("a. El arreglo con la suma más alta:", suma_mas_alta(arreglo1, arreglo2))
print("b. El número mayor entre ambos arreglos:", numero_mayor(arreglo1, arreglo2))
print("c. El número menor entre ambos arreglos:", numero_menor(arreglo1, arreglo2))
print("d. El promedio conjunto de ambos arreglos:", promedio_conjunto(arreglo1, arreglo2))
print("e. Comparación del promedio individual con el promedio conjunto:")
print(comparar_promedio_conjunto(arreglo1, arreglo2))

pares_arreglo1, impares_arreglo1 = contar_pares_impares(arreglo1)
pares_arreglo2, impares_arreglo2 = contar_pares_impares(arreglo2)
print("f. Cantidad de pares en arreglo 1:", pares_arreglo1)
print("f. Cantidad de pares en arreglo 2:", pares_arreglo2)
print("g. Cantidad de impares en arreglo 1:", impares_arreglo1)
print("g. Cantidad de impares en arreglo 2:", impares_arreglo2)
