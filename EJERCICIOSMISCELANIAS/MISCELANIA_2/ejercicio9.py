#9. Calcular la operación x n sin utilizar la función pow 

#Si el exponente n es igual a 0, la función devuelve 1, ya que cualquier número elevado a 0 es 1.

#Si el exponente n es negativo, la función invoca a sí misma con el exponente positivo y devuelve 
#el inverso del resultado, ya que x^-n = 1/(x^n).

#Si el exponente n es positivo, la función se llama recursivamente con un exponente reducido en 1 
#y multiplica el resultado por x.

def calcular_potencia(x, n):
    if n == 0:
        return 1
    elif n < 0:
        return 1 / calcular_potencia(x, -n)
    else:
        return x * calcular_potencia(x, n - 1)

# Ejemplo de uso
x = 2
n = 3
#al llamar calcular_potencia(2, 3), obtendremos como resultado 2^3 = 8
resultado = calcular_potencia(x, n)
print(f"{x} elevado a la {n} es igual a {resultado}")
# calcular otras potencias, se cambian los valores de x y n en la llamada a la función.