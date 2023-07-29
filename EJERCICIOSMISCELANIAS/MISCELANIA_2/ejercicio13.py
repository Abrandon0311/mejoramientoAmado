#13. Solicitar al usuario un número de hasta 9 dígitos e imprimirlo en orden contrario.
#Ej. digito 6754 imprimo 4576 


#define una función invertir_numero que toma un número entero, lo convierte en cadena, 
#invierte la cadena y luego lo convierte nuevamente en entero.
def invertir_numero(numero):
    # Convertimos el número en una cadena para poder manipular sus dígitos
    numero_str = str(numero)
    # Invertimos la cadena usando slicing con paso -1
    numero_invertido = numero_str[::-1]
    return int(numero_invertido)

#la función main, se solicita al usuario ingresar un número y se verifica que tenga hasta
#9 dígitos. Si cumple con esta condición, se invierte el número y se imprime en orden contrario.
def main():
    # Pedimos al usuario un número
    numero_usuario = input("Ingrese un número de hasta 9 dígitos: ")

    # Verificamos que el número tenga hasta 9 dígitos
    if len(numero_usuario) > 9:
        print("El número debe tener hasta 9 dígitos.")
    else:
        # Convertimos el número ingresado en entero
        numero_entero = int(numero_usuario)

        # Invertimos el número utilizando la función invertir_numero
        numero_invertido = invertir_numero(numero_entero)

        # Imprimimos el número invertido
        print("Número invertido:", numero_invertido)

#La cláusula if __name__ == "__main__": asegura que la función main se ejecute solo si
#el script se ejecuta directamente y no si se importa como un módulo.
if __name__ == "__main__":
    main()
