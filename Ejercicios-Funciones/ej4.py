def es_capicua(numero):
    numero_str = str(numero)
    return numero_str == numero_str[::-1]

resultado = es_capicua(12321)
print(resultado)

resultado = es_capicua(12345)
print(resultado)
