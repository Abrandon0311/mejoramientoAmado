#crea una funcion que dice si un numero ingresado por el usuario es primo

def numero_primo():
    num_primo = 0
    numero_usuario = int(input("Digite el numero hasta cual quiera saber si es primo: "))
    for i in range(1, numero_usuario+1):
        if numero_usuario % i == 0:
            num_primo += 1
        
    if num_primo == 2:
            print("Este numero es primo")
    
    if num_primo > 2:
            print("Este numero no es primo")

numero_primo()
numero_primo()
numero_primo()
numero_primo()
