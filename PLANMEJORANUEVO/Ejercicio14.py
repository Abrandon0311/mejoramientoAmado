#Definir una función que reciba un conjunto de números racionales y devuelva los que son mayores que 1.

def numeros_mayores_que_uno(racionales):
    resultados = []
    for numerador, denominador in racionales:
        if numerador / denominador > 1:
            resultados.append((numerador, denominador))
    return resultados

# Ejemplo de uso
conjunto_racionales = [(2, 1), (3, 2), (1, 3), (5, 4), (7, 2)]
resultado = numeros_mayores_que_uno(conjunto_racionales)
print(resultado)  # Esto imprimirá [(2, 1), (3, 2), (7, 2)]
