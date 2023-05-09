palabra = input("Ingresa una palabra: ")
i = len(palabra) - 1
palabra_invertida = ""
while i >= 0:
    palabra_invertida += palabra[i]
    i -= 1
print("La palabra invertida es:", palabra_invertida)
