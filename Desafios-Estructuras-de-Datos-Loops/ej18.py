n = int(input("Ingrese un número: "))
contador = 1
for i in range(n):
    for j in range(i+1):
        print(contador, end=' ')
        contador += 1
    print() # para imprimir la nueva línea al final de cada fila
