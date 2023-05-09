palabra = input("Ingresa una palabra: ")
inversa = ""
i = len(palabra) - 1

while i >= 0:
    inversa += palabra[i]
    i -= 1

if palabra == inversa:
    print("La palabra es un palíndromo.")
else:
    print("La palabra no es un palíndromo.")
