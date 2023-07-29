#10. Algoritmo para hallar el m.c.d de dos números m y n por el algoritmo de Euclides. 

def euclidean_algorithm(m, n):
    while n != 0:
        m, n = n, m % n
    return m

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

if __name__ == "__main__":
    main()
