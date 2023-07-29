#10. Algoritmo para hallar el m.c.d de dos números m y n por el algoritmo de Euclides. 

#La función euclidean_algorithm(m, n) toma dos números enteros m y n como parámetros y
#calcula su MCD utilizando el algoritmo de Euclides.
def euclidean_algorithm(m, n):
    #Se utiliza un bucle while que se repite hasta que n sea igual a cero. En cada iteración,
    #se actualizan los valores de m y n de acuerdo con el algoritmo de Euclides.
    while n != 0:
        m, n = n, m % n
    return m

#La función main() es el punto de entrada del programa. Solicita al usuario los valores de m y n,
#llama a la función euclidean_algorithm() para calcular el MCD y luego muestra el resultado en la pantalla.
def main():
    try:
        # Solicitamos al usuario los números m y n
        m = int(input("Ingrese el primer número (m): "))
        n = int(input("Ingrese el segundo número (n): "))

        # Calculamos el MCD utilizando el algoritmo de Euclides
        mcd = euclidean_algorithm(m, n)

        # Mostramos el resultado
        print("El MCD de", m, "y", n, "es:", mcd)

    except ValueError:
        print("Error: Ingrese números enteros válidos.")

#La cláusula if __name__ == "__main__": asegura que la función main se ejecute solo si
#el script se ejecuta directamente y no si se importa como un módulo.
if __name__ == "__main__":
    main()
