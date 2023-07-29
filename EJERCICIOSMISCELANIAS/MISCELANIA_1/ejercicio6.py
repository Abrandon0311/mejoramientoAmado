#6-Si el elemento esta por encima del promedio, debajo o es igual

def calcular_promedio(lista):
    total = sum(lista)
    return total / len(lista)

def comparar_con_promedio(elemento, promedio):
    if elemento > promedio:
        return "por encima"
    elif elemento < promedio:
        return "por debajo"
    else:
        return "igual"

def main():
    # Ejemplo: lista de elementos
    elementos = [10, 20, 30, 40, 50]

    # Calcular el promedio
    promedio = calcular_promedio(elementos)

    # Comparar cada elemento con el promedio e imprimir el resultado
    for elemento in elementos:
        resultado = comparar_con_promedio(elemento, promedio)
        print(f"{elemento} está {resultado} del promedio.")

if __name__ == "__main__":
    main()
