#genera la funcion para un juego el cual solicitara al usuario adivinar un numero y le dara pistas segun el numero ingresado
import random
def generar_numero_aleatorio():
    return random.randint(1, 100)
def solicitar_numero():
    return int(input("Intenta adivinar el numero, Digita un numero: "))

def jugar():
    num_aleatorio = generar_numero_aleatorio()
    print(num_aleatorio)
    num_usuario = solicitar_numero()
    while num_usuario != num_aleatorio:
        if num_usuario < num_aleatorio:
            print(f"!Pista¡ El numero a adivinar es mayor a {num_usuario}")
        if num_usuario > num_aleatorio:
            print(f"!Pista¡ El numero a adivinar es menor a {num_usuario}")

        print("¡! JA JA JA este numero es incorrecto")
        num_usuario = solicitar_numero()

    print("Lograste adividar el numero ¡FELICIDADES!")

jugar()
