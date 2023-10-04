#Crear una función que sume los números racionales en un diccionario y devuelva el resultado.

from fractions import Fraction

def sumar_numeros_racionales(diccionario):
    resultado = Fraction(0, 1)  # Inicializamos el resultado como 0
    for valor in diccionario.values():
        numerador, denominador = valor
        fraccion_actual = Fraction(numerador, denominador)
        resultado += fraccion_actual
    return resultado

# Ejemplo de uso
diccionario_racionales = {
    'fraccion1': (1, 2),  # 1/2
    'fraccion2': (3, 4),  # 3/4
    'fraccion3': (1, 5)   # 1/5
}

resultado = sumar_numeros_racionales(diccionario_racionales)
print(f"La suma de los números racionales es: {resultado}")
