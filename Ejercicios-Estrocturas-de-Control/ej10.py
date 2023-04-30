# Escribir un programa que pida al usuario una letra y muestre por pantalla si es una vocal o una consonante
letra = input("Ingrese una letra: ")
if letra.lower() in ["a", "e", "i", "o", "u"]:
    print("La letra ingresada es una vocal.")
else:
    print("La letra ingresada es una consonante.")
