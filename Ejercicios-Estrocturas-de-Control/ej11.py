# Escribir un programa que pida al usuario dos números y muestre por pantalla la suma de ellos solo si ambos son pares.

num1 = int(input("Ingrese el primer número: "))

num2 = int(input("Ingrese el segundo número: "))

if num1 % 2 == 0 and num2 % 2 == 0:
    suma = num1 + num2
    print("La suma de los dos números es:", suma)
else:
    print("Al menos uno de los números ingresados no es par.")
