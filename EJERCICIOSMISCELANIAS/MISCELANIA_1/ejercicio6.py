#6-Si el elemento esta por encima del promedio, debajo o es igual

#la función calcular_promedio(lista) calcula el promedio de los elementos en la lista
def calcular_promedio(lista):
    total = sum(lista)
    return total / len(lista)

#la función comparar_con_promedio(elemento, promedio) compara un elemento dado con el
#promedio y devuelve un mensaje indicando si está por encima, por debajo o es igual al promedio. 
def comparar_con_promedio(elemento, promedio):
    if elemento > promedio:
        return "por encima"
    elif elemento < promedio:
        return "por debajo"
    else:
        return "igual"

# la función main(), se muestra un ejemplo de cómo usar estas funciones para una lista de elementos dada.
def main():
    # Ejemplo: lista de elementos
    elementos = [10, 20, 30, 40, 50]

    # Calcular el promedio
    promedio = calcular_promedio(elementos)

    # Comparar cada elemento con el promedio e imprimir el resultado
    for elemento in elementos:
        resultado = comparar_con_promedio(elemento, promedio)
        print(f"{elemento} está {resultado} del promedio.")

#La cláusula if __name__ == "__main__": asegura que la función main se ejecute solo si
#el script se ejecuta directamente y no si se importa como un módulo.
if __name__ == "__main__":
    main()
