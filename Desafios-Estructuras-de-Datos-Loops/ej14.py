num = int(input("Ingresa un número: "))

for i in range(1, num+1):
    for j in range(i):
        print(i, end=" ")
    print()
