#11. Solicitar 2 números al usuario e imprimir el cociente y el residuo del mayor
#en el menor sin utilizar la división ni el mod.

#definimos la función sustraccion_repetida(dividendo, divisor) que calcula el cociente
#y el residuo usando sustracción repetida. 
def sustraccion_repetida(dividendo, divisor):
    cociente = 0
    while dividendo >= divisor:
        dividendo -= divisor
        cociente += 1
    return cociente, dividendo

#la función main(), solicitamos dos números enteros al usuario, identificamos cuál es el mayor y cuál es el menor
def main():
    try:
        num1 = int(input("Ingrese el primer número: "))
        num2 = int(input("Ingrese el segundo número: "))

        mayor = max(num1, num2)
        menor = min(num1, num2)
#llamamos a la función sustraccion_repetida() para obtener el cociente y el residuo del mayor en el menor. 
#Los resultados se imprimen al final.
        cociente, residuo = sustraccion_repetida(mayor, menor)

        print(f"Cociente: {cociente}")
        print(f"Residuo: {residuo}")

    except ValueError:
        print("Error: Ingrese solo números enteros.")

#La cláusula if __name__ == "__main__": asegura que la función main se ejecute solo si
#el script se ejecuta directamente y no si se importa como un módulo.
if __name__ == "__main__":
    main()
