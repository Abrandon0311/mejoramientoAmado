#Verificar si dos números racionales son iguales:

from Ejercicio1 import NumeroRacional

def son_iguales(racional1, racional2):
    return racional1.numerador * racional2.denominador == racional2.numerador * racional1.denominador

# Ejemplo de uso
racional1 = NumeroRacional(3, 4)
racional2 = NumeroRacional(6, 8)
print(son_iguales(racional1, racional2))
