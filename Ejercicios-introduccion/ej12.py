# Escribe un programa que solicite al usuario su fecha de nacimiento en formato dd/mm/aaaa y luego imprima su edad en años. Utiliza la función .split()
fecha_nacimiento = input("Ingrese su fecha de nacimiento con formato dd/mm/aaaa: ")
anio = fecha_nacimiento.split('/') [2]
edad = 2023 - int(anio)
print(edad)
