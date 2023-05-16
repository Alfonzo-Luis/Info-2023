def es_palindromo(cadena):
    cadena = cadena.lower().replace(" ", "")  # Convertir a minúsculas y eliminar espacios
    
    # Verificar si la cadena es igual a su reverso
    if cadena == cadena[::-1]:
        return "es palindromo"
    else:
        return "no es palindromo"

resultado = es_palindromo("Anita lava la tina")
print(resultado)