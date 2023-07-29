#8-Suma pares y promedio de los impares

#es_par(numero): Verifica si un número dado es par y devuelve True si lo es,
#de lo contrario, devuelve False.
def es_par(numero):
    return numero % 2 == 0

#suma_pares(lista): Recorre una lista de números y suma solo los números pares.
#Luego devuelve el resultado de la suma.
def suma_pares(lista):
    suma = 0
    for numero in lista:
        if es_par(numero):
            suma += numero
    return suma

#promedio_impares(lista): Crea una nueva lista con los números impares de la
#lista original, calcula el promedio de esos números y lo devuelve. Si no hay 
#impares, devuelve 0 para evitar la división por cero.
def promedio_impares(lista):
    impares = [numero for numero in lista if not es_par(numero)]
    if len(impares) == 0:
        return 0  # Si no hay impares, el promedio es 0 para evitar la división por cero.
    return sum(impares) / len(impares)

#El programa principal (main()) crea una lista de números de ejemplo y llama a las
#funciones suma_pares y promedio_impares para mostrar los resultados en la consola.
def main():
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    suma_pares_resultado = suma_pares(numeros)
    promedio_impares_resultado = promedio_impares(numeros)

    print("Lista de números:", numeros)
    print("Suma de los números pares:", suma_pares_resultado)
    print("Promedio de los números impares:", promedio_impares_resultado)

if __name__ == "__main__":
    main()
