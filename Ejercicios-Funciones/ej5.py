def es_divisible(num1, num2):
    if num1 % num2 == 0:
        return "Es divisible"
    else:
        return "No es divisible"

resultado = es_divisible(10, 2)
print(resultado)