def convertir_temperatura(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

celsius = 25
fahrenheit = convertir_temperatura(celsius)
print(fahrenheit)