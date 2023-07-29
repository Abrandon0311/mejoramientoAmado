#3. Determinar si un número es o no es perfecto. Un numero es perfecto si la suma de 
#sus divisores sin incluir el propio número es igual a este

#Esta función toma un número como entrada y calcula la suma de todos sus divisores, 
#excluyendo el propio número.
def suma_divisores(numero):
    suma = 0
    #Utiliza un bucle for para verificar todos los números desde 1 hasta el número-1 
    #e incrementa la variable suma cada vez que encuentra un divisor.
    for i in range(1, numero): #
        if numero % i == 0:
            suma += i
    return suma

#Esta función toma un número como entrada y utiliza la función suma_divisores(numero) 
#para determinar si el número es perfecto o no
def es_perfecto(numero):
    return numero == suma_divisores(numero)
#Retorna True si la suma de los divisores es igual al número original; 
#de lo contrario, retorna False.

# Prueba de la función
num = int(input("Ingrese un número para verificar si es perfecto: "))

if es_perfecto(num):
    print(f"{num} es un número perfecto.")
else:
    print(f"{num} no es un número perfecto.")