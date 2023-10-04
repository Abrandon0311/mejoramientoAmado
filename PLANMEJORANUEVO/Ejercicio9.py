#Calcular el producto de una lista de números racionales utilizando un bucle while.

# Definir una lista de números racionales como pares de enteros (numerador, denominador)
numeros_racionales = [(1, 2), (3, 4), (5, 6)]

# Inicializar el producto a 1/1
producto = (1, 1)

# Usar un bucle while para multiplicar los números racionales uno por uno
indice = 0
while indice < len(numeros_racionales):
    numerador_actual, denominador_actual = numeros_racionales[indice]
    
    # Calcular el nuevo numerador y denominador del producto
    nuevo_numerador = producto[0] * numerador_actual
    nuevo_denominador = producto[1] * denominador_actual
    
    # Actualizar el producto con el nuevo valor
    producto = (nuevo_numerador, nuevo_denominador)
    
    # Incrementar el índice para procesar el siguiente número racional
    indice += 1

# Imprimir el resultado como un número racional simplificado
# Puedes utilizar una función para simplificar el resultado si es necesario
def simplificar_racional(numerador, denominador):
    # Aquí puedes implementar un algoritmo para simplificar el número racional
    # Por simplicidad, vamos a retornar el numerador y denominador sin simplificar
    return numerador, denominador

resultado_simplificado = simplificar_racional(producto[0], producto[1])
print("El producto de la lista de números racionales es:", resultado_simplificado)
