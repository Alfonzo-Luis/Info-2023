def eliminar_duplicados(lista):
    lista_sin_duplicados = []
    for elemento in lista:
        if elemento not in lista_sin_duplicados:
            lista_sin_duplicados.append(elemento)
    return lista_sin_duplicados

lista = [1, 2, 3, 2, 4, 1, 5, 4, 6]
lista_sin_duplicados = eliminar_duplicados(lista)
print(lista_sin_duplicados)