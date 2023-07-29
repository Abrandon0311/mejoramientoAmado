#1.	Llenar un arreglo de n elementos con números generados con la función random. N es ingresado por el usuario. Diseñe un menú con las siguientes operaciones. 
#a.	Imprimir arreglo original (El primero que se generó)
#b.	Suma
#c.	Promedio
#d.	Mayor
#e.	Menor
#f.	Ordenar ascendente (No perder el arreglo original; el del punto a)
#g.	Ordenar descendente (No perder el arreglo original; el del punto a)
#h.	Moda
#i.	Mediana
#j.	Buscar. Decir si encuentra el número, en qué posición(es) está, cuantas veces está


import random
from collections import Counter

def generar_arreglo(n):
    return [random.randint(1, 100) for _ in range(n)]

def imprimir_arreglo(arreglo):
    print("Arreglo original:")
    print(arreglo)

def suma_arreglo(arreglo):
    return sum(arreglo)

def promedio_arreglo(arreglo):
    return sum(arreglo) / len(arreglo)

def mayor_arreglo(arreglo):
    return max(arreglo)

def menor_arreglo(arreglo):
    return min(arreglo)

def ordenar_ascendente(arreglo):
    return sorted(arreglo)

def ordenar_descendente(arreglo):
    return sorted(arreglo, reverse=True)

def moda_arreglo(arreglo):
    count = Counter(arreglo)
    moda = max(count.values())
    return [num for num, freq in count.items() if freq == moda]

def mediana_arreglo(arreglo):
    sorted_arreglo = sorted(arreglo)
    n = len(sorted_arreglo)
    if n % 2 == 0:
        return (sorted_arreglo[n // 2 - 1] + sorted_arreglo[n // 2]) / 2
    else:
        return sorted_arreglo[n // 2]

def buscar_numero(arreglo, numero):
    indices = [i for i, num in enumerate(arreglo) if num == numero]
    veces = len(indices)
    return indices, veces

def main():
    print("Bienvenido al programa de generación de arreglos aleatorios.")
    n = int(input("Ingrese el tamaño del arreglo (n): "))

    arreglo = generar_arreglo(n)

    while True:
        print("\nMenú de opciones:")
        print("a. Imprimir arreglo original")
        print("b. Suma del arreglo")
        print("c. Promedio del arreglo")
        print("d. Valor mayor del arreglo")
        print("e. Valor menor del arreglo")
        print("f. Ordenar el arreglo en forma ascendente")
        print("g. Ordenar el arreglo en forma descendente")
        print("h. Moda del arreglo")
        print("i. Mediana del arreglo")
        print("j. Buscar número en el arreglo")
        print("q. Salir")

        opcion = input("Ingrese la opción deseada: ")

        if opcion == "a":
            imprimir_arreglo(arreglo)
        elif opcion == "b":
            print("Suma del arreglo:", suma_arreglo(arreglo))
        elif opcion == "c":
            print("Promedio del arreglo:", promedio_arreglo(arreglo))
        elif opcion == "d":
            print("Valor mayor del arreglo:", mayor_arreglo(arreglo))
        elif opcion == "e":
            print("Valor menor del arreglo:", menor_arreglo(arreglo))
        elif opcion == "f":
            print("Arreglo ordenado en forma ascendente:", ordenar_ascendente(arreglo))
        elif opcion == "g":
            print("Arreglo ordenado en forma descendente:", ordenar_descendente(arreglo))
        elif opcion == "h":
            print("Moda del arreglo:", moda_arreglo(arreglo))
        elif opcion == "i":
            print("Mediana del arreglo:", mediana_arreglo(arreglo))
        elif opcion == "j":
            numero_buscado = int(input("Ingrese el número a buscar: "))
            indices, veces = buscar_numero(arreglo, numero_buscado)
            if veces > 0:
                print(f"El número {numero_buscado} está en las posiciones {indices} y aparece {veces} veces.")
            else:
                print(f"El número {numero_buscado} no se encuentra en el arreglo.")
        elif opcion == "q":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, ingrese una opción válida.")

if __name__ == "__main__":
    main()

