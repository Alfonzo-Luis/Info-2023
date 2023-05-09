numero = int(input("Ingrese un número: "))

factorial = 1

if numero < 0:
    print("El factorial de números negativos no está definido.")
elif numero == 0:
    print("El factorial de 0 es 1.")
else:
    for i in range(1, numero+1):
        factorial *= i
    print(f"El factorial de {numero} es {factorial}.")
