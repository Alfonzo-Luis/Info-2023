texto = input("Ingrese una cadena de texto: ")
palabras = texto.split()
palabras_invertidas = list(reversed(palabras))
texto_invertido = ' '.join(palabras_invertidas)
print(texto_invertido)
