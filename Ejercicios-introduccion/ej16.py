#Escribe un programa que solicite al usuario su peso y su altura, y luego calcule e imprima su índice de masa corporal (IMC). La fórmula para calcular el IMC es: IMC = peso / (altura ** 2).
peso = float(input("Introduce tu peso en kilogramos: "))
altura = float(input("Introduce tu altura en metros: "))

imc = peso / (altura ** 2)

print("Tu índice de masa corporal (IMC) es:", imc)
