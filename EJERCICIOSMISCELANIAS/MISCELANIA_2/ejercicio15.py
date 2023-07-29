#15. Diseñar e implementar un programa que solicite a su usuario un valor no negativo n
#y visualice la siguiente salida:  
#1 2 3 ........ n-1 n  
#1 2 3 ........ n-1  
#.........  
#1 2 3  
#1 2  
#1

#una función llamada print_pattern que tomará como parámetro el valor no negativo n ingresado 
#por el usuario y generará la salida solicitada.
def print_pattern(n):
    # Bucle externo para imprimir filas desde n hasta 1
    for i in range(n, 0, -1):
        # Bucle interno para imprimir números desde 1 hasta i
        for j in range(1, i + 1):
            # Imprimir cada número seguido de un espacio
            print(j, end=' ')
        # Imprimir una nueva línea después de cada fila
        print()

# Solicitar al usuario el valor no negativo n
try:
    n = int(input("Ingresa un valor no negativo: "))
    if n < 0:
        print("El valor ingresado debe ser no negativo.")
    else:
        # Llamar a la función para imprimir el patrón
        print_pattern(n)
except ValueError:
    print("Debes ingresar un número entero no negativo.")
