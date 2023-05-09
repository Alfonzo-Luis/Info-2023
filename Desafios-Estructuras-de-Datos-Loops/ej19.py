num = int(input("Ingrese un número: "))
divisores = []

# Buscamos los divisores propios del número
for i in range(1, num):
    if num % i == 0:
        divisores.append(i)

# Sumamos los divisores propios
suma_divisores = sum(divisores)

# Verificamos si el número es perfecto o no
if suma_divisores == num:
    print(num, "es un número perfecto")
else:
    print(num, "no es un número perfecto")
