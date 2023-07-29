#3.	Llenar un arreglo con la serie de Fibonacci, con la cantidad de dígitos que el usuario
#indique al inicio del programa

def fibonacci_series(num_digits):
    if num_digits <= 0:
        return []

    fibonacci_array = [0, 1]
    while len(str(fibonacci_array[-1])) < num_digits:
        next_fibonacci = fibonacci_array[-1] + fibonacci_array[-2]
        fibonacci_array.append(next_fibonacci)

    return fibonacci_array

def main():
    try:
        num_digits = int(input("Ingrese la cantidad de dígitos para la serie de Fibonacci: "))
        fibonacci_array = fibonacci_series(num_digits)
        print("Serie de Fibonacci con", num_digits, "dígitos:", fibonacci_array)
    except ValueError:
        print("Ingrese un número entero válido.")

if __name__ == "__main__":
    main()
