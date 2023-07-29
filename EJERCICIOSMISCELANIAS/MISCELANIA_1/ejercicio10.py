#10-Busqueda, decir cuantas veces está y en que posiciones

#la función buscar_elemento recibe una lista y un elemento como parámetros
def buscar_elemento(lista, elemento):
    # Inicializamos una lista para almacenar las posiciones encontradas
    posiciones = []
    
    # Variable para contar cuántas veces aparece el elemento
    contador = 0
    
    # Recorremos la lista para buscar el elemento y contar sus ocurrencias
    for i, valor in enumerate(lista):
        if valor == elemento:
            contador += 1
            posiciones.append(i)
    
    return contador, posiciones

# Ejemplo de uso
lista_ejemplo = [2, 5, 8, 5, 4, 5]
elemento_buscado = 5

cantidad, posiciones = buscar_elemento(lista_ejemplo, elemento_buscado)

print(f"El elemento {elemento_buscado} aparece {cantidad} veces en las posiciones {posiciones}")
