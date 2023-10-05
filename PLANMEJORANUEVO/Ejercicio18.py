#Implementar una clase CalculadoraRacional que tenga métodos para suma, resta, multiplicación y división de números racionales.

from fractions import Fraction

class CalculadoraRacional:
    @staticmethod
    def suma(num1, num2):
        return num1 + num2

    @staticmethod
    def resta(num1, num2):
        return num1 - num2

    @staticmethod
    def multiplicacion(num1, num2):
        return num1 * num2

    @staticmethod
    def division(num1, num2):
        if num2 == 0:
            raise ValueError("La división por cero no está permitida")
        return num1 / num2

# Ejemplo de uso
racional1 = Fraction(1, 2)
racional2 = Fraction(3, 4)

calculadora = CalculadoraRacional()

print("Suma:", calculadora.suma(racional1, racional2))
print("Resta:", calculadora.resta(racional1, racional2))
print("Multiplicación:", calculadora.multiplicacion(racional1, racional2))
print("División:", calculadora.division(racional1, racional2))
