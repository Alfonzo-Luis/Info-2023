# Crea un programa que pida al usuario una cantidad en dólares y la convierta a euros. Supón que el tipo de cambio es de 0.84 euros por dólar.
dolares = float(input("Ingrese una cantidad de dólares: "))

tipo_cambio = 0.84

euros = dolares * tipo_cambio

print("Lavantidad de ",dolares, "dólares equivale a ", euros, "euros")