def promedio(lista):
    if len(lista) == 0:
        return None
    
    suma = sum(lista)
    promedio = suma / len(lista)
    return promedio

numeros = [5, 10, 15, 20, 25]
resultado = promedio(numeros)
print(resultado)
