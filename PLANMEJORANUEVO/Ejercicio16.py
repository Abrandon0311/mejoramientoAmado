#Usar una estructura de control if-elif-else para clasificar un número racional como propio o impropio.

# Pedir al usuario que ingrese el numerador y el denominador
numerador = int(input("Ingrese el numerador: "))
denominador = int(input("Ingrese el denominador: "))

# Verificar si el número es propio o impropio
if abs(numerador) < abs(denominador):
    print("El número es propio.")
elif abs(numerador) >= abs(denominador):
    print("El número es impropio.")
else:
    print("El número es igual a 0.")
