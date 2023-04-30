#Escribe un programa que solicite al usuario su información personal, incluyendo
#su nombre completo, edad, estatura, peso, dirección y número de teléfono.
#A continuación, el programa deberá imprimir un mensaje con los datos
#ingresados por el usuario en el siguiente formato:
#La información ingresada es la siguiente:
#Nombre completo: [nombre completo]
#Edad: [edad]
#Estatura: [estatura] cm
#Peso: [peso] kg
#Dirección: [dirección]
#Número de teléfono: [número de teléfono]

nombre_completo = input("Ingresa tu nombre completo: ")
edad = int(input("Ingresa tu edad: "))
estatura = float(input("Ingresa tu estatura en cm: "))
peso = float(input("Ingresa tu peso en kg: "))
direccion = input("Ingresa tu dirección: ")
telefono = input("Ingresa tu número de teléfono: ")

print("La información ingresada es la siguiente:")
print("Nombre completo:", nombre_completo)
print("Edad:", edad)
print("Estatura:", estatura, "cm")
print("Peso:", peso, "kg")
print("Dirección:", direccion)
print("Número de teléfono:", telefono)