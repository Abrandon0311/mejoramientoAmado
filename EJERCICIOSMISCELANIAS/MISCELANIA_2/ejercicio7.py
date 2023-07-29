#7. Encontrar un número natural n más pequeño tal que la suma de los n primeros números
#naturales (1 + 2 + 3 + 4…..) exceda de una cantidad (máximo) introducida por el teclado. 
#Es decir cuantos números  de la serie de los naturales debo sumar para superar el dato máximo. 

# función suma_naturales_exceder_maximo utiliza un bucle while para ir sumando los números 
#naturales de forma acumulativa hasta que la suma supere el valor máximo proporcionado.
def suma_naturales_exceder_maximo(maximo):
    suma = 0
    numero_natural = 0
#Una vez que la suma excede el valor máximo, la función devuelve el número mínimo
#de términos naturales sumados.
    while suma <= maximo:
        numero_natural += 1
        suma += numero_natural

    return numero_natural

# Solicitar el valor máximo al usuario
try:
    #la función input() toma la entrada del usuario como una cadena, 
    # por lo que necesitamos convertirla a un número entero usando int()
    maximo = int(input("Introduce el valor máximo: ")) 
    resultado = suma_naturales_exceder_maximo(maximo)
    print(f"El número mínimo de términos naturales a sumar para superar {maximo} es: {resultado}")
except ValueError:
    print("Error: Debes introducir un número entero válido.")
