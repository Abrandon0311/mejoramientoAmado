#Funcion Recibe un diccionario y una palabra que representa la clave (key), y nos retorna el valor asociado y el tipo de dato de ese valor. Si no existe debe indicarlo
def FunDiccionario(diccionario):
    clave = input("Digite la clave del diccionario: ")
    if clave in diccionario:
        print(f"el valor asociado a la clave es {diccionario[clave]}")
    else:
        print("Esta clave no se encuentra en este diccionario")
diccionario_1 = {"perro":"dog",
               "gato":"cat",
               "pato":"duck"}
FunDiccionario(diccionario_1)