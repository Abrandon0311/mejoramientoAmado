#9-Ordenar el arreglo, de mayor a menor y de menor a mayor (algoritmo de la burbuja)

# Función para ordenar el arreglo de mayor a menor usando el algoritmo de la burbuja
def bubble_sort_descending(arr):
    n = len(arr)
    for i in range(n):
        # Hacemos n-i-1 comparaciones en cada iteración
        for j in range(0, n-i-1):
            if arr[j] < arr[j+1]:
                # Intercambiamos los elementos si están en el orden equivocado
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Función para ordenar el arreglo de menor a mayor usando el algoritmo de la burbuja
def bubble_sort_ascending(arr):
    n = len(arr)
    for i in range(n):
        # Hacemos n-i-1 comparaciones en cada iteración
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                # Intercambiamos los elementos si están en el orden equivocado
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Ejemplo de uso
if __name__ == "__main__":
    # Arreglo de ejemplo
    my_array = [64, 34, 25, 12, 22, 11, 90]

    print("Arreglo original:", my_array)

    # Ordenar de mayor a menor
    bubble_sort_descending(my_array.copy())
    print("Arreglo ordenado de mayor a menor:", my_array)

    # Ordenar de menor a mayor
    bubble_sort_ascending(my_array.copy())
    print("Arreglo ordenado de menor a mayor:", my_array)
