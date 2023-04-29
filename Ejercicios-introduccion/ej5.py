#Crea un programa que pida al usuario dos números enteros y muestre en pantalla su cociente y su resto.
num1 = int(input("Ingrese el primer numero"))
num2 = int(input("Ingrese el segundo numero"))
cociente = num1 // num2
resto = num1 % num2
print("El cociente es: ",cociente)
print("El resto es: ",resto)