texto = input("Introduce una cadena de texto: ")
vocales = "aeiouAEIOU"
nuevo_texto = ""

for letra in texto:
    if letra in vocales:
        nuevo_texto += letra.upper()
    else:
        nuevo_texto += letra

print(nuevo_texto)
