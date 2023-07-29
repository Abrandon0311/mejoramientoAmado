#12. Escribir un programa que visualice la siguiente figura, utilizando ciclos. 
#El usuario decide cuantas líneas quiere imprimir 
#* 
#* * 
#* * * 
#* * * *  
#* * * * * 
#* * * * * * 
#* * * * * * * 
#* * * * * * * * 
#* * * * * * * * *

#Definimos una función llamada imprimir_figura que toma un parámetro num_lineas.
def imprimir_figura(num_lineas):
    #Utilizamos un bucle for que va desde 1 hasta num_lineas + 1, ya que queremos
    # imprimir hasta el número de líneas ingresado por el usuario.
    for i in range(1, num_lineas + 1):
        print('* ' * i)

#En el bloque if __name__ == '__main__':, solicitamos al usuario que ingrese el
#número de líneas que desea imprimir y llamamos a la función imprimir_figura para mostrar la figura.
if __name__ == '__main__':
    try:
        num_lineas = int(input("Ingrese el número de líneas que desea imprimir: "))
        imprimir_figura(num_lineas)
    except ValueError:
        print("Error: Ingrese un número válido.")

#En cada iteración, imprimimos una cadena formada por el carácter asterisco '*' seguido de un espacio ' ', 
#repetido i veces. Esto crea una línea con la cantidad adecuada de asteriscos según el número de la línea actual.