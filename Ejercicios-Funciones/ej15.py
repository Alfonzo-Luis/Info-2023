def contar_palabras(cadena):
    palabras = cadena.split()
    cantidad_palabras = len(palabras)
    return cantidad_palabras

texto = "Este es un ejemplo de texto"
cantidad_palabras = contar_palabras(texto)
print(cantidad_palabras)
