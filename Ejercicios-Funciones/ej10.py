def calcular_factorial(numero):
    if numero < 0:
        return None
    
    factorial = 1
    for i in range(1, numero + 1):
        factorial *= i
    
    return factorial

numero = 5
resultado = calcular_factorial(numero)
print(resultado)
