# Escribir un programa que pida al usuario tres números y muestre por pantalla el mayor de ellos.

num1 = int(input("Ingresa el primer número: "))

num2 = int(input("Ingresa el segundo número: "))

num3 = int(input("Ingresa el tercer número: "))

if num1 >= num2 and num1 >= num3:
    print("El mayor número es:", num1)
elif num2 >= num1 and num2 >= num3:
    print("El mayor número es:", num2)
else:
    print("El mayor número es:", num3)