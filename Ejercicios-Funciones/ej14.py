def encontrar_maximo(lista_numeros):
    if len(lista_numeros) == 0:
        return None

    maximo = lista_numeros[0]
    for numero in lista_numeros:
        if numero > maximo:
            maximo = numero

    return maximo

numeros = [10, 5, 8, 12, 3]
maximo = encontrar_maximo(numeros)
print(maximo)