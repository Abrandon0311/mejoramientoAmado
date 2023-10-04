#Crear un diccionario que asocie nombres de números racionales con sus valores y luego imprimir el valor correspondiente a un nombre dado.

# Crear el diccionario de números racionales
numeros_racionales = {
    "uno medio": 1/2,
    "dos tercios": 2/3,
    "tres cuartos": 3/4,
    "cinco sextos": 5/6,
    # Agrega más nombres y valores de números racionales según sea necesario
}

# Solicitar al usuario un nombre de número racional
nombre_deseado = input("Ingresa el nombre del número racional: ")

# Buscar el valor correspondiente en el diccionario
valor_correspondiente = numeros_racionales.get(nombre_deseado)

# Verificar si el nombre existe en el diccionario y mostrar el resultado
if valor_correspondiente is not None:
    print(f"El valor de {nombre_deseado} es {valor_correspondiente}")
else:
    print(f"{nombre_deseado} no se encuentra en el diccionario.")
