#6. Calcular el máximo de números positivos introducidos por teclado, sabiendo que metemos
#números hasta que introduzcamos uno negativo. El negativo no cuenta. 

def obtener_maximo_positivo():
    numeros = []
    #usamos un bucle para solicitar al usuario que ingrese números 
    #repetidamente hasta que se ingrese un número negativo. 
    while True:
        num = float(input("Ingrese un número (negativo para terminar): "))
        if num < 0:
            break
        numeros.append(num)
    
    if numeros:
        maximo = max(numeros)
        print(f"El máximo de los números positivos ingresados es: {maximo}")
    else:
        print("No se ingresaron números positivos.")

obtener_maximo_positivo()
