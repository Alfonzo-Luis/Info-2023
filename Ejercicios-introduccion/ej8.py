#Crea un programa que pida al usuario el radio de un círculo y muestre su diámetro, su circunferencia y su área. Supón que pi es aproximadamente 3.14159.
radio = float(input ("IIngrese el radio del circulo "))

pi = 3.14159

diametro = 2 * radio

circunferencia = 2 * pi * radio

area = pi * radio ** 2

print("El díametro del círculo es: ",diametro)

print("La circunferncia del círculo es de: ",circunferencia)

print("El área del círculo es: ",area)