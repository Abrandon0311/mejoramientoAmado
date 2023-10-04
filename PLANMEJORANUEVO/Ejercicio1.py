#Crear una clase para representar números racionales:

class NumeroRacional:
    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador

    def __str__(self):
        return f"{self.numerador}/{self.denominador}"

# Ejemplo de uso
racional = NumeroRacional(3, 4)
print(racional)


def son_iguales(racional1, racional2):
    return racional1.numerador * racional2.denominador == racional2.numerador * racional1.denominador

# Ejemplo de uso
racional1 = NumeroRacional(3, 4)
racional2 = NumeroRacional(6, 8)
print(son_iguales(racional1, racional2))
