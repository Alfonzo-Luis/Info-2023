#Escribe un programa que solicite al usuario una temperatura en grados Celsius y luego imprima la temperatura equivalente en grados Fahrenheit. La fórmula para convertir de Celsius a Fahrenheit es: F = (C * 1.8) + 32.
temp = int(input("Ingrese los grados celsius que desea transformar a fahrenheit: "))

grados_a_f = (temp * 1.8) + 32

print(temp," grados celsius a fahrenheit son: ", grados_a_f)
