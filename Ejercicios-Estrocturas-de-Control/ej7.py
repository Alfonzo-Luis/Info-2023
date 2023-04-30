# -Escribir un programa que pida al usuario un carácter y muestre por pantalla si es una letra mayúscula, una letra minúscula, un número o un carácter especial.
car = input ("Ingresa un carácter: ")

if car.isupper():
    print("El carácter es una letra en mayúscula")
elif car.islower():
    print("El carácter es una letra en minúscula")
elif car.isdigit():
    print("El carácter es un número")
else:
    car_especiales = ['!', '@', '#', '$', '%', '&', '*']
    if car in car_especiales:
        print("El carácter es especial")
    else:
        print("El caracter no es una letra ni número")
