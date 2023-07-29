#8. Determinar cuales son los múltiplos de 5 comprendidos entre 1 y N. 

#define la función obtener_multiplos_de_cinco(N) que encuentra los múltiplos de 5 entre 1 y el número dado N
def obtener_multiplos_de_cinco(N):
    multiplos_de_cinco = []  # Lista para almacenar los múltiplos de 5 encontrados

    for numero in range(1, N + 1): #utiliza un bucle para iterar desde 1 hasta N.
        if numero % 5 == 0:  # Verifica si el número es múltiplo de 5
            multiplos_de_cinco.append(numero)  # Agrega el número a la lista
#Al finalizar el bucle, devuelve la lista de múltiplos de 5 encontrados.
    return multiplos_de_cinco

# Ejemplo de uso de la función
numero_limite = int(input("Ingrese un número límite (N): "))
resultados = obtener_multiplos_de_cinco(numero_limite)
print("Los múltiplos de 5 entre 1 y", numero_limite, "son:", resultados)
